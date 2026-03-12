# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The provided function creates an architectural concept model inspired by the metaphor "Suspended intersecting assembly." It generates a series of floating arcs using random parameters for height, radius, and angles, reflecting the metaphor's emphasis on lightness and dynamic intersections. The arcs are designed to appear elevated and interconnected, forming a network of pathways that enhances spatial engagement. By using flexible materials represented through pipe geometries, the model captures the essence of fluidity and transparency. The randomization of parameters allows for diverse configurations, contributing to the overall adaptability and visual complexity of the architectural concept."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_arcs=5, height_range=(5, 15), seed=42):
    \"""
    Creates an architectural Concept Model encapsulating the 'Suspended intersecting assembly' metaphor.
    
    The model consists of a series of floating, intersecting arcs representing a network of pathways and visual connections.
    The arcs are suspended to create a sense of lightness and fluidity, emphasizing dynamic intersections and spatial dialogues.
    
    Inputs:
    - num_arcs: The number of arcs to generate in the model.
    - height_range: A tuple representing the minimum and maximum height for the arc's suspension.
    - seed: A seed for random number generation to ensure replicability.
    
    Outputs:
    - A list of Brep geometries representing the suspended arcs.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import the math module for mathematical constants
    
    # Set the random seed for replicability
    random.seed(seed)
    
    # Define the base plane for the model
    base_plane = rg.Plane.WorldXY
    
    # Initialize a list to hold the generated Breps
    brep_list = []
    
    # Generate arcs with random parameters
    for _ in range(num_arcs):
        # Randomly determine the center of the arc within a defined range
        x_center = random.uniform(-10, 10)
        y_center = random.uniform(-10, 10)
        z_center = random.uniform(height_range[0], height_range[1])
        
        # Create a point for the center of the arc
        center_point = rg.Point3d(x_center, y_center, z_center)
        
        # Define the radius and angles for the arc
        radius = random.uniform(2, 5)
        start_angle = random.uniform(0, math.pi)  # Use math.pi for the constant PI
        angle_span = random.uniform(math.pi / 4, math.pi)
        
        # Create the arc plane using the base plane and center point
        arc_plane = rg.Plane(center_point, base_plane.Normal)
        
        # Create the arc using the correct constructor
        arc = rg.Arc(arc_plane, radius, angle_span)
        
        # Convert the arc to a NurbsCurve
        arc_curve = arc.ToNurbsCurve()
        
        # Create a Pipe around the arc to represent a flexible material
        pipe_brep = rg.Brep.CreatePipe(arc_curve, 0.2, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0]
        
        # Add the pipe to the list of Breps
        brep_list.append(pipe_brep)
    
    # Return the list of Breps representing the model
    return brep_list"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_arcs=7, height_range=(10, 20), seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_arcs=10, height_range=(8, 18), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_arcs=3, height_range=(6, 12), seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_arcs=4, height_range=(7, 14), seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_arcs=6, height_range=(4, 12), seed=88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
