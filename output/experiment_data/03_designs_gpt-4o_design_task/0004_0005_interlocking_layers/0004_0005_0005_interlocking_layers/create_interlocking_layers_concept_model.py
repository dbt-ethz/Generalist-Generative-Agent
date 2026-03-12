# Created for 0004_0005_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_concept_model`, generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping and intersecting planes or volumes. It uses randomized parameters for the dimensions and positioning of each layer, ensuring a dynamic and multifaceted structure. The model illustrates diverse spatial experiences, balancing openness and seclusion, by varying the size, orientation, and height of each layer. This complexity mimics the metaphor's emphasis on intricate relationships between spaces, allowing for a cohesive yet diverse architectural expression that captures the essence of interlocking layers."""

#! python 3
function_code = """def create_interlocking_layers_concept_model(base_length, base_width, height, num_layers, seed):
    \"""
    Create an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function generates a structure composed of intersecting and overlapping planes or volumes,
    illustrating diverse spatial experiences with varying degrees of openness and seclusion.

    Parameters:
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - height (float): The maximum height of the model in meters.
    - num_layers (int): The number of interlocking layers to create.
    - seed (int): A seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Plane, Box, Brep, Point3d

    random.seed(seed)
    geometries = []

    # Define the base plane
    base_plane = Plane(Point3d(0, 0, 0), Rhino.Geometry.Vector3d.ZAxis)

    for i in range(num_layers):
        # Randomly decide orientation and position changes
        length_variation = random.uniform(0.5, 1.5)
        width_variation = random.uniform(0.5, 1.5)
        height_variation = height / num_layers

        offset_x = random.uniform(-base_length / 4, base_length / 4)
        offset_y = random.uniform(-base_width / 4, base_width / 4)
        offset_z = i * height_variation

        # Create a plane for each layer
        layer_plane = Plane(Point3d(offset_x, offset_y, offset_z), Rhino.Geometry.Vector3d.ZAxis)

        # Create a box representing a layer
        layer_box = Box(layer_plane, Rhino.Geometry.Interval(0, base_length * length_variation),
                        Rhino.Geometry.Interval(0, base_width * width_variation),
                        Rhino.Geometry.Interval(0, height_variation))

        # Convert the box to a Brep and add it to the list
        layer_brep = layer_box.ToBrep()
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_concept_model(10.0, 5.0, 15.0, 4, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_concept_model(8.0, 4.0, 12.0, 6, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_concept_model(12.0, 6.0, 10.0, 5, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_concept_model(15.0, 7.0, 20.0, 3, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_concept_model(9.0, 3.0, 18.0, 7, 32)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
