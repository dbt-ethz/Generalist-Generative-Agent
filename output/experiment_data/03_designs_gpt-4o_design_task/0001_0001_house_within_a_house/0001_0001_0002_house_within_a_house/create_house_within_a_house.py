# Created for 0001_0001_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "House within a house." It constructs a series of nested volumes to reflect a spatial hierarchy of privacy and function. The inner volume, representing the core sanctuary, is designed to be opaque, while the outer volume functions as a translucent shell, illustrating the transition from public to private spaces. The creation of a middle layer adds complexity and enhances the progression between these spaces. By manipulating dimensions, the function allows for varied spatial experiences, effectively embodying the metaphor's key traits of enclosure and layered design."""

#! python 3
function_code = """def create_house_within_a_house(inner_width=4.0, inner_height=3.0, inner_depth=4.0,
                                outer_width=8.0, outer_height=5.0, outer_depth=8.0):
    \"""
    Creates a conceptual architectural model representing a 'House within a house' metaphor.
    This function generates nested volumes, with an opaque inner core and translucent outer shell,
    to illustrate layers of privacy and spatial hierarchy.

    Parameters:
    inner_width (float): Width of the inner volume, representing the core sanctuary.
    inner_height (float): Height of the inner volume.
    inner_depth (float): Depth of the inner volume.
    outer_width (float): Width of the outer volume, representing the protective shell.
    outer_height (float): Height of the outer volume.
    outer_depth (float): Depth of the outer volume.

    Returns:
    list: A list of RhinoCommon Breps representing the nested volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness
    random.seed(42)

    # Create the inner sanctuary volume (more opaque and intimate)
    inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-inner_width/2, inner_width/2),
                       rg.Interval(-inner_depth/2, inner_depth/2), rg.Interval(0, inner_height))
    inner_brep = inner_box.ToBrep()

    # Create the outer protective shell volume (transparent or translucent)
    outer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-outer_width/2, outer_width/2),
                       rg.Interval(-outer_depth/2, outer_depth/2), rg.Interval(0, outer_height))
    outer_brep = outer_box.ToBrep()

    # Optionally add more layers or intermediary spaces for complexity
    # Create a middle layer as a transition space
    middle_width = (outer_width + inner_width) / 2
    middle_depth = (outer_depth + inner_depth) / 2
    middle_height = (outer_height + inner_height) / 2
    middle_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-middle_width/2, middle_width/2),
                        rg.Interval(-middle_depth/2, middle_depth/2), rg.Interval(0, middle_height))
    middle_brep = middle_box.ToBrep()

    return [outer_brep, middle_brep, inner_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_a_house(inner_width=5.0, inner_height=3.5, inner_depth=5.0, outer_width=10.0, outer_height=6.0, outer_depth=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_a_house(inner_width=3.0, inner_height=2.5, inner_depth=3.0, outer_width=7.0, outer_height=4.0, outer_depth=7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_a_house(inner_width=6.0, inner_height=4.0, inner_depth=6.0, outer_width=12.0, outer_height=8.0, outer_depth=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_a_house(inner_width=4.5, inner_height=3.0, inner_depth=4.5, outer_width=9.0, outer_height=5.5, outer_depth=9.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_a_house(inner_width=2.0, inner_height=2.0, inner_depth=2.0, outer_width=6.0, outer_height=4.0, outer_depth=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
