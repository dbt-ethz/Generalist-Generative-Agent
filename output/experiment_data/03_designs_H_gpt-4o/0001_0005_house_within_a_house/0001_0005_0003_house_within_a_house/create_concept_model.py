# Created for 0001_0005_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a series of concentric, layered volumes. Each layer represents a transition from the external environment to an internal sanctuary, with varying dimensions that symbolize different degrees of enclosure and intimacy. The model employs interstitial spaces to enhance the experience of movement through these layers, fostering a sense of journey and discovery. By manipulating core dimensions, layer counts, and gaps, the function articulates the metaphor's themes of nesting, protection, and spatial hierarchy, visually conveying the progression from public to private realms."""

#! python 3
function_code = """def create_concept_model(core_length=8, core_width=6, core_height=10, num_layers=4, layer_gap=2):
    \"""
    Creates an architectural Concept Model embodying the 'House within a house' metaphor.

    This function generates a series of concentric, layered volumes representing transitions from the external
    environment to an internal sanctuary. The model uses varying forms and interstitial spaces to accentuate
    the journey through different spatial hierarchies.

    Parameters:
    - core_length (float): The length of the core volume in meters.
    - core_width (float): The width of the core volume in meters.
    - core_height (float): The height of the core volume in meters.
    - num_layers (int): The number of concentric layers surrounding the core.
    - layer_gap (float): The distance between each concentric layer in meters, providing transitional zones.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg

    geometries = []

    # Create the central core volume
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_length / 2, core_length / 2),
                  rg.Interval(-core_width / 2, core_width / 2), rg.Interval(0, core_height))
    geometries.append(core.ToBrep())

    # Offset dimensions for each layer
    current_length = core_length
    current_width = core_width
    current_height = core_height

    for i in range(1, num_layers + 1):
        # Increase dimensions for each layer
        current_length += layer_gap
        current_width += layer_gap
        current_height += layer_gap * 0.5  # Slight height increase for variation

        # Create outer and inner boxes for layers
        outer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-current_length / 2, current_length / 2),
                           rg.Interval(-current_width / 2, current_width / 2), rg.Interval(0, current_height))
        inner_length = current_length - layer_gap
        inner_width = current_width - layer_gap
        inner_height = current_height - layer_gap * 0.5

        inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-inner_length / 2, inner_length / 2),
                           rg.Interval(-inner_width / 2, inner_width / 2), rg.Interval(0, inner_height))

        # Create shell by subtracting inner box from outer box
        layer_brep = rg.Brep.CreateBooleanDifference(outer_box.ToBrep(), inner_box.ToBrep(), 0.01)
        if layer_brep:
            geometries.extend(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(core_length=10, core_width=8, core_height=12, num_layers=5, layer_gap=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(core_length=7, core_width=5, core_height=9, num_layers=3, layer_gap=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(core_length=12, core_width=10, core_height=15, num_layers=6, layer_gap=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(core_length=9, core_width=7, core_height=11, num_layers=4, layer_gap=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(core_length=15, core_width=12, core_height=20, num_layers=7, layer_gap=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
