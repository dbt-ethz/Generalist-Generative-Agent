# Created for 0008_0003_branching_network_shell.json

""" Summary:
The provided function, `create_branching_network_shell`, generates an architectural concept model inspired by the "branching network shell" metaphor. It begins by creating a central core from which a lattice of branches radiates, mimicking organic growth patterns. The function defines the number, length, and thickness of these branches, resulting in a web-like network that facilitates various spatial interactions. The resulting structure is porous and adaptable, allowing light penetration and dynamic shadow play, which enhances its integration with the environment. Ultimately, the model embodies the metaphor's themes of interconnectedness, fluidity, and organic form, fostering a harmonious relationship with its surroundings."""

#! python 3
function_code = """def create_branching_network_shell(core_radius=5.0, branch_count=10, branch_length=15.0, shell_thickness=0.5):
    \"""
    Creates an architectural Concept Model embodying the 'branching network shell' metaphor.
    
    This function generates a lattice framework with a branching network of pathways and nodes 
    extending from a central core. It forms a porous and adaptive shell-like enclosure, allowing 
    for dynamic light and shadow interplay, and promoting integration with the environment.

    Parameters:
    - core_radius (float): The radius of the central core from which branches emanate.
    - branch_count (int): The number of primary branches extending from the core.
    - branch_length (float): The length of each branch.
    - shell_thickness (float): The thickness of the shell structure.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import math
    import random

    # Set seed for randomness to ensure replicability
    random.seed(42)

    geometries = []

    # Create the central core as a sphere
    core = rg.Sphere(rg.Point3d(0, 0, 0), core_radius).ToBrep()
    geometries.append(core)

    # Generate primary branches
    branch_angle_step = 360 / branch_count
    for i in range(branch_count):
        angle = branch_angle_step * i
        direction_vector = rg.Vector3d(
            branch_length * random.uniform(0.8, 1.2),
            branch_length * random.uniform(0.8, 1.2),
            branch_length * random.uniform(0.8, 1.2)
        )
        direction_vector.Rotate(math.radians(angle), rg.Vector3d.ZAxis)
        direction_vector.Unitize()
        start_point = rg.Point3d(core_radius * direction_vector.X, core_radius * direction_vector.Y, core_radius * direction_vector.Z)
        end_point = start_point + direction_vector * branch_length
        branch_curve = rg.LineCurve(start_point, end_point)
        
        # Extrude to form a cylindrical branch
        pipe_result = rg.Brep.CreatePipe(branch_curve, shell_thickness, True, rg.PipeCapMode.Round, True, 0.01, 0.01)
        if pipe_result is not None and len(pipe_result) > 1:
            branch = pipe_result[1]
            geometries.append(branch)

    # Creating the shell-like enclosure
    for branch in geometries[1:]:
        bounding_box = branch.GetBoundingBox(True)
        box_center = bounding_box.Center
        shell = rg.Sphere(box_center, shell_thickness * 3).ToBrep()
        geometries.append(shell)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(core_radius=6.0, branch_count=12, branch_length=20.0, shell_thickness=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(core_radius=4.0, branch_count=8, branch_length=10.0, shell_thickness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(core_radius=7.0, branch_count=15, branch_length=25.0, shell_thickness=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(core_radius=5.5, branch_count=5, branch_length=18.0, shell_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(core_radius=3.0, branch_count=20, branch_length=12.0, shell_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
