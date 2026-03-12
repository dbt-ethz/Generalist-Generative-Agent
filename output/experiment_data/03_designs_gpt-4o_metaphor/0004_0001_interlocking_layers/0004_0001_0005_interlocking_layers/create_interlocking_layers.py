# Created for 0004_0001_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers`, generates an architectural model based on the metaphor of "Interlocking Layers." It creates multiple overlapping planes with random offsets and rotations to simulate dynamic spatial relationships and visual depth. By specifying parameters such as width, depth, height, number of layers, and layer thickness, the function produces a series of Brep geometries that embody the metaphor's essence. This design approach emphasizes complexity and interaction between layers, allowing for a blend of openness and separation, which aligns with the conceptual goals of the architectural design task."""

#! python 3
function_code = """def create_interlocking_layers(width, depth, height, num_layers, layer_thickness, seed=None):
    \"""
    Creates a concept model based on the metaphor of 'Interlocking Layers'.
    
    This function generates a series of overlapping and interconnected planes or volumes, emphasizing spatial complexity
    and dynamic relationships between layers. It provides a sense of openness and separation within the architecture.

    Parameters:
    - width (float): The overall width of the model in meters.
    - depth (float): The overall depth of the model in meters.
    - height (float): The total height of the model in meters.
    - num_layers (int): The number of interlocking layers.
    - layer_thickness (float): The thickness of each layer in meters.
    - seed (int, optional): A seed value for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking layers.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Brep, Vector3d, Plane, Box

    if seed is not None:
        random.seed(seed)

    layers = []
    layer_height = height / num_layers
    base_plane = Plane.WorldXY

    for i in range(num_layers):
        # Random offset and rotation for each layer to create interlocking effect
        offset_x = random.uniform(-width * 0.1, width * 0.1)
        offset_y = random.uniform(-depth * 0.1, depth * 0.1)
        rotation = random.uniform(-15, 15)  # degrees

        # Create a base plane for the layer
        plane = base_plane.Clone()
        plane.Translate(Vector3d(0, 0, i * layer_height))
        plane.Translate(Vector3d(offset_x, offset_y, 0))
        plane.Rotate(rotation * (3.14159 / 180), plane.ZAxis)

        # Define the corners of the layer
        box = Box(plane, [Rhino.Geometry.Point3d(0, 0, 0),
                          Rhino.Geometry.Point3d(width, 0, 0),
                          Rhino.Geometry.Point3d(width, depth, 0),
                          Rhino.Geometry.Point3d(0, depth, 0),
                          Rhino.Geometry.Point3d(0, 0, layer_thickness),
                          Rhino.Geometry.Point3d(width, 0, layer_thickness),
                          Rhino.Geometry.Point3d(width, depth, layer_thickness),
                          Rhino.Geometry.Point3d(0, depth, layer_thickness)])

        # Convert the box to a brep and add to the list
        brep = box.ToBrep()
        layers.append(brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers(10.0, 5.0, 20.0, 4, 0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers(15.0, 10.0, 30.0, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers(8.0, 6.0, 15.0, 5, 0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers(12.0, 8.0, 25.0, 5, 0.6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers(20.0, 10.0, 40.0, 8, 0.2, seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
