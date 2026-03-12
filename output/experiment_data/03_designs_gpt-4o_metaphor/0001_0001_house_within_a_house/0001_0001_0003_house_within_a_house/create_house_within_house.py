# Created for 0001_0001_house_within_a_house.json

""" Summary:
The provided function, `create_house_within_house`, generates an architectural concept model based on the metaphor "House within a house." It creates two 3D geometric boxes: an inner house and an outer house, establishing a layered spatial hierarchy that reflects the metaphor's essence. The inner dimensions are defined by the user's specifications, while the outer dimensions incorporate a margin, enhancing the sense of protection and enclosure. This design fosters complex interior-exterior relationships, allowing for varied spatial experiences. The result is a pair of Brep geometries that visually represent the concept of nested spaces, embodying privacy and sanctuary."""

#! python 3
function_code = """def create_house_within_house(inner_length, inner_width, inner_height, outer_margin):
    \"""
    Creates a concept model based on the metaphor 'House within a house'. This model consists of an inner 'house' 
    encapsulated by a larger outer 'house', creating a layered spatial hierarchy.

    Inputs:
    - inner_length: The length of the inner house (in meters).
    - inner_width: The width of the inner house (in meters).
    - inner_height: The height of the inner house (in meters).
    - outer_margin: The margin distance between the inner house and the outer house (in meters).

    Outputs:
    - A list of 3D Brep geometries representing the inner and outer houses.
    \"""
    import Rhino
    from Rhino.Geometry import Box, Brep, Plane, Point3d, Interval

    # Inner house dimensions
    inner_base = Box(Plane.WorldXY, Interval(0, inner_length), Interval(0, inner_width), Interval(0, inner_height))
    
    # Outer house dimensions
    outer_length = inner_length + 2 * outer_margin
    outer_width = inner_width + 2 * outer_margin
    outer_height = inner_height + outer_margin  # A bit higher for an enclosing effect
    outer_base = Box(Plane.WorldXY, Interval(0, outer_length), Interval(0, outer_width), Interval(0, outer_height))
    
    # Convert boxes to Breps
    inner_brep = Brep.CreateFromBox(inner_base)
    outer_brep = Brep.CreateFromBox(outer_base)
    
    # Return the list of Brep geometries
    return [outer_brep, inner_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house(10, 8, 6, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house(15, 12, 10, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house(5, 4, 3, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house(20, 15, 12, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house(7, 5, 4, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
