# Created for 0008_0005_branching_network_shell.json

""" Summary:
The provided function generates an architectural concept model by creating a fractal-based structure that embodies the 'branching network shell' metaphor. It utilizes recursive branching to form intricate, interconnected patterns that reflect organic growth, resembling natural systems. Each branch is scaled down, ensuring a rhythmic and cohesive design. The semi-transparent shell is simulated through pipe geometry, allowing for light and air interaction, emphasizing openness while maintaining a sense of enclosure. By adjusting parameters like initial length and iterations, the function fosters adaptability and continuity, aligning with the metaphor's essence of harmony with nature."""

#! python 3
function_code = """def create_branching_network_shell_fractal(seed: int, initial_length: float, scale_factor: float, iterations: int, shell_thickness: float):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.

    This function generates a fractal-like structure utilizing a recursive branching system that emphasizes
    organic growth and interconnectedness. The result is a rhythmic, semi-transparent shell that allows light
    and air to interact dynamically with the environment.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicable results.
    - initial_length (float): The initial length of each branching element (meters).
    - scale_factor (float): The factor by which each subsequent branch is scaled down.
    - iterations (int): The number of recursive branching iterations.
    - shell_thickness (float): The thickness of the shell structure.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    def create_fractal_branch(start_point, direction, length, depth):
        if depth == 0:
            return []

        end_point = rg.Point3d.Add(start_point, direction * length)
        branch_line = rg.Line(start_point, end_point)
        branches = [branch_line]

        # Create new branches
        for _ in range(3):  # Fixed branch factor for a consistent fractal pattern
            rotation_angle = random.uniform(-0.5, 0.5) * 3.14  # Random rotation for organic feel
            new_direction = direction
            new_direction.Rotate(rotation_angle, rg.Vector3d(0, 0, 1))
            new_length = length * scale_factor
            branches.extend(create_fractal_branch(end_point, new_direction, new_length, depth - 1))

        return branches

    base_point = rg.Point3d(0, 0, 0)
    base_direction = rg.Vector3d(0, 0, 1)
    fractal_branches = create_fractal_branch(base_point, base_direction, initial_length, iterations)

    breps = []
    for branch in fractal_branches:
        # Create a pipe around each branch for visualization of the network
        pipe = rg.Brep.CreatePipe(branch.ToNurbsCurve(), shell_thickness * 0.1, False, rg.PipeCapMode.Round, False, 0.01, 0.01)[0]
        breps.append(pipe)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell_fractal(seed=42, initial_length=10.0, scale_factor=0.7, iterations=5, shell_thickness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell_fractal(seed=123, initial_length=15.0, scale_factor=0.6, iterations=4, shell_thickness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell_fractal(seed=7, initial_length=12.0, scale_factor=0.8, iterations=6, shell_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell_fractal(seed=99, initial_length=20.0, scale_factor=0.5, iterations=3, shell_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell_fractal(seed=10, initial_length=8.0, scale_factor=0.75, iterations=7, shell_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
