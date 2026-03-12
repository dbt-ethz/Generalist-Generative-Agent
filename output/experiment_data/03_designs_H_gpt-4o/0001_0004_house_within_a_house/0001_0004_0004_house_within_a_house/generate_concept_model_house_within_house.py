# Created for 0001_0004_house_within_a_house.json

""" Summary:
The function `generate_concept_model_house_within_house` creates an architectural model based on the metaphor of a "House within a house." It generates a series of nested layers, represented as interlocking cubic forms, which illustrate the concept of nesting and protection. Each layer is incrementally smaller, creating a spatial hierarchy that transitions from an outer protective envelope to an inner sanctuary. The function employs random rotations for the layers to enhance visual complexity, while parameters like height and layer count allow for customization. This approach facilitates an experiential journey, emphasizing the interplay between public and private spaces within the design."""

#! python 3
function_code = """def generate_concept_model_house_within_house(base_width, base_depth, height, layer_count, seed=None):
    \"""
    Generates a conceptual architectural model based on the 'House within a house' metaphor.

    This function creates a series of interlocking or nested cubic forms that represent
    different spatial realms, transitioning from an outer protective layer to an inner sanctuary.
    The model uses a rectangular base and incrementally smaller layers to evoke a sense of nesting and spatial hierarchy.

    Parameters:
    - base_width (float): The width of the outermost rectangular layer.
    - base_depth (float): The depth of the outermost rectangular layer.
    - height (float): The height of each layer.
    - layer_count (int): The number of nested layers.
    - seed (int, optional): A seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the layers of the Concept Model.
    \"""
    
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    # Ensure valid input
    if layer_count < 1 or height <= 0 or base_width <= 0 or base_depth <= 0:
        raise ValueError("Invalid input parameters for concept model.")

    # Calculate the decrement in dimension for each nested layer
    width_decrement = base_width * 0.15
    depth_decrement = base_depth * 0.15

    # Generate the layers
    breps = []
    for i in range(layer_count):
        # Calculate dimensions for this layer
        current_width = base_width - i * width_decrement
        current_depth = base_depth - i * depth_decrement

        # Create a box for this layer
        base_plane = rg.Plane.WorldXY
        box_corners = [
            rg.Point3d(-current_width / 2, -current_depth / 2, 0),
            rg.Point3d(current_width / 2, -current_depth / 2, 0),
            rg.Point3d(current_width / 2, current_depth / 2, 0),
            rg.Point3d(-current_width / 2, current_depth / 2, 0),
            rg.Point3d(-current_width / 2, -current_depth / 2, height)
        ]

        box = rg.Box(base_plane, box_corners)
        brep_box = box.ToBrep()

        # Randomly rotate the layer to create interwoven effect
        if i % 2 == 0:
            angle = random.uniform(-0.1, 0.1)  # Small random angle
            rotation_axis = rg.Line(box_corners[0], rg.Point3d(0, 0, height)).Direction
            brep_box.Transform(rg.Transform.Rotation(angle, rotation_axis, rg.Point3d(0, 0, 0)))

        breps.append(brep_box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_concept_model_house_within_house(10.0, 8.0, 3.0, 5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_concept_model_house_within_house(15.0, 10.0, 4.0, 3, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_concept_model_house_within_house(12.0, 9.0, 2.5, 4, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_concept_model_house_within_house(20.0, 15.0, 5.0, 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_concept_model_house_within_house(18.0, 12.0, 3.5, 7, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
