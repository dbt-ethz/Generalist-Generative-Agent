import argparse
import os
import sys
from enum import Enum

import bpy
from mathutils import Vector


DESIGNS_COLLECTION_NAME = "DESIGNS"
SCENE_COLLECTION_NAME = "SCENE"
HIDDEN_COLLECTION_NAME = "HIDDEN"
PLACEHOLDER_BOX_NAME = "placeholderbox"


class RenderStyle(Enum):
    SOLID = "SOLID"
    GHOSTED = "GHOSTED"
    WIREFRAME = "WIREFRAME"


def parse_args():
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1 :]
    else:
        argv = []

    parser = argparse.ArgumentParser(description="Batch render GH OBJ outputs in Blender.")
    parser.add_argument(
        "--input-dir",
        required=True,
        help="Root directory containing GH output folders, or a single design folder with OBJ files.",
    )
    parser.add_argument(
        "--render-style",
        choices=[style.value for style in RenderStyle],
        default=RenderStyle.GHOSTED.value,
        help="Render style suffix and material setup.",
    )
    parser.add_argument(
        "--resolution-x",
        type=int,
        default=1280,
        help="Render width in pixels.",
    )
    parser.add_argument(
        "--resolution-y",
        type=int,
        default=1280,
        help="Render height in pixels.",
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=300,
        help="Cycles sample count.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Re-render images even if they already exist.",
    )
    parser.add_argument(
        "--y-up",
        action="store_true",
        help="Import OBJ files as Y-up instead of Z-up.",
    )
    parser.add_argument(
        "--global-scale",
        action="store_true",
        help="Use one shared scale factor across all variants in a design folder.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of design folders to render.",
    )
    return parser.parse_args(argv)


def clear_collection_contents(collection):
    for child in list(collection.children):
        clear_collection_contents(child)
        bpy.data.collections.remove(child, do_unlink=True)
    for obj in list(collection.objects):
        bpy.data.objects.remove(obj, do_unlink=True)


def ensure_collection(name):
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def reset_design_collection():
    collection = ensure_collection(DESIGNS_COLLECTION_NAME)
    clear_collection_contents(collection)
    return collection


def ensure_render_materials(render_style):
    render_material = bpy.data.materials.get("render_material")
    if render_material is None:
        render_material = bpy.data.materials.new(name="render_material")
        render_material.use_nodes = True
    render_material.blend_method = "BLEND"
    render_material.shadow_method = "NONE"
    render_bsdf = render_material.node_tree.nodes.get("Principled BSDF")
    if render_bsdf is not None:
        render_bsdf.inputs["Base Color"].default_value = (0.88, 0.88, 0.88, 1.0)
        render_bsdf.inputs["Roughness"].default_value = 0.6
        render_bsdf.inputs["Alpha"].default_value = (
            1.0 if render_style == RenderStyle.SOLID else 0.3
        )

    wire_material = bpy.data.materials.get("wire_material")
    if wire_material is None:
        wire_material = bpy.data.materials.new(name="wire_material")
        wire_material.use_nodes = True
    wire_bsdf = wire_material.node_tree.nodes.get("Principled BSDF")
    if wire_bsdf is not None:
        wire_bsdf.inputs["Base Color"].default_value = (0.1, 0.1, 0.1, 1.0)
        wire_bsdf.inputs["Roughness"].default_value = 0.5

    return render_material, wire_material


def unlink_from_all_collections(obj):
    for collection in list(obj.users_collection):
        collection.objects.unlink(obj)


def import_obj(filepath, collection, y_up=False):
    if hasattr(bpy.ops.wm, "obj_import"):
        kwargs = {"filepath": filepath}
        if y_up:
            kwargs.update({"forward_axis": "Z", "up_axis": "Y"})
        else:
            kwargs.update({"forward_axis": "Y", "up_axis": "Z"})
        bpy.ops.wm.obj_import(**kwargs)
    else:
        kwargs = {"filepath": filepath}
        if y_up:
            kwargs.update({"axis_forward": "Z", "axis_up": "Y"})
        else:
            kwargs.update({"axis_forward": "Y", "axis_up": "Z"})
        bpy.ops.import_scene.obj(**kwargs)

    imported_objects = list(bpy.context.selected_objects)
    for obj in imported_objects:
        unlink_from_all_collections(obj)
        collection.objects.link(obj)
    return imported_objects


