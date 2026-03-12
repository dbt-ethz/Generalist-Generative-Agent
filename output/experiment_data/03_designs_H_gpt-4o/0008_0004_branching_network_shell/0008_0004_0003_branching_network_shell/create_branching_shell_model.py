# Created for 0008_0004_branching_network_shell.json

""" Summary:
The function `create_branching_shell_model` generates an architectural concept model inspired by the "branching network shell" metaphor. It constructs a central core from which multiple branching elements radiate, simulating organic growth patterns found in nature. The model features a complex arrangement of branches that diverge and converge, promoting spatial exploration. An outer shell is created with openings to facilitate airflow and natural light, embodying the protective yet permeable qualities of the metaphor. The interplay of light and shadow within the model enhances its adaptive characteristics, ensuring harmonious integration with the surrounding environment."""

#! python 3
function_code = """def create_branching_shell_model(center_point, core_radius, core_height, num_branches, branch_radius, shell_opening_size):
    \"""
    Generates an architectural Concept Model based on the 'branching network shell' metaphor.
    The model features a central core with branching elements and a permeable shell structure.

    Parameters:
    - center_point (tuple): The 3D coordinates of the central core's base (x, y, z).
    - core_radius (float): Radius of the central core from where branches emerge, in meters.
    - core_height (float): Height of the central core, in meters.
    - num_branches (int): Number of branching elements.
    - branch_radius (float): Radius of each branch, in meters.
    - shell_opening_size (float): Size of the openings in the shell, in meters.

    Returns:
    - List of 3D geometries (breps) representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensures replicable randomness

    geometries = []

    # Create the central core
    core_center = rg.Point3d(*center_point)
    core_base = rg.Circle(rg.Plane(core_center, rg.Vector3d.ZAxis), core_radius)
    core_cylinder = rg.Cylinder(core_base, core_height).ToBrep(True, True)
    geometries.append(core_cylinder)

    # Create branching elements
    for i in range(num_branches):
        angle_rad = 2 * math.pi * i / num_branches
        branch_vector = rg.Vector3d(math.cos(angle_rad), math.sin(angle_rad), random.uniform(0.3, 0.7))
        branch_vector.Unitize()
        branch_vector *= core_height * random.uniform(0.5, 1.0)

        branch_start = rg.Point3d(
            core_center.X + core_radius * math.cos(angle_rad),
            core_center.Y + core_radius * math.sin(angle_rad),
            random.uniform(0, core_height)
        )
        branch_end = branch_start + branch_vector

        branch_line = rg.Line(branch_start, branch_end)
        branch_curve = rg.NurbsCurve.CreateFromLine(branch_line)
        branch_profile = rg.Circle(rg.Plane(branch_start, branch_vector), branch_radius).ToNurbsCurve()
        branch_brep = rg.Brep.CreateFromSweep(branch_curve, branch_profile, True, 0.01)[0]

        geometries.append(branch_brep)

    # Create the outer shell
    shell_center = rg.Point3d(center_point[0], center_point[1], core_height / 2)
    shell_sphere = rg.Sphere(shell_center, core_radius * 2).ToBrep()

    # Create openings in the shell
    opening_centers = [
        rg.Point3d(
            shell_center.X + random.uniform(-core_radius, core_radius),
            shell_center.Y + random.uniform(-core_radius, core_radius),
            shell_center.Z + random.uniform(-core_radius / 2, core_radius / 2)
        )
        for _ in range(num_branches)
    ]

    for oc in opening_centers:
        opening_sphere = rg.Sphere(oc, shell_opening_size).ToBrep()
        diff_result = rg.Brep.CreateBooleanDifference([shell_sphere], [opening_sphere], 0.01)
        if diff_result:
            shell_sphere = diff_result[0]

    geometries.append(shell_sphere)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_shell_model((0, 0, 0), 2.0, 5.0, 8, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_shell_model((1, 1, 1), 3.0, 4.0, 10, 0.4, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_shell_model((2, 2, 0), 1.5, 6.0, 5, 0.6, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_shell_model((3, 0, 0), 2.5, 7.0, 6, 0.7, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_shell_model((0, 3, 1), 1.0, 3.0, 12, 0.3, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
