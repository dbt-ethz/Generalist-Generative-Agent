# Created for 0002_0002_cubic_nest.json

""" Summary:
The function `generate_cubic_nest_model` creates an architectural concept model based on the "Cubic nest" metaphor by generating a series of interlocking cubic volumes. Each cube's position, orientation, and scale are randomized to reflect the complexity and layering described in the design task. The overlapping cubes symbolize interconnectedness and protective qualities, while variations in size represent material transitions from solid to void, enhancing perceptions of shelter. By manipulating these elements, the function fosters dynamic spatial relationships and unexpected pathways, inviting exploration and interaction, thus embodying the essence of the 'Cubic nest' concept in its architectural form."""

#! python 3
function_code = """def generate_cubic_nest_model(base_size, cube_count, overlap_factor, material_variation):
    \"""
    Generates an architectural Concept Model based on the 'Cubic nest' metaphor by creating a system of nested and interlocking cubic volumes.
    
    Parameters:
    - base_size (float): The base size of cubes in meters.
    - cube_count (int): The number of cubes to generate.
    - overlap_factor (float): A factor determining the degree of overlap between cubes.
    - material_variation (float): A factor to vary materiality from solid to void.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import the math module

    random.seed(42)  # Ensures replicable randomness

    breps = []

    # Define the initial base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size / 2, base_size / 2),
                       rg.Interval(-base_size / 2, base_size / 2),
                       rg.Interval(-base_size / 2, base_size / 2)).ToBrep()

    # Generate cubes with random transformations and overlaps
    for i in range(cube_count):
        # Randomly determine the position and orientation of the cube
        translation_vector = rg.Vector3d(
            random.uniform(-overlap_factor, overlap_factor) * base_size,
            random.uniform(-overlap_factor, overlap_factor) * base_size,
            random.uniform(-overlap_factor, overlap_factor) * base_size
        )

        rotation_axis = rg.Vector3d(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        rotation_axis.Unitize()

        rotation_angle = random.uniform(0, 2 * math.pi / 8)  # Use math.pi

        # Create a transformation combining translation and rotation
        transform = rg.Transform.Translation(translation_vector) * rg.Transform.Rotation(rotation_angle, rotation_axis, rg.Point3d.Origin)

        # Apply transformation to base cube
        transformed_cube = base_cube.DuplicateBrep()
        transformed_cube.Transform(transform)

        # Vary materiality using scale transformation
        if random.random() < material_variation:
            scale_factor = random.uniform(0.5, 1.0)  # Smaller scale for void-like cubes
        else:
            scale_factor = random.uniform(1.0, 1.5)  # Larger scale for solid-like cubes

        scale_transform = rg.Transform.Scale(rg.Point3d.Origin, scale_factor)
        transformed_cube.Transform(scale_transform)

        # Add the transformed cube to the list of breps
        breps.append(transformed_cube)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_model(2.0, 10, 0.5, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_model(1.5, 5, 0.3, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_model(3.0, 20, 0.4, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_model(2.5, 15, 0.6, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_model(1.0, 8, 0.2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
