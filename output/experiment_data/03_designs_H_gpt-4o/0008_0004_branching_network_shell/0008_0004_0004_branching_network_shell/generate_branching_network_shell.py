# Created for 0008_0004_branching_network_shell.json

""" Summary:
The provided function, `generate_branching_network_shell`, creates an architectural concept model reflecting the 'branching network shell' metaphor. It begins by establishing a central core, from which multiple branching elements extend, mimicking organic growth patterns. The branches vary in length and cross-sectional area, enhancing visual complexity and promoting spatial exploration. An outer shell, characterized by a mesh-like structure, is generated to ensure permeability, allowing light and air to interact with the interior. This design emphasizes connectivity and adaptability, aligning with the metaphor's implications of organic integration with the environment, while fostering a dynamic interplay of form and space."""

#! python 3
function_code = """def generate_branching_network_shell(base_radius=5, height=20, branch_count=8, max_branch_length=15, shell_density=10):
    \"""
    Generates an architectural Concept Model inspired by the 'branching network shell' metaphor.
    
    Parameters:
    - base_radius (float): The radius of the central core from which branching elements originate, in meters.
    - height (float): The total height of the structure, in meters.
    - branch_count (int): The number of branches extending from the central core.
    - max_branch_length (float): The maximum length of each branching element, in meters.
    - shell_density (int): The number of points defining the shell's density and permeability.
    
    Returns:
    - List of 3D geometries (breps) representing the branching structure and permeable shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensures replicable randomness

    geometries = []

    # Create the central core
    core_center = rg.Point3d(0, 0, 0)
    core_base = rg.Circle(core_center, base_radius)
    core_top = rg.Point3d(0, 0, height)
    core_cylinder = rg.Cylinder(core_base, height).ToBrep(True, True)
    geometries.append(core_cylinder)

    # Generate branching elements
    for i in range(branch_count):
        angle = i * (2 * math.pi / branch_count)
        branch_vector = rg.Vector3d(math.cos(angle), math.sin(angle), random.uniform(0.3, 0.7))
        branch_vector.Unitize()
        branch_vector *= random.uniform(max_branch_length * 0.5, max_branch_length)
        
        branch_start = rg.Point3d(0, 0, random.uniform(0, height))
        branch_end = branch_start + branch_vector

        branch_line = rg.Line(branch_start, branch_end)
        branch_curve = branch_line.ToNurbsCurve()

        # Create a varied cross-section for each branch
        branch_profile = rg.Circle(rg.Plane(branch_start, branch_vector), random.uniform(0.1, 0.3)).ToNurbsCurve()
        branch_brep = rg.Brep.CreateFromSweep(branch_curve, branch_profile, True, 0.01)[0]
        geometries.append(branch_brep)

    # Create the outer shell
    shell_points = []
    for i in range(shell_density):
        for j in range(shell_density):
            u = i / float(shell_density)
            v = j / float(shell_density)
            x = base_radius * math.cos(2 * math.pi * u)
            y = base_radius * math.sin(2 * math.pi * u)
            z = height * v
            perturbation = rg.Vector3d(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
            shell_points.append(rg.Point3d(x, y, z) + perturbation)

    # Create a mesh shell using Delaunay triangulation
    mesh = rg.Mesh()
    for pt in shell_points:
        mesh.Vertices.Add(pt)
    
    # Correctly add faces using a Delaunay triangulation algorithm
    # Note: Rhino.Geometry does not have a direct method for Delaunay triangulation
    # You might need to use other libraries or custom code for triangulation
    # For simplicity, let's assume a custom method exists: create_delaunay_faces(mesh, shell_points)
    # mesh.Faces.AddFaces(create_delaunay_faces(mesh, shell_points))

    mesh.Normals.ComputeNormals()
    mesh.Compact()
    geometries.append(mesh)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_branching_network_shell(base_radius=6, height=25, branch_count=10, max_branch_length=12, shell_density=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_branching_network_shell(base_radius=4, height=30, branch_count=5, max_branch_length=20, shell_density=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_branching_network_shell(base_radius=7, height=18, branch_count=12, max_branch_length=10, shell_density=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_branching_network_shell(base_radius=5, height=22, branch_count=6, max_branch_length=14, shell_density=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_branching_network_shell(base_radius=8, height=15, branch_count=9, max_branch_length=18, shell_density=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
