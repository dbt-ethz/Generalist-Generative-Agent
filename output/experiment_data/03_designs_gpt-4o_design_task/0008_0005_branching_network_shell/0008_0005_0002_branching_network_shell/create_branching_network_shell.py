# Created for 0008_0005_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model based on the provided "branching network shell" metaphor. It creates a 3D structure using a specified number of branching elements, each represented by curves that simulate organic, fractal-like growth. The model features layered shells with a defined thickness, allowing for semi-transparency and interaction with light and air. This design approach emphasizes interconnectedness and fluidity, reflecting the metaphor's essence of natural systems. The randomness in branch placement fosters a dynamic, adaptable form, ensuring the model resonates with the themes of growth and harmony with the environment."""

#! python 3
function_code = """def create_branching_network_shell(width, depth, height, branch_count, layer_thickness, randomness_seed=42):
    \"""
    Generates an architectural Concept Model embodying the 'branching network shell' metaphor.
    
    Args:
        width (float): The width of the bounding box of the model in meters.
        depth (float): The depth of the bounding box of the model in meters.
        height (float): The height of the bounding box of the model in meters.
        branch_count (int): The number of major branching elements in the structure.
        layer_thickness (float): The thickness of each layer in the shell structure.
        randomness_seed (int, optional): Seed for random number generation to ensure replicability. Default is 42.

    Returns:
        list: A list of Rhino.Geometry.Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)

    # Create the main bounding box for the model
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
    
    # Generate branching network
    branches = []
    for i in range(branch_count):
        start_point = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), 0)
        end_point = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), height)
        branch_curve = rg.NurbsCurve.Create(False, 3, [start_point, end_point])
        if branch_curve:  # Check if curve creation was successful
            branches.append(branch_curve)

    # Creating a layered shell using the branching curves
    shell_layers = []
    for branch in branches:
        offset_start = branch.PointAtStart + rg.Vector3d(0, 0, layer_thickness)
        offset_end = branch.PointAtEnd + rg.Vector3d(0, 0, layer_thickness)
        offset_curve = rg.NurbsCurve.Create(False, 3, [offset_start, offset_end])
        if offset_curve:  # Check if curve creation was successful
            loft = rg.Brep.CreateFromLoft([branch, offset_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft:  # Check if loft creation was successful
                shell_layers.append(loft[0])

    # Create a semi-transparent shell by adding more layers
    transparency_layers = []
    for i in range(1, branch_count):
        for layer in shell_layers:
            offset_brep = layer.DuplicateBrep()
            translation = rg.Transform.Translation(rg.Vector3d(0, 0, i * layer_thickness))
            offset_brep.Transform(translation)
            transparency_layers.append(offset_brep)

    # Combine all breps into a single list
    all_geometries = shell_layers + transparency_layers

    return all_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(10.0, 5.0, 15.0, 8, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(12.0, 8.0, 20.0, 10, 0.3, randomness_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(15.0, 10.0, 25.0, 5, 0.15, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(20.0, 15.0, 30.0, 12, 0.1, randomness_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(8.0, 6.0, 18.0, 6, 0.25, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
