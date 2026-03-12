# Created for 0002_0003_cubic_nest.json

""" Summary:
The provided function, `create_dynamic_cubic_nest`, generates an architectural concept model inspired by the 'Cubic nest' metaphor. It constructs a series of interwoven cubic forms, each representing a unique module while contributing to a cohesive structure. By manipulating the size, rotation, and translation of each cube across multiple levels, the function creates dynamic spatial relationships that embody both enclosure and openness. This approach fosters exploration and interaction, allowing users to experience varied spatial encounters. The result is a nested configuration that emphasizes interconnectedness and individuality, aligning with the metaphor's essence of complexity and shelter."""

#! python 3
function_code = """def create_dynamic_cubic_nest(base_size, levels, layer_rotation, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Cubic nest' metaphor using interwoven cubic forms.
    
    The model creates nested cubic structures with varying rotations at different levels to enhance the interplay
    between enclosure and openness, fostering a dynamic and interconnected environment.

    Parameters:
        base_size (float): The base size of each cube in meters.
        levels (int): The number of levels of cubes to generate.
        layer_rotation (float): The maximum rotation in radians to apply to each layer.
        seed (int, optional): Seed for random number generator to ensure replicability. Default is 42.

    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D geometry of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for reproducibility
    random.seed(seed)

    # List to store the resulting geometry
    cubic_nest = []

    # Create initial cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size))
    cubic_nest.append(base_cube.ToBrep())

    # Create additional cubes in layers
    for level in range(1, levels):
        # Scale factor to gradually reduce cube size
        scale_factor = 1 - (level * 0.1)
        scaled_size = base_size * scale_factor

        # Rotation angle for this layer
        rotation_angle = random.uniform(-layer_rotation, layer_rotation)

        # Create a plane for rotation
        rotation_plane = rg.Plane.WorldXY
        rotation_center = rg.Point3d(base_size / 2, base_size / 2, base_size / 2)

        # Create a new cube with rotation
        new_cube = rg.Box(rotation_plane, rg.Interval(0, scaled_size), rg.Interval(0, scaled_size), rg.Interval(0, scaled_size))
        
        # Apply rotation transformation
        rotation = rg.Transform.Rotation(rotation_angle, rotation_plane.ZAxis, rotation_center)
        new_cube.Transform(rotation)

        # Translate the cube to create a nested effect
        translation_vector = rg.Vector3d(level * 0.5, level * 0.5, level * 0.5)
        translation = rg.Transform.Translation(translation_vector)
        new_cube.Transform(translation)

        # Add the new cube to the list
        cubic_nest.append(new_cube.ToBrep())

    return cubic_nest"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cubic_nest(base_size=5.0, levels=4, layer_rotation=1.57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cubic_nest(base_size=3.0, levels=5, layer_rotation=0.785)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cubic_nest(base_size=4.0, levels=3, layer_rotation=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cubic_nest(base_size=2.5, levels=6, layer_rotation=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cubic_nest(base_size=6.0, levels=5, layer_rotation=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
