# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model inspired by the metaphor "Porous fractured monolith." It starts with a solid base mass, representing the monolithic aspect, and introduces irregular fissures to create a sense of fragmentation and movement. The function uses parameters to define the size, number, and depth of these fissures, which enhances visual and physical connections between spaces, promoting light penetration and airflow. By balancing solidity with dynamic voids, the model embodies exploration and interaction, fostering engagement between private and communal areas, ultimately reflecting the metaphor's essence."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, fissure_count, max_fissure_depth, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Porous fractured monolith' metaphor.
    
    The model begins as a cohesive monolithic mass, with irregular fissures and voids introduced to 
    convey a sense of movement and complexity. The voids enhance light penetration and spatial interaction.

    Parameters:
    - base_length (float): The length of the monolith base in meters.
    - base_width (float): The width of the monolith base in meters.
    - base_height (float): The height of the monolith base in meters.
    - fissure_count (int): The number of fissures to introduce.
    - max_fissure_depth (float): The maximum depth of each fissure.
    - seed (int, optional): Seed for random number generation to ensure replicable results.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries including the main mass and the voids.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Box, Brep, Plane, Point3d, Vector3d, Line, Surface, BrepFace, Transform

    # Set random seed
    random.seed(seed)

    # Create the base monolithic mass
    base_plane = Plane(Point3d(0, 0, 0), Vector3d.ZAxis)
    base_corners = [
        Point3d(0, 0, 0),
        Point3d(base_length, 0, 0),
        Point3d(base_length, base_width, 0),
        Point3d(0, base_width, 0),
        Point3d(0, 0, base_height),
        Point3d(base_length, 0, base_height),
        Point3d(base_length, base_width, base_height),
        Point3d(0, base_width, base_height)
    ]
    monolith = Box(base_plane, base_corners).ToBrep()

    # Function to create random fissures
    def create_fissure():
        start_x = random.uniform(0, base_length)
        start_y = random.uniform(0, base_width)
        start_point = Point3d(start_x, start_y, 0)
        end_point = Point3d(
            start_x + random.uniform(-max_fissure_depth, max_fissure_depth),
            start_y + random.uniform(-max_fissure_depth, max_fissure_depth),
            base_height
        )
        line = Line(start_point, end_point)
        # Create a cutting plane along the fissure line
        normal = Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 0)
        cutting_plane = Plane(line.PointAt(0.5), normal)
        cutting_surface = Surface.CreateExtrusion(line.ToNurbsCurve(), normal)
        return monolith.Trim(cutting_surface.ToBrep(), 0.01)

    # List to hold the final geometry
    geometries = [monolith]

    # Generate fissures
    for _ in range(fissure_count):
        fissure = create_fissure()
        if fissure:
            geometries.append(fissure)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(5.0, 3.0, 7.0, 10, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(10.0, 8.0, 12.0, 15, 3.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(4.0, 4.0, 10.0, 8, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(6.0, 5.0, 9.0, 20, 4.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(8.0, 6.0, 5.0, 12, 3.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