def obj_files_in_dir(path):
    return sorted(
        os.path.join(path, filename)
        for filename in os.listdir(path)
        if filename.lower().endswith(".obj")
    )


def discover_design_dirs(path):
    path = os.path.abspath(path)
    if not os.path.isdir(path):
        raise FileNotFoundError(f"Input directory not found: {path}")

    if obj_files_in_dir(path):
        return [path]

    design_dirs = []
    for root, _, files in os.walk(path):
        if any(filename.lower().endswith(".obj") for filename in files):
            design_dirs.append(root)

    return sorted(design_dirs)


def world_bounds(objects):
    xs, ys, zs = [], [], []
    for obj in objects:
        if not hasattr(obj, "bound_box"):
            continue
        for corner in obj.bound_box:
            world_corner = obj.matrix_world @ Vector(corner)
            xs.append(world_corner.x)
            ys.append(world_corner.y)
            zs.append(world_corner.z)

    if not xs:
        return None
    return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


def reference_dimension():
    ref_box = bpy.data.objects.get(PLACEHOLDER_BOX_NAME)
    if ref_box is None:
        print(f"Reference object '{PLACEHOLDER_BOX_NAME}' not found. Using dimension 1.0.")
        return 1.0

    ref_bbox = [Vector(corner) for corner in ref_box.bound_box]
    return max(corner.x for corner in ref_bbox) - min(corner.x for corner in ref_bbox)


def prepare_variants(variants, ref_dim, scale_local):
    variant_bounds = []
    for variant in variants:
        bounds = world_bounds(variant["objects"])
        if bounds is None:
            continue
        largest_dim = max(
            bounds[1] - bounds[0],
            bounds[3] - bounds[2],
            bounds[5] - bounds[4],
        )
        scale_factor = ref_dim / largest_dim if largest_dim else 1.0
        variant_bounds.append(
            {
                "variant": variant,
                "bounds": bounds,
                "scale_factor": scale_factor,
            }
        )

    if not variant_bounds:
        return

    shared_scale_factor = min(item["scale_factor"] for item in variant_bounds)
    for item in variant_bounds:
        bounds = item["bounds"]
        scale_factor = item["scale_factor"] if scale_local else shared_scale_factor
        center_x = (bounds[0] + bounds[1]) / 2
        center_y = (bounds[2] + bounds[3]) / 2
        min_z = bounds[4]

        for obj in item["variant"]["objects"]:
            obj.location.x -= center_x
            obj.location.y -= center_y
            obj.location.z -= min_z
            obj.location *= scale_factor
            obj.scale *= scale_factor


def apply_materials(variants, render_style):
    render_material, wire_material = ensure_render_materials(render_style)
    for variant in variants:
        for obj in variant["objects"]:
            if obj.type != "MESH":
                continue
            obj.data.materials.clear()
            obj.data.materials.append(render_material)
            if render_style != RenderStyle.SOLID:
                obj.data.materials.append(wire_material)
                wireframe = obj.modifiers.new(name="wireframe", type="WIREFRAME")
                wireframe.thickness = 0.02
                wireframe.material_offset = 1
                wireframe.use_even_offset = False
                wireframe.use_replace = render_style == RenderStyle.WIREFRAME


def grease_pencil_modifier():
    for obj in bpy.data.objects:
        if obj.type == "GPENCIL" and obj.grease_pencil_modifiers:
            return obj.grease_pencil_modifiers[0]
    return None


