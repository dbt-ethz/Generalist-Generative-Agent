# Created for 0004_0001_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Interlocking Layers." It creates multiple overlapping layers with varying heights and offsets, reflecting the complexity and dynamism suggested by the metaphor. Each layer is represented as a three-dimensional box, whose dimensions and positions are randomized within specified constraints, ensuring a unique arrangement. This results in interconnected planes that exhibit both visual depth and spatial variety. By adjusting parameters like base dimensions and layer count, the function produces diverse models that embody the principles of openness and separation inherent in the interlocking layers concept."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length=10, base_width=8, height_variation=4, layer_count=3, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    Parameters:
    - base_length (float): The base length of the model.
    - base_width (float): The base width of the model.
    - height_variation (float): The maximum variation in height among different layers.
    - layer_count (int): The number of interlocking layers to create.
    - seed (int): Seed for randomness to ensure replicability.
    
    Returns:
    - List of RhinoCommon Brep objects representing the interlocking layers of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set seed for randomness
    random.seed(seed)
    
    # List to store the resulting geometries
    geometries = []
    
    # Base plane for construction
    base_plane = rg.Plane.WorldXY

    for i in range(layer_count):
        # Random offset for interlocking effect
        offset_x = random.uniform(-base_length / 4, base_length / 4)
        offset_y = random.uniform(-base_width / 4, base_width / 4)
        
        # Random height for each layer
        height = base_width / 2 + random.uniform(0, height_variation)
        
        # Create a box representing each layer
        origin = rg.Point3d(offset_x, offset_y, i * height_variation / 2)
        box_corners = [
            origin,
            rg.Point3d(origin.X + base_length, origin.Y, origin.Z),
            rg.Point3d(origin.X + base_length, origin.Y + base_width, origin.Z),
            rg.Point3d(origin.X, origin.Y + base_width, origin.Z),
            rg.Point3d(origin.X, origin.Y, origin.Z + height),
            rg.Point3d(origin.X + base_length, origin.Y, origin.Z + height),
            rg.Point3d(origin.X + base_length, origin.Y + base_width, origin.Z + height),
            rg.Point3d(origin.X, origin.Y + base_width, origin.Z + height),
        ]
        
        # Create a Brep from box corners
        brep = rg.Brep.CreateFromBox(box_corners)
        
        if brep:
            geometries.append(brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(base_length=12, base_width=10, height_variation=5, layer_count=4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(base_length=15, base_width=12, height_variation=3, layer_count=5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(base_length=8, base_width=6, height_variation=2, layer_count=2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(base_length=20, base_width=15, height_variation=6, layer_count=6, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(base_length=14, base_width=10, height_variation=4, layer_count=4, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
