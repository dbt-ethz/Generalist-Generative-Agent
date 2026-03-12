# Created for 0008_0001_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates a 3D architectural concept model based on the metaphor of a "branching network shell." It creates a dynamic structure that embodies organic growth and interconnectivity by defining parameters like base radius, height, branch count, and division count. The function uses trigonometric calculations to position primary branches around a base circle, while random deviations introduce an organic feel. These branches are lofted to form a shell-like surface that reflects the metaphor's protective, open nature, allowing light and air to permeate. This results in fluid, adaptive designs integrated with the environment."""

#! python 3
function_code = """def create_branching_network_shell(base_radius=10.0, height=15.0, branch_count=5, division_count=10):
    \"""
    Creates a 3D architectural Concept Model based on the 'branching network shell' metaphor.
    
    Parameters:
    - base_radius (float): The radius of the base circle from which the network branches out.
    - height (float): The overall height of the shell structure.
    - branch_count (int): The number of primary branches extending from the base.
    - division_count (int): The number of divisions along the height for the branching network.
    
    Returns:
    - List of Breps: A list of 3D geometries representing the branching network shell.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Vector3d, Circle, Plane, Polyline, LoftType, Brep
    from math import cos, sin, radians

    # Seed for reproducibility
    random.seed(42)

    # Create a base circle
    base_circle = Circle(Plane.WorldXY, base_radius)

    # Calculate the angle increment for branch division
    angle_increment = 360.0 / branch_count

    # Store the geometry
    breps = []

    for i in range(branch_count):
        # Calculate the initial point on the base circle for each branch
        angle_rad = radians(i * angle_increment)
        x = base_radius * cos(angle_rad)
        y = base_radius * sin(angle_rad)

        # Create a primary branch polyline
        branch_points = [Point3d(x, y, 0)]
        for j in range(1, division_count + 1):
            # Random deviation for organic feel
            deviation = random.uniform(-0.5, 0.5)

            # Calculate next point in the branch
            new_x = x + deviation
            new_y = y + deviation
            new_z = (height / division_count) * j

            branch_points.append(Point3d(new_x, new_y, new_z))

        # Create polyline and loft it to form a surface
        polyline = Polyline(branch_points)
        loft = Brep.CreateFromLoft([polyline.ToNurbsCurve()], Point3d.Unset, Point3d.Unset, LoftType.Straight, False)
        
        if loft is not None:
            breps.extend(loft)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(base_radius=12.0, height=20.0, branch_count=6, division_count=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(base_radius=8.0, height=10.0, branch_count=4, division_count=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(base_radius=15.0, height=25.0, branch_count=8, division_count=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(base_radius=10.0, height=18.0, branch_count=7, division_count=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(base_radius=5.0, height=10.0, branch_count=3, division_count=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
