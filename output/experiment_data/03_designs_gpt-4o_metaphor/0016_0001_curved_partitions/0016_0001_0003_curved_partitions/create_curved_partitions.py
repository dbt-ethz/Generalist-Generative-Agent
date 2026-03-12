# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function, `create_curved_partitions`, generates an architectural concept model based on the metaphor of "curved partitions." It creates a series of fluid, curved walls that embody organic movement and continuity. By defining parameters such as width, depth, height, and the number of partitions, the function uses randomization to establish start, control, and end points for each curve, enhancing the dynamic nature of the design. The extruded surfaces from these curves create enclosures that foster interaction while maintaining a sense of openness, aligning with the metaphor's emphasis on fluidity and spatial transition."""

#! python 3
function_code = """def create_curved_partitions(width, depth, height, num_partitions, seed=42):
    \"""
    Create a conceptual architectural model based on the metaphor of 'curved partitions'.
    
    This function generates a series of curved partition walls within a defined space, 
    creating a fluid and dynamic spatial organization. The partitions are designed to 
    introduce a sense of continuity and natural progression within the space, encouraging 
    exploration and interaction.

    Parameters:
    - width (float): The width of the space in meters.
    - depth (float): The depth of the space in meters.
    - height (float): The height of the partitions in meters.
    - num_partitions (int): The number of curved partitions to generate.
    - seed (int, optional): The seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    partitions = []
    for _ in range(num_partitions):
        # Randomly generate the start and end points for each partition
        start_x = random.uniform(0, width)
        start_y = random.uniform(0, depth)
        end_x = random.uniform(0, width)
        end_y = random.uniform(0, depth)
        
        # Create a curve between the start and end points with a control point to add curvature
        control_x = (start_x + end_x) / 2 + random.uniform(-width * 0.2, width * 0.2)
        control_y = (start_y + end_y) / 2 + random.uniform(-depth * 0.2, depth * 0.2)
        
        start_point = rg.Point3d(start_x, start_y, 0)
        control_point = rg.Point3d(control_x, control_y, height / 2)
        end_point = rg.Point3d(end_x, end_y, 0)
        
        curve = rg.NurbsCurve.Create(False, 2, [start_point, control_point, end_point])
        
        # Extrude the curve vertically to create a partition wall
        extrusion_vector = rg.Vector3d(0, 0, height)
        surface = rg.Surface.CreateExtrusion(curve, extrusion_vector)
        
        if surface:
            partition = rg.Brep.CreateFromSurface(surface)
            partitions.append(partition)
    
    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions(10.0, 5.0, 3.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions(15.0, 10.0, 5.0, 6, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions(8.0, 4.0, 2.5, 3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions(12.0, 6.0, 4.0, 5, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions(20.0, 15.0, 7.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
