# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The provided function, `create_subterranean_cavern_model`, generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates stacked layers with random horizontal offsets, simulating the stratified nature of a cave. Each layer integrates a central void, mirroring a cavern's central chamber, and is designed to evoke vertical movement and exploration. By controlling parameters such as layer height, offset, and void size, the function captures the essence of depth and immersion. The resulting geometries emphasize varying textures and shadows, enhancing the organic and mysterious qualities associated with a subterranean environment."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_length, base_width, total_height, num_layers, central_void_size, layer_offset_factor, seed=101):
    \"""
    Generates an architectural Concept Model based on the 'subterranean cavern' metaphor. The model features 
    stacked, offset layers around a central void, creating a sense of depth and exploration reminiscent of 
    a cavern's stratified and immersive spaces.

    Parameters:
    - base_length (float): The length of the model's rectangular footprint in meters.
    - base_width (float): The width of the model's rectangular footprint in meters.
    - total_height (float): The total vertical height of the model in meters.
    - num_layers (int): The number of layers to stack vertically.
    - central_void_size (float): The size of the central void's square dimension in meters.
    - layer_offset_factor (float): Factor controlling the horizontal offset shift of each layer.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Initialize the list to store geometries
    geometries = []

    # Calculate the average height of each layer
    layer_height = total_height / num_layers

    # Create each layer with random offset
    for i in range(num_layers):
        # Random offset for each layer
        offset_x = random.uniform(-layer_offset_factor, layer_offset_factor)
        offset_y = random.uniform(-layer_offset_factor, layer_offset_factor)

        # Define the base rectangle
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)
        base_rect.Transform(rg.Transform.Translation(offset_x, offset_y, i * layer_height))

        # Create the central void as a rectangle
        void_rect = rg.Rectangle3d(rg.Plane.WorldXY, central_void_size, central_void_size)
        void_offset = (base_length - central_void_size) / 2
        void_rect.Transform(rg.Transform.Translation(void_offset + offset_x, void_offset + offset_y, i * layer_height))

        # Create the layer with a void
        layer_brep = rg.Brep.CreateFromBox([
            rg.Point3d(base_rect.Corner(0)),
            rg.Point3d(base_rect.Corner(1)),
            rg.Point3d(base_rect.Corner(2)),
            rg.Point3d(base_rect.Corner(3)),
            rg.Point3d(base_rect.Corner(0) + rg.Vector3d(0, 0, layer_height)),
            rg.Point3d(base_rect.Corner(1) + rg.Vector3d(0, 0, layer_height)),
            rg.Point3d(base_rect.Corner(2) + rg.Vector3d(0, 0, layer_height)),
            rg.Point3d(base_rect.Corner(3) + rg.Vector3d(0, 0, layer_height))
        ])

        if layer_brep:
            # Create the void brep
            void_brep = rg.Brep.CreateFromBox([
                rg.Point3d(void_rect.Corner(0)),
                rg.Point3d(void_rect.Corner(1)),
                rg.Point3d(void_rect.Corner(2)),
                rg.Point3d(void_rect.Corner(3)),
                rg.Point3d(void_rect.Corner(0) + rg.Vector3d(0, 0, layer_height)),
                rg.Point3d(void_rect.Corner(1) + rg.Vector3d(0, 0, layer_height)),
                rg.Point3d(void_rect.Corner(2) + rg.Vector3d(0, 0, layer_height)),
                rg.Point3d(void_rect.Corner(3) + rg.Vector3d(0, 0, layer_height))
            ])

            # Subtract the void from the layer
            if void_brep:
                layer_with_void = rg.Brep.CreateBooleanDifference(layer_brep, void_brep, 0.01)
                if layer_with_void:
                    geometries.append(layer_with_void[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(20.0, 15.0, 30.0, 5, 5.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(10.0, 10.0, 20.0, 8, 3.0, 1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(25.0, 20.0, 40.0, 6, 6.0, 3.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(15.0, 10.0, 25.0, 4, 4.0, 2.5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(30.0, 25.0, 50.0, 7, 7.0, 4.0, seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
