# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model by interpreting the metaphor of "Cantilevering corners," which emphasizes dynamic tension through projecting elements. It begins by creating a central core, establishing a stable base. Randomly generated extensions are then added, which extend outward from various faces of the core, simulating cantilevers that appear to defy gravity. Each extension varies in length and height, embodying the metaphor's essence of balance and instability. The use of random rotations enhances the sense of movement, while contrasting materials and dimensions accentuate the interplay between solid structures and voids, resulting in a visually compelling model."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_dimensions, num_extensions, extension_max_length, extension_max_height, seed=42):
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Create the central core
    core_width, core_depth, core_height = core_dimensions
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Convert the core box to a Brep to access its faces
    core_brep = core_box.ToBrep()

    # Function to create a cantilevered extension
    def create_extension(core_brep, max_length, max_height):
        # Randomly select a face of the core to attach the extension
        face_index = random.randint(0, core_brep.Faces.Count - 1)
        face = core_brep.Faces[face_index]

        # Determine the direction based on face normal and random rotation
        face_center = face.PointAt(face.Domain(0).Mid, face.Domain(1).Mid)
        normal = face.NormalAt(face.Domain(0).Mid, face.Domain(1).Mid)
        rotation_angle = random.uniform(-30, 30)
        rotation_axis = rg.Vector3d.ZAxis
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, face_center)

        # Define extension dimensions
        length = random.uniform(max_length / 2, max_length)
        height = random.uniform(max_height / 2, max_height)
        width = core_width / 4

        # Create the extension box
        face_plane = face.TryGetPlane()[1]  # Get the plane from the face
        extension_box = rg.Box(face_plane, rg.Interval(0, length), rg.Interval(-width / 2, width / 2), rg.Interval(0, height))
        extension_brep = extension_box.ToBrep()
        extension_brep.Transform(rotation)

        return extension_brep

    # Add extensions
    for _ in range(num_extensions):
        extension = create_extension(core_brep, extension_max_length, extension_max_height)
        geometries.append(extension)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model((10, 5, 15), 3, 8, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model((12, 6, 10), 4, 10, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model((15, 7, 20), 2, 12, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model((8, 4, 12), 5, 9, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model((14, 5, 18), 6, 15, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
