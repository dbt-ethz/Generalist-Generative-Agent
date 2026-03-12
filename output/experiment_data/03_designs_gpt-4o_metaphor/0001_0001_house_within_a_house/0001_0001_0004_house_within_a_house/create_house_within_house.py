# Created for 0001_0001_house_within_a_house.json

""" Summary:
The provided function, `create_house_within_house`, generates an architectural concept model based on the metaphor of a "House within a house." It creates two nested volumes: an inner sanctuary and an outer protective shell, emphasizing themes of privacy, nesting, and spatial complexity. The function takes dimensions for both volumes and wall thickness as parameters, constructs the 3D geometries using Rhino.Geometry, and models the relationship between the inner and outer spaces through a boolean operation. This results in a conceptual design that visually represents the metaphors traits, allowing for varied spatial experiences within a protective environment."""

#! python 3
function_code = """def create_house_within_house(inner_length, inner_width, inner_height, outer_length, outer_width, outer_height, wall_thickness):
    \"""
    Creates a Concept Model based on the metaphor 'House within a house'. This function generates two nested architectural
    volumes, representing the idea of an inner sanctuary enclosed within an outer protective shell. The design emphasizes
    privacy, retreat, and complex spatial relationships.

    Parameters:
    - inner_length (float): The length of the inner house volume in meters.
    - inner_width (float): The width of the inner house volume in meters.
    - inner_height (float): The height of the inner house volume in meters.
    - outer_length (float): The length of the outer house volume in meters.
    - outer_width (float): The width of the outer house volume in meters.
    - outer_height (float): The height of the outer house volume in meters.
    - wall_thickness (float): The thickness of the walls separating the inner and outer volumes in meters.

    Returns:
    - list: A list of Breps representing the architectural geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    
    # Create the inner sanctuary volume
    inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, inner_length), rg.Interval(0, inner_width), rg.Interval(0, inner_height))
    inner_brep = inner_box.ToBrep()
    
    # Create the outer protective shell volume
    outer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-wall_thickness, outer_length + wall_thickness), 
                       rg.Interval(-wall_thickness, outer_width + wall_thickness), 
                       rg.Interval(0, outer_height))
    outer_brep = outer_box.ToBrep()
    
    # Subtract the inner volume from the outer volume to create a void
    boolean_result = rg.Brep.CreateBooleanDifference(outer_brep, inner_brep, 0.01)
    
    # Check and return the resulting Breps
    if boolean_result:
        return boolean_result
    else:
        return [outer_brep, inner_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house(5.0, 4.0, 3.0, 10.0, 9.0, 6.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house(6.0, 5.0, 4.0, 12.0, 11.0, 8.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house(7.0, 6.0, 5.0, 14.0, 13.0, 10.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house(8.0, 7.0, 6.0, 15.0, 14.0, 9.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house(4.0, 3.0, 2.5, 9.0, 8.0, 5.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
