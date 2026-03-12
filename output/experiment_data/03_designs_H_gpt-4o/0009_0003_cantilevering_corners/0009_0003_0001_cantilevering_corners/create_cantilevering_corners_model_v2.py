# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a central mass with various cantilevered extensions. It employs parameters like length, width, height, and orientation to define each cantilever's position and form. The central mass serves as a stable core, while the cantilevered sections project outward at different angles and heights, creating a dynamic interplay between stability and motion. This design approach emphasizes contrasting scales and materiality, while voids beneath the cantilevers enhance the sense of suspension, inviting exploration and interaction with the surrounding environment."""

#! python 3
function_code = """def create_cantilevering_corners_model_v2(base_size, cantilever_params, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Cantilevering corners' metaphor using a different approach.

    This function generates a model with a central mass and multiple cantilevered sections, each with varying dimensions
    and orientations, emphasizing the dynamic interplay between stability and motion.

    Parameters:
    - base_size (tuple): A tuple of three floats (width, depth, height) representing the dimensions of the central base.
    - cantilever_params (list of dicts): A list of dictionaries, each containing parameters for a cantilever:
        - 'length' (float): Length of the cantilever.
        - 'width' (float): Width of the cantilever.
        - 'height' (float): Height of the cantilever from the base.
        - 'orientation' (tuple): A tuple of three floats (x, y, z) for the orientation vector.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for reproducibility
    random.seed(seed)

    # Create the central mass
    base_width, base_depth, base_height = base_size
    central_mass = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, base_height))
    geometries = [central_mass.ToBrep()]

    # Generate cantilevered sections
    for params in cantilever_params:
        length = params['length']
        width = params['width']
        height = params['height']
        orientation = params['orientation']
        
        # Create a cantilevered box
        cantilever_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, length),
            rg.Interval(-width / 2, width / 2),
            rg.Interval(0, base_height / 4)
        )

        # Move the cantilever to the appropriate height and orientation
        translation = rg.Vector3d(orientation[0], orientation[1], height)
        cantilever_box.Transform(rg.Transform.Translation(translation))

        # Rotate the cantilever based on the orientation vector
        orientation_vector = rg.Vector3d(orientation[0], orientation[1], 0)
        if orientation_vector.IsZero:
            continue
        rotation_axis = rg.Vector3d.CrossProduct(rg.Vector3d(0, 0, 1), orientation_vector)
        rotation_angle = math.acos(rg.Vector3d(0, 0, 1) * orientation_vector / (rg.Vector3d(0, 0, 1).Length * orientation_vector.Length))
        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, rg.Point3d(0, 0, height))
        cantilever_box.Transform(rotation_transform)

        # Add the cantilever to the list of geometries
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model_v2((10.0, 5.0, 3.0), [{'length': 4.0, 'width': 1.0, 'height': 2.0, 'orientation': (1, 0, 0)}, {'length': 3.0, 'width': 1.5, 'height': 1.5, 'orientation': (0, 1, 0)}])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model_v2((8.0, 6.0, 4.0), [{'length': 5.0, 'width': 2.0, 'height': 3.0, 'orientation': (0, 0, 1)}, {'length': 3.5, 'width': 1.0, 'height': 2.5, 'orientation': (1, 1, 0)}])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model_v2((12.0, 7.0, 5.0), [{'length': 6.0, 'width': 2.5, 'height': 4.0, 'orientation': (1, 0, 0)}, {'length': 2.5, 'width': 3.0, 'height': 3.0, 'orientation': (0, 1, 1)}])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model_v2((15.0, 10.0, 6.0), [{'length': 7.0, 'width': 2.0, 'height': 3.0, 'orientation': (1, 1, 0)}, {'length': 4.0, 'width': 1.5, 'height': 2.0, 'orientation': (0, -1, 0)}])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model_v2((9.0, 4.0, 5.0), [{'length': 3.0, 'width': 1.0, 'height': 1.0, 'orientation': (0, 1, 0)}, {'length': 5.0, 'width': 2.0, 'height': 2.0, 'orientation': (1, 0, 1)}])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