def configure_scene(resolution_x, resolution_y, samples):
    scene = bpy.context.scene
    scene.render.resolution_x = resolution_x
    scene.render.resolution_y = resolution_y
    if scene.render.engine == "CYCLES":
        scene.cycles.samples = samples
        try:
            scene.cycles.device = "GPU"
        except Exception:
            scene.cycles.device = "CPU"

    scene_collection = bpy.data.collections.get(SCENE_COLLECTION_NAME)
    if scene_collection is not None:
        scene_collection.hide_render = False

    hidden_collection = bpy.data.collections.get(HIDDEN_COLLECTION_NAME)
    if hidden_collection is not None:
        for obj in hidden_collection.objects:
            obj.hide_render = True


def build_output_path(design_dir, obj_path, render_style, resolution_x, resolution_y):
    base_parts = os.path.basename(design_dir).split("_")
    obj_prefix = os.path.basename(obj_path).split("_")[0]
    try:
        obj_index = int(obj_prefix) + 1
    except ValueError:
        obj_index = 1
    base_parts.insert(3, f"{obj_index:04d}")
    filename = "_".join(base_parts)
    return os.path.join(
        design_dir,
        f"{filename}_{render_style.value}_{resolution_x}x{resolution_y}.png",
    )


def render_design_dir(
    design_dir,
    render_style,
    resolution_x,
    resolution_y,
    samples,
    overwrite,
    y_up,
    scale_local,
):
    print(f"Rendering design folder: {design_dir}")
    design_collection = reset_design_collection()
    variants = []
    for obj_path in obj_files_in_dir(design_dir):
        variant_collection = bpy.data.collections.new(os.path.splitext(os.path.basename(obj_path))[0])
        design_collection.children.link(variant_collection)
        imported_objects = import_obj(obj_path, variant_collection, y_up=y_up)
        if not imported_objects:
            continue
        variants.append(
            {
                "obj_path": obj_path,
                "collection": variant_collection,
                "objects": imported_objects,
            }
        )

    if not variants:
        print(f"No OBJ files found in {design_dir}")
        return

    ref_dim = reference_dimension()
    prepare_variants(variants, ref_dim=ref_dim, scale_local=scale_local)
    apply_materials(variants, render_style)
    configure_scene(resolution_x=resolution_x, resolution_y=resolution_y, samples=samples)

    gp_modifier = grease_pencil_modifier()
    for variant in variants:
        for other_variant in variants:
            for obj in other_variant["objects"]:
                obj.hide_render = True

        final_output_path = build_output_path(
            design_dir,
            variant["obj_path"],
            render_style,
            resolution_x,
            resolution_y,
        )
        if os.path.exists(final_output_path) and not overwrite:
            print(f"Skipping existing render: {final_output_path}")
            continue

        for obj in variant["objects"]:
            obj.hide_render = False
        if gp_modifier is not None and variant["objects"]:
            gp_modifier.source_object = variant["objects"][0]

        temp_output_path = final_output_path.replace(".png", "_temp.png")
        bpy.context.scene.render.image_settings.file_format = "PNG"
        bpy.context.scene.render.filepath = temp_output_path
        bpy.ops.render.render(write_still=True)

        if os.path.exists(temp_output_path):
            os.replace(temp_output_path, final_output_path)
            print(f"Saved render: {final_output_path}")
        else:
            print(f"Render finished but no file was created: {final_output_path}")


def main():
    args = parse_args()
    render_style = RenderStyle(args.render_style)
    design_dirs = discover_design_dirs(args.input_dir)
    if args.limit is not None:
        design_dirs = design_dirs[: args.limit]

    if not design_dirs:
        raise FileNotFoundError(
            f"No design folders with OBJ files were found under: {args.input_dir}"
        )

    print(f"Found {len(design_dirs)} design folders to render.")
    for design_dir in design_dirs:
        render_design_dir(
            design_dir=design_dir,
            render_style=render_style,
            resolution_x=args.resolution_x,
            resolution_y=args.resolution_y,
            samples=args.samples,
            overwrite=args.overwrite,
            y_up=args.y_up,
            scale_local=not args.global_scale,
        )

    print("Rendering complete.")


if __name__ == "__main__":
    main()
