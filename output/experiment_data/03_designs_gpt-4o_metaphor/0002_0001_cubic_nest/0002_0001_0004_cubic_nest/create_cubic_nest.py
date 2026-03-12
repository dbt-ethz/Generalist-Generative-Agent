# Created for 0002_0001_cubic_nest.json

""" Summary:
The function `create_cubic_nest` generates an architectural concept model inspired by the metaphor of a "Cubic nest." It creates a series of interlocking cubic volumes that reflect the metaphor's key traits, such as complexity and interconnectedness. Each cube is generated with random offsets, allowing for overlapping structures, while voids are incorporated within the cubes to enhance spatial dynamics. The parameters control the size, number, overlap, and void proportions, resulting in a cohesive yet distinct architectural composition. Ultimately, the function outputs a collection of geometries that embody the protective and exploratory essence of the "Cubic nest" design concept."""

#! python 3
function_code = """def create_cubic_nest(base_size, cube_count, overlap_ratio, void_ratio):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor.
    
    Parameters:
    - base_size (float): The base size of the primary cube in meters.
    - cube_count (int): The number of interlocking cubes to generate.
    - overlap_ratio (float): The amount of overlap between cubes, as a fraction of the cube size.
    - void_ratio (float): The proportion of voids within the cubes, as a fraction of the cube volume.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of brep geometries representing the solid and void spaces.
    \"""
    
    import Rhino.Geometry as rg
    import random
    
    random.seed(42)  # Ensure replicability
    
    # Define cube size and overlap
    cube_size = base_size
    overlap_distance = cube_size * overlap_ratio
    void_volume = cube_size ** 3 * void_ratio
    
    # Initialize a list to hold the resulting geometries
    geometries = []
    
    # Function to create a cube centered at (x, y, z)
    def create_cube(center, size):
        box_corners = [
            rg.Point3d(center.X - size / 2, center.Y - size / 2, center.Z - size / 2),
            rg.Point3d(center.X + size / 2, center.Y - size / 2, center.Z - size / 2),
            rg.Point3d(center.X + size / 2, center.Y + size / 2, center.Z - size / 2),
            rg.Point3d(center.X - size / 2, center.Y + size / 2, center.Z - size / 2),
            rg.Point3d(center.X - size / 2, center.Y - size / 2, center.Z + size / 2),
            rg.Point3d(center.X + size / 2, center.Y - size / 2, center.Z + size / 2),
            rg.Point3d(center.X + size / 2, center.Y + size / 2, center.Z + size / 2),
            rg.Point3d(center.X - size / 2, center.Y + size / 2, center.Z + size / 2)
        ]
        box = rg.Box(rg.BoundingBox(box_corners))
        return box.ToBrep()
    
    # Generate cubes with random offsets for interlocking
    for i in range(cube_count):
        offset_x = random.uniform(-overlap_distance, overlap_distance)
        offset_y = random.uniform(-overlap_distance, overlap_distance)
        offset_z = random.uniform(-overlap_distance, overlap_distance)
        
        center = rg.Point3d(offset_x, offset_y, offset_z)
        cube = create_cube(center, cube_size)
        
        # Generate voids within the cube
        void_size = cube_size * void_ratio ** (1/3)  # Calculate the size of the void cube
        void_center = rg.Point3d(
            center.X + random.uniform(-cube_size / 4, cube_size / 4),
            center.Y + random.uniform(-cube_size / 4, cube_size / 4),
            center.Z + random.uniform(-cube_size / 4, cube_size / 4)
        )
        void_cube = create_cube(void_center, void_size)
        
        # Subtract voids from the solid cube
        bool_result = rg.Brep.CreateBooleanDifference(cube, void_cube, 0.01)
        
        if bool_result:
            geometries.extend(bool_result)
        else:
            geometries.append(cube)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest(2.0, 5, 0.3, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest(1.5, 10, 0.2, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest(3.0, 8, 0.25, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest(2.5, 6, 0.4, 0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest(4.0, 12, 0.15, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
