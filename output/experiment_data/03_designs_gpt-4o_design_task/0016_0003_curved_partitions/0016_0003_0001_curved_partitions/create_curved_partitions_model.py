# Created for 0016_0003_curved_partitions.json

""" Summary:
The function generates an architectural concept model by creating a series of interconnected curvilinear partitions that embody the metaphor of "curved partitions." It constructs these partitions as dynamic, flowing surfaces using parameters like base radius, height, number of partitions, and curvature factor. Through a randomized approach, each partition is defined by a unique set of control points that guide its curve, allowing for organic movement and seamless transitions between spaces. The resulting geometries enhance light and shadow interplay, fostering an atmosphere of tranquility and exploration, while maintaining a fluid aesthetic aligned with the metaphor's intent."""

#! python 3
function_code = """def create_curved_partitions_model(base_radius=10, height=5, num_partitions=5, curvature_factor=0.5, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'curved partitions' metaphor.
    
    This function generates a series of interconnected curvilinear partitions that define spaces with soft, 
    flowing boundaries. The partitions are arranged to create a spatial narrative of division and continuity, 
    enhancing the experiential quality through dynamic light and shadow interplay.
    
    Parameters:
    - base_radius (float): The base radius around which the partitions are arranged.
    - height (float): The height of the partitions.
    - num_partitions (int): The number of curvilinear partitions to create.
    - curvature_factor (float): A factor that influences the degree of curvature in the partitions.
    - seed (int): A seed for randomness to ensure replicability of the design.
    
    Returns:
    - list: A list of RhinoCommon Brep geometries representing the partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    partitions = []
    angle_increment = 2 * math.pi / num_partitions
    
    for i in range(num_partitions):
        angle = i * angle_increment
        center_point = rg.Point3d(base_radius * math.cos(angle), base_radius * math.sin(angle), 0)
        
        # Create a base curve with a random amplitude for curvature
        amplitude = random.uniform(0.1, curvature_factor)
        points = [
            rg.Point3d(center_point.X + random.uniform(-amplitude, amplitude), center_point.Y, 0),
            rg.Point3d(center_point.X, center_point.Y + random.uniform(-amplitude, amplitude), height / 3),
            rg.Point3d(center_point.X, center_point.Y, 2 * height / 3),
            rg.Point3d(center_point.X + random.uniform(-amplitude, amplitude), center_point.Y, height)
        ]
        
        curve = rg.NurbsCurve.Create(False, 3, points)
        
        # Create a surface from the curve by revolving around the center point
        revolve_axis = rg.Line(center_point, rg.Point3d(center_point.X, center_point.Y, height))
        surface = rg.RevSurface.Create(curve, revolve_axis)
        
        # Convert surface to Brep for output
        brep = surface.ToBrep()
        partitions.append(brep)
    
    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(base_radius=15, height=8, num_partitions=6, curvature_factor=0.7, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(base_radius=12, height=6, num_partitions=8, curvature_factor=0.6, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(base_radius=20, height=10, num_partitions=4, curvature_factor=0.4, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(base_radius=18, height=7, num_partitions=10, curvature_factor=0.8, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(base_radius=22, height=9, num_partitions=7, curvature_factor=0.9, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
