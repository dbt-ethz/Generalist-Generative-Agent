# Created for 0008_0004_branching_network_shell.json

""" Summary:
The provided function `generate_branching_network_shell` creates an architectural concept model based on the 'branching network shell' metaphor. It begins by establishing a central core from which branching elements radiate, emulating organic structures like coral reefs. By defining parameters such as height, branch levels, and materials, it generates a visually dynamic form with interconnected pathways. The model features a lightweight, permeable shell designed to facilitate light and air flow, embodying the metaphor's protective yet open quality. The interplay of light and shadow within the model enhances its organic, adaptive nature, promoting exploration and connection with the environment."""

#! python 3
function_code = """def generate_branching_network_shell(center_radius=5, height=20, branch_levels=3, branches_per_level=4, shell_material_thickness=0.3):
    \"""
    Generates an architectural Concept Model that embodies the 'branching network shell' metaphor.
    
    Parameters:
    - center_radius (float): Radius of the central core from which branches emerge, in meters.
    - height (float): Overall height of the structure, in meters.
    - branch_levels (int): Number of levels of branching from the core.
    - branches_per_level (int): Number of branches at each level.
    - shell_material_thickness (float): Thickness of the shell material, in meters.
    
    Returns:
    - List of 3D geometries (breps) representing the model's branching structure and shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)

    geometries = []

    # Create the central core as a vertical cylinder
    core_center = rg.Point3d(0, 0, 0)
    core_base = rg.Circle(core_center, center_radius)
    core_cylinder = rg.Cylinder(core_base, height).ToBrep(True, True)
    geometries.append(core_cylinder)

    # Function to create branching structure
    def create_branch(origin, length, angle):
        direction = rg.Vector3d(math.cos(angle), math.sin(angle), random.uniform(0.3, 0.7))
        direction.Unitize()
        direction *= length
        end_point = origin + direction
        branch_curve = rg.Line(origin, end_point).ToNurbsCurve()
        profile = rg.Circle(rg.Plane(origin, direction), shell_material_thickness).ToNurbsCurve()
        branch_brep = rg.Brep.CreateFromSweep(branch_curve, profile, True, 0.01)[0]
        return branch_brep, end_point

    # Generate branches at different levels
    level_height = height / branch_levels
    for level in range(branch_levels):
        level_origin = rg.Point3d(0, 0, level * level_height)
        branch_length = (height - level * level_height) / 2
        for i in range(branches_per_level):
            angle = i * (2 * math.pi / branches_per_level) + random.uniform(-0.1, 0.1)
            branch, branch_end = create_branch(level_origin, branch_length, angle)
            geometries.append(branch)
    
    # Create a lightweight permeable shell using a network of lofts
    shell_lines = []
    for i in range(branch_levels - 1):
        for j in range(branches_per_level):
            pt1 = rg.Point3d(center_radius * math.cos(j * (2 * math.pi / branches_per_level)), 
                             center_radius * math.sin(j * (2 * math.pi / branches_per_level)), 
                             i * level_height)
            pt2 = rg.Point3d(center_radius * math.cos(j * (2 * math.pi / branches_per_level)), 
                             center_radius * math.sin(j * (2 * math.pi / branches_per_level)), 
                             (i + 1) * level_height)
            shell_lines.append(rg.Line(pt1, pt2).ToNurbsCurve())
    
    if shell_lines:
        shell_brep = rg.Brep.CreateFromLoft(shell_lines, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if shell_brep:
            geometries.extend(shell_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_branching_network_shell(center_radius=10, height=30, branch_levels=4, branches_per_level=5, shell_material_thickness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_branching_network_shell(center_radius=7, height=25, branch_levels=3, branches_per_level=6, shell_material_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_branching_network_shell(center_radius=8, height=15, branch_levels=2, branches_per_level=3, shell_material_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_branching_network_shell(center_radius=6, height=22, branch_levels=5, branches_per_level=4, shell_material_thickness=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_branching_network_shell(center_radius=12, height=18, branch_levels=3, branches_per_level=7, shell_material_thickness=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
