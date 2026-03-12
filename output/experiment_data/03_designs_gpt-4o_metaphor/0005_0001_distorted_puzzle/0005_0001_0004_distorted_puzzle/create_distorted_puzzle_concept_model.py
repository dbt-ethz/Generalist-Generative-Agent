# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept_model`, generates an architectural concept model based on the metaphor of a "Distorted puzzle." It creates a series of interlocking 3D elements that feature irregular shapes and misaligned forms, embodying the complexity and unpredictability of a distorted puzzle. By manipulating the sizes and positions of these elements with a distortion factor, the model expresses a dynamic interplay, maintaining coherence despite its irregularities. The function outputs a list of geometric representations, allowing for varied configurations, thereby facilitating exploration of architectural concepts that are visually engaging and interconnected."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_size, num_elements, distortion_factor, seed=None):
    \"""
    Create a 3D architectural Concept Model based on the metaphor 'Distorted puzzle'.
    
    This function generates a complex, interlocking arrangement of volumes that appear 
    misaligned or irregularly shaped, reflecting a dynamic interplay of forms that fit together 
    in unexpected ways. The distorted aspect introduces unpredictability, while the puzzle nature 
    maintains coherence.

    Args:
        base_size (float): The size of the base element in meters.
        num_elements (int): The number of interlocking elements to create.
        distortion_factor (float): A factor controlling the degree of distortion.
        seed (int, optional): A seed for the random number generator to ensure replicability.

    Returns:
        List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    if seed is not None:
        random.seed(seed)

    geometries = []

    for i in range(num_elements):
        # Define a base box for each element
        x = random.uniform(-distortion_factor, distortion_factor) * base_size
        y = random.uniform(-distortion_factor, distortion_factor) * base_size
        z = random.uniform(-distortion_factor, distortion_factor) * base_size

        # Randomly adjust the size of each box to create a "distorted" effect
        width = base_size + random.uniform(-distortion_factor, distortion_factor) * base_size
        depth = base_size + random.uniform(-distortion_factor, distortion_factor) * base_size
        height = base_size + random.uniform(-distortion_factor, distortion_factor) * base_size

        box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + width), rg.Interval(y, y + depth), rg.Interval(z, z + height))

        # Convert box to brep and add to the list of geometries
        brep = box.ToBrep()
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(2.0, 10, 0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(1.5, 15, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(3.0, 8, 0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(2.5, 12, 0.6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(1.0, 20, 0.2, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
