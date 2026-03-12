# Created for 0008_0005_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model based on the "branching network shell" metaphor by creating a layered structure that reflects fractal patterns. It takes parameters like base radius, layer count, branch factor, height, and transparency to define the model's characteristics. The function constructs each layer with branching elements that diverge and converge, mimicking natural systems. It employs a tapering effect for the radius and creates semi-transparent shell layers that allow light and air to permeate. This process fosters a dynamic relationship with the environment, promoting a sense of growth and harmony inherent in nature."""

#! python 3
function_code = """def create_branching_network_shell(base_radius, layer_count, branch_factor, height, transparency):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.
    
    The model consists of a fractal-like matrix of branching elements forming a layered shell,
    allowing for a rhythmic and organic pattern that emphasizes continuity and moments of rest.
    The semi-transparent shell interacts dynamically with light and air, promoting harmony with the environment.

    Parameters:
    - base_radius (float): The radius of the base circle from which the branching network originates.
    - layer_count (int): Number of layers in the shell structure.
    - branch_factor (int): The factor by which each branch splits into further branches.
    - height (float): The total height of the structure.
    - transparency (float): A value between 0 and 1 representing the transparency of the shell.

    Returns:
    - List of Brep: A list of 3D geometries representing the branching network shell.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)

    def create_branching_layer(center_point, radius, branch_factor, height):
        branches = []
        for i in range(branch_factor):
            angle = 2 * math.pi * i / branch_factor
            direction = rg.Vector3d(radius * math.cos(angle), radius * math.sin(angle), height)
            branch_line = rg.Line(center_point, center_point + direction)
            branches.append(branch_line.ToNurbsCurve())
        return branches

    def create_shell_layer(base_curves, height, transparency):
        shell_surfaces = []
        for curve in base_curves:
            loft_curve = curve.DuplicateCurve()
            translation_vector = rg.Vector3d(0, 0, height)
            loft_curve.Translate(translation_vector)
            loft_surface = rg.Brep.CreateFromLoft([curve, loft_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft_surface:
                shell_surfaces.append(loft_surface[0])
        return shell_surfaces

    center = rg.Point3d(0, 0, 0)
    all_breps = []
    layer_height = height / layer_count

    for layer in range(layer_count):
        current_height = layer * layer_height
        current_radius = base_radius * (1 - (layer / layer_count))  # Tapering effect
        branches = create_branching_layer(center, current_radius, branch_factor, layer_height)
        shell_layer = create_shell_layer(branches, layer_height, transparency)
        all_breps.extend(shell_layer)

    return all_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(base_radius=5.0, layer_count=10, branch_factor=3, height=20.0, transparency=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(base_radius=7.0, layer_count=8, branch_factor=4, height=15.0, transparency=0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(base_radius=4.0, layer_count=12, branch_factor=5, height=25.0, transparency=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(base_radius=6.0, layer_count=6, branch_factor=2, height=10.0, transparency=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(base_radius=3.0, layer_count=15, branch_factor=6, height=30.0, transparency=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
