# Created for 0008_0005_branching_network_shell.json

""" Summary:
The provided function, `create_branching_network_shell`, generates an architectural concept model based on the metaphor of a "branching network shell." Utilizing recursive techniques, it creates a fractal-like branching structure that reflects organic growth and interconnectedness. Parameters such as branch levels, angles, and shell thickness dictate the model's complexity and layering. The resulting geometry features a semi-transparent shell, designed to interact dynamically with light and air, emphasizing fluid transitions and spaces for pause. This approach encapsulates the metaphor's essence, promoting a harmonious relationship between the structure and its natural environment while highlighting adaptability and continuity."""

#! python 3
function_code = """def create_branching_network_shell(seed: int, overall_height: float, branch_levels: int, branch_angle: float, shell_thickness: float):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.
    
    This approach uses a recursive branching structure to reflect organic growth and interconnectedness.
    The model features a layered, semi-transparent shell that interacts dynamically with light and air.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicable results.
    - overall_height (float): The total height of the structure (meters).
    - branch_levels (int): The number of hierarchical levels in the branching structure.
    - branch_angle (float): The angle in degrees at which branches diverge.
    - shell_thickness (float): The thickness of the shell layers (meters).

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    def create_branch_structure(start_point, direction, current_level):
        if current_level > branch_levels:
            return []
        
        # Create a new end point for the branch
        length = overall_height / (branch_levels + 1)
        end_point = rg.Point3d(
            start_point.X + direction.X * length,
            start_point.Y + direction.Y * length,
            start_point.Z + direction.Z * length
        )
        line = rg.LineCurve(start_point, end_point)

        # Calculate new directions for sub-branches
        branches = [line]
        for _ in range(2):  # Each branch splits into two
            new_direction = rg.Vector3d(
                direction.X * math.cos(math.radians(branch_angle)) - direction.Y * math.sin(math.radians(branch_angle)),
                direction.X * math.sin(math.radians(branch_angle)) + direction.Y * math.cos(math.radians(branch_angle)),
                direction.Z * random.uniform(0.8, 1.2)
            )
            new_direction.Unitize()
            branches.extend(create_branch_structure(end_point, new_direction, current_level + 1))

        return branches

    # Create the initial branch
    initial_point = rg.Point3d(0, 0, 0)
    initial_direction = rg.Vector3d(0, 0, 1)
    branch_lines = create_branch_structure(initial_point, initial_direction, 0)

    # Create pipes around branches for visualization
    breps = []
    for branch in branch_lines:
        pipe = rg.Brep.CreatePipe(branch, shell_thickness * 0.1, False, rg.PipeCapMode.Round, False, 0.01, 0.01)[0]
        breps.append(pipe)

    # Create semi-transparent shell layers
    for i in range(branch_levels):
        height = overall_height * (i + 1) / (branch_levels + 1)
        radius = overall_height * 0.1 * (i + 1)
        shell = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d(0, 0, height), radius))
        if shell:
            breps.append(shell)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(42, 10.0, 5, 30.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(7, 15.0, 3, 45.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(99, 12.5, 4, 60.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(1, 20.0, 6, 25.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(12, 8.0, 2, 15.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
