# Created for 0001_0005_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a series of concentric, layered volumes. It begins with a core volume, representing the internal sanctuary, and progressively adds layers that vary in size, height, and materiality to signify transitions between public and private spaces. Each layer is achieved through a boolean difference operation that creates shells around the core, enhancing the interplay of solid and void. This approach fosters a journey of discovery as users move through the layers, embodying the metaphor's themes of nesting, protection, and spatial hierarchy."""

#! python 3
function_code = """def create_concept_model(base_length, base_width, base_height, num_layers, layer_thickness):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor. 
    The model consists of concentric, layered volumes with varying heights and forms to 
    articulate transitions from public to private spaces.

    Parameters:
    - base_length (float): The length of the innermost core volume in meters.
    - base_width (float): The width of the innermost core volume in meters.
    - base_height (float): The height of the innermost core volume in meters.
    - num_layers (int): Number of concentric layers surrounding the core volume.
    - layer_thickness (float): Thickness of each surrounding layer in meters.

    Returns:
    - List of Rhino.Geometry.Brep: The generated 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed random number generator for replicability
    random.seed(42)

    geometries = []

    # Create the core central volume
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    geometries.append(core.ToBrep())

    # Generate concentric layers
    for i in range(1, num_layers + 1):
        # Create a larger box for each layer
        length = base_length + i * 2 * layer_thickness
        width = base_width + i * 2 * layer_thickness
        height = base_height * (1 + 0.1 * i)  # Slightly increase height for variation

        # Create a surrounding layer box
        outer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-length / 2, length / 2), rg.Interval(-width / 2, width / 2), rg.Interval(0, height))
        
        # Create an inner void by subtracting the previous layer (or core)
        inner_length = length - 2 * layer_thickness
        inner_width = width - 2 * layer_thickness
        inner_height = height - layer_thickness

        inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-inner_length / 2, inner_length / 2), rg.Interval(-inner_width / 2, inner_width / 2), rg.Interval(0, inner_height))
        
        # Subtract inner box from outer box to create a shell
        layer_brep = rg.Brep.CreateBooleanDifference(outer_box.ToBrep(), inner_box.ToBrep(), 0.01)

        # Add the layer to the geometry list
        if layer_brep:
            geometries.extend(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(5.0, 3.0, 4.0, 3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(7.0, 4.0, 5.0, 4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(6.0, 2.5, 3.0, 5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(8.0, 5.0, 6.0, 2, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(10.0, 7.0, 8.0, 6, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
