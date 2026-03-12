# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function, `create_concept_model_mirrored_folded_planes`, generates an architectural concept model based on the metaphor of "Mirrored Folded Planes." It creates dynamic, angular forms by generating a folded plane using specified dimensions and a fold angle. The function then mirrors this plane at a defined distance, emphasizing symmetry and complexity. This process yields a pair of Brep objects that visually represent the interplay of movement, depth, and reflective symmetry, aligning with the metaphor's traits. As a result, the function effectively translates conceptual design ideas into tangible 3D geometries, enabling further exploration of architectural possibilities."""

#! python 3
function_code = """def create_concept_model_mirrored_folded_planes(base_length=10, height=5, fold_angle=45, mirror_distance=15):
    \"""
    Creates a concept model inspired by the 'Mirrored Folded Planes' metaphor, using symmetry and angular forms
    to generate dynamic and reflective architectural spaces.

    Args:
        base_length (float): The length of the base of the folded plane in meters.
        height (float): The height of the folded plane in meters.
        fold_angle (float): The angle at which the plane is folded, in degrees.
        mirror_distance (float): The distance between the original and mirrored planes in meters.

    Returns:
        list: A list of RhinoCommon Brep objects representing the folded planes and their mirrored counterparts.
    \"""

    import Rhino.Geometry as rg
    import math

    # Convert the fold angle from degrees to radians
    fold_angle_rad = math.radians(fold_angle)
    
    # Create the initial folded plane
    def create_folded_plane(base_length, height, fold_angle_rad):
        pts = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_length, 0, 0),
            rg.Point3d(base_length, height * math.tan(fold_angle_rad), height),
            rg.Point3d(0, height * math.tan(fold_angle_rad), height)
        ]
        plane_curve = rg.Polyline(pts).ToNurbsCurve()
        return rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(plane_curve, rg.Vector3d(0, 0, 0.1)))

    # Create mirrored folded plane
    def mirror_plane(plane_brep, mirror_distance):
        mirror_plane = rg.Plane(rg.Point3d(mirror_distance, 0, 0), rg.Vector3d(1, 0, 0))
        mirrored_brep = plane_brep.Duplicate()
        mirrored_brep.Transform(rg.Transform.Mirror(mirror_plane.Origin, mirror_plane.Normal))
        return mirrored_brep

    # Generate the initial folded plane and its mirrored counterpart
    original_plane = create_folded_plane(base_length, height, fold_angle_rad)
    mirrored_plane = mirror_plane(original_plane, mirror_distance)
    
    # Return the list of Brep geometries
    return [original_plane, mirrored_plane]

# Example usage:
# geometries = create_concept_model_mirrored_folded_planes()
# This function call would return a list of 3D Brep objects representing the concept model."""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_mirrored_folded_planes(base_length=12, height=6, fold_angle=30, mirror_distance=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_mirrored_folded_planes(base_length=8, height=4, fold_angle=60, mirror_distance=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_mirrored_folded_planes(base_length=15, height=7, fold_angle=90, mirror_distance=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_mirrored_folded_planes(base_length=14, height=3, fold_angle=75, mirror_distance=18)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_mirrored_folded_planes(base_length=11, height=5, fold_angle=45, mirror_distance=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
