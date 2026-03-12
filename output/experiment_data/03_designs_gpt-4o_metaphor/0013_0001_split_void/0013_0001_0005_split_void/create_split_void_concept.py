# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept` generates an architectural concept model based on the metaphor of "Split void" by creating a central void that divides a solid base volume into two distinct zones. By specifying parameters like base dimensions and a split ratio, the function creates a main volume and uses a split surface to separate it, resulting in two separate geometries. This design reflects the metaphor's key traits of division and dynamic interaction with light and shadow, allowing for a sense of openness and movement while maintaining a cohesive formal identity. The output is a list of 3D geometries representing this concept."""

#! python 3
function_code = """def create_split_void_concept(base_length, base_width, height, split_ratio=0.5, seed=42):
    \"""
    Creates an architectural concept model based on the 'Split void' metaphor. It generates a central void
    that is split into two distinct zones with a clear separation, allowing for dynamic light and shadow 
    interactions.

    Parameters:
    - base_length (float): The length of the base rectangle of the model in meters.
    - base_width (float): The width of the base rectangle of the model in meters.
    - height (float): The height of the model in meters.
    - split_ratio (float, optional): The ratio by which the central void is split. Default is 0.5 for an equal split.
    - seed (int, optional): Random seed for replicable results.

    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create the base volume
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0)
    ]
    base_curve = rg.Polyline(base_corners + [base_corners[0]]).ToNurbsCurve()
    base_surface = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)

    # Extrude the base to create a solid block
    extrude_vector = rg.Vector3d(0, 0, height)
    extrusion = rg.Surface.CreateExtrusion(base_curve, extrude_vector)
    main_volume = rg.Brep.CreateFromSurface(extrusion)

    # Calculate the split line
    split_line_start = rg.Point3d(base_length * split_ratio, 0, 0)
    split_line_end = rg.Point3d(base_length * split_ratio, base_width, 0)
    split_line = rg.Line(split_line_start, split_line_end)

    # Create the split surface
    split_surface = rg.Surface.CreateExtrusion(split_line.ToNurbsCurve(), extrude_vector)

    # Split the main volume with the split surface
    split_volumes = main_volume.Split(split_surface.ToBrep(), 0.01)

    # Ensure we have two volumes
    if split_volumes is None or len(split_volumes) < 2:
        raise ValueError("Failed to split the volume into two parts.")

    # Return the two split volumes as a list
    return list(split_volumes)"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept(10, 5, 8, split_ratio=0.3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept(15, 10, 12, split_ratio=0.6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept(20, 15, 10, split_ratio=0.4, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept(25, 20, 15, split_ratio=0.7, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept(30, 25, 20, split_ratio=0.8, seed=111)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
