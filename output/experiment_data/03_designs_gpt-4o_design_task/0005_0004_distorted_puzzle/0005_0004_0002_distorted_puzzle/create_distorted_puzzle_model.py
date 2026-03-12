# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model embodying the "Distorted puzzle" metaphor through a systematic approach. It creates a series of interconnected, irregularly shaped units that reflect tension and dynamic alignment rather than seamless fitting. Each unit's dimensions and orientations are randomly varied, resulting in tilted planes and skewed edges that contribute to a visually complex massing. The spatial arrangement promotes non-linear flows, forming niches and alcoves that encourage exploration. By manipulating visual axes, the model maintains coherence while revealing unexpected relationships, thus capturing the essence of a distorted yet unified architectural puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_length, base_width, base_height, unit_count, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    This function generates a series of interconnected, irregularly shaped units that align through tension rather than seamless fit. 
    The massing consists of tilted planes and skewed edges, promoting a non-linear spatial flow and creating niches and alcoves.
    
    Inputs:
        base_length (float): The base length of the model in meters.
        base_width (float): The base width of the model in meters.
        base_height (float): The base height of the model in meters.
        unit_count (int): The number of interlocking units to generate.
        seed (int): Random seed for replicable results (default is 42).
    
    Outputs:
        List[Rhino.Geometry.Brep]: A list of 3D brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(seed)
    geometries = []

    # Define base plane
    base_plane = rg.Plane.WorldXY

    # Generate units
    for i in range(unit_count):
        # Randomly vary size and orientation
        length_variation = random.uniform(0.6, 1.4)
        width_variation = random.uniform(0.6, 1.4)
        height_variation = random.uniform(0.6, 1.4)

        # Create base box
        box = rg.Box(base_plane, rg.Interval(0, base_length * length_variation), 
                              rg.Interval(0, base_width * width_variation), 
                              rg.Interval(0, base_height * height_variation))

        # Randomly rotate and tilt the box
        angle_x = random.uniform(-15, 15)
        angle_y = random.uniform(-15, 15)
        angle_z = random.uniform(-15, 15)

        xform_rotate_x = rg.Transform.Rotation(math.radians(angle_x), base_plane.XAxis, base_plane.Origin)
        xform_rotate_y = rg.Transform.Rotation(math.radians(angle_y), base_plane.YAxis, base_plane.Origin)
        xform_rotate_z = rg.Transform.Rotation(math.radians(angle_z), base_plane.ZAxis, base_plane.Origin)

        box.Transform(xform_rotate_x)
        box.Transform(xform_rotate_y)
        box.Transform(xform_rotate_z)

        # Translate the box to create non-linear flow and spatial complexity
        translation_vector = rg.Vector3d(random.uniform(-base_length, base_length), 
                                         random.uniform(-base_width, base_width), 
                                         random.uniform(-base_height, base_height))
        xform_translate = rg.Transform.Translation(translation_vector)
        box.Transform(xform_translate)

        # Convert box to brep and add to geometries list
        geometries.append(box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(10.0, 5.0, 3.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(8.0, 4.0, 2.5, 20, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(12.0, 6.0, 4.0, 10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(15.0, 7.0, 5.0, 25, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(9.0, 4.5, 3.5, 18, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
