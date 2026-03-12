# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model based on the 'Distorted puzzle' metaphor by creating interlocking geometric volumes that are slightly misaligned. It first establishes a base volume and applies random distortions to its vertices, introducing unpredictability while maintaining coherence. The function then creates additional volumes by translating the base volume with random shifts, enhancing the sense of movement and tension. The resulting model consists of irregularly shaped, interlocking forms that evoke exploration and discovery, embodying the metaphor's characteristics of complexity and interconnectedness while forming a visually intriguing assembly."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size=10, num_volumes=5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Distorted puzzle' metaphor.

    The model is composed of interlocking geometric volumes with slight misalignments,
    emphasizing a dynamic and visually intriguing assembly that suggests movement and tension.

    Parameters:
    - base_size (float): The base size in meters for the largest volume.
    - num_volumes (int): The number of interlocking volumes to generate.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    def create_base_volume(size):
        \"""Creates a base box volume with the given size.\"""
        return rg.Box(rg.Plane.WorldXY, rg.Interval(0, size), rg.Interval(0, size), rg.Interval(0, size)).ToBrep()

    def distort_volume(brep, distortion_factor=0.1):
        \"""Applies a slight distortion to the volume by randomly moving its vertices.\"""
        vertices = brep.DuplicateVertices()
        new_vertices = []
        for vertex in vertices:
            offset = rg.Vector3d(random.uniform(-distortion_factor, distortion_factor),
                                 random.uniform(-distortion_factor, distortion_factor),
                                 random.uniform(-distortion_factor, distortion_factor))
            new_vertices.append(vertex + offset)
        
        # Create a distorted brep using a bounding box and moving its corners
        distorted_brep = rg.Brep()
        for face in brep.Faces:
            face_brep = face.DuplicateFace(False)
            for i in range(face_brep.Vertices.Count):
                face_brep.Vertices[i].Location = new_vertices[i]
            distorted_brep.Append(face_brep)
        return distorted_brep

    def interlock_volumes(base_volume, num_interlocks, max_shift=2):
        \"""Create interlocking volumes starting from a base volume.\"""
        volumes = [base_volume]
        base_box = base_volume.GetBoundingBox(True)

        for _ in range(num_interlocks):
            # Clone and shift the base volume
            shift_vector = rg.Vector3d(random.uniform(-max_shift, max_shift),
                                       random.uniform(-max_shift, max_shift),
                                       random.uniform(-max_shift, max_shift))
            transform = rg.Transform.Translation(shift_vector)
            new_volume = base_volume.DuplicateBrep()
            new_volume.Transform(transform)
            distorted_volume = distort_volume(new_volume)
            volumes.append(distorted_volume)

        return volumes

    # Create the base volume and interlock additional volumes
    base_volume = create_base_volume(base_size)
    all_volumes = interlock_volumes(base_volume, num_volumes - 1)

    return all_volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(base_size=15, num_volumes=7, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_size=12, num_volumes=6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_size=20, num_volumes=4, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_size=8, num_volumes=10, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_size=18, num_volumes=3, seed=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
