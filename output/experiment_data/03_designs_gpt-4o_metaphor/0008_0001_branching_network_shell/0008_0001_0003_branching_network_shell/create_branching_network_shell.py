# Created for 0008_0001_branching_network_shell.json

""" Summary:
The provided function, `create_branching_network_shell`, generates an architectural concept model based on the "branching network shell" metaphor. It constructs a central core cylinder representing the protective shell, while also creating branching elements that diverge from the core, mimicking organic growth and interconnectedness. By utilizing randomized parameters for angles and heights, the model achieves a dynamic and adaptive structure, reflecting fluidity and integration with the environment. The resulting 3D geometries embody the metaphor's key traits, showcasing a harmonious blend of form and function, allowing light and air to permeate through the interconnected spaces."""

#! python 3
function_code = """def create_branching_network_shell(base_radius, height, branch_count, shell_thickness, randomness_seed=42):
    \"""
    Generate an architectural concept model inspired by a 'branching network shell'. This model consists of a 
    central core structure with branching elements that intersect the core, forming a shell-like protective layer.

    Parameters:
    - base_radius: float, the radius of the central core.
    - height: float, the height of the central structure.
    - branch_count: int, the number of branching elements.
    - shell_thickness: float, the thickness of the shell elements.
    - randomness_seed: int, seed for random number generation to ensure repeatability.

    Returns:
    - List of Breps: the generated 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set the random seed for repeatability
    random.seed(randomness_seed)

    # Create the central core cylinder
    core = rg.Cylinder(rg.Circle(rg.Point3d(0, 0, 0), base_radius), height).ToBrep(True, True)

    # Generate branching elements
    branches = []
    for i in range(branch_count):
        # Randomize the angle and height position for branching
        angle = random.uniform(0, 2 * math.pi)  # Random angle in radians
        branch_height = random.uniform(0, height)  # Random height along the core

        # Determine the start and end points of the branch
        start_point = rg.Point3d(base_radius * random.uniform(0.8, 1.2) * math.cos(angle),
                                 base_radius * random.uniform(0.8, 1.2) * math.sin(angle),
                                 branch_height)
        end_point = rg.Point3d(base_radius * random.uniform(1.5, 2.0) * math.cos(angle + random.uniform(0, 0.5)),
                               base_radius * random.uniform(1.5, 2.0) * math.sin(angle + random.uniform(0, 0.5)),
                               branch_height + random.uniform(-2, 2))

        # Create a curve for the branch
        branch_curve = rg.LineCurve(start_point, end_point)

        # Create a pipe around the branch curve
        branch_pipe = rg.Brep.CreatePipe(branch_curve, shell_thickness, True, rg.PipeCapMode.Round, True, 0.1, 0.1)[0]
        branches.append(branch_pipe)

    # Create the shell by unioning all branch elements with the core
    all_elements = [core] + branches
    shell = rg.Brep.CreateBooleanUnion(all_elements, 0.01)

    return shell if shell else all_elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(5.0, 10.0, 20, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(3.0, 15.0, 10, 0.3, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(4.0, 8.0, 15, 0.2, randomness_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(6.0, 12.0, 25, 0.4, randomness_seed=18)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(7.0, 14.0, 30, 0.6, randomness_seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
