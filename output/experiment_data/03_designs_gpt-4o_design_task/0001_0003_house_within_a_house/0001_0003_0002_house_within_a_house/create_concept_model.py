# Created for 0001_0003_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by constructing a dual-layered form. It creates an inner sanctuary volume defined by specified dimensions and an outer protective shell that encapsulates it, using boolean operations to form a hollow structure. The model features a staircase facilitating movement between layers, emphasizing the transition from public to private spaces. By utilizing contrasting materials and interlocking geometries, the function embodies the metaphor's essence, showcasing nested spaces that promote varying spatial experiences and a sense of refuge within the overall design."""

#! python 3
function_code = """def create_concept_model(inner_width, inner_length, inner_height, outer_thickness):
    \"""
    Creates a dual-layered architectural Concept Model based on the 'House within a house' metaphor.

    Parameters:
    - inner_width (float): The width of the inner sanctuary volume in meters.
    - inner_length (float): The length of the inner sanctuary volume in meters.
    - inner_height (float): The height of the inner sanctuary volume in meters.
    - outer_thickness (float): The thickness of the outer protective shell in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model layers.
    \"""

    import Rhino
    import Rhino.Geometry as rg

    # Create the inner sanctuary as a simple box
    inner_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(0, inner_width),
        rg.Interval(0, inner_length),
        rg.Interval(0, inner_height)
    )
    inner_brep = inner_box.ToBrep()

    # Create the outer protective shell as a larger box, offset from the inner box
    outer_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(-outer_thickness, inner_width + outer_thickness),
        rg.Interval(-outer_thickness, inner_length + outer_thickness),
        rg.Interval(-outer_thickness, inner_height + outer_thickness)
    )
    outer_brep = outer_box.ToBrep()

    # Subtract the inner box from the outer box to create a hollow shell
    outer_shell = rg.Brep.CreateBooleanDifference([outer_brep], [inner_brep], 0.01)

    # Check if the boolean operation was successful
    if not outer_shell or len(outer_shell) == 0:
        outer_shell = [outer_brep]  # Fallback to returning outer_brep if difference fails

    # Create a staircase to connect the inner and outer volumes
    stair_width = inner_width * 0.2
    stair_length = inner_length * 0.2
    stair_height = inner_height * 0.5
    
    stair_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(inner_width - stair_width, inner_width),
        rg.Interval(inner_length - stair_length, inner_length),
        rg.Interval(0, stair_height)
    )
    stair_brep = stair_box.ToBrep()

    # Offset the staircase to create a hollow core
    stair_offset_distance = 0.1  # 10 cm offset for hollow
    stair_hollow = rg.Brep.CreateOffsetBrep(stair_brep, -stair_offset_distance, True, True, 0.01)
    if stair_hollow and len(stair_hollow) > 0:
        stair_hollow = stair_hollow[0]

    # Return the list of geometries representing the concept model
    return [inner_brep, outer_shell[0], stair_hollow]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(5.0, 10.0, 3.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(4.0, 8.0, 2.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(6.0, 12.0, 4.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(7.0, 14.0, 3.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(8.0, 16.0, 5.0, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
