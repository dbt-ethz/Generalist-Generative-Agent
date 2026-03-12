# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The provided function, `generate_distorted_puzzle_volumes`, creates an architectural concept model that embodies the "Distorted Puzzle" metaphor. It generates a series of fragmented and interlocking volumes, varying in height and form to evoke dynamic light and shadow effects. Each volume is extruded from a base rectangle, with random twists applied for an asymmetric appearance. The design emphasizes a cohesive yet complex structure, combining individuality with interconnectedness. By allowing for varied spatial experiences, the model captures the essence of tension and equilibrium, reflecting the metaphor's implications of unpredictability and visual interest in the architectural form."""

#! python 3
function_code = """def generate_distorted_puzzle_volumes(base_area, volume_count, height_range, base_height, randomness_seed):
    \"""
    Generates an architectural Concept Model based on the 'Distorted Puzzle' metaphor.

    This function creates a series of fragmented, interlocking volumes that vary in height and form. The volumes emphasize
    a dynamic play of light and shadow, featuring asymmetric shapes and cohesion within the overall structure. The spatial
    arrangement allows for varied experiences of light and enclosure, promoting a sense of tension and equilibrium.

    Parameters:
    - base_area (tuple of floats): The base area dimensions (length, width) in meters.
    - volume_count (int): The number of volumes to generate.
    - height_range (tuple of floats): The minimum and maximum heights for the volumes in meters.
    - base_height (float): The base height from which the volumes start in meters.
    - randomness_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)
    volumes = []
    min_height, max_height = height_range
    base_length, base_width = base_area

    for _ in range(volume_count):
        # Determine random dimensions for each volume
        length = random.uniform(base_length * 0.1, base_length * 0.25)
        width = random.uniform(base_width * 0.1, base_width * 0.25)
        height = random.uniform(min_height, max_height)

        # Randomly determine the position and orientation of each volume
        x_pos = random.uniform(0, base_length - length)
        y_pos = random.uniform(0, base_width - width)

        # Create a base rectangle and extrude it to form a volume
        base_point = rg.Point3d(x_pos, y_pos, base_height)
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, length, width)
        base_rect.Transform(rg.Transform.Translation(base_point.X, base_point.Y, base_point.Z))

        # Create a distorted extrusion to form an asymmetric volume
        extrusion_vector = rg.Vector3d(0, 0, height)
        volume = rg.Extrusion.Create(base_rect.ToNurbsCurve(), height, True)

        # Apply random twist for added distortion
        twist_angle = random.uniform(-0.3, 0.3)  # Radians
        twist_center = base_point + extrusion_vector * 0.5
        twist_axis = rg.Line(twist_center, twist_center + rg.Vector3d.ZAxis * height).ToNurbsCurve()
        twist_transform = rg.Transform.Rotation(twist_angle, rg.Vector3d.ZAxis, twist_center)
        volume.Transform(twist_transform)

        # Convert the extrusion to a Brep and add to the list
        brep = volume.ToBrep()
        volumes.append(brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_distorted_puzzle_volumes((10, 5), 15, (2, 10), 0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_distorted_puzzle_volumes((8, 4), 20, (3, 12), 1, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_distorted_puzzle_volumes((12, 6), 10, (1, 8), 0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_distorted_puzzle_volumes((15, 7), 25, (2, 15), 0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_distorted_puzzle_volumes((6, 3), 12, (4, 9), 2, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
