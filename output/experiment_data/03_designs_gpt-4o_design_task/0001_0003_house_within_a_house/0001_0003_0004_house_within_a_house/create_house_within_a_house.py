# Created for 0001_0003_house_within_a_house.json

""" Summary:
The function `create_house_within_a_house` generates an architectural concept model that embodies the "House within a house" metaphor by creating two interconnected 3D volumes: an inner sanctuary and an outer protective form. It accepts parameters for dimensions and material contrasts, ensuring the outer layer encapsulates the inner space. The model features random openings to symbolize dynamic spatial connections between the layers, enhancing the experience of transitioning from public to private realms. The geometric interplay emphasizes the duality of spaces, illustrating nesting, protection, and varied spatial experiences within an integrated architectural concept."""

#! python 3
function_code = """def create_house_within_a_house(inner_width, inner_length, inner_height, outer_width, outer_length, outer_height, material_contrast_factor):
    \"""
    Create a 'House within a House' architectural concept model using distinct yet interconnected layers,
    representing the metaphor of a dual-layered form where each layer serves a distinct function and spatial quality.

    Parameters:
    - inner_width (float): Width of the inner sanctuary.
    - inner_length (float): Length of the inner sanctuary.
    - inner_height (float): Height of the inner sanctuary.
    - outer_width (float): Width of the outer protective form.
    - outer_length (float): Length of the outer protective form.
    - outer_height (float): Height of the outer protective form.
    - material_contrast_factor (float): A factor to define the contrasting opacity of the materials between the layers.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino
    from Rhino.Geometry import Box, Point3d, Brep, Plane
    from System import Random

    # Ensure that the outer dimensions are larger than the inner dimensions
    assert outer_width > inner_width and outer_length > inner_length and outer_height > inner_height, \
        "Outer dimensions must be larger than inner dimensions."

    # Create the inner sanctuary as a Brep
    inner_base = Point3d(0, 0, 0)
    inner_box = Box(Plane(inner_base, Rhino.Geometry.Vector3d.ZAxis), Rhino.Geometry.Interval(0, inner_width),
                    Rhino.Geometry.Interval(0, inner_length), Rhino.Geometry.Interval(0, inner_height))
    inner_brep = inner_box.ToBrep()

    # Create the outer protective form as a Brep
    outer_base = Point3d(-(outer_width - inner_width) / 2, -(outer_length - inner_length) / 2, 0)
    outer_box = Box(Plane(outer_base, Rhino.Geometry.Vector3d.ZAxis), Rhino.Geometry.Interval(0, outer_width),
                    Rhino.Geometry.Interval(0, outer_length), Rhino.Geometry.Interval(0, outer_height))
    outer_brep = outer_box.ToBrep()

    # Create openings and connections between inner and outer spaces
    random_seed = int(material_contrast_factor * 100)
    rand = Random(random_seed)
    openings = []
    for _ in range(3):  # Create 3 random openings
        opening_width = rand.NextDouble() * 2 + 1  # Random width between 1 and 3 meters
        opening_length = rand.NextDouble() * 2 + 1  # Random length between 1 and 3 meters
        opening_height = rand.NextDouble() * 2 + 1  # Random height between 1 and 3 meters
        opening_base = Point3d(rand.NextDouble() * (outer_width - opening_width), 
                               rand.NextDouble() * (outer_length - opening_length), 
                               rand.NextDouble() * (outer_height - opening_height))
        opening_box = Box(Plane(opening_base, Rhino.Geometry.Vector3d.ZAxis), Rhino.Geometry.Interval(0, opening_width),
                          Rhino.Geometry.Interval(0, opening_length), Rhino.Geometry.Interval(0, opening_height))
        openings.append(opening_box.ToBrep())

    # Subtract openings from the outer brep to simulate interconnections
    for opening in openings:
        result = Brep.CreateBooleanDifference(outer_brep, opening, 0.01)
        if result:
            outer_brep = result[0]

    # Return the breps as a list
    return [outer_brep, inner_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_a_house(5.0, 10.0, 3.0, 8.0, 12.0, 5.0, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_a_house(4.0, 6.0, 2.5, 7.0, 9.0, 4.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_a_house(6.0, 9.0, 4.0, 10.0, 15.0, 6.0, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_a_house(3.0, 7.0, 2.0, 5.0, 10.0, 4.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_a_house(7.0, 11.0, 3.5, 12.0, 16.0, 7.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
