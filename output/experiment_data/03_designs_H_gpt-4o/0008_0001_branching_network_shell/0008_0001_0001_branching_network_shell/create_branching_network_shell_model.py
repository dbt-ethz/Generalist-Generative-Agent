# Created for 0008_0001_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell_model` generates an architectural concept model inspired by the "branching network shell" metaphor. It constructs a central hub from which a series of interconnected branching elements radiate outward, mimicking organic structures like trees. The model emphasizes dynamic forms with pathways that converge and diverge, promoting fluidity and interaction within spaces. A permeable outer shell is created to allow light and air penetration, enhancing environmental integration. By utilizing parameters such as core radius, branch length, and count, the function produces various geometries that encapsulate the metaphor's essence, reflecting adaptability and continuity."""

#! python 3
function_code = """def create_branching_network_shell_model(core_radius=5.0, branch_length=15.0, branch_count=8, shell_thickness=0.5):
    \"""
    Creates an architectural Concept Model inspired by the 'branching network shell' metaphor.
    
    This function generates a series of interconnected, branching structural elements that radiate
    from a central hub, following the metaphor of a branching network. The model features a dynamic
    form with a series of converging and diverging pathways, and includes a permeable outer shell
    to suggest openness and integration with the surroundings.
    
    Inputs:
    - core_radius: The radius of the central hub from which branches originate, in meters.
    - branch_length: The length of each branching element from the core, in meters.
    - branch_count: The number of branching elements radiating from the core.
    - shell_thickness: The thickness of the outer shell, in meters.
    
    Outputs:
    - A list of 3D geometries (breps, surfaces, or meshes) representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import math module to replace RhinoMath

    random.seed(42)  # Ensure replicability of random elements

    geometries = []

    # Central core
    core = rg.Sphere(rg.Point3d(0, 0, 0), core_radius).ToBrep()
    geometries.append(core)

    # Branching network
    angle_step = 360.0 / branch_count
    for i in range(branch_count):
        angle = i * angle_step
        branch_direction = rg.Vector3d(branch_length, 0, 0)
        branch_direction.Rotate(math.radians(angle), rg.Vector3d(0, 0, 1))
        
        branch_line = rg.Line(rg.Point3d(0, 0, 0), branch_direction)
        branch = rg.Cylinder(rg.Circle(branch_line.From, shell_thickness), branch_line.Length).ToBrep(True, True)
        
        geometries.append(branch)

    # Permeable outer shell
    # Create a bounding sphere for the shell
    bounding_sphere = rg.Sphere(rg.Point3d(0, 0, 0), core_radius + branch_length)
    shell = rg.Brep.CreateFromSphere(bounding_sphere)
    
    # Create perforations in the shell
    for i in range(branch_count):
        for j in range(3):  # Three perforations per branch
            random_angle = random.uniform(0, 360)
            random_azimuth = random.uniform(-90, 90)
            perforation_center = bounding_sphere.Center + rg.Point3d(
                (core_radius + branch_length / 2) * math.cos(math.radians(random_azimuth)) * math.cos(math.radians(random_angle)),
                (core_radius + branch_length / 2) * math.cos(math.radians(random_azimuth)) * math.sin(math.radians(random_angle)),
                (core_radius + branch_length / 2) * math.sin(math.radians(random_azimuth))
            )
            perforation = rg.Sphere(perforation_center, shell_thickness * 2).ToBrep()
            boolean_result = rg.Brep.CreateBooleanDifference(shell, perforation, 0.001)
            if boolean_result:
                shell = boolean_result[0]
    
    geometries.append(shell)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell_model(core_radius=6.0, branch_length=20.0, branch_count=10, shell_thickness=0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell_model(core_radius=4.0, branch_length=12.0, branch_count=6, shell_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell_model(core_radius=7.5, branch_length=18.0, branch_count=12, shell_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell_model(core_radius=5.5, branch_length=14.0, branch_count=9, shell_thickness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell_model(core_radius=5.0, branch_length=25.0, branch_count=15, shell_thickness=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
