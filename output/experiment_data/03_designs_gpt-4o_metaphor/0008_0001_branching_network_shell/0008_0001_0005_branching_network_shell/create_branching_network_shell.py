# Created for 0008_0001_branching_network_shell.json

""" Summary:
The `create_branching_network_shell` function generates an architectural concept model inspired by the "branching network shell" metaphor. It utilizes a parametric approach to create an organic structure characterized by interconnected pathways. The function defines parameters such as base radius, height, number of branches, branch angles, and shell thickness, simulating a natural growth pattern. By creating a base circle and extruding it into a shell, the function adds diverging and converging branches that evoke a dynamic form. The result is a model that embodies fluidity and integration with the environment, reflecting the metaphor's essence of connection and adaptability."""

#! python 3
function_code = """def create_branching_network_shell(base_radius, height, num_branches, branch_angle, shell_thickness):
    \"""
    Creates a branching network shell Concept Model using a parametric approach.
    The model is inspired by the metaphor of a 'branching network shell', emphasizing
    organic growth and interconnectedness.

    Parameters:
    - base_radius (float): The radius of the base of the shell structure in meters.
    - height (float): The height of the shell structure in meters.
    - num_branches (int): The number of primary branches forming the network.
    - branch_angle (float): The angle at which the branches diverge in degrees.
    - shell_thickness (float): The thickness of the shell in meters.

    Returns:
    - List of Brep: A list of 3D geometries representing the branching network shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for randomness
    random.seed(42)

    # Helper function to create a branch
    def create_branch(base_point, direction, length, angle):
        # Create the main line of the branch
        main_line = rg.Line(base_point, base_point + direction * length)

        # Calculate branching vectors
        perp_vector = rg.Vector3d.CrossProduct(direction, rg.Vector3d.ZAxis)
        perp_vector.Unitize()
        branch_vector = rg.Vector3d(perp_vector)
        branch_vector.Rotate(math.radians(angle), direction)

        # Create branch lines
        branch_line1 = rg.Line(main_line.To, main_line.To + branch_vector * (length * 0.6))
        branch_line2 = rg.Line(main_line.To, main_line.To - branch_vector * (length * 0.6))

        return main_line, branch_line1, branch_line2

    # Create base circle
    base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
    base_circle_curve = base_circle.ToNurbsCurve()

    # Create shell surface
    shell_surface = rg.Surface.CreateExtrusion(base_circle_curve, rg.Vector3d(0, 0, height))

    # Store all branches
    branches = []

    # Create initial branches from the base
    for i in range(num_branches):
        angle_offset = (360.0 / num_branches) * i
        direction = rg.Vector3d(
            math.cos(math.radians(angle_offset)),
            math.sin(math.radians(angle_offset)),
            0
        )
        branch_base_point = rg.Point3d(direction * base_radius)
        branch_length = height * 0.5
        main_branch, sub_branch1, sub_branch2 = create_branch(branch_base_point, direction, branch_length, branch_angle)

        branches.extend([main_branch, sub_branch1, sub_branch2])

    # Convert branch lines to pipes (cylindrical shapes)
    pipes = []
    for branch in branches:
        pipe = rg.Brep.CreatePipe(branch.ToNurbsCurve(), shell_thickness, True, rg.PipeCapMode.Round, True, 0.1, 0.1)[0]
        pipes.append(pipe)

    # Return the shell surface and the branching pipes
    return [shell_surface] + pipes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(5.0, 10.0, 8, 30.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(3.0, 7.5, 5, 45.0, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(4.0, 12.0, 6, 60.0, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(6.0, 15.0, 10, 20.0, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(2.5, 5.0, 4, 75.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
