# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern by creating a complex interplay of solid and void spaces. It constructs spherical chambers to represent expansive areas, utilizing organic forms that evoke the fluidity of natural caves. Connecting corridors are generated as angular structures, enhancing the rugged appearance. The model incorporates random elements for variation, simulating the labyrinthine quality of cave systems. By adjusting chamber sizes, corridor widths, and overall dimensions, the function captures the essence of exploration and surprise, ultimately creating an immersive architectural experience reflective of the metaphor."""

#! python 3
function_code = """def cavernous_architecture_model(base_length, base_width, base_height, corridor_width, chamber_radius, seed=42):
    \"""
    Creates an architectural Concept Model inspired by a subterranean cavern,
    using a combination of angular and organic forms.

    Parameters:
    - base_length (float): Overall length of the model in meters.
    - base_width (float): Overall width of the model in meters.
    - base_height (float): Overall height of the model in meters.
    - corridor_width (float): Width of the connecting corridors in meters.
    - chamber_radius (float): Radius of the spherical chambers in meters.
    - seed (int): Random seed for reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create base chambers (spheres) to represent large, open spaces
    for _ in range(3):
        center = rg.Point3d(
            random.uniform(0, base_length),
            random.uniform(0, base_width),
            random.uniform(0, base_height)
        )
        sphere = rg.Sphere(center, chamber_radius)
        sphere_brep = sphere.ToBrep()
        geometries.append(sphere_brep)

    # Create connecting corridors (angular forms) between chambers
    for _ in range(4):
        start_pt = rg.Point3d(
            random.uniform(0, base_length),
            random.uniform(0, base_width),
            random.uniform(0, base_height)
        )
        end_pt = rg.Point3d(
            random.uniform(0, base_length),
            random.uniform(0, base_width),
            random.uniform(0, base_height)
        )
        line = rg.LineCurve(start_pt, end_pt)
        corridor = rg.Brep.CreatePipe(line, corridor_width, False, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]
        if corridor:
            geometries.append(corridor)

    # Create angular volumes to give a rugged appearance
    for _ in range(3):
        corner_points = [
            rg.Point3d(
                random.uniform(0, base_length),
                random.uniform(0, base_width),
                random.uniform(0, base_height)
            ) for _ in range(4)
        ]
        poly = rg.Polyline(corner_points + [corner_points[0]])
        extrusion_vector = rg.Vector3d(0, 0, random.uniform(1, base_height))
        surface = rg.Surface.CreateExtrusion(poly.ToNurbsCurve(), extrusion_vector)
        if surface:
            brep = rg.Brep.CreateFromSurface(surface)
            geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = cavernous_architecture_model(50, 30, 20, 5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = cavernous_architecture_model(100, 50, 30, 10, 4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = cavernous_architecture_model(75, 40, 25, 6, 5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = cavernous_architecture_model(60, 35, 15, 4, 2, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = cavernous_architecture_model(80, 45, 22, 8, 6, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
