# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model by creating a series of curved partitions that embody the metaphor of fluidity and organic movement. It takes parameters such as radius, height, and number of partitions to create interlocking, flowing forms. Each partition is represented as a NURBS curve, designed to suggest movement and continuity, with control points that define its curvature. The extruded surfaces of these curves define spaces that transition seamlessly, promoting dynamic interactions. By varying input parameters, the model explores different spatial relationships and light effects, ultimately enhancing the overall aesthetic of calmness and exploration."""

#! python 3
function_code = """def create_curved_partitions_model(base_radius, height, num_partitions, partition_thickness, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'curved partitions'.
    
    The model consists of interlocking, flowing forms that suggest movement and continuity. 
    The design uses curved partitions to define spaces that flow into one another without creating 
    stark separations, allowing for dynamic interaction of spaces.

    Inputs:
    - base_radius: float, the radius of the base circle from which the partitions will radiate.
    - height: float, the height of the partitions.
    - num_partitions: int, the number of curved partitions to create.
    - partition_thickness: float, the thickness of each partition.
    - seed: int, optional, the seed for random number generation to ensure replicable results.

    Outputs:
    - List of RhinoCommon Brep objects representing the 3D geometry of the partitions.
    \"""
    import Rhino.Geometry as rg
    import math
    import random
    random.seed(seed)
    
    breps = []
    angle_increment = 2 * math.pi / num_partitions
    
    for i in range(num_partitions):
        # Randomly perturb the angle to create a more organic layout
        angle = i * angle_increment + random.uniform(-angle_increment/4, angle_increment/4)
        
        # Create control points for a NURBS curve
        start_point = rg.Point3d(base_radius * math.cos(angle), 
                                 base_radius * math.sin(angle), 
                                 0)
        mid_point = rg.Point3d((base_radius - partition_thickness) * math.cos(angle + angle_increment/4), 
                               (base_radius - partition_thickness) * math.sin(angle + angle_increment/4), 
                               height / 2)
        end_point = rg.Point3d(base_radius * math.cos(angle + angle_increment/2), 
                               base_radius * math.sin(angle + angle_increment/2), 
                               height)
        
        # Create a NURBS curve
        nurbs_curve = rg.NurbsCurve.Create(False, 2, [start_point, mid_point, end_point])
        
        # Create a surface from the curve by extruding it along its tangent
        extrusion_vector = rg.Vector3d(0, 0, 1)
        extrusion = rg.Extrusion.Create(nurbs_curve, partition_thickness, True)
        
        # Convert extrusion to a Brep
        brep = extrusion.ToBrep()
        
        if brep:
            breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(10.0, 5.0, 8, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(15.0, 8.0, 12, 0.3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(20.0, 10.0, 6, 0.8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(12.0, 6.0, 10, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(25.0, 15.0, 10, 1.0, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
