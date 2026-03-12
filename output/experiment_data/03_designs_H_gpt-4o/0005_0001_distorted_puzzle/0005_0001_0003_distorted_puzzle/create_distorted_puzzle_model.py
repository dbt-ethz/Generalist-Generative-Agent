# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model that embodies the 'Distorted puzzle' metaphor by assembling interlocking geometric volumes. Each volume is created as a distorted box, with random misalignments applied to its corners, reflecting the metaphor's emphasis on complexity and dynamism. The function allows for variability in size, number of volumes, and distortion levels, ensuring a unique design each time. By translating these volumes randomly, the model achieves a visually intriguing arrangement that promotes exploration and interaction among spaces, capturing the essence of a puzzle with interconnected yet irregular forms."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size=10, num_volumes=6, distortion_factor=0.2, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'Distorted puzzle' metaphor, featuring interlocking
    geometric volumes with slight misalignments. The design emphasizes a dynamic interplay of forms, creating
    pathways that invite exploration.

    Parameters:
    - base_size (float): The base size of the primary volume in meters.
    - num_volumes (int): The number of interlocking volumes to assemble.
    - distortion_factor (float): The factor by which each volume can be distorted.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    def create_distorted_volume(base_size):
        \"""Creates a distorted box volume with specified base size.\"""
        # Define the initial box corners
        corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_size, 0, 0),
            rg.Point3d(base_size, base_size, 0),
            rg.Point3d(0, base_size, 0),
            rg.Point3d(0, 0, base_size),
            rg.Point3d(base_size, 0, base_size),
            rg.Point3d(base_size, base_size, base_size),
            rg.Point3d(0, base_size, base_size)
        ]

        # Apply random distortion to each corner within the given factor
        distorted_corners = [
            rg.Point3d(
                corner.X + random.uniform(-distortion_factor, distortion_factor),
                corner.Y + random.uniform(-distortion_factor, distortion_factor),
                corner.Z + random.uniform(-distortion_factor, distortion_factor)
            )
            for corner in corners
        ]

        # Create a Brep from the distorted corners
        return rg.Brep.CreateFromBox(distorted_corners)

    volumes = []
    for _ in range(num_volumes):
        # Create a distorted volume
        volume = create_distorted_volume(base_size)
        
        # Random translation to interlock the volumes
        translation_vector = rg.Vector3d(
            random.uniform(-base_size * 0.5, base_size * 0.5),
            random.uniform(-base_size * 0.5, base_size * 0.5),
            random.uniform(-base_size * 0.5, base_size * 0.5)
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
    geometry = create_distorted_puzzle_model(base_size=15, num_volumes=8, distortion_factor=0.3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_size=12, num_volumes=5, distortion_factor=0.1, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_size=20, num_volumes=10, distortion_factor=0.4, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_size=8, num_volumes=4, distortion_factor=0.25, seed=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_size=18, num_volumes=7, distortion_factor=0.15, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
