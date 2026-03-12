# Created for 0008_0001_branching_network_shell.json

""" Summary:
The provided function, `create_branching_network_shell`, generates an architectural concept model inspired by the metaphor of a "branching network shell." It creates an organic, interconnected structure by defining a base circle and vertical axis, where branches emerge at specified intervals. Each branch is generated with random angles and directions, simulating the growth and divergence found in natural systems. The function sweeps circles along these branches to form solid structures, then lofts these with a top circle to create a protective shell. This approach results in a dynamic, adaptive form that integrates with the surrounding environment, embodying fluidity and connection."""

#! python 3
function_code = """def create_branching_network_shell(base_radius, height, num_branches, shell_thickness):
    \"""
    Creates a conceptual architectural model based on the 'branching network shell' metaphor. The model
    consists of a branching network of paths or structural elements that converge and diverge, forming
    an organic and interconnected shell.

    Parameters:
    - base_radius (float): The radius of the base of the shell.
    - height (float): The total height of the shell structure.
    - num_branches (int): The number of main branches in the network.
    - shell_thickness (float): The thickness of the shell structure.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the branching network shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    # Create a base circle
    base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)

    # Create a vertical axis line for the shell
    axis_line = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height))

    # Divide the axis line into segments where branches will emerge
    division_points = axis_line.ToNurbsCurve().DivideByCount(num_branches, True)

    breps = []

    for i, param in enumerate(division_points):
        point = axis_line.PointAt(param)
        # Determine branch angle and direction
        angle = random.uniform(-0.5, 0.5) * math.pi
        direction_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 1)
        direction_vector.Unitize()

        # Create a branch path
        branch_line = rg.Line(point, point + direction_vector * (base_radius * 0.5))

        # Sweep a circle along the branch line to create a branch solid
        branch_circle = rg.Circle(branch_line.PointAt(0), shell_thickness)
        sweep = rg.SweepOneRail()
        branch_brep = sweep.PerformSweep(branch_line.ToNurbsCurve(), branch_circle.ToNurbsCurve())[0]
        breps.append(branch_brep)

    # Loft the base circle and top branches to form the shell
    top_circle = rg.Circle(rg.Plane.WorldXY, base_radius * 0.5).ToNurbsCurve()
    loft = rg.Brep.CreateFromLoft([base_circle.ToNurbsCurve(), top_circle], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
    if loft:
        breps.append(loft[0])

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(5.0, 10.0, 8, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(3.5, 12.0, 10, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(4.0, 15.0, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(6.0, 8.0, 5, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(7.0, 20.0, 12, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
