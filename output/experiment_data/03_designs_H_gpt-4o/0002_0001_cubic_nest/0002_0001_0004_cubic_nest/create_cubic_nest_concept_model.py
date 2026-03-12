# Created for 0002_0001_cubic_nest.json

""" Summary:
The function `create_cubic_nest_concept_model` generates an architectural concept model by creating a series of interlocking cubic volumes, embodying the 'Cubic nest' metaphor. It organizes cubes in layered arrangements, emphasizing spatial interplay between solid and void. The model incorporates randomness in cube size and positioning, reflecting the complexity and interconnectedness suggested by the metaphor. Each layer's height and variation factor allow for distinct spatial experiences, encouraging exploration. The result is a dynamic structure that balances individual cube identities with a cohesive whole, embodying a protective shell that invites discovery within its nested volumes."""

#! python 3
function_code = """def create_cubic_nest_concept_model(base_cube_size, num_layers, layer_height, variation_factor, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Cubic nest' metaphor.

    This function creates a series of layered, modular cubic volumes that interlock and overlap,
    focusing on the interplay of solid and void spaces. The cubes are arranged vertically to form
    a protective and dynamic structure, emphasizing a sense of exploration and interconnectedness.

    Parameters:
    - base_cube_size: float, the size of the base cube in meters.
    - num_layers: int, the number of vertical layers of cubes.
    - layer_height: float, the height increment between each layer.
    - variation_factor: float, a factor determining the scale variation of cubes within layers (0 to 1).
    - seed: int, seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the layered cubic nest model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    breps = []
    current_height = 0

    for layer in range(num_layers):
        layer_scale = 1 + random.uniform(-variation_factor, variation_factor)
        cube_size = base_cube_size * layer_scale
        
        num_cubes_in_layer = random.randint(3, 6)
        for i in range(num_cubes_in_layer):
            # Randomly position the cube within the layer
            offset_x = random.uniform(-0.5, 0.5) * cube_size
            offset_y = random.uniform(-0.5, 0.5) * cube_size

            # Create a base cube
            base_cube = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(offset_x, offset_x + cube_size),
                rg.Interval(offset_y, offset_y + cube_size),
                rg.Interval(current_height, current_height + cube_size)
            )

            # Convert the box to a Brep and add to the list
            brep_cube = base_cube.ToBrep()
            breps.append(brep_cube)

        # Increment the height for the next layer
        current_height += layer_height

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept_model(2.0, 5, 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept_model(1.0, 4, 2.0, 0.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept_model(3.0, 6, 1.0, 0.2, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept_model(1.5, 3, 2.5, 0.4, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept_model(2.5, 7, 1.0, 0.6, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
