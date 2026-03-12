# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_architecture` generates an architectural concept model based on the "Distorted puzzle" metaphor. It creates a series of fragmented, interlocking volumes with varying heights and asymmetric forms, reflecting the metaphor's theme of dynamic interplay. By using random dimensions and positions, the function produces distinct yet interconnected shapes, emphasizing light and shadow. Each volume is extruded and slightly rotated to enhance visual complexity, contributing to a cohesive whole that evokes tension and equilibrium. The resulting model allows for varied spatial experiences, aligning with the metaphor's essence of unpredictability and interconnectedness in design."""

#! python 3
function_code = """def create_distorted_puzzle_architecture(base_area, height_range, num_elements, random_seed):
    \"""
    Creates an architectural Concept Model based on the 'Distorted Puzzle' metaphor.

    This function generates a network of fragmented, interlocking volumes with asymmetric forms and varying heights.
    The design emphasizes a dynamic interplay of light and shadow, with volumes that are distinct yet part of a cohesive whole.

    Parameters:
    - base_area (tuple): A tuple (base_length, base_width) defining the base dimensions of the site in meters.
    - height_range (tuple): A tuple (min_height, max_height) defining the range of heights for the volumes.
    - num_elements (int): The number of fragmented volumes to generate.
    - random_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)
    volumes = []

    base_length, base_width = base_area
    min_height, max_height = height_range

    for _ in range(num_elements):
        # Random dimensions and position
        width = random.uniform(0.1 * base_length, 0.25 * base_length)
        length = random.uniform(0.1 * base_width, 0.25 * base_width)
        height = random.uniform(min_height, max_height)
        x_pos = random.uniform(0, base_length - width)
        y_pos = random.uniform(0, base_width - length)

        # Create base shape
        base_profile = rg.Polyline([
            rg.Point3d(0, 0, 0),
            rg.Point3d(width, 0, 0),
            rg.Point3d(width, length, 0),
            rg.Point3d(0, length, 0),
            rg.Point3d(0, 0, 0)
        ])
        base_curve = base_profile.ToNurbsCurve()

        # Create extrusion
        path_curve = rg.LineCurve(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height))
        sweep = rg.SweepOneRail()
        volume = sweep.PerformSweep(base_curve, path_curve)[0]

        # Apply transformations
        translation = rg.Transform.Translation(x_pos, y_pos, 0)
        volume.Transform(translation)
        rotation_axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        rotation_axis.Unitize()
        rotation_angle = random.uniform(-0.1, 0.1)  # Small rotation in radians
        rotation = rg.Transform.Rotation(rotation_angle, rotation_axis, volume.GetBoundingBox(True).Center)
        volume.Transform(rotation)

        volumes.append(volume)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_architecture((20, 15), (5, 10), 10, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_architecture((30, 20), (3, 8), 15, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_architecture((25, 18), (4, 12), 12, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_architecture((40, 25), (6, 15), 20, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_architecture((35, 22), (2, 5), 8, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
