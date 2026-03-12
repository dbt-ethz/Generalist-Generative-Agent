# Created for 0008_0005_branching_network_shell.json

""" Summary:
The function `generate_branching_network_shell_v2` creates an architectural concept model based on the "branching network shell" metaphor by generating a fractal structure with a network of branching elements. It uses recursive branching to create a rhythmic and organic geometry, reflecting interconnected natural systems. The model features a semi-transparent shell that emphasizes light and air interaction, aligning with the design task's goal of promoting a dynamic relationship with the environment. By adjusting parameters like base size, height, branching levels, and transparency, the function allows for diverse interpretations of the metaphor, fostering adaptability and harmony in architectural design."""

#! python 3
function_code = """def generate_branching_network_shell_v2(seed: int, base_size: float, height: float, branching_levels: int, transparency: float):
    \"""
    Generate an architectural Concept Model inspired by the 'branching network shell' metaphor.

    This function creates a fractal-like structure with branching elements that form a rhythmic and organic pattern.
    The model includes a layered, semi-transparent shell to emphasize the interaction of light and air, promoting 
    growth and harmony with the environment.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicable results.
    - base_size (float): The base size of the structure (meters).
    - height (float): The total height of the structure (meters).
    - branching_levels (int): The number of hierarchical levels of branching.
    - transparency (float): A value between 0 and 1 representing the degree of transparency of the shell.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    def create_branches(base_curve, level):
        if level == 0:
            return []

        branches = []
        curve_length = base_curve.GetLength()
        division_count = random.randint(2, 4)
        division_points = base_curve.DivideByCount(division_count, True)

        if not division_points:
            return branches

        for i in range(1, len(division_points)):
            start = base_curve.PointAt(division_points[i-1])
            end = base_curve.PointAt(division_points[i])
            branch_curve = rg.LineCurve(start, end)
            branches.append(branch_curve)

            # Recursively create sub-branches
            sub_branch_curve = branch_curve.DuplicateCurve()
            sub_branch_curve.Transform(rg.Transform.Scale(start, 0.7))
            sub_branches = create_branches(sub_branch_curve, level - 1)
            branches.extend(sub_branches)

        return branches

    # Create initial base structure
    base_circle = rg.Circle(rg.Plane.WorldXY, base_size)
    initial_curve = base_circle.ToNurbsCurve()
    branches = create_branches(initial_curve, branching_levels)

    # Create semi-transparent shell
    shell = []
    for branch in branches:
        offset_distance = base_size * (0.1 + transparency * 0.2)
        offset_curve = branch.DuplicateCurve()
        offset_curve.Transform(rg.Transform.Translation(rg.Vector3d(0, 0, offset_distance)))
        loft = rg.Brep.CreateFromLoft([branch, offset_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            shell.append(loft[0])

    # Raise the structure to the specified height
    for i, brep in enumerate(shell):
        translation = rg.Transform.Translation(rg.Vector3d(0, 0, (i / len(shell)) * height))
        brep.Transform(translation)

    return shell"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_branching_network_shell_v2(seed=42, base_size=5.0, height=10.0, branching_levels=3, transparency=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_branching_network_shell_v2(seed=123, base_size=3.5, height=8.0, branching_levels=4, transparency=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_branching_network_shell_v2(seed=99, base_size=4.0, height=12.0, branching_levels=2, transparency=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_branching_network_shell_v2(seed=2023, base_size=6.0, height=15.0, branching_levels=5, transparency=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_branching_network_shell_v2(seed=7, base_size=2.5, height=6.0, branching_levels=2, transparency=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
