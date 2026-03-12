# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The function `create_dynamic_cantilever_model` generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It creates a central mass that serves as a stable base, from which various cantilevered segments extend at different heights and angles, embodying a dynamic interplay of stability and motion. The cantilevers are designed with varying lengths and orientations to emphasize their dramatic projections. Additionally, voids are incorporated beneath these extensions, enhancing the sense of suspension and tension. The model's interaction with natural light and shadows further enriches the exploration of spatial dynamics, inviting engagement with its environment."""

#! python 3
function_code = """def create_dynamic_cantilever_model(base_dims, cantilever_specs, void_height_factor, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Cantilevering corners' metaphor.

    This function generates a central mass with dynamically cantilevered segments that extend 
    at various heights and orientations, emphasizing the interplay between stability and motion. 
    The model integrates voids beneath the cantilevers to accentuate suspension.

    Parameters:
    - base_dims (tuple): Dimensions of the central mass (width, depth, height) in meters.
    - cantilever_specs (list of dicts): Specifications for each cantilever, each dict containing:
        - 'length': Length of the cantilever.
        - 'height_offset': Height offset from the base where the cantilever starts.
        - 'orientation_angle': Orientation angle in degrees from the base.
    - void_height_factor (float): Factor to determine the height of the voids beneath cantilevers.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(seed)

    # Unpack base dimensions
    base_width, base_depth, base_height = base_dims

    # Create the central base mass
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_width, 0, 0),
        rg.Point3d(base_width, base_depth, 0),
        rg.Point3d(0, base_depth, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_width, 0, base_height),
        rg.Point3d(base_width, base_depth, base_height),
        rg.Point3d(0, base_depth, base_height)
    ]
    base_box = rg.Brep.CreateFromBox(base_corners)

    geometries = [base_box]

    # Create cantilevered sections
    for spec in cantilever_specs:
        length = spec['length']
        height_offset = spec['height_offset']
        orientation_angle = spec['orientation_angle']

        # Create cantilever starting at a random base corner
        base_corner = random.choice([
            rg.Point3d(0, 0, height_offset),
            rg.Point3d(base_width, 0, height_offset),
            rg.Point3d(base_width, base_depth, height_offset),
            rg.Point3d(0, base_depth, height_offset)
        ])

        # Define the cantilever geometry
        cantilever_corners = [
            base_corner,
            base_corner + rg.Vector3d(length, 0, 0),
            base_corner + rg.Vector3d(length, length, 0),
            base_corner + rg.Vector3d(0, length, 0),
            base_corner + rg.Vector3d(0, 0, base_height / 4),
            base_corner + rg.Vector3d(length, 0, base_height / 4),
            base_corner + rg.Vector3d(length, length, base_height / 4),
            base_corner + rg.Vector3d(0, length, base_height / 4)
        ]
        cantilever_box = rg.Brep.CreateFromBox(cantilever_corners)

        # Rotate cantilever around its base corner
        rotation_transform = rg.Transform.Rotation(
            math.radians(orientation_angle), rg.Vector3d.ZAxis, base_corner)
        cantilever_box.Transform(rotation_transform)

        geometries.append(cantilever_box)

        # Create void beneath the cantilever
        void_base = base_corner + rg.Vector3d(0, 0, -base_height * void_height_factor)
        void_corners = [
            void_base,
            void_base + rg.Vector3d(length, 0, 0),
            void_base + rg.Vector3d(length, length, 0),
            void_base + rg.Vector3d(0, length, 0),
            base_corner,
            base_corner + rg.Vector3d(length, 0, 0),
            base_corner + rg.Vector3d(length, length, 0),
            base_corner + rg.Vector3d(0, length, 0)
        ]
        void_box = rg.Brep.CreateFromBox(void_corners)
        geometries.append(void_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cantilever_model((5, 5, 3), [{'length': 2, 'height_offset': 1, 'orientation_angle': 30}, {'length': 3, 'height_offset': 2, 'orientation_angle': 45}], 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cantilever_model((10, 8, 4), [{'length': 4, 'height_offset': 2, 'orientation_angle': 60}], 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cantilever_model((7, 3, 5), [{'length': 3, 'height_offset': 1.5, 'orientation_angle': 15}, {'length': 2.5, 'height_offset': 2.5, 'orientation_angle': 75}], 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cantilever_model((8, 6, 4), [{'length': 5, 'height_offset': 1, 'orientation_angle': 90}, {'length': 2, 'height_offset': 2, 'orientation_angle': 120}], 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cantilever_model((6, 4, 2), [{'length': 2.5, 'height_offset': 1, 'orientation_angle': 90}, {'length': 3.5, 'height_offset': 1.5, 'orientation_angle': 180}], 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
