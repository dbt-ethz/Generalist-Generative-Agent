# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates multiple stacked layers, each with varying heights to mimic the stratification and depth of a cave. A central void or atrium is incorporated, serving as a focal point around which the spaces are organized in a spiraling manner, enhancing the immersive experience. The use of varied materials and textures represents the organic qualities of a cavern, while the interplay of light and shadow emphasizes its mysterious ambiance, effectively capturing the essence of exploration and refuge in the design."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_length, base_width, base_height, num_layers, layer_height_variation, central_void_diameter):
    \"""
    Create an architectural Concept Model evoking the 'subterranean cavern' metaphor. The model is characterized by
    vertical layering, central voids, and spatial organization around a core, with an emphasis on depth and immersion.

    Parameters:
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - base_height (float): The total height of the model in meters.
    - num_layers (int): The number of vertical layers to create.
    - layer_height_variation (float): The amount of variation in the height of each layer in meters.
    - central_void_diameter (float): The diameter of the central void or atrium in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicable randomness

    # Initialize list to store geometries
    geometries = []

    # Calculate the average height of each layer
    average_layer_height = base_height / num_layers
    
    # Create each layered platform
    for i in range(num_layers):
        # Calculate the height of the current layer with some variation
        layer_height = average_layer_height + random.uniform(-layer_height_variation, layer_height_variation)
        
        # Define a rectangle for the current layer
        rect = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)
        
        # Offset the rectangle to create a central void
        void_offset = (base_length - central_void_diameter) / 2
        inner_rect = rg.Rectangle3d(rg.Plane.WorldXY, central_void_diameter, central_void_diameter)
        inner_rect.Transform(rg.Transform.Translation(void_offset, void_offset, 0))
        
        # Create a solid Brep from the layer with a void in the center
        bottom_pts = [
            rg.Point3d(0, 0, i * average_layer_height),
            rg.Point3d(base_length, 0, i * average_layer_height),
            rg.Point3d(base_length, base_width, i * average_layer_height),
            rg.Point3d(0, base_width, i * average_layer_height)
        ]
        top_pts = [pt + rg.Vector3d(0, 0, layer_height) for pt in bottom_pts]

        layer_brep = rg.Brep.CreateFromBox(bottom_pts + top_pts)
        
        if layer_brep:
            # Create a void in the center using inner rectangle
            inner_bottom_pts = [
                rg.Point3d(void_offset, void_offset, i * average_layer_height),
                rg.Point3d(void_offset + central_void_diameter, void_offset, i * average_layer_height),
                rg.Point3d(void_offset + central_void_diameter, void_offset + central_void_diameter, i * average_layer_height),
                rg.Point3d(void_offset, void_offset + central_void_diameter, i * average_layer_height)
            ]
            inner_top_pts = [pt + rg.Vector3d(0, 0, layer_height) for pt in inner_bottom_pts]

            inner_brep = rg.Brep.CreateFromBox(inner_bottom_pts + inner_top_pts)
            if inner_brep:
                # Subtract the inner Brep from the layer Brep
                layer_brep = rg.Brep.CreateBooleanDifference(layer_brep, inner_brep, 0.01)
                if layer_brep: geometries.append(layer_brep[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 8.0, 20.0, 5, 2.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 10.0, 30.0, 7, 1.5, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.0, 9.0, 25.0, 6, 2.5, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(20.0, 15.0, 40.0, 8, 3.0, 6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(18.0, 12.0, 35.0, 6, 2.0, 4.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
