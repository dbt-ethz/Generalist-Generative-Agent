# Created for 0008_0004_branching_network_shell.json

""" Summary:
The function `branching_network_shell` generates an architectural concept model inspired by the "branching network shell" metaphor. It starts by creating a central core from which multiple branches radiate, simulating natural branching patterns. The parameters define the core's size, branch angles, and the thickness of the outer shell. Each branch is represented as a cylindrical geometry, emphasizing vertical and horizontal dispersion. An outer shell, designed to be protective yet permeable, is created by subtracting the core and branches from a larger spherical shape, allowing light and air to pass through. This approach fosters a dynamic, interconnected spatial experience."""

#! python 3
function_code = """def branching_network_shell(radius=10, height=30, num_branches=5, branch_angle=45, shell_thickness=0.5):
    \"""
    Creates an architectural Concept Model reflecting the 'branching network shell' metaphor.
    
    Parameters:
    - radius (float): The radius of the central core from where branches emanate, in meters.
    - height (float): The height of the entire structure, in meters.
    - num_branches (int): The number of primary branches radiating from the central core.
    - branch_angle (float): The angle at which branches diverge from the central core, in degrees.
    - shell_thickness (float): The thickness of the outer shell layer, in meters.
    
    Returns:
    - List of 3D geometries (breps) representing the branching structure and shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Added import for math module

    random.seed(42)  # Ensures replicable randomness

    geometries = []

    # Create the central core
    core_center = rg.Point3d(0, 0, 0)
    core_base = rg.Circle(core_center, radius)
    core_top = rg.Point3d(0, 0, height)
    core_cylinder = rg.Cylinder(core_base, height).ToBrep(True, True)
    geometries.append(core_cylinder)

    # Create primary branching elements
    for i in range(num_branches):
        angle_rad = random.uniform(0, 2 * math.pi)
        branch_vector = rg.Vector3d(math.sin(angle_rad), math.cos(angle_rad), random.uniform(0.5, 1.0))
        branch_vector.Unitize()
        
        # Create branch path
        branch_path = rg.Line(core_center, branch_vector * height)
        branch_curve = rg.NurbsCurve.CreateFromLine(branch_path)
        
        # Sweep a circular profile along branch path to create branch geometry
        profile_circle = rg.Circle(rg.Plane(branch_curve.PointAtStart, branch_curve.TangentAtStart), shell_thickness)
        branch_brep = rg.Brep.CreateFromSweep(branch_curve, profile_circle.ToNurbsCurve(), True, 0.01)[0]
        geometries.append(branch_brep)

    # Create the outer shell
    shell_height = height * 0.8
    shell_radius = radius * 1.5
    shell_center = rg.Point3d(0, 0, shell_height / 2)
    shell_sphere = rg.Sphere(shell_center, shell_radius).ToBrep()
    
    # Subtract core and branches from the shell to create a permeable effect
    shell_perforated = shell_sphere
    for geom in geometries:
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
    geometry = branching_network_shell(radius=15, height=40, num_branches=6, branch_angle=60, shell_thickness=0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = branching_network_shell(radius=12, height=25, num_branches=4, branch_angle=30, shell_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = branching_network_shell(radius=8, height=20, num_branches=3, branch_angle=90, shell_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = branching_network_shell(radius=20, height=50, num_branches=8, branch_angle=75, shell_thickness=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = branching_network_shell(radius=10, height=35, num_branches=7, branch_angle=50, shell_thickness=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
