# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a central core and adding extensions that project outward. It defines the core's dimensions and randomly generates cantilevered elements, varying their lengths and heights to evoke a sense of movement and balance. The function employs Rhino's geometry tools to create solid forms, using the core's faces as attachment points for the extensions. This approach highlights the contrast between solid and void, emphasizing dynamic tension and engaging with light and shadow to enhance the model's visual impact, thereby fulfilling the design task."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_width, core_depth, core_height, num_extensions, max_extension_length, extension_height_variation):
    \"""
    Generates an architectural Concept Model with a central core and cantilevered extensions.
    
    Parameters:
    core_width (float): The width of the central core in meters.
    core_depth (float): The depth of the central core in meters.
    core_height (float): The height of the central core in meters.
    num_extensions (int): Number of cantilevered extensions.
    max_extension_length (float): Maximum length of the cantilevered extensions in meters.
    extension_height_variation (float): Maximum variation in height for extensions in meters.

    Returns:
    list: A list of Rhino.Geometry.Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino
    import System
    from Rhino.Geometry import Point3d, Vector3d, Box, Plane

    # Seed the random number generator for reproducibility
    random_seed = 42
    random = System.Random(random_seed)

    # Create the central core as a solid box
    core_plane = Plane.WorldXY
    core_box = Box(core_plane, Rhino.Geometry.Interval(0, core_width), Rhino.Geometry.Interval(0, core_depth), Rhino.Geometry.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    # Prepare list for storing geometries
    geometries = [core_brep]

    # Generate cantilevered extensions
    for i in range(num_extensions):
        # Randomly select a face of the core to attach the extension
        face_index = random.Next(0, core_brep.Faces.Count)
        face = core_brep.Faces[face_index]

        # Determine the extension direction based on the selected face normal
        face_normal = face.NormalAt(0.5, 0.5)
        extension_direction = Vector3d(face_normal)
        
        # Determine the length and height of the extension
        extension_length = random.NextDouble() * max_extension_length
        extension_height = core_height + (random.NextDouble() - 0.5) * extension_height_variation

        # Get the center of the face to position the base of the extension
        u, v = face.Domain(0).Mid, face.Domain(1).Mid
        center_point = face.PointAt(u, v)

        # Create a plane at the center point of the face with normal in the extension direction
        extension_plane = Plane(center_point, extension_direction)
        extension_plane.Origin += Vector3d(extension_direction) * core_depth / 2
        
        # Create the extension box
        extension_box = Box(extension_plane, Rhino.Geometry.Interval(0, extension_length), Rhino.Geometry.Interval(0, core_depth / 2), Rhino.Geometry.Interval(0, extension_height))
        extension_brep = extension_box.ToBrep()

        # Add the extension to the list of geometries
        geometries.append(extension_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(5.0, 3.0, 4.0, 4, 2.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(6.0, 4.0, 5.0, 3, 3.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(7.0, 5.0, 6.0, 5, 4.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(4.0, 2.0, 3.0, 6, 1.5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(8.0, 6.0, 7.0, 2, 5.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
