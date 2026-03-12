# Created for 0013_0004_split_void.json

""" Summary:
The function `create_split_void_concept_model_v3` generates an architectural concept model that embodies the "Split void" metaphor by creating a structure with a central void that divides the solid mass. It takes input parameters like building dimensions, void size, and curvature, generating a dynamic void using control points to define its shape. The void is extruded to create an engaging interplay between solid and void, enhancing spatial relationships and interactions with light and air. This model reflects the metaphor's emphasis on contrast, movement, and the duality of enclosed and open spaces, facilitating a vivid spatial experience."""

#! python 3
function_code = """def create_split_void_concept_model_v3(length, width, height, void_width, void_height, curve_points, seed):
    \"""
    Create an architectural Concept Model based on the 'Split void' metaphor.

    This function generates a structure with a split void that divides the space, emphasizing
    the contrast and interaction between solid and void spaces. The void is created with a
    dynamic, multi-point curve that introduces complexity and interaction within the structure.

    Parameters:
    length (float): The total length of the building footprint.
    width (float): The total width of the building footprint.
    height (float): The height of the building.
    void_width (float): The maximum width of the central void.
    void_height (float): The height of the void.
    curve_points (int): Number of control points for shaping the void curve.
    seed (int): Random seed for reproducibility of the design.

    Returns:
    list: A list of Brep geometry objects representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the building solid
    building_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, length), rg.Interval(0, height))

    # Create control points for the void curve
    control_points = []
    for i in range(curve_points):
        x = width / 2 + random.uniform(-void_width / 2, void_width / 2)
        y = length / curve_points * i
        z = random.uniform(0, void_height)
        control_points.append(rg.Point3d(x, y, z))
    
    # Create a nurbs curve for the void
    void_curve = rg.NurbsCurve.Create(False, 3, control_points)

    # Extrude the void curve to create a surface
    void_surface = rg.Extrusion.Create(void_curve, height, True)
    void_surface_brep = void_surface.ToBrep() if void_surface else None

    # Split the building with the void surface to create the concept model
    split_breps = building_box.ToBrep().Split(void_surface_brep, 0.01) if void_surface_brep else None

    # Return the resulting geometries
    if split_breps and len(split_breps) > 0:
        return split_breps
    else:
        return [building_box.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model_v3(10.0, 5.0, 15.0, 2.0, 8.0, 10, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model_v3(20.0, 10.0, 30.0, 4.0, 12.0, 15, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model_v3(15.0, 8.0, 20.0, 3.0, 10.0, 12, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model_v3(25.0, 12.0, 18.0, 5.0, 9.0, 20, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model_v3(18.0, 9.0, 22.0, 6.0, 11.0, 8, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
