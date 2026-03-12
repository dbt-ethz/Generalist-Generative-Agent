# Created for 0008_0004_branching_network_shell.json

""" Summary:
The function `generate_branching_network_shell` creates an architectural concept model based on the "branching network shell" metaphor. It starts by forming a central cylindrical core, symbolizing the foundational point. The function then generates branching elements that radiate outward, mimicking organic structures like coral reefs, enhancing the interconnectedness of spaces. The shell surrounding the core is designed with varying degrees of openness, allowing light and air to permeate, fostering a dynamic interaction between interior and exterior. By emphasizing vertical and horizontal dispersion, the model embodies exploration and unity with the environment, aligning with the metaphor's implications."""

#! python 3
function_code = """def generate_branching_network_shell(core_radius=5, height=20, branch_density=10, shell_openness=0.7):
    \"""
    Generates an architectural Concept Model inspired by the 'branching network shell' metaphor.

    Parameters:
    - core_radius (float): The radius of the central cylindrical core, in meters.
    - height (float): The total height of the structure, in meters.
    - branch_density (int): Density of branching elements per unit height.
    - shell_openness (float): A factor (0 to 1) determining the openness of the shell, where 1 is fully open.

    Returns:
    - List of 3D geometries (breps and surfaces) representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensures replicable randomness

    geometries = []

    # Create the central core
    core_center = rg.Point3d(0, 0, 0)
    core_base = rg.Circle(core_center, core_radius)
    core_cylinder = rg.Cylinder(core_base, height).ToBrep(True, True)
    geometries.append(core_cylinder)

    # Generate branching elements
    for i in range(int(branch_density * height)):
        branch_height = random.uniform(0, height)
        branch_radius = random.uniform(core_radius * 0.2, core_radius * 0.4)
        angle = random.uniform(0, 2 * math.pi)
        branch_origin = rg.Point3d(math.cos(angle) * core_radius, math.sin(angle) * core_radius, branch_height)
        branch_direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0.2, 1))
        branch_direction.Unitize()
        branch_end = branch_origin + branch_direction * random.uniform(core_radius, core_radius * 2)
        branch_line = rg.Line(branch_origin, branch_end)
        branch_curve = branch_line.ToNurbsCurve()
        branch_brep = rg.Brep.CreatePipe(branch_curve, branch_radius, False, rg.PipeCapMode.Round, False, 0.01, 0.01)[0]
        geometries.append(branch_brep)

    # Create an outer shell with perforations
    shell_radius = core_radius * 1.5
    shell_sphere = rg.Sphere(core_center, shell_radius).ToBrep()
    shell_perforated = shell_sphere
    for geom in geometries:
        if random.random() < shell_openness:
            result = rg.Brep.CreateBooleanDifference([shell_perforated], [geom], 0.01)
            if result:
                shell_perforated = result[0]

    geometries.append(shell_perforated)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_branching_network_shell(core_radius=7, height=25, branch_density=15, shell_openness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_branching_network_shell(core_radius=4, height=15, branch_density=12, shell_openness=0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_branching_network_shell(core_radius=6, height=30, branch_density=20, shell_openness=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_branching_network_shell(core_radius=5, height=18, branch_density=10, shell_openness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_branching_network_shell(core_radius=8, height=22, branch_density=18, shell_openness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
