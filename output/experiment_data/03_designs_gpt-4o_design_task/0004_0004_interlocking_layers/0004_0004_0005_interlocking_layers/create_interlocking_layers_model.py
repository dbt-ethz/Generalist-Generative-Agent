# Created for 0004_0004_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_model`, generates an architectural concept model that embodies the "Interlocking Layers" metaphor. It creates multiple overlapping planes or volumes, each representing a distinct layer. The function takes parameters to define the model's dimensions, the number of layers, their thickness, and a randomness seed to ensure unique arrangements. By applying random offsets to each layer, the design achieves dynamic spatial relationships and visual depth, reflecting the interplay of openness and separation. The resulting 3D geometry illustrates the interconnected yet distinct nature of spaces, fulfilling the design task of showcasing interaction and connectivity in architecture."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, height, num_layers, layer_thickness, randomness_seed):
    \"""
    Creates an architectural Concept Model embodying the 'Interlocking Layers' metaphor. 
    The model consists of a series of overlapping and integrated planes or volumes that emphasize 
    interaction and connectivity.

    Inputs:
    - base_length: The base length of the initial volume (float).
    - base_width: The base width of the initial volume (float).
    - height: The height of the entire model (float).
    - num_layers: The number of interlocking layers (int).
    - layer_thickness: The thickness of each layer (float).
    - randomness_seed: Seed for randomness to ensure replicable results (int).

    Outputs:
    - A list of RhinoCommon Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize randomness
    random.seed(randomness_seed)

    # Calculate the height of each layer
    layer_height = height / num_layers

    # List to store the resulting Breps
    breps = []

    # Create interlocking layers
    for i in range(num_layers):
        # Random offset for interlocking effect
        offset_x = random.uniform(-layer_thickness / 2, layer_thickness / 2)
        offset_y = random.uniform(-layer_thickness / 2, layer_thickness / 2)

        # Base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = i * layer_height

        # Create a box for the current layer
        box_corners = [
            rg.Point3d(offset_x, offset_y, base_plane.OriginZ),
            rg.Point3d(base_length + offset_x, offset_y, base_plane.OriginZ),
            rg.Point3d(base_length + offset_x, base_width + offset_y, base_plane.OriginZ),
            rg.Point3d(offset_x, base_width + offset_y, base_plane.OriginZ),
            rg.Point3d(offset_x, offset_y, base_plane.OriginZ + layer_height),
            rg.Point3d(base_length + offset_x, offset_y, base_plane.OriginZ + layer_height),
            rg.Point3d(base_length + offset_x, base_width + offset_y, base_plane.OriginZ + layer_height),
            rg.Point3d(offset_x, base_width + offset_y, base_plane.OriginZ + layer_height)
        ]

        # Create a Brep from the box
        box_brep = rg.Brep.CreateFromBox(box_corners)
        breps.append(box_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 4, 1.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 20.0, 5, 1.5, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 10.0, 3, 0.5, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(15.0, 10.0, 25.0, 6, 2.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(20.0, 10.0, 30.0, 7, 1.2, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
