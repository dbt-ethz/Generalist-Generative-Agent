# Created for 0008_0005_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model inspired by the "branching network shell" metaphor. It constructs a fractal-like structure characterized by a matrix of branching elements that create an organic and rhythmic pattern. The function employs recursive methods to generate branches that diverge and converge, reflecting interconnected natural systems. Each branch forms part of a layered, semi-transparent shell, allowing light and air to filter through, enhancing the dynamic interaction with the environment. The model emphasizes fluidity and adaptability, promoting a harmonious relationship between the architecture and nature."""

#! python 3
function_code = """def create_branching_network_shell(seed: int, base_radius: float, max_height: float, num_branches: int, layer_thickness: float):
    \"""
    Generates an architectural Concept Model embodying the 'branching network shell' metaphor.

    This function constructs a fractal-like structure with branching elements that form a rhythmic
    and organic pattern. It uses a layered shell to interact with light and air, promoting growth
    and harmony with the environment.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicable results.
    - base_radius (float): The radius of the base circle from which branches originate (meters).
    - max_height (float): The maximum height of the structure (meters).
    - num_branches (int): Number of primary branches in the structure.
    - layer_thickness (float): Thickness of each layer in the shell (meters).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep objects representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    def create_fractal_branches(center, radius, height, depth):
        if depth <= 0:
            return []

        branches = []
        angle_increment = 2 * math.pi / num_branches
        for i in range(num_branches):
            angle = i * angle_increment
            x = center.X + radius * math.cos(angle)
            y = center.Y + radius * math.sin(angle)
            z = center.Z + height
            end_point = rg.Point3d(x, y, z)

            line = rg.Line(center, end_point)
            branches.append(line.ToNurbsCurve())

            # Recursive call for sub-branches
            branches.extend(create_fractal_branches(end_point, radius * 0.5, height * 0.6, depth - 1))

        return branches

    def create_layered_shell(curves, thickness):
        shells = []
        for curve in curves:
            offset_curve = curve.DuplicateCurve()
            offset_curve.Translate(rg.Vector3d(0, 0, thickness))
            loft = rg.Brep.CreateFromLoft([curve, offset_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft:
                shells.append(loft[0])
        return shells

    base_point = rg.Point3d(0, 0, 0)
    branches = create_fractal_branches(base_point, base_radius, max_height / num_branches, 3)

    shell_layers = create_layered_shell(branches, layer_thickness)

    return shell_layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(seed=42, base_radius=5.0, max_height=10.0, num_branches=6, layer_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(seed=7, base_radius=4.0, max_height=15.0, num_branches=8, layer_thickness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(seed=12, base_radius=3.5, max_height=12.0, num_branches=5, layer_thickness=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(seed=21, base_radius=6.0, max_height=20.0, num_branches=10, layer_thickness=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(seed=99, base_radius=7.0, max_height=18.0, num_branches=4, layer_thickness=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
