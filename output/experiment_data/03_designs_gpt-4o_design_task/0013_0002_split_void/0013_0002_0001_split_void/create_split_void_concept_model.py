# Created for 0013_0002_split_void.json

""" Summary:
The provided function, `create_split_void_concept_model`, generates an architectural concept model that embodies the 'Split void' metaphor by creating two distinct volumes divided by a central void. It takes parameters for the dimensions of the building and void, and incorporates height variations to emphasize spatial dynamics. The function constructs three-dimensional boxes representing the two halves and the void, allowing for the exploration of light, shadow, and movement across the division. By varying the heights and widths, it captures the essence of duality and interaction, resulting in a cohesive architectural identity that aligns with the metaphor's implications."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, base_height, void_width, height_variation):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor. This model features a central void that 
    separates two distinct volumes, incorporating varying heights on either side of the void to enhance spatial dynamics.

    Parameters:
    - base_length (float): The total length of the building in meters.
    - base_width (float): The total width of the building in meters.
    - base_height (float): The average height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - height_variation (float): The variation in height between the two halves in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the geometries of the concept model.
    \"""
    import Rhino.Geometry as rg

    # Calculate dimensions for the two halves
    half_length = base_length / 2
    half_width = (base_width - void_width) / 2

    # Create the base box for the first half
    first_half_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(-half_length, 0),
        rg.Interval(-half_width, half_width),
        rg.Interval(0, base_height + height_variation)
    )

    # Create the base box for the second half
    second_half_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(0, half_length),
        rg.Interval(-half_width, half_width),
        rg.Interval(0, base_height - height_variation)
    )

    # Create the void as a box
    void_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(-void_width / 2, void_width / 2),
        rg.Interval(-half_width, half_width),
        rg.Interval(0, base_height)
    )

    # Convert boxes to Breps
    first_half_brep = first_half_box.ToBrep()
    second_half_brep = second_half_box.ToBrep()
    void_brep = void_box.ToBrep()

    # Return the list of Breps representing the concept model
    return [first_half_brep, second_half_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(20.0, 10.0, 6.0, 3.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15.0, 8.0, 5.0, 2.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(25.0, 12.0, 7.0, 4.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(30.0, 15.0, 8.0, 5.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(18.0, 9.0, 5.5, 3.5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
