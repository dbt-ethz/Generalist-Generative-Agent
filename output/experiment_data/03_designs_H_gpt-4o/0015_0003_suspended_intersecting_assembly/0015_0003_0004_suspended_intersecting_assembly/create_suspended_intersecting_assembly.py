# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "Suspended intersecting assembly." It creates a series of modular elements that mimic floating structures through the use of arcs and pipes, emphasizing lightness and fluidity. By randomly positioning these components around a central point and applying slight rotations, the function simulates dynamic intersections and complex spatial relationships. The result is a cohesive network of elements that visually embodies the metaphor's themes of transparency and adaptability, while ensuring the model reflects a delicate balance and an engaging interplay between its parts."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_modules=8, module_height=2.5, module_radius=0.15, seed=42):
    \"""
    Creates an architectural Concept Model that embodies the 'Suspended intersecting assembly' metaphor.
    
    This model features a series of modular, intersecting arcs and lines, representing floating and flexible elements.
    The design emphasizes adaptability, movement, and the interplay between components to create a sense of lightness
    and fluidity within a cohesive network.

    Inputs:
    - num_modules: The number of modular elements to generate.
    - module_height: The height of each module in meters.
    - module_radius: The radius of each module's arc in meters.
    - seed: A seed for randomization to ensure replicable results.

    Outputs:
    - A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for replicability
    random.seed(seed)

    # Initialize a list to hold the generated Breps
    brep_list = []

    # Define the central point of the model
    central_point = rg.Point3d(0, 0, 0)

    # Generate modular elements
    for i in range(num_modules):
        # Randomly position each module around the central point
        angle = random.uniform(0, 2 * math.pi)
        offset_distance = random.uniform(5, 10)
        module_center = rg.Point3d(
            central_point.X + offset_distance * math.cos(angle),
            central_point.Y + offset_distance * math.sin(angle),
            random.uniform(0, module_height * 2)
        )

        # Create a base plane for the module
        module_plane = rg.Plane(module_center, rg.Vector3d(0, 0, 1))

        # Define a random angle span for the arc
        angle_span = random.uniform(math.pi / 3, math.pi)

        # Create an arc for the module
        arc = rg.Arc(module_plane, module_radius, angle_span)
        arc_curve = arc.ToNurbsCurve()

        # Create a pipe around the arc to represent the module
        module_brep = rg.Brep.CreatePipe(arc_curve, module_radius * 0.1, False, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]

        # Apply slight rotation to simulate different intersecting angles
        rotation_angle = random.uniform(-math.pi / 4, math.pi / 4)
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation = rg.Transform.Rotation(rotation_angle, rotation_axis, module_center)
        module_brep.Transform(rotation)

        # Add the module to the list of Breps
        brep_list.append(module_brep)

    # Return the list of Breps representing the model
    return brep_list"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_modules=10, module_height=3.0, module_radius=0.2, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_modules=5, module_height=2.0, module_radius=0.1, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_modules=12, module_height=4.0, module_radius=0.25, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_modules=15, module_height=3.5, module_radius=0.3, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_modules=7, module_height=2.8, module_radius=0.18, seed=33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
