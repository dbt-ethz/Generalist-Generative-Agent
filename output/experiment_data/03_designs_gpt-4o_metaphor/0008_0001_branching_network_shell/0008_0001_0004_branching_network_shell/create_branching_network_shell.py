# Created for 0008_0001_branching_network_shell.json

""" Summary:
The provided function, `create_branching_network_shell`, generates an architectural concept model inspired by the metaphor of a "branching network shell." It creates an organic, interconnected structure with a base circle and multiple primary branches that extend upward, simulating a natural branching system. Each branch's dynamic geometry is influenced by random variations in length and orientation, reflecting the metaphor's emphasis on adaptability and fluidity. Additional secondary branches further enhance the shell's complexity, resulting in a protective, permeable form that integrates with its environment, allowing light and air to permeate, ultimately embodying the metaphor's essence of connection and continuity."""

#! python 3
function_code = """def create_branching_network_shell(base_radius, height, num_branches, branch_length, seed):
    \"""
    Creates an architectural Concept Model based on the 'Branching network shell' metaphor.
    
    The model features an organic, interconnected structure reminiscent of a natural branching system.
    It forms a dynamic and adaptive shell that is both protective and permeable.

    Parameters:
    - base_radius (float): The radius of the base of the shell.
    - height (float): The total height of the shell.
    - num_branches (int): The number of primary branches emanating from the base.
    - branch_length (float): The length of each branch.
    - seed (int): Seed for random generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D structure of the shell.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create a base circle
    base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
    
    # Create primary branches
    branches = []
    for i in range(num_branches):
        angle = 2 * 3.14159 * i / num_branches
        direction = rg.Vector3d(branch_length * random.uniform(0.8, 1.2), 0, height)
        direction.Rotate(angle, rg.Vector3d.ZAxis)
        
        start_point = base_circle.PointAt(angle)
        end_point = rg.Point3d.Add(start_point, direction)
        
        branch_curve = rg.LineCurve(start_point, end_point)
        branches.append(branch_curve)

    # Create secondary branches and shell
    shell_surfaces = []
    for branch in branches:
        num_secondary = random.randint(2, 5)
        for j in range(num_secondary):
            div_param = branch.Domain.ParameterAt(j / float(num_secondary))
            point_on_branch = branch.PointAt(div_param)
            secondary_direction = rg.Vector3d(branch_length * 0.5 * random.uniform(0.8, 1.2), 0, height * 0.5)
            secondary_direction.Rotate(random.uniform(-0.5, 0.5), rg.Vector3d.ZAxis)
            
            secondary_end_point = rg.Point3d.Add(point_on_branch, secondary_direction)
            secondary_branch = rg.LineCurve(point_on_branch, secondary_end_point)
            
            loft_brep = rg.Brep.CreateFromLoft([branch, secondary_branch], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
            if loft_brep:
                shell_surfaces.extend(loft_brep)
    
    return shell_surfaces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(5.0, 10.0, 8, 3.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(4.0, 12.0, 6, 2.5, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(6.0, 15.0, 10, 4.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(7.0, 20.0, 12, 5.0, 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(3.5, 8.0, 5, 2.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
