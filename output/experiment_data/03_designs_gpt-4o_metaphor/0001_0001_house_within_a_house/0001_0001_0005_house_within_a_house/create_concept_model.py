# Created for 0001_0001_house_within_a_house.json

""" Summary:
The provided function `create_concept_model` generates an architectural concept model based on the metaphor "House within a house." It constructs a layered spatial hierarchy by creating two nested geometric volumes: an inner core representing the internal sanctuary and an outer shell symbolizing protection and privacy. By defining dimensions, offsets, and floor heights, the function encapsulates the essence of nesting and varied spatial experiences. The result is a list of geometric representations, allowing for complex interior-exterior relationships and a sense of enclosure, effectively embodying the metaphor's intent in the architectural design process."""

#! python 3
function_code = """def create_concept_model(inner_size, outer_size, inner_offset, outer_offset, floor_height, num_floors):
    \"""
    Creates a 'House within a House' architectural concept model using nested geometric volumes.
    
    This function generates a core (inner house) surrounded by an encapsulating structure (outer house),
    representing a layered spatial hierarchy. The design focuses on nesting, protection, and privacy, 
    creating varied spatial experiences.

    Inputs:
    - inner_size: Tuple of (width, depth) for the inner core dimensions.
    - outer_size: Tuple of (width, depth) for the outer shell dimensions.
    - inner_offset: Offset distance for the inner core from the ground.
    - outer_offset: Offset distance for the outer shell from the ground.
    - floor_height: Height of each floor in meters.
    - num_floors: Number of floors for the inner core.

    Output:
    - List of RhinoCommon geometries (Breps) representing the concept model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set a random seed for replicability
    random.seed(42)

    # Calculate heights
    inner_height = floor_height * num_floors
    outer_height = inner_height + 2 * outer_offset

    # Create the base plane
    base_plane = rg.Plane.WorldXY

    # Create the inner core (house)
    inner_box = rg.Box(base_plane, rg.Interval(-inner_size[0]/2, inner_size[0]/2), rg.Interval(-inner_size[1]/2, inner_size[1]/2), rg.Interval(inner_offset, inner_offset + inner_height))
    inner_brep = inner_box.ToBrep()

    # Create the outer shell (house)
    outer_box = rg.Box(base_plane, rg.Interval(-outer_size[0]/2, outer_size[0]/2), rg.Interval(-outer_size[1]/2, outer_size[1]/2), rg.Interval(outer_offset, outer_offset + outer_height))
    outer_brep = outer_box.ToBrep()

    # Create a list to store the generated geometries
    geometries = []

    # Add inner and outer breps to the geometry list
    geometries.append(inner_brep)
    geometries.append(outer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model((5, 7), (10, 12), 1, 2, 3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model((8, 10), (15, 18), 2, 3, 4, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model((6, 9), (11, 14), 1.5, 2.5, 3.5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model((4, 5), (9, 10), 0.5, 1, 2.5, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model((7, 8), (12, 15), 1, 2, 3, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
