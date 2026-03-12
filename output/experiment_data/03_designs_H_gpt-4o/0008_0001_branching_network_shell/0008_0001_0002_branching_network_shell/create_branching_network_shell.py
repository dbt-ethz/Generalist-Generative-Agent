# Created for 0008_0001_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model based on the 'branching network shell' metaphor by creating a central core surrounded by branching elements that radiate outward. It utilizes specified parameters like core radius and branch length to define the model's form and massing, ensuring a dynamic silhouette. The branches diverge and converge, reflecting fluidity and movement, while a permeable outer shell allows light and air to enhance environmental integration. This approach embodies the metaphor's essence, producing a structure that emphasizes organic growth, adaptability, and spatial continuity, fostering interaction among different areas."""

#! python 3
function_code = """def create_branching_network_shell(core_radius, branch_length, num_branches, shell_thickness, randomness_seed=42):
    \"""
    Create an architectural Concept Model based on the 'Branching Network Shell' metaphor.

    This function generates a dynamic form consisting of a central core from which a series of branching
    structural elements radiate outward. These branches converge and diverge, creating a network that defines
    the spatial organization of the model. The model also includes a permeable outer shell that suggests
    openness and integration with the environment.

    Parameters:
    - core_radius (float): The radius of the central core, in meters.
    - branch_length (float): The length of the branching elements, in meters.
    - num_branches (int): The number of branches radiating from the core.
    - shell_thickness (float): The thickness of the outer shell, in meters.
    - randomness_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model, including branches and shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(randomness_seed)
    
    # Create the central core
    core = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d.Origin, core_radius))
    
    # Create branching elements
    branches = []
    for i in range(num_branches):
        angle = i * (360.0 / num_branches) + random.uniform(-10, 10)
        direction = rg.Vector3d(1, 0, 0)
        direction.Rotate(math.radians(angle), rg.Vector3d.ZAxis)
        end_point = rg.Point3d(direction * branch_length)
        branch_curve = rg.LineCurve(rg.Point3d.Origin, end_point)
        
        # Create a pipe around the branch curve to give it volume
        branch_brep = rg.Brep.CreatePipe(branch_curve, core_radius * 0.1, True, rg.PipeCapMode.Round, True, 0.01, 0.1)[0]
        branches.append(branch_brep)
    
    # Create a permeable shell
    shell = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d.Origin, core_radius + branch_length + shell_thickness))
    
    # Combine all elements into one list
    geometries = [core] + branches + [shell]
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(5.0, 10.0, 8, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(3.0, 15.0, 12, 0.5, randomness_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(4.0, 8.0, 6, 2.0, randomness_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(6.0, 12.0, 10, 1.5, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(2.5, 20.0, 5, 0.75, randomness_seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
