# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The provided function generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of interconnected, irregularly shaped units. These units are designed with varying heights, tilts, and offsets, which mimic the tension and dynamic alignment suggested by the metaphor. The function uses randomization to produce unique spatial arrangements that promote non-linear flow, allowing for unexpected niches and alcoves. Key visual axes are maintained to ensure structural coherence, while the overall assembly reflects a complex interplay of forms that evoke movement and surprise, embodying the essence of a distorted yet coherent architectural puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_assemblage(base_length, height_range, unit_count, tilt_range, offset_range, seed=0):
    \"""
    Create an architectural Concept Model inspired by the 'Distorted puzzle' metaphor.

    This function generates a series of interconnected units with irregular shapes that fit together
    through perceived tension and dynamic alignment. The design emphasizes non-linear spatial flow,
    with tilted planes and skewed edges forming niches and alcoves, while maintaining coherence through
    alignment of key visual axes.

    Parameters:
    - base_length (float): The base length of each unit in meters.
    - height_range (tuple): A tuple of two floats representing the minimum and maximum heights of the units.
    - unit_count (int): The number of units to generate.
    - tilt_range (tuple): A tuple of two floats representing the minimum and maximum tilt angles (in degrees).
    - offset_range (tuple): A tuple of two floats representing the minimum and maximum offsets between units.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the seed for randomness
    random.seed(seed)

    def create_irregular_unit(base, height, tilt, offset):
        # Create a base box
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base), rg.Interval(0, base), rg.Interval(0, height))
        
        # Apply tilt
        tilt_rad = math.radians(tilt)
        xform_tilt = rg.Transform.Rotation(tilt_rad, rg.Vector3d(1, 0, 0), box.Center)
        box.Transform(xform_tilt)

        # Apply offset
        translation = rg.Vector3d(random.uniform(*offset_range), random.uniform(*offset_range), 0)
        xform_translate = rg.Transform.Translation(translation)
        box.Transform(xform_translate)

        return box.ToBrep()

    geometries = []
    for _ in range(unit_count):
        height = random.uniform(*height_range)
        tilt = random.uniform(*tilt_range)
        offset = random.uniform(*offset_range)
        unit = create_irregular_unit(base_length, height, tilt, offset)
        geometries.append(unit)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_assemblage(5.0, (3.0, 10.0), 10, (-15, 15), (-2, 2), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_assemblage(4.0, (2.0, 8.0), 8, (-10, 10), (-1, 1), seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_assemblage(6.0, (4.0, 12.0), 12, (-20, 20), (-3, 3), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_assemblage(3.5, (2.5, 9.5), 15, (-25, 25), (-4, 4), seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_assemblage(7.0, (5.0, 15.0), 5, (-30, 30), (-5, 5), seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
