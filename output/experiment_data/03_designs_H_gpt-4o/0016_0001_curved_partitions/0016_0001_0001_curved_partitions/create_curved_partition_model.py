# Created for 0016_0001_curved_partitions.json

""" Summary:
The function `create_curved_partition_model` generates an architectural concept model by creating a series of interlocking, flowing curved partitions. Utilizing specified parameters such as width, depth, height, and the number of curves, the function defines smooth, organic shapes that embody the metaphor of 'curved partitions'. It employs random variations in curve heights to enhance dynamism, allowing for seamless spatial transitions. By revolving NURBS curves around a vertical axis, the function produces 3D geometries that suggest movement and continuity. Ultimately, this approach fosters a harmonious environment, encouraging exploration and interaction within the architectural space."""

#! python 3
function_code = """def create_curved_partition_model(width, depth, height, num_curves, curve_height_variation, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'curved partitions'.
    
    This function generates a series of interlocking, flowing partitions that define spaces 
    in a fluid and organic manner. The partitions transition smoothly from one to another, 
    allowing for dynamic spatial relationships. The design emphasizes movement and continuity.

    Parameters:
    - width: float, the total width of the area where partitions will be created.
    - depth: float, the total depth of the area for the partitions.
    - height: float, the average height of the partitions.
    - num_curves: int, the number of curved partitions to create.
    - curve_height_variation: float, the range of height variation for the curves to add dynamism.
    - seed: int, optional, the seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometry of the partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    breps = []
    interval_x = width / (num_curves + 1)
    
    for i in range(num_curves):
        # Define control points for a smooth curve
        start_x = (i + 1) * interval_x
        start_y = random.uniform(0, depth / 3)
        end_y = random.uniform(2 * depth / 3, depth)
        mid_y = random.uniform(start_y, end_y)
        
        start_point = rg.Point3d(start_x, start_y, 0)
        mid_point = rg.Point3d(start_x, mid_y, height + random.uniform(-curve_height_variation, curve_height_variation))
        end_point = rg.Point3d(start_x, end_y, 0)
        
        control_points = [start_point, mid_point, end_point]
        
        # Create a NURBS curve from control points
        nurbs_curve = rg.NurbsCurve.Create(False, 2, control_points)
        
        # Create a vertical partition by revolving the curve around a vertical axis
        axis = rg.Line(start_point, rg.Point3d(start_point.X, start_point.Y, start_point.Z + height))
        revolve_surface = rg.RevSurface.Create(nurbs_curve, axis)
        
        # Convert surface to a Brep and add to the list if successful
        if revolve_surface:
            brep = revolve_surface.ToBrep()
            breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partition_model(10.0, 5.0, 3.0, 4, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_model(15.0, 7.0, 4.0, 6, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_model(20.0, 10.0, 5.0, 5, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_model(12.0, 6.0, 3.5, 3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_model(25.0, 12.0, 6.0, 8, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
