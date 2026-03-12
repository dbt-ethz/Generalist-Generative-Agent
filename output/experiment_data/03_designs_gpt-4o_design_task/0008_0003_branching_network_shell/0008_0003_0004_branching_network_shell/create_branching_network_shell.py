# Created for 0008_0003_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model based on the "branching network shell" metaphor. It begins by establishing a central core, from which multiple branches radiate outward, forming a lattice-like structure. Each branch represents a pathway, enhancing spatial organization and interactions. The shell is created by lofting surfaces between the ends of the branches, providing a protective yet permeable enclosure. This design allows for light filtration and dynamic shadow play, reflecting adaptability and organic growth. The result is a conceptual model that embodies connectivity and integration with the surrounding environment, aligning with the metaphor's key traits."""

#! python 3
function_code = """def create_branching_network_shell(core_radius=5, branch_length=10, branch_count=8, shell_thickness=0.5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'branching network shell' metaphor.
    
    Parameters:
    - core_radius (float): The radius of the central core from which the network branches out.
    - branch_length (float): The length of each branching pathway.
    - branch_count (int): The number of primary branches extending from the core.
    - shell_thickness (float): The thickness of the shell-like enclosure.
    - seed (int): Seed for the random generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Create the core sphere
    core = rg.Sphere(rg.Point3d.Origin, core_radius).ToBrep()

    # Create branches
    branches = []
    for i in range(branch_count):
        angle = 2 * math.pi * i / branch_count
        direction = rg.Vector3d(math.cos(angle), math.sin(angle), random.uniform(0.5, 1.5))
        direction.Unitize()
        direction *= branch_length
        line = rg.Line(rg.Point3d.Origin, direction)
        plane = rg.Plane(line.From, direction)
        # Fix: Create a Cylinder with a height and call ToBrep(True, True) to cap both ends
        branch = rg.Cylinder(rg.Circle(plane, 0.1), branch_length).ToBrep(True, True)
        branches.append(branch)

    # Create the shell as a lofted surface from the ends of the branches
    shell_profiles = [rg.Circle(branch.Faces[0].PointAt(0.5, 0.5), shell_thickness).ToNurbsCurve() for branch in branches]
    loft = rg.Brep.CreateFromLoft(shell_profiles, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

    # Combine all geometries
    concept_model = [core] + branches + list(loft)

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(core_radius=6, branch_length=12, branch_count=10, shell_thickness=0.6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(core_radius=4, branch_length=8, branch_count=5, shell_thickness=0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(core_radius=7, branch_length=15, branch_count=12, shell_thickness=0.7, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(core_radius=3, branch_length=9, branch_count=6, shell_thickness=0.3, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(core_radius=5, branch_length=10, branch_count=15, shell_thickness=0.8, seed=2022)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
