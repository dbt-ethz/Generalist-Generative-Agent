# Created for 0008_0005_branching_network_shell.json

""" Summary:
The `generate_branching_network_shell` function creates an architectural concept model inspired by the 'branching network shell' metaphor. It employs a recursive method to generate a fractal pattern of branching elements that reflect organic forms found in nature, such as mycelium networks. By defining parameters like seed, base radius, number of branches, and maximum height, the function constructs a rhythmic, layered structure that balances openness and enclosure. The semi-transparent shell allows light and air to permeate, fostering a dynamic interaction with the environment while promoting continuity and adaptability, ultimately embodying the interconnectedness and growth theme inherent in the metaphor."""

#! python 3
function_code = """def generate_branching_network_shell(seed:int, base_radius:float, num_branches:int, max_height:float):
    \"""
    Generate an architectural Concept Model embodying the 'branching network shell' metaphor.
    
    This function creates a fractal matrix of branching elements that form a rhythmic and organic pattern,
    with a semi-transparent layered shell. The model emphasizes the interaction of light and air, promoting
    growth and harmony with the environment. The structure is designed to be both protective and open, 
    allowing for fluid transitions and moments of reflection.

    Parameters:
    - seed (int): A seed for the random number generator to ensure replicability.
    - base_radius (float): The base radius for the branching elements.
    - num_branches (int): The number of primary branches in the structure.
    - max_height (float): The maximum height of the model.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, LineCurve, Brep, Vector3d
    from Rhino.Geometry import PipeCapMode
    from Rhino.Collections import Point3dList
    from math import radians

    random.seed(seed)
    
    def create_branch(start_point, direction, length, radius, depth, max_depth):
        if depth >= max_depth:
            return []
        
        end_point = Point3d(start_point.X + direction.X * length, start_point.Y + direction.Y * length, start_point.Z + direction.Z * length)
        line = LineCurve(start_point, end_point)
        pipe = Brep.CreatePipe(line, radius, True, PipeCapMode.Flat, True, 0.01, 0.01)[0]
        breps = [pipe]

        # Create branches off this branch
        num_sub_branches = random.randint(2, 4)
        sub_branches = []
        for _ in range(num_sub_branches):
            angle = radians(random.uniform(30, 60))
            sub_direction = direction
            sub_direction.Rotate(angle, Vector3d(0, 0, 1))
            sub_length = length * random.uniform(0.5, 0.8)
            sub_radius = radius * random.uniform(0.5, 0.7)
            sub_branches.extend(create_branch(end_point, sub_direction, sub_length, sub_radius, depth + 1, max_depth))
        
        return breps + sub_branches

    # Start creating the main branches
    base_point = Point3d(0, 0, 0)
    branches = []
    for i in range(num_branches):
        angle = radians(i * (360 / num_branches))
        direction = Vector3d(1, 0, 0)
        direction.Rotate(angle, Vector3d(0, 0, 1))
        branch_length = max_height / random.uniform(2, 3)
        branch_radius = base_radius * random.uniform(0.8, 1.2)
        branches.extend(create_branch(base_point, direction, branch_length, branch_radius, 0, 3))
    
    return branches"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_branching_network_shell(seed=42, base_radius=5.0, num_branches=8, max_height=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_branching_network_shell(seed=7, base_radius=3.5, num_branches=12, max_height=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_branching_network_shell(seed=15, base_radius=4.0, num_branches=10, max_height=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_branching_network_shell(seed=21, base_radius=6.0, num_branches=6, max_height=18.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_branching_network_shell(seed=30, base_radius=4.5, num_branches=15, max_height=22.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
