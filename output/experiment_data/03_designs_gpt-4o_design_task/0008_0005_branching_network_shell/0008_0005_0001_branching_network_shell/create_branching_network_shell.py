# Created for 0008_0005_branching_network_shell.json

""" Summary:
The provided function generates an architectural concept model embodying the "branching network shell" metaphor through a recursive algorithm that creates a fractal-like structure. It initiates branching from a defined base point and extends into multiple directions, reflecting organic growth and interconnectedness characteristic of natural systems. Each branch represents a structural element, while the layering simulates a semi-transparent shell, allowing light and air to permeate. The model incorporates varying lengths and heights to emphasize rhythmic patterns and moments of pause, aligning with the design task's focus on fluidity and adaptability, ultimately fostering a harmonious relationship with the environment."""

#! python 3
function_code = """def create_branching_network_shell(seed: int, base_length: float, layer_height: float, num_layers: int, branch_factor: int):
    \"""
    Creates a 3D architectural Concept Model based on the 'branching network shell' metaphor.
    
    This function generates a fractal-like structure with branching elements that form a semi-transparent shell. 
    The design emphasizes organic growth, interconnectedness, and interaction with light and air.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicable results.
    - base_length (float): The base length of the primary branching element (meters).
    - layer_height (float): The height of each layer in the structure (meters).
    - num_layers (int): The number of layers to build vertically.
    - branch_factor (int): The number of branches each element splits into.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    def create_branch(start_point, direction, length, depth):
        if depth == 0:
            return []

        end_point = rg.Point3d.Add(start_point, direction * length)
        branch_line = rg.Line(start_point, end_point)
        branches = [branch_line]
        
        # Generate new branches
        for _ in range(branch_factor):
            new_direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0.5, 1))
            new_direction.Unitize()
            new_length = length * 0.7  # Reduce length for subsequent branches
            branches.extend(create_branch(end_point, new_direction, new_length, depth - 1))
        
        return branches

    base_point = rg.Point3d(0, 0, 0)
    base_direction = rg.Vector3d(0, 0, 1)
    branches = create_branch(base_point, base_direction, base_length, num_layers)

    breps = []
    for branch in branches:
        # Create a pipe around each branch for visualization of the network
        pipe = rg.Brep.CreatePipe(branch.ToNurbsCurve(), 0.1, False, rg.PipeCapMode.Round, False, 0.01, 0.01)[0]
        breps.append(pipe)
    
    # Create the layered shell structure
    for i in range(num_layers):
        height = i * layer_height
        radius = base_length * (i + 1) * 0.1
        center = rg.Point3d(0, 0, height)
        shell = rg.Brep.CreateFromSphere(rg.Sphere(center, radius))
        if shell:
            breps.append(shell)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(seed=42, base_length=5.0, layer_height=2.0, num_layers=3, branch_factor=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(seed=10, base_length=3.0, layer_height=1.5, num_layers=5, branch_factor=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(seed=99, base_length=4.0, layer_height=1.0, num_layers=4, branch_factor=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(seed=25, base_length=6.0, layer_height=1.2, num_layers=6, branch_factor=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(seed=7, base_length=2.5, layer_height=1.0, num_layers=4, branch_factor=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
