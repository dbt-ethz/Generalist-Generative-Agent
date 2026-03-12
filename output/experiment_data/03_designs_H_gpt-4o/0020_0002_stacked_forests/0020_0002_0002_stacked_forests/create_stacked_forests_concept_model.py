# Created for 0020_0002_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a series of interlocking, organically shaped volumes that reflect the layered structure of a forest. Each layer is designed with a base rectangle that is distorted to mimic natural forms, representing the complexity of a forest ecosystem. The function also incorporates vertical and horizontal pathways, simulating trails found in nature. By varying parameters like width, depth, and height, the model achieves a balance between density and openness, reflecting the hierarchical and dynamic qualities of a forest while offering diverse spatial experiences."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_width=10.0, base_depth=10.0, num_layers=6, layer_height=3.0, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Stacked forests' metaphor.

    The model consists of interlocking volumes that emulate a forest's layered nature,
    with a focus on density, hierarchy, and organic growth. The concept incorporates
    vertical and horizontal pathways that simulate movement through a forest.

    Parameters:
    - base_width (float): The width of the base layer in meters.
    - base_depth (float): The depth of the base layer in meters.
    - num_layers (int): The number of vertical layers representing the forest.
    - layer_height (float): The height of each layer in meters.
    - seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for i in range(num_layers):
        # Calculate the vertical position of the current layer
        z_position = i * layer_height

        # Create a base rectangle for the layer
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, base_width, base_depth)
        base_rect.Transform(rg.Transform.Translation(0, 0, z_position))

        # Generate a distorted organic shape by moving control points
        control_points = [pt for pt in base_rect.ToPolyline().ToNurbsCurve().Points]
        for pt in control_points:
            offset_x = random.uniform(-1, 1)
            offset_y = random.uniform(-1, 1)
            pt.Location += rg.Vector3d(offset_x, offset_y, 0)

        organic_curve = rg.Polyline([pt.Location for pt in control_points]).ToNurbsCurve()

        # Create a lofted surface from the base rectangle to the organic curve
        loft_brep = rg.Brep.CreateFromLoft([base_rect.ToNurbsCurve(), organic_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

        if loft_brep and len(loft_brep) > 0:
            geometries.append(loft_brep[0])

        # Add vertical pathways to mimic forest trails
        if random.random() < 0.5:
            path_start = rg.Point3d(random.uniform(0, base_width), random.uniform(0, base_depth), z_position)
            path_end = rg.Point3d(path_start.X, path_start.Y, z_position + layer_height)
            path_line = rg.Line(path_start, path_end).ToNurbsCurve()
            path_brep = rg.Brep.CreatePipe(path_line, 0.1, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)
            if path_brep:
                geometries.append(path_brep[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(base_width=15.0, base_depth=15.0, num_layers=8, layer_height=4.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(base_width=12.0, base_depth=12.0, num_layers=5, layer_height=2.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(base_width=20.0, base_depth=10.0, num_layers=10, layer_height=3.5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(base_width=8.0, base_depth=16.0, num_layers=7, layer_height=2.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(base_width=18.0, base_depth=9.0, num_layers=4, layer_height=3.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
