# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the "Distorted puzzle" metaphor by creating a series of irregularly shaped units. Each unit is formed through random transformations, including rotations and translations, which promote a sense of dynamic tension and non-linear spatial relationships. The function emphasizes tilted planes and skewed edges, resulting in an intricate assemblage that invites exploration through interlocking niches and alcoves. Key visual axes are maintained to ensure overall coherence, while unexpected alignments introduce moments of surprise, effectively capturing the essence of a complex yet unified architectural puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, unit_count, angle_variation, translation_variation, seed):
    \"""
    Create an architectural Concept Model inspired by the 'Distorted puzzle' metaphor.

    This function generates a series of interconnected, irregularly shaped units that align through dynamic tension.
    The design features tilted planes and skewed edges, promoting a non-linear spatial flow with niches and alcoves.
    The spatial arrangement maintains coherence through key visual axes while allowing for unexpected connections.

    Parameters:
    - base_size (float): The average size of each unit in meters.
    - unit_count (int): The number of units to generate.
    - angle_variation (float): Maximum variation in degrees for tilting and skewing angles.
    - translation_variation (float): Maximum translation in meters for positioning units.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the seed for replicability
    random.seed(seed)

    def create_irregular_unit(origin, size, angle_variation):
        # Create a base box
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(-size / 2, size / 2),
            rg.Interval(-size / 2, size / 2),
            rg.Interval(-size / 2, size / 2)
        )

        # Apply a random rotation to simulate tilting
        x_angle = math.radians(random.uniform(-angle_variation, angle_variation))
        y_angle = math.radians(random.uniform(-angle_variation, angle_variation))
        z_angle = math.radians(random.uniform(-angle_variation, angle_variation))

        transform = rg.Transform.Rotation(x_angle, rg.Vector3d.XAxis, box.Center)
        box.Transform(transform)
        transform = rg.Transform.Rotation(y_angle, rg.Vector3d.YAxis, box.Center)
        box.Transform(transform)
        transform = rg.Transform.Rotation(z_angle, rg.Vector3d.ZAxis, box.Center)
        box.Transform(transform)

        # Translate the box to a random position
        translation = rg.Vector3d(
            random.uniform(-translation_variation, translation_variation),
            random.uniform(-translation_variation, translation_variation),
            random.uniform(-translation_variation, translation_variation)
        )
        box.Transform(rg.Transform.Translation(translation))

        return box.ToBrep()

    # List to store the generated units
    units = []

    # Generate units with random orientation and position
    for _ in range(unit_count):
        # Randomly determine the origin of each unit within a defined space
        origin = rg.Point3d(
            random.uniform(-base_size * unit_count / 2, base_size * unit_count / 2),
            random.uniform(-base_size * unit_count / 2, base_size * unit_count / 2),
            random.uniform(0, base_size * unit_count / 4)
        )

        # Create an irregular unit
        unit = create_irregular_unit(origin, base_size, angle_variation)
        units.append(unit)

    return units"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(5.0, 10, 45.0, 2.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(3.0, 15, 30.0, 1.5, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(4.0, 12, 60.0, 3.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(6.0, 8, 50.0, 2.5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(7.0, 20, 35.0, 4.0, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
