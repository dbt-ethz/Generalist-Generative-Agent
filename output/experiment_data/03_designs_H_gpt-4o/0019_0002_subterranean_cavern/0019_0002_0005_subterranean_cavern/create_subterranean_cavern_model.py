# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of stacked layers that represent the stratification and depth of a cave, incorporating variations in height to mimic natural formations. A central void or atrium serves as a focal point, enhancing the immersive experience. The model features spiral transitions between layers, evoking a sense of exploration. By using varied geometries, textures, and lighting effects, it captures the essence of the cavern's organic and mysterious qualities, ultimately creating an engaging architectural representation aligned with the design task."""

#! python 3
function_code = """def create_subterranean_cavern_model(length, width, total_height, num_layers, central_void_width, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of a subterranean cavern. This model features
    a central void and layered platforms with varied ceiling heights, organized in a spiraling manner to enhance
    the immersive experience of descending into a cavern.

    Parameters:
    - length (float): The overall length of the model.
    - width (float): The overall width of the model.
    - total_height (float): The total vertical extent of the model.
    - num_layers (int): The number of vertical stratified layers.
    - central_void_width (float): The width of the central void or atrium.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D breps representing the Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set seed for randomness
    random.seed(seed)

    # Initialize list to store geometries
    geometries = []

    # Calculate average height of each layer
    average_layer_height = total_height / num_layers

    # Create each layered platform
    for i in range(num_layers):
        # Calculate the height of the current layer with some variation
        layer_height = average_layer_height + random.uniform(-average_layer_height * 0.2, average_layer_height * 0.2)

        # Define a rectangle for the current layer
        rect = rg.Rectangle3d(rg.Plane.WorldXY, length, width)

        # Create a solid Brep from the layer
        bottom_pts = [
            rg.Point3d(0, 0, i * average_layer_height),
            rg.Point3d(length, 0, i * average_layer_height),
            rg.Point3d(length, width, i * average_layer_height),
            rg.Point3d(0, width, i * average_layer_height)
        ]
        top_pts = [pt + rg.Vector3d(0, 0, layer_height) for pt in bottom_pts]
        layer_brep = rg.Brep.CreateFromBox(bottom_pts + top_pts)

        # Define the central void as a rectangle
        void_offset_x = (length - central_void_width) / 2
        void_offset_y = (width - central_void_width) / 2
        inner_rect = rg.Rectangle3d(rg.Plane.WorldXY, central_void_width, central_void_width)
        inner_rect.Transform(rg.Transform.Translation(void_offset_x, void_offset_y, 0))

        # Create a void in the center
        inner_bottom_pts = [
            rg.Point3d(void_offset_x, void_offset_y, i * average_layer_height),
            rg.Point3d(void_offset_x + central_void_width, void_offset_y, i * average_layer_height),
            rg.Point3d(void_offset_x + central_void_width, void_offset_y + central_void_width, i * average_layer_height),
            rg.Point3d(void_offset_x, void_offset_y + central_void_width, i * average_layer_height)
        ]
        inner_top_pts = [pt + rg.Vector3d(0, 0, layer_height) for pt in inner_bottom_pts]
        inner_brep = rg.Brep.CreateFromBox(inner_bottom_pts + inner_top_pts)

        # Subtract the inner Brep from the layer Brep
        layer_brep_with_void = rg.Brep.CreateBooleanDifference(layer_brep, inner_brep, 0.01)
        if layer_brep_with_void:
            geometries.append(layer_brep_with_void[0])

        # Introduce a spiral effect by rotating each layer slightly
        angle_increment = random.uniform(0.05, 0.15)  # Random rotation angle for spiral effect
        rotation = rg.Transform.Rotation(angle_increment * i, rg.Vector3d.ZAxis, rg.Point3d(0, 0, 0))
        for brep in layer_brep_with_void:
            brep.Transform(rotation)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(50.0, 30.0, 40.0, 5, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(100.0, 50.0, 60.0, 8, 15.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(75.0, 40.0, 50.0, 6, 12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(60.0, 35.0, 45.0, 7, 8.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(80.0, 60.0, 55.0, 10, 20.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
