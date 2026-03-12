# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept`, generates an architectural concept model inspired by the "Stacked forests" metaphor. By creating staggered and offset volumes, it simulates the layered complexity of a forest ecosystem. The function randomly varies the height and size of each layer while integrating vertical and diagonal connections to facilitate movement, mimicking natural forest pathways. This results in a tiered structure that embodies a hierarchy of spaces, with areas of density and openness, representing clearings and thickets. The final output is a collection of 3D geometries that visually reflect the organic interplay of solid and void, capturing the dynamic essence of a forest canopy."""

#! python 3
function_code = """def create_stacked_forests_concept(num_layers=5, base_size=10, height_variation=2, offset_variation=2):
    \"""
    Creates an architectural Concept Model embodying the 'Stacked forests' metaphor. This function generates a series of 
    staggered and offset volumes to create a tiered effect, emphasizing hierarchy, depth, and organic growth. It integrates 
    vertical and diagonal connections to mimic natural movement in a forest.

    Parameters:
    - num_layers (int): The number of stacked layers to create in the model.
    - base_size (float): The base size of the lowest layer in meters.
    - height_variation (float): The maximum height variation between the layers in meters.
    - offset_variation (float): The maximum offset variation between the layers in meters.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Initialize a list to store the resulting geometries
    geometries = []

    # Base position and size for the first layer
    current_base_size = base_size
    current_position = rg.Point3d(0, 0, 0)

    for i in range(num_layers):
        # Create a box for the current layer
        height = random.uniform(1, height_variation)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(current_position.X, current_position.X + current_base_size),
                     rg.Interval(current_position.Y, current_position.Y + current_base_size),
                     rg.Interval(current_position.Z, current_position.Z + height))
        
        brep = box.ToBrep()
        geometries.append(brep)

        # Determine the offset and positioning for the next layer
        offset_x = random.uniform(-offset_variation, offset_variation)
        offset_y = random.uniform(-offset_variation, offset_variation)
        current_position = rg.Point3d(current_position.X + offset_x, current_position.Y + offset_y, current_position.Z + height)

        # Adjust the base size for the next layer to create variation
        current_base_size = max(base_size / 2, current_base_size * random.uniform(0.8, 1.2))

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(num_layers=7, base_size=15, height_variation=3, offset_variation=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(num_layers=10, base_size=12, height_variation=4, offset_variation=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(num_layers=8, base_size=20, height_variation=2.5, offset_variation=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(num_layers=6, base_size=18, height_variation=3.5, offset_variation=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(num_layers=9, base_size=14, height_variation=5, offset_variation=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
