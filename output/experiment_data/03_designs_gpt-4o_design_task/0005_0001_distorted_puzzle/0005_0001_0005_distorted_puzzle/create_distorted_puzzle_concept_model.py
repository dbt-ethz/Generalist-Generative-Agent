# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Distorted puzzle" metaphor by creating a series of interlocking geometric volumes. It defines a base size, height variation, and skew factor to produce varying, slightly misaligned shapes that evoke movement and tension. Each volume is randomly adjusted in height and skew, while translation vectors create a sense of interlocking and exploration. The model comprises unique, irregularly shaped spaces that connect coherently, reflecting the metaphor's theme of dynamic, interconnected forms. The final output is a list of 3D geometries that embody the metaphor's essence, inviting discovery within the design."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_size, height_variation, skew_factor, seed_value):
    \"""
    Creates an architectural Concept Model embodying the 'Distorted puzzle' metaphor by assembling a series of
    interlocking geometric volumes with slight misalignments. This function generates dynamic and visually intriguing
    spaces that promote exploration and discovery.

    Parameters:
    - base_size (float): The base size of the modules in meters.
    - height_variation (float): Maximum height variation for the volumes in meters.
    - skew_factor (float): The amount of skew applied to the volumes, affecting the distortion.
    - seed_value (int): Seed for random number generation to ensure replicability.

    Returns:
    - list of RhinoCommon.Geometry.Brep: A list of Breps representing the generated 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed_value)

    def create_volume(base_size, height, skew):
        \"""Helper function to create a skewed box volume.\"""
        box_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_size, 0, 0),
            rg.Point3d(base_size, base_size, 0),
            rg.Point3d(0, base_size, 0),
            rg.Point3d(random.uniform(-skew, skew), random.uniform(-skew, skew), height),
            rg.Point3d(base_size + random.uniform(-skew, skew), random.uniform(-skew, skew), height),
            rg.Point3d(base_size + random.uniform(-skew, skew), base_size + random.uniform(-skew, skew), height),
            rg.Point3d(random.uniform(-skew, skew), base_size + random.uniform(-skew, skew), height)
        ]

        return rg.Brep.CreateFromBox(box_corners)

    volumes = []
    num_volumes = random.randint(5, 10)  # Randomly choose the number of volumes

    for i in range(num_volumes):
        height = base_size + random.uniform(-height_variation, height_variation)
        skew = skew_factor * (0.5 - random.random())  # Skew can be positive or negative
        volume = create_volume(base_size, height, skew)

        # Translate the volume to create a sense of interlocking
        translation_vector = rg.Vector3d(
            random.uniform(-base_size, base_size),
            random.uniform(-base_size, base_size),
            random.uniform(-height_variation, height_variation)
        )
        volume.Translate(translation_vector)

        volumes.append(volume)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(5.0, 2.0, 1.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(3.0, 1.0, 0.8, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(4.0, 1.5, 2.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(6.0, 3.0, 1.0, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(7.0, 2.5, 1.2, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
