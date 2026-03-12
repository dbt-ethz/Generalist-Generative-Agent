# Created for 0008_0002_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model inspired by the metaphor of a "branching network shell." It constructs a dome-like structure that represents the organic silhouette of interwoven branches. The parameters define the dome's radius, height, number of branching pathways, and thickness. Using randomization, the function simulates branches that extend from the dome, creating a structure that balances enclosed and open spaces. This design fosters fluidity and interconnectedness, allowing light and air to permeate through, reflecting the protective yet permeable nature of the metaphor while integrating seamlessly with the environment."""

#! python 3
function_code = """def create_branching_network_shell(radius, height, num_branches, branch_thickness, seed):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.

    Parameters:
    - radius (float): The radius of the dome-like structure.
    - height (float): The maximum height of the dome.
    - num_branches (int): The number of branching pathways.
    - branch_thickness (float): The thickness of the branches.
    - seed (int): The seed for random number generation to ensure replicable results.

    Returns:
    - List of Breps: A list containing the 3D geometries of the concept model.
    \"""

    import Rhino
    import random
    from Rhino.Geometry import Point3d, Vector3d, Brep, NurbsSurface, Line
    from System.Collections.Generic import List
    import math

    # Set seed for replicable randomness
    random.seed(seed)

    # Create the dome surface
    dome = Rhino.Geometry.Sphere(Point3d(0, 0, height / 2), radius).ToBrep()

    # List to store all geometry
    geometry = []

    # Create branching pathways
    for _ in range(num_branches):
        # Random start and end points on the dome
        angle = random.uniform(0, 2 * math.pi)
        start_z = random.uniform(0, height)
        end_z = random.uniform(0, height)
        
        start_pt = Point3d(radius * math.cos(angle), radius * math.sin(angle), start_z)
        end_pt = Point3d((radius - branch_thickness) * math.cos(angle), (radius - branch_thickness) * math.sin(angle), end_z)

        # Create a line for the branch
        branch_line = Line(start_pt, end_pt)
        
        # Create a pipe around the line to form the branch
        branch_pipe = Rhino.Geometry.Brep.CreatePipe(branch_line.ToNurbsCurve(), branch_thickness, True, Rhino.Geometry.PipeCapMode.Round, True, 0.01, 0.01)[0]
        
        geometry.append(branch_pipe)

    # Merge dome and branches
    geometry.append(dome)

    return geometry"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(5.0, 10.0, 8, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(3.0, 15.0, 10, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(4.0, 12.0, 6, 0.4, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(6.0, 8.0, 12, 0.6, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(7.0, 20.0, 5, 0.7, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
