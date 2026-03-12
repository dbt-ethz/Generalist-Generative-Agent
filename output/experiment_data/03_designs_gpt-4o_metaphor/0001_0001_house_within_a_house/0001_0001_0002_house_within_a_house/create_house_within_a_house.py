# Created for 0001_0001_house_within_a_house.json

""" Summary:
The function `create_house_within_a_house` generates an architectural concept model that embodies the metaphor of a "House within a house." It does this by creating two nested geometrical volumes: an inner house representing a core sanctuary and an outer house providing a protective envelope. The function accepts dimensions for both houses and wall thickness, establishing a layered spatial hierarchy. By employing boolean operations, it forms hollow walls between the inner and outer structures, enhancing the concept of privacy and enclosure. This results in a design that reflects complex interior-exterior relationships, as suggested by the metaphor."""

#! python 3
function_code = """def create_house_within_a_house(inner_width, inner_length, inner_height, outer_width, outer_length, outer_height, wall_thickness):
    \"""
    Creates a conceptual architectural model based on the metaphor 'House within a house'.
    
    This function generates a spatial hierarchy by nesting one volume within another, suggesting layered privacy and 
    protection. The inner volume represents a core sanctuary, surrounded by an outer volume, creating complex 
    interior-exterior relationships.

    Parameters:
    - inner_width (float): Width of the inner house in meters.
    - inner_length (float): Length of the inner house in meters.
    - inner_height (float): Height of the inner house in meters.
    - outer_width (float): Width of the outer house in meters.
    - outer_length (float): Length of the outer house in meters.
    - outer_height (float): Height of the outer house in meters.
    - wall_thickness (float): Thickness of the walls surrounding the inner house in meters.

    Returns:
    - List of Rhino.Geometry.Brep: A list containing the breps of the outer and inner house volumes, 
      and the separating walls.
    \"""
    import Rhino.Geometry as rg

    # Create the inner house as a box
    inner_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(-inner_width / 2, inner_width / 2),
        rg.Interval(-inner_length / 2, inner_length / 2),
        rg.Interval(0, inner_height)
    )
    
    # Create the outer house as a box
    outer_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(-outer_width / 2, outer_width / 2),
        rg.Interval(-outer_length / 2, outer_length / 2),
        rg.Interval(0, outer_height)
    )

    # Calculate the offset for the inner house to accommodate wall thickness
    offset_inner_width = inner_width + 2 * wall_thickness
    offset_inner_length = inner_length + 2 * wall_thickness
    offset_inner_height = inner_height + wall_thickness

    # Create the enclosing walls as a box larger than the inner house
    wall_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(-offset_inner_width / 2, offset_inner_width / 2),
        rg.Interval(-offset_inner_length / 2, offset_inner_length / 2),
        rg.Interval(0, offset_inner_height)
    )

    # Subtract the inner house from the enclosing walls to create hollow walls
    walls = rg.Brep.CreateBooleanDifference([wall_box.ToBrep()], [inner_box.ToBrep()], 0.01)

    # Return the outer box, hollow walls, and inner box as breps
    return [outer_box.ToBrep(), walls[0], inner_box.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_a_house(5.0, 7.0, 3.0, 10.0, 12.0, 5.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_a_house(4.0, 6.0, 2.5, 9.0, 11.0, 4.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_a_house(6.0, 8.0, 4.0, 11.0, 13.0, 6.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_a_house(3.0, 5.0, 2.0, 8.0, 10.0, 3.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_a_house(7.0, 9.0, 3.5, 12.0, 14.0, 5.5, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
