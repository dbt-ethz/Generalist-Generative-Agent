# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor of a "Suspended intersecting assembly." It creates a series of curved rods that represent floating, intersecting elements, arranged into overlapping arcs and lines to evoke a sense of lightness and fluidity. The rods are randomly positioned within a defined space, simulating suspension through transformations that suggest elevation. These geometries form a dynamic network that reflects spatial relationships, enhancing visual connectivity and transparency. The use of randomized parameters allows for diverse configurations, embodying adaptability and movement in the design process."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_rods, rod_length, arc_radius, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.
    
    This function generates a series of curved rods and flexible materials to represent floating and intersecting elements.
    It arranges these components into overlapping arcs and lines, forming a network that suggests lightness and fluidity.
    
    Parameters:
    - num_rods: The number of rods to generate.
    - rod_length: The length of each rod in meters.
    - arc_radius: The radius of the arcs formed by the rods.
    - seed: An optional seed for randomization to ensure replicable results.
    
    Returns:
    - A list of 3D geometries (Breps) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    geometries = []
    
    # Generate random positions for the base of each rod
    for i in range(num_rods):
        # Randomly place the base of each rod in a 10x10x10 meter space
        base_x = random.uniform(-5, 5)
        base_y = random.uniform(-5, 5)
        base_z = random.uniform(0, 5)  # Start from the ground up
        
        # Create a circular arc representing the rod
        plane = rg.Plane(rg.Point3d(base_x, base_y, base_z), rg.Vector3d(0, 0, 1))
        arc = rg.Arc(plane, arc_radius, math.pi)  # Half-circle arc
        
        # Create a pipe around the arc to represent a flexible rod
        rod = rg.Brep.CreatePipe(arc.ToNurbsCurve(), rod_length * 0.1, True, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]
        
        # Apply a transformation to simulate suspension and intersection
        translation = rg.Transform.Translation(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(2, 5))
        rod.Transform(translation)
        
        geometries.append(rod)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10, 2.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(5, 3.0, 2.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(8, 1.5, 2.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15, 2.5, 1.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(12, 2.2, 1.8, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
