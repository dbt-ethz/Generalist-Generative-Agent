# Created for 0008_0004_branching_network_shell.json

""" Summary:
The function `generate_branching_network_shell` creates an architectural concept model based on the "branching network shell" metaphor. It begins by establishing a central ellipsoid core, from which vertical and horizontal branches emerge, mimicking natural growth patterns. The number and density of these branches can be adjusted, enhancing the model's dynamism and complexity. The outer shell is designed as a perforated surface, allowing light and air to permeate, symbolizing protection and unity with the environment. This intricate interplay of forms and spaces fosters exploration and connectivity, aligning with the metaphor's emphasis on organic integration and adaptive qualities."""

#! python 3
function_code = """def generate_branching_network_shell(center_radius=5, max_height=25, branch_density=8, shell_openness=0.3):
    \"""
    Generates an architectural Concept Model reflecting the 'branching network shell' metaphor.
    
    Parameters:
    - center_radius (float): Radius of the central core, from which the network emerges, in meters.
    - max_height (float): Maximum height of the entire structure, in meters.
    - branch_density (int): Density of branch connections originating from the central structure.
    - shell_openness (float): Openness factor of the shell, dictating perforation density (0 to 1 scale).

    Returns:
    - List of 3D geometries (breps) representing the branching network and shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for reproducibility
    random.seed(42)

    geometries = []

    # Create the central core as an ellipsoid
    core_center = rg.Point3d(0, 0, max_height / 2)
    core_ellipsoid = rg.Brep.CreateFromSphere(rg.Sphere(core_center, center_radius))
    geometries.append(core_ellipsoid)

    # Create branching network
    branch_length = max_height * 0.5
    branches = []
    for _ in range(branch_density):
        angle_xy = random.uniform(0, 2 * math.pi)
        angle_z = random.uniform(-0.5, 0.5)
        direction = rg.Vector3d(
            branch_length * random.uniform(0.7, 1.0) * math.cos(angle_xy),
            branch_length * random.uniform(0.7, 1.0) * math.sin(angle_xy),
            branch_length * angle_z
        )
        start_point = rg.Point3d(
            core_center.X + random.uniform(-center_radius, center_radius),
            core_center.Y + random.uniform(-center_radius, center_radius),
            core_center.Z + random.uniform(-center_radius / 2, center_radius / 2)
        )
        end_point = start_point + direction
        branch_line = rg.Line(start_point, end_point).ToNurbsCurve()
        branches.append(branch_line)
        # Create branch geometry
        branch_brep = rg.Brep.CreatePipe(branch_line, center_radius * 0.1, True, rg.PipeCapMode.Round, True, 0.01, 0.01)
        if branch_brep:
            geometries.append(branch_brep[0])

    # Create the outer shell as a perforated surface
    shell_radius = center_radius * 2
    shell_sphere = rg.Sphere(core_center, shell_radius).ToBrep()
    shell_perforations = []

    # Perforate the shell with circles
    for branch in branches:
        t = random.uniform(0.2, 0.8)
        circle_plane = rg.Plane(branch.PointAt(t), branch.TangentAt(t))
        perforation_radius = shell_radius * shell_openness * random.uniform(0.5, 1.0)
        circle = rg.Circle(circle_plane, perforation_radius).ToNurbsCurve()
        shell_perforations.append(circle)

    # Subtract perforations from the shell
    for hole in shell_perforations:
        planar_breps = rg.Brep.CreatePlanarBreps(hole)
        if planar_breps:
            difference_result = rg.Brep.CreateBooleanDifference([shell_sphere], planar_breps, 0.01)
            if difference_result:
                shell_sphere = difference_result[0]

    geometries.append(shell_sphere)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_branching_network_shell(center_radius=10, max_height=30, branch_density=12, shell_openness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_branching_network_shell(center_radius=7, max_height=20, branch_density=10, shell_openness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_branching_network_shell(center_radius=8, max_height=25, branch_density=15, shell_openness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_branching_network_shell(center_radius=6, max_height=22, branch_density=9, shell_openness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_branching_network_shell(center_radius=9, max_height=28, branch_density=14, shell_openness=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
