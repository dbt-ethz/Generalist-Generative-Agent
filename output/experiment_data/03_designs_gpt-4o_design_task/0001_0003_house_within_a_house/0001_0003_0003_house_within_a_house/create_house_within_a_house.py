# Created for 0001_0003_house_within_a_house.json

""" Summary:
The provided function, `create_house_within_a_house`, generates an architectural concept model reflecting the "House within a house" metaphor. It creates a dual-layered structure, where an inner sanctuary is encapsulated by an outer protective form. The function defines the inner box and expands it to form the outer shell, integrating openings for interaction and visual connection between layers. Staircases facilitate movement, emphasizing the transition between distinct spatial realms. By using varying dimensions and random elements, the model captures the essence of nested spaces, highlighting the interplay of privacy and openness, and fostering a dynamic spatial experience."""

#! python 3
function_code = """def create_house_within_a_house(inner_length, inner_width, inner_height, outer_thickness, seed=None):
    \"""
    Constructs an architectural Concept Model based on the 'House within a house' metaphor. 
    The model features an inner sanctuary enveloped by an outer protective form, with distinct yet interconnected layers.

    Parameters:
    - inner_length (float): Length of the inner house in meters.
    - inner_width (float): Width of the inner house in meters.
    - inner_height (float): Height of the inner house in meters.
    - outer_thickness (float): Thickness of the outer protective layer in meters.
    - seed (int, optional): Seed for randomization to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)
    
    # Define the inner sanctuary as a box
    inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, inner_length), rg.Interval(0, inner_width), rg.Interval(0, inner_height))
    inner_brep = inner_box.ToBrep()

    # Define the outer protective form by expanding the inner box dimensions
    outer_length = inner_length + 2 * outer_thickness
    outer_width = inner_width + 2 * outer_thickness
    outer_height = inner_height + outer_thickness
    outer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-outer_thickness, inner_length + outer_thickness), rg.Interval(-outer_thickness, inner_width + outer_thickness), rg.Interval(0, outer_height))
    outer_brep = outer_box.ToBrep()

    # Create openings in the outer shell for interaction with the inner sanctuary
    opening_width = random.uniform(inner_width * 0.2, inner_width * 0.3)
    opening_height = random.uniform(inner_height * 0.3, inner_height * 0.5)
    opening_plane = rg.Plane.WorldXY
    opening_plane.Origin = rg.Point3d(0, inner_width / 2, 0)
    opening = rg.Box(opening_plane, rg.Interval(0, outer_thickness), rg.Interval(-opening_width / 2, opening_width / 2), rg.Interval(0, opening_height))
    opening_brep = opening.ToBrep()
    
    # Subtract the opening from the outer shell
    outer_with_opening = rg.Brep.CreateBooleanDifference([outer_brep], [opening_brep], 0.01)

    # Define a staircase connecting the two layers
    stair_width = outer_thickness / 2
    stair_depth = outer_thickness / 2
    stair_height = outer_thickness / 3
    stair_steps = 5

    stairs = []
    for i in range(stair_steps):
        step_plane = rg.Plane(rg.Point3d(0, inner_width + outer_thickness / 2, i * stair_height), rg.Vector3d.ZAxis)
        step_box = rg.Box(step_plane,
                          rg.Interval(0, stair_width),
                          rg.Interval(0, stair_depth),
                          rg.Interval(0, stair_height))
        stairs.append(step_box.ToBrep())
    
    # Combine all elements into a single list of Breps
    geometries = [inner_brep] + list(outer_with_opening) + stairs

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_a_house(10, 8, 6, 2, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_a_house(12, 9, 7, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_a_house(15, 10, 5, 1.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_a_house(8, 5, 4, 1, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_a_house(20, 15, 10, 4, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
