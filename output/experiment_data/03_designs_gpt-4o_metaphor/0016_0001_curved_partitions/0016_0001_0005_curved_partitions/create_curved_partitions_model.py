# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function, `create_curved_partitions_model`, generates an architectural concept model inspired by the metaphor of "curved partitions." It constructs a series of fluid, organic partitions that transition smoothly, enhancing spatial dynamics. By utilizing parameters such as base radius, height, number of partitions, and curvature, the model creates diverse configurations of curves that evoke a sense of continuity and intimacy. Each partition is designed to foster exploration and interaction, reflecting the metaphor's emphasis on soft boundaries and natural progression. The resulting geometries illustrate the metaphor's essence, showcasing elegance and inviting engagement within the architectural space."""

#! python 3
function_code = """def create_curved_partitions_model(base_radius=10.0, height=5.0, num_partitions=5, curvature=0.5, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'curved partitions'.
    
    This model is characterized by fluidity and organic movement, with partitions that transition smoothly,
    creating intimate and private areas within a larger open space. The design uses curves for continuity and 
    natural progression, encouraging exploration and interaction with the environment.
    
    Parameters:
    - base_radius (float): The radius of the base circle defining the core area of the model, in meters.
    - height (float): The height of the partitions, in meters.
    - num_partitions (int): The number of curved partitions to create.
    - curvature (float): A factor controlling the amount of curvature in the partitions.
    - seed (int): Seed for random number generator to ensure replicability.
    
    Returns:
    - List of RhinoCommon Brep objects representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Set seed for replicability
    random.seed(seed)
    
    partitions = []
    
    # Create partitions
    for i in range(num_partitions):
        # Random angle for the base curve start and end
        start_angle = random.uniform(0, 2 * math.pi)
        end_angle = start_angle + random.uniform(math.pi / 4, math.pi / 2)
        
        # Create base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        
        # Define points on the base circle for start and end of the partition
        start_point = base_circle.PointAt(start_angle)
        end_point = base_circle.PointAt(end_angle)
        
        # Define a mid-point to control curvature
        mid_angle = (start_angle + end_angle) / 2
        mid_point = base_circle.PointAt(mid_angle)
        mid_point += rg.Vector3d(random.uniform(-curvature, curvature), random.uniform(-curvature, curvature), 0)
        
        # Create a 3-point arc
        arc = rg.Arc(start_point, mid_point, end_point)
        
        # Create a vertical line to define the height of the partition
        vertical_line = rg.Line(arc.StartPoint, rg.Point3d(arc.StartPoint.X, arc.StartPoint.Y, height))
        
        # Sweep the arc along the vertical line to create a surface
        sweep = rg.SweepOneRail()
        partition_surface = sweep.PerformSweep(vertical_line.ToNurbsCurve(), arc.ToNurbsCurve())[0]
        
        # Append the surface itself as a Brep
        partitions.append(partition_surface)
    
    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(base_radius=12.0, height=6.0, num_partitions=8, curvature=0.7, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(base_radius=15.0, height=7.0, num_partitions=10, curvature=0.3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(base_radius=8.0, height=4.0, num_partitions=6, curvature=0.4, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(base_radius=14.0, height=5.5, num_partitions=7, curvature=0.6, seed=33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(base_radius=11.0, height=5.0, num_partitions=4, curvature=0.8, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
