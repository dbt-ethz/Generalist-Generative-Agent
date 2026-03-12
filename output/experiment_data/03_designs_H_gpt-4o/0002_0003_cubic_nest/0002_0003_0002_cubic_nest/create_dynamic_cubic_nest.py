# Created for 0002_0003_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of interwoven cubic forms. Each cube is randomly scaled, translated, and rotated, reflecting the metaphor's emphasis on interconnectedness and complexity. The function takes parameters like base size, number of cubes, spacing, and rotation angles to create varied spatial arrangements. This results in a multi-dimensional structure that balances enclosure and openness, encouraging exploration. By manipulating these parameters, the model embodies a protective yet engaging environment, allowing for unique spatial experiences within the nested configuration of cubic modules."""

#! python 3
function_code = """def create_dynamic_cubic_nest(base_size=10.0, num_cubes=10, layer_spacing=5.0, rotation_angle_max=15, seed=42):
    \"""
    Create a dynamic architectural Concept Model based on the 'Cubic nest' metaphor using interwoven cubic forms.
    
    Parameters:
    - base_size (float): The base size of the cubes in meters.
    - num_cubes (int): The number of cubic modules to generate.
    - layer_spacing (float): The spacing between each layer of cubes in meters.
    - rotation_angle_max (float): Maximum rotation angle in degrees for each cube.
    - seed (int): Seed for random number generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for i in range(num_cubes):
        # Calculate scaling factor to vary cube sizes
        scale_factor = 0.8 + 0.4 * (random.random())

        # Create the base cube
        cube = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, base_size * scale_factor),
            rg.Interval(0, base_size * scale_factor),
            rg.Interval(0, base_size * scale_factor)
        )

        # Calculate translation
        translation_vector = rg.Vector3d(
            random.uniform(-layer_spacing, layer_spacing),
            random.uniform(-layer_spacing, layer_spacing),
            i * layer_spacing
        )
        translation = rg.Transform.Translation(translation_vector)

        # Calculate rotation
        angle_rad = math.radians(random.uniform(-rotation_angle_max, rotation_angle_max))
        rotation_axis = rg.Vector3d(random.choice([1, 0, 0]), random.choice([0, 1, 0]), random.choice([0, 0, 1]))
        rotation = rg.Transform.Rotation(angle_rad, rotation_axis, cube.Center)

        # Apply transformations
        cube.Transform(translation)
        cube.Transform(rotation)

        # Convert to Brep and add to list
        geometries.append(cube.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cubic_nest(base_size=12.0, num_cubes=15, layer_spacing=6.0, rotation_angle_max=20, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cubic_nest(base_size=8.0, num_cubes=20, layer_spacing=4.0, rotation_angle_max=30, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cubic_nest(base_size=15.0, num_cubes=5, layer_spacing=3.0, rotation_angle_max=10, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cubic_nest(base_size=11.0, num_cubes=12, layer_spacing=7.0, rotation_angle_max=25, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cubic_nest(base_size=9.0, num_cubes=8, layer_spacing=5.0, rotation_angle_max=12, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
