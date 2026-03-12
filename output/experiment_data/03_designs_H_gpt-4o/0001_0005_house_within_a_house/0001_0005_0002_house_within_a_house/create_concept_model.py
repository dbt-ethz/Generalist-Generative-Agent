# Created for 0001_0005_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model based on the "House within a house" metaphor by creating a series of concentric, layered volumes. It begins by defining a core volume that represents the inner sanctuary. The function then iteratively generates outer layers, each offset from the previous one to create interstitial spaces. These gaps facilitate movement and exploration, embodying a journey through varying levels of enclosure and intimacy. The resulting model highlights the transition from public to private realms, effectively capturing the essence of nesting, protection, and the layered spatial hierarchy inherent in the metaphor."""

#! python 3
function_code = """def create_concept_model(core_dimensions=(5, 5, 10), number_of_layers=4, layer_gap=2):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.

    This function generates a series of concentric, layered volumes that transition from the outer environment
    to an inner sanctuary. Each layer is offset from the previous one, creating interstitial spaces that guide
    movement and provide a sense of discovery.

    Parameters:
    - core_dimensions (tuple of floats): Dimensions of the core volume (length, width, height) in meters.
    - number_of_layers (int): The number of concentric layers surrounding the core.
    - layer_gap (float): The gap between each concentric layer in meters.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg

    geometries = []

    # Create the core central volume
    length, width, height = core_dimensions
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-length / 2, length / 2), rg.Interval(-width / 2, width / 2), rg.Interval(0, height))
    geometries.append(core.ToBrep())

    # Generate concentric layers
    for i in range(1, number_of_layers + 1):
        # Calculate new dimensions for each layer
        new_length = length + i * 2 * layer_gap
        new_width = width + i * 2 * layer_gap
        new_height = height + i * layer_gap
        
        # Create outer box for the layer
        outer_layer = rg.Box(rg.Plane.WorldXY, rg.Interval(-new_length / 2, new_length / 2), rg.Interval(-new_width / 2, new_width / 2), rg.Interval(0, new_height))
        
        # Create an inner void by subtracting the previous layer
        inner_length = new_length - 2 * layer_gap
        inner_width = new_width - 2 * layer_gap
        inner_height = new_height - layer_gap

        inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-inner_length / 2, inner_length / 2), rg.Interval(-inner_width / 2, inner_width / 2), rg.Interval(0, inner_height))
        
        # Subtract inner box from outer box to create a shell
        layer_brep = rg.Brep.CreateBooleanDifference(outer_layer.ToBrep(), inner_box.ToBrep(), 0.01)

        # Add the layer to the geometry list, if valid
        if layer_brep:
            geometries.extend(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(core_dimensions=(6, 4, 12), number_of_layers=5, layer_gap=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(core_dimensions=(8, 8, 15), number_of_layers=3, layer_gap=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(core_dimensions=(10, 5, 20), number_of_layers=6, layer_gap=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(core_dimensions=(4, 6, 10), number_of_layers=2, layer_gap=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(core_dimensions=(7, 3, 14), number_of_layers=4, layer_gap=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
