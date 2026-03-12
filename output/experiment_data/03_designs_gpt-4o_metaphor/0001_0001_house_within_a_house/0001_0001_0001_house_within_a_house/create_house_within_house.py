# Created for 0001_0001_house_within_a_house.json

""" Summary:
The function `create_house_within_house` generates an architectural concept model based on the metaphor of "House within a house," which emphasizes spatial hierarchy and enclosure. It constructs two geometrical layers: an inner box representing the core sanctuary and an outer box symbolizing the protective shell. The parameters define the dimensions of the inner house and the thickness of the outer shell, allowing for varied spatial experiences. By creating a Boolean difference between these two boxes, the function effectively models the relationship and interaction between the internal and external spaces, embodying the metaphor's themes of nesting and privacy."""

#! python 3
function_code = """def create_house_within_house(inner_length, inner_width, inner_height, outer_thickness):
    \"""
    Creates a concept model of a 'house within a house' using RhinoCommon, based on the metaphor
    of nested spatial entities. The model consists of two layers: an inner core representing 
    the internal sanctuary and an outer shell representing the enclosing volume.

    Parameters:
    - inner_length (float): The length of the inner 'house' in meters.
    - inner_width (float): The width of the inner 'house' in meters.
    - inner_height (float): The height of the inner 'house' in meters.
    - outer_thickness (float): The thickness of the outer enclosing shell in meters.

    Returns:
    - List of Rhino.Geometry.Brep: A list containing the Breps representing the inner house and the outer shell.
    \"""

    import Rhino
    from Rhino.Geometry import Box, Brep, Point3d, Interval

    # Define the inner house as a box
    inner_box = Box(
        Rhino.Geometry.Plane.WorldXY,
        Interval(0, inner_length),
        Interval(0, inner_width),
        Interval(0, inner_height)
    )

    # Define the outer shell dimensions
    outer_length = inner_length + 2 * outer_thickness
    outer_width = inner_width + 2 * outer_thickness
    outer_height = inner_height + outer_thickness

    # Define the outer house as a box
    outer_box = Box(
        Rhino.Geometry.Plane.WorldXY,
        Interval(-outer_thickness, outer_length - outer_thickness),
        Interval(-outer_thickness, outer_width - outer_thickness),
        Interval(0, outer_height)
    )

    # Create Breps from boxes
    inner_brep = inner_box.ToBrep()
    outer_brep = outer_box.ToBrep()

    # Create the outer shell by subtracting the inner house from the outer house
    outer_shell = Brep.CreateBooleanDifference([outer_brep], [inner_brep], 0.01)

    # Return the resulting geometries: inner house and outer shell
    return [inner_brep] + list(outer_shell)"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house(5, 4, 3, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house(10, 8, 6, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house(7, 5, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house(6, 5, 4, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house(8, 6, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
