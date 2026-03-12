# Created for 0008_0003_branching_network_shell.json

""" Summary:
The provided function `create_branching_network_shell` generates an architectural concept model that embodies the 'branching network shell' metaphor by creating a lattice-like structure. It starts with a central core from which multiple branches extend, simulating the organic growth described in the metaphor. Each branch terminates with nodes, which represent interaction points. The function constructs a shell-like enclosure that is both protective and permeable, allowing light to filter through, enhancing the dynamic interplay of light and shadow. This approach emphasizes adaptability and fluidity, fostering a harmonious relationship with the environment while reflecting interconnectedness and spatial organization."""

#! python 3
function_code = """def create_branching_network_shell(core_radius=5.0, branch_count=12, branch_length=15.0, node_radius=1.0, shell_thickness=0.3):
    \"""
    Creates an architectural Concept Model embodying the 'branching network shell' metaphor.

    This function generates a lattice framework with branching networks of nodes and pathways 
    extending from a central core. It forms a porous and adaptive shell-like enclosure, promoting 
    integration with the environment through light and shadow dynamics.

    Parameters:
    - core_radius (float): The radius of the central core from which branches emanate.
    - branch_count (int): The number of primary branches extending from the core.
    - branch_length (float): The length of each branch.
    - node_radius (float): The radius of nodes that occur at each branch endpoint.
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
            branch_length * math.cos(math.radians(angle)),
            branch_length * math.sin(math.radians(angle)),
            random.uniform(-branch_length / 2, branch_length / 2)
        )
        direction_vector.Unitize()
        start_point = rg.Point3d(core_radius * direction_vector.X, core_radius * direction_vector.Y, core_radius * direction_vector.Z)
        end_point = start_point + direction_vector * branch_length
        branch_curve = rg.LineCurve(start_point, end_point)
        
        # Create nodes at endpoints of branches
        node = rg.Sphere(end_point, node_radius).ToBrep()
        geometries.append(node)
        
        # Extrude to form a cylindrical branch
        pipe_result = rg.Brep.CreatePipe(branch_curve, shell_thickness, True, rg.PipeCapMode.Round, True, 0.01, 0.01)
        if pipe_result:
            geometries.extend(pipe_result)

    # Creating the shell-like enclosure by connecting nodes
    node_centers = [node.Faces[0].PointAt(0.5, 0.5) for node in geometries if isinstance(node, rg.Brep)]
    if len(node_centers) > 2:
        shell = rg.Brep.CreateFromLoft(
            [rg.Circle(rg.Plane(node_center, rg.Vector3d.ZAxis), node_radius).ToNurbsCurve() for node_center in node_centers],
            rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False
        )
        if shell:
            geometries.extend(shell)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(core_radius=10.0, branch_count=16, branch_length=20.0, node_radius=2.0, shell_thickness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(core_radius=7.5, branch_count=8, branch_length=12.0, node_radius=1.5, shell_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(core_radius=6.0, branch_count=10, branch_length=18.0, node_radius=1.2, shell_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(core_radius=8.0, branch_count=14, branch_length=25.0, node_radius=1.0, shell_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(core_radius=5.0, branch_count=20, branch_length=30.0, node_radius=0.5, shell_thickness=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
