# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept` generates an architectural concept model based on the "Split void" metaphor by creating a central void space that divides the overall structure into distinct zones. It takes parameters such as dimensions and a division ratio to determine how to split the central space. By defining two sub-volumes on either side of the void and incorporating a wall thickness, the model emphasizes openness, movement, and dynamic contrasts of light and shadow. The result is a list of geometric representations (Brep objects) that visually embody the metaphor's core traits, allowing exploration of spatial interactions."""

#! python 3
function_code = """def create_split_void_concept(width, depth, height, wall_thickness, division_ratio):
    \"""
    Creates an architectural Concept Model based on the "Split Void" metaphor. This concept involves a central void space
    that is split to create distinct zones or pathways, emphasizing openness and movement with a dynamic contrast of light and shadow.

    Parameters:
    width (float): The total width of the model in meters.
    depth (float): The total depth of the model in meters.
    height (float): The total height of the model in meters.
    wall_thickness (float): The thickness of the walls in meters.
    division_ratio (float): A ratio (0 to 1) that defines the division of the central void space.

    Returns:
    list: A list of RhinoCommon Brep objects representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg

    # Create the main bounding box for the entire volume
    main_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

    # Determine the division point based on the division ratio
    division_point = division_ratio * width

    # Create two sub-volumes to represent the split
    left_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, division_point), rg.Interval(0, depth), rg.Interval(0, height))
    right_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(division_point + wall_thickness, width), rg.Interval(0, depth), rg.Interval(0, height))

    # Create the void space
    void_space = rg.Box(rg.Plane.WorldXY, rg.Interval(division_point, division_point + wall_thickness), rg.Interval(0, depth), rg.Interval(0, height))

    # Convert the boxes to breps
    main_brep = main_volume.ToBrep()
    left_brep = left_volume.ToBrep()
    right_brep = right_volume.ToBrep()
    void_brep = void_space.ToBrep()

    # Return the breps representing the concept model
    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept(10.0, 5.0, 3.0, 0.2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept(15.0, 10.0, 4.0, 0.3, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept(8.0, 6.0, 2.5, 0.1, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept(12.0, 8.0, 5.0, 0.25, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept(20.0, 10.0, 6.0, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
