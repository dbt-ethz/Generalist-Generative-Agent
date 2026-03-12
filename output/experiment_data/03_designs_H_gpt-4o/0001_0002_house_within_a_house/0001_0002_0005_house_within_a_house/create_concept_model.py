# Created for 0001_0002_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model based on the "House within a house" metaphor by creating a series of interlocking and nested geometric forms. Each layer represents varying dimensions, evoking a sense of containment and retreat. The outer shell serves as a protective layer, while the inner layers, with random height variations, allow for exploration of spatial hierarchies. The use of contrasting dimensions and heights emphasizes the transition from the outer to inner spaces, fostering a dialogue between openness and enclosure. The resulting 3D geometries visually convey the layered relationships and dynamic interactions central to the design task."""

#! python 3
function_code = """def create_concept_model(length_outer, width_outer, height_outer, num_layers, height_variation, random_seed=1):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor, using interlocking
    and nested forms to convey a sense of nesting and protection.

    Parameters:
    - length_outer (float): The length of the outer shell.
    - width_outer (float): The width of the outer shell.
    - height_outer (float): The height of the outer shell.
    - num_layers (int): The number of nested layers within the outer shell.
    - height_variation (float): The maximum variation in height for each inner layer.
    - random_seed (int, optional): Seed for random number generation to ensure replicability.

    Returns:
    - List of Breps: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness
    random.seed(random_seed)

    # List to hold the resulting geometries
    geometries = []

    # Create the outer shell as a box
    outer_shell = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length_outer), rg.Interval(0, width_outer), rg.Interval(0, height_outer))
    geometries.append(outer_shell.ToBrep())

    # Calculate step values for reducing dimensions
    length_step = length_outer / (num_layers + 1)
    width_step = width_outer / (num_layers + 1)

    # Create nested inner layers
    for i in range(num_layers):
        # Calculate dimensions for current layer
        length_inner = length_outer - (i + 1) * length_step
        width_inner = width_outer - (i + 1) * width_step
        height_inner = height_outer - random.uniform(0, height_variation)

        # Create an inner layer as a box
        inner_layer = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval((length_outer - length_inner) / 2, (length_outer + length_inner) / 2),
            rg.Interval((width_outer - width_inner) / 2, (width_outer + width_inner) / 2),
            rg.Interval(0, height_inner)
        )
        geometries.append(inner_layer.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10.0, 8.0, 6.0, 3, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(15.0, 12.0, 10.0, 5, 3.0, random_seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(20.0, 15.0, 12.0, 4, 1.5, random_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(25.0, 20.0, 15.0, 6, 4.0, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(30.0, 25.0, 20.0, 2, 5.0, random_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
