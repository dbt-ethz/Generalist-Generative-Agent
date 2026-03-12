# Created for 0008_0003_branching_network_shell.json

""" Summary:
The provided function generates an architectural concept model inspired by the "branching network shell" metaphor. It creates a foundational core and generates branching pathways that extend outward, forming a web-like structure. By defining parameters such as core radius, branch length, and count, the model reflects the intricate lattice and organic silhouette suggested by the metaphor. The branches are represented as pipe geometries, while the shell is formed by lofting these branches, creating a protective yet permeable enclosure. The design emphasizes adaptability and connectivity, integrating the building with its environment and allowing dynamic light interplay, aligning with the metaphors essence."""

#! python 3
function_code = """def create_branching_network_shell(core_radius=5, branch_length=20, branch_count=8, shell_thickness=0.3):
    \"""
    Creates an architectural Concept Model embodying the 'branching network shell' metaphor.
    
    Parameters:
    - core_radius (float): The radius of the foundational core of the structure.
    - branch_length (float): The length of each branching pathway extending from the core.
    - branch_count (int): The number of branches extending from the core.
    - shell_thickness (float): The thickness of the shell-like enclosure.

    Returns:
    - List[Brep]: A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Create the central core
    core = rg.Sphere(rg.Point3d(0, 0, 0), core_radius).ToBrep()

    # Generate branching pathways from the core
    branches = []
    angle_step = 360.0 / branch_count
    for i in range(branch_count):
        angle = i * angle_step
        direction = rg.Vector3d(branch_length * math.cos(math.radians(angle)), branch_length * math.sin(math.radians(angle)), random.uniform(-branch_length / 2, branch_length / 2))
        start_point = rg.Point3d(core_radius * math.cos(math.radians(angle)), core_radius * math.sin(math.radians(angle)), 0)
        end_point = rg.Point3d(start_point + direction)
        branch_curve = rg.LineCurve(start_point, end_point)
        pipe_breps = rg.Brep.CreatePipe(branch_curve, shell_thickness, True, rg.PipeCapMode.Round, True, 0.01, 0.01)
        branches.extend(pipe_breps)

    # Create the shell-like enclosure by lofting the branches
    loft_sections = [branch.DuplicateEdgeCurves()[0] for branch in branches if branch]
    shell = rg.Brep.CreateFromLoft(loft_sections, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

    # Output the geometries: core, branches, and shell
    geometries = [core] + branches + [shell]
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(core_radius=5, branch_length=20, branch_count=8, shell_thickness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(core_radius=10, branch_length=15, branch_count=12, shell_thickness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(core_radius=7, branch_length=25, branch_count=10, shell_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(core_radius=6, branch_length=30, branch_count=6, shell_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(core_radius=4, branch_length=18, branch_count=5, shell_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
