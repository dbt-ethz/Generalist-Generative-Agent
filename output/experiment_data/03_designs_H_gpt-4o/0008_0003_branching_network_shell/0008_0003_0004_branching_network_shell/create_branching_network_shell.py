# Created for 0008_0003_branching_network_shell.json

""" Summary:
The provided function creates an architectural concept model inspired by the "branching network shell" metaphor. It generates a central core from which multiple branches extend, forming a lattice-like structure that emphasizes interconnectedness and adaptability. Each branch is represented as a curved pathway that varies in thickness and length, simulating organic growth. The function also incorporates a shell-like enclosure, designed to be permeable, allowing natural light to filter through and create dynamic shadows. Through its parameters, the function allows for customization of the model, promoting fluidity and integration with the surrounding environment, aligning with the metaphors implications."""

#! python 3
function_code = """def create_branching_network_shell(core_radius=5.0, branch_count=10, branch_length=15.0, branch_thickness=0.3, shell_density=0.1, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'branching network shell' metaphor.
    
    This function generates a branching lattice framework emanating from a central core. The design
    features an intricate web-like network of pathways and nodes, forming a protective yet permeable
    shell-like enclosure. It emphasizes adaptability, fluidity, and integration with the environment,
    promoting dynamic light and shadow interplay.

    Parameters:
    - core_radius (float): The radius of the central core from which branches emanate.
    - branch_count (int): The number of primary branches extending from the core.
    - branch_length (float): The length of each branch.
    - branch_thickness (float): The thickness of each branching pathway.
    - shell_density (float): The density of the shell structure, affecting its porosity.
    - seed (int): Seed for the random generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set seed for randomness to ensure replicability
    random.seed(seed)

    geometries = []

    # Create the central core as a sphere
    core = rg.Sphere(rg.Point3d(0, 0, 0), core_radius).ToBrep()
    geometries.append(core)

    # Generate primary branches
    branch_angle_step = 360 / branch_count
    for i in range(branch_count):
        angle = branch_angle_step * i
        direction_vector = rg.Vector3d(
            branch_length * math.cos(math.radians(angle)),
            branch_length * math.sin(math.radians(angle)),
            random.uniform(-branch_length / 2, branch_length / 2)
        )
        direction_vector.Unitize()
        start_point = rg.Point3d(
            core_radius * math.cos(math.radians(angle)),
            core_radius * math.sin(math.radians(angle)),
            0
        )
        end_point = start_point + direction_vector * branch_length
        branch_curve = rg.LineCurve(start_point, end_point)

        # Create a pipe around the branch curve
        pipe_breps = rg.Brep.CreatePipe(branch_curve, branch_thickness, True, rg.PipeCapMode.Round, True, 0.01, 0.01)
        if pipe_breps:
            geometries.extend(pipe_breps)

    # Creating a shell-like enclosure with varying porosity
    for branch in geometries[1:]:
        bounding_box = branch.GetBoundingBox(True)
        box_center = bounding_box.Center
        shell_sphere = rg.Sphere(box_center, branch_thickness * 3)
        shell_mesh = rg.Mesh.CreateIcoSphere(shell_sphere, int(shell_density * 10))

        if shell_mesh:
            geometries.append(shell_mesh)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(core_radius=6.0, branch_count=12, branch_length=20.0, branch_thickness=0.5, shell_density=0.2, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(core_radius=4.0, branch_count=8, branch_length=10.0, branch_thickness=0.4, shell_density=0.15, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(core_radius=5.5, branch_count=15, branch_length=18.0, branch_thickness=0.25, shell_density=0.05, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(core_radius=7.0, branch_count=20, branch_length=25.0, branch_thickness=0.6, shell_density=0.3, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(core_radius=5.0, branch_count=5, branch_length=12.0, branch_thickness=0.2, shell_density=0.15, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
