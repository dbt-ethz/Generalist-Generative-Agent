# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of interlocking and overlapping cubic volumes. Each cube is randomly scaled, translated, and rotated to establish a complex, layered silhouette that emphasizes both solid and void spaces. This approach encourages exploration and discovery within the structure, reflecting the protective and interconnected qualities of the metaphor. Varying cube sizes and orientations ensure distinct spatial experiences while maintaining overall cohesiveness. The model effectively embodies the metaphor's essence, showcasing shelter and complexity through dynamic spatial relationships."""

#! python 3
function_code = """def create_cubic_nest_model(seed=42, base_cube_size=10, num_cubes=10, scale_variation=0.5):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor. 
    This model consists of interlocking and overlapping cubic volumes that form a complex, layered silhouette.
    
    Parameters:
    - seed (int): Seed for random number generator to ensure replicability.
    - base_cube_size (float): The base size of the cubes in meters.
    - num_cubes (int): The number of cubes to generate.
    - scale_variation (float): The maximum variation of the scale factor for each cube (0 to 1).
    
    Returns:
    - List of Breps: A list of 3D geometries (Breps) representing the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import math module for mathematical constants and functions

    random.seed(seed)
    
    geometries = []
    
    # Base point for the first cube
    base_point = rg.Point3d(0, 0, 0)
    
    for i in range(num_cubes):
        # Randomly scale the cube
        scale_factor = 1 + random.uniform(-scale_variation, scale_variation)
        cube_size = base_cube_size * scale_factor

        # Create a cube
        cube = rg.Box(
            rg.Plane(base_point, rg.Vector3d(1, 0, 0), rg.Vector3d(0, 1, 0)),
            rg.Interval(0, cube_size),
            rg.Interval(0, cube_size),
            rg.Interval(0, cube_size)
        ).ToBrep()
        
        # Randomly translate the cube to create an interlocking effect
        translation_vector = rg.Vector3d(
            random.uniform(-cube_size / 2, cube_size / 2),
            random.uniform(-cube_size / 2, cube_size / 2),
            random.uniform(-cube_size / 2, cube_size / 2)
        )
        cube.Transform(rg.Transform.Translation(translation_vector))
        
        # Randomly rotate the cube around its center
        center_point = cube.GetBoundingBox(True).Center
        rotation_axis = rg.Vector3d(
            random.choice([0, 1]),
            random.choice([0, 1]),
            random.choice([0, 1])
        )
        rotation_angle = random.uniform(0, math.pi / 4)  # Rotate up to 45 degrees
        cube.Transform(rg.Transform.Rotation(rotation_angle, rotation_axis, center_point))
        
        # Store the cube
        geometries.append(cube)
        
        # Move base point for the next cube
        base_point = rg.Point3d(
            base_point.X + random.uniform(0, base_cube_size),
            base_point.Y + random.uniform(0, base_cube_size),
            base_point.Z + random.uniform(0, base_cube_size)
        )
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(seed=123, base_cube_size=15, num_cubes=5, scale_variation=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(seed=99, base_cube_size=20, num_cubes=7, scale_variation=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(seed=456, base_cube_size=12, num_cubes=12, scale_variation=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(seed=1, base_cube_size=8, num_cubes=15, scale_variation=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(seed=77, base_cube_size=25, num_cubes=8, scale_variation=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
