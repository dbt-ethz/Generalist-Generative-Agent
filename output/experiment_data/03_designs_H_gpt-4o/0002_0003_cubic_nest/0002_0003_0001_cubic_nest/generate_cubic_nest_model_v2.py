# Created for 0002_0003_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic nest" metaphor by creating interwoven cubic volumes that embody a sense of enclosure and openness. It arranges a specified number of cubes in a layered manner, applying random offsets to enhance the interconnectivity and visual complexity of the structure. Each cube is represented as a Brep object, while bridges or ramps connect the cubes, facilitating movement and exploration. By manipulating the size, layer height, and connection width, the function creates a dynamic spatial experience, highlighting the interplay of solid and void, and fostering an environment of curiosity within the nested design."""

#! python 3
function_code = """def generate_cubic_nest_model_v2(base_size, num_cubes, layer_height, connection_width, randomness_seed=42):
    \"""
    Generates a 3D architectural concept model based on the 'Cubic nest' metaphor.
    This model consists of interwoven cubic volumes that create a protective and multi-dimensional enclosure.
    
    Parameters:
        base_size (float): The base size of each cubic module in meters.
        num_cubes (int): The number of cubes to generate in the model.
        layer_height (float): The height of each layer of cubes.
        connection_width (float): The width of connections (bridges or ramps) between cubes.
        randomness_seed (int, optional): Seed for random number generator to ensure replicability. Default is 42.
    
    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D geometry of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Initialize the random seed
    random.seed(randomness_seed)
    
    # Initialize the list to hold the resulting Breps
    model_breps = []
    
    # Create cubes and arrange them in a nested pattern
    for i in range(num_cubes):
        # Random offsets to create a sense of interweaving
        x_offset = random.uniform(-base_size/4, base_size/4)
        y_offset = random.uniform(-base_size/4, base_size/4)
        z_offset = i * layer_height
        
        # Base point for the cube
        base_point = rg.Point3d(x_offset, y_offset, z_offset)
        
        # Create a cube (as a Brep) at the base point
        cube_corners = [
            rg.Point3d(base_point.X, base_point.Y, base_point.Z),
            rg.Point3d(base_point.X + base_size, base_point.Y, base_point.Z),
            rg.Point3d(base_point.X + base_size, base_point.Y + base_size, base_point.Z),
            rg.Point3d(base_point.X, base_point.Y + base_size, base_point.Z),
            rg.Point3d(base_point.X, base_point.Y, base_point.Z + base_size),
            rg.Point3d(base_point.X + base_size, base_point.Y, base_point.Z + base_size),
            rg.Point3d(base_point.X + base_size, base_point.Y + base_size, base_point.Z + base_size),
            rg.Point3d(base_point.X, base_point.Y + base_size, base_point.Z + base_size)
        ]
        
        # Create a Brep from the cube corners
        cube_brep = rg.Brep.CreateFromBox(cube_corners)
        if cube_brep:
            model_breps.append(cube_brep)
        
        # Create connection elements (bridges or ramps)
        if i < num_cubes - 1:
            next_base_point = rg.Point3d(x_offset, y_offset, z_offset + layer_height)
            connection_corners = [
                rg.Point3d(base_point.X + base_size / 2 - connection_width / 2, base_point.Y + base_size / 2 - connection_width / 2, base_point.Z + base_size),
                rg.Point3d(next_base_point.X + base_size / 2 - connection_width / 2, next_base_point.Y + base_size / 2 - connection_width / 2, next_base_point.Z),
                rg.Point3d(next_base_point.X + base_size / 2 + connection_width / 2, next_base_point.Y + base_size / 2 + connection_width / 2, next_base_point.Z),
                rg.Point3d(base_point.X + base_size / 2 + connection_width / 2, base_point.Y + base_size / 2 + connection_width / 2, base_point.Z + base_size),
                rg.Point3d(base_point.X + base_size / 2 - connection_width / 2, base_point.Y + base_size / 2 - connection_width / 2, base_point.Z + base_size),
                rg.Point3d(next_base_point.X + base_size / 2 - connection_width / 2, next_base_point.Y + base_size / 2 - connection_width / 2, next_base_point.Z + connection_width),
                rg.Point3d(next_base_point.X + base_size / 2 + connection_width / 2, next_base_point.Y + base_size / 2 + connection_width / 2, next_base_point.Z + connection_width),
                rg.Point3d(base_point.X + base_size / 2 + connection_width / 2, base_point.Y + base_size / 2 + connection_width / 2, base_point.Z + base_size)
            ]
            connection_brep = rg.Brep.CreateFromBox(connection_corners)
            if connection_brep:
                model_breps.append(connection_brep)
    
    return model_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_model_v2(base_size=2.0, num_cubes=5, layer_height=3.0, connection_width=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_model_v2(base_size=1.5, num_cubes=10, layer_height=2.0, connection_width=0.3, randomness_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_model_v2(base_size=3.0, num_cubes=8, layer_height=4.0, connection_width=0.7, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_model_v2(base_size=2.5, num_cubes=6, layer_height=2.5, connection_width=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_model_v2(base_size=1.0, num_cubes=12, layer_height=2.0, connection_width=0.2, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
