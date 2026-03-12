# Created for 0004_0005_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model that embodies the "Interlocking Layers" metaphor. It constructs a series of intersecting and overlapping planes, reflecting the design's dynamic and multifaceted nature. By varying the rotation and translation of each layer, the function creates unique spatial relationships that embody both openness and intimacy. The parameters allow for customization of size and number of layers, while the use of randomization ensures diverse configurations. The resulting 3D geometries illustrate the metaphor's complexity, showcasing how each layer interacts to form a cohesive yet intricate architectural form."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, height, num_layers, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    The model consists of intersecting and overlapping planes or volumes, creating a dynamic
    and multifaceted form. The function returns a list of 3D geometries representing the 
    concept model.

    Parameters:
    - base_length (float): The length of the base layer in meters.
    - base_width (float): The width of the base layer in meters.
    - height (float): The height of each layer in meters.
    - num_layers (int): The number of interlocking layers.
    - seed (int): Seed for randomization to ensure replicability (default is 42).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the seed for randomization
    random.seed(seed)
    
    # Initialize an empty list to store the geometry
    geometries = []
    
    # Generate the base layer
    base_plane = rg.Plane.WorldXY
    base_rect = rg.Rectangle3d(base_plane, base_length, base_width)
    base_brep = rg.Brep.CreateFromCornerPoints(base_rect.Corner(0), base_rect.Corner(1), 
                                               base_rect.Corner(2), base_rect.Corner(3), 0.01)
    geometries.append(base_brep)
    
    # Generate interlocking layers
    for i in range(1, num_layers + 1):
        # Randomize the rotation and translation for each layer
        angle = random.uniform(-30, 30)  # Rotation angle in degrees
        translation_x = random.uniform(-base_length/4, base_length/4)
        translation_y = random.uniform(-base_width/4, base_width/4)
        
        # Create a new plane for each layer
        layer_plane = rg.Plane(base_plane)
        layer_plane.Translate(rg.Vector3d(0, 0, i * height))
        layer_plane.Rotate(math.radians(angle), layer_plane.ZAxis)
        
        # Create the rectangle for the layer
        layer_rect = rg.Rectangle3d(layer_plane, base_length, base_width)
        layer_rect.Transform(rg.Transform.Translation(translation_x, translation_y, 0))
        
        # Create the brep for the layer
        layer_brep = rg.Brep.CreateFromCornerPoints(layer_rect.Corner(0), layer_rect.Corner(1), 
                                                    layer_rect.Corner(2), layer_rect.Corner(3), 0.01)
        geometries.append(layer_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(5.0, 3.0, 2.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(10.0, 6.0, 1.5, 3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(7.0, 4.0, 3.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(8.0, 5.0, 2.5, 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(6.0, 4.5, 2.0, 2, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
