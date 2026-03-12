# Created for 0020_0002_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Stacked forests" metaphor by creating a series of interlocking cylindrical volumes that represent different layers of a forest. Each layer's geometries are defined by varying heights and radii, simulating the organic growth and complexity of a forest ecosystem. The function incorporates random positioning within a defined radius to mimic natural density and spatial relationships, while also introducing voids that represent clearings. This dynamic interaction fosters exploration and circulation paths, reflecting the layered nature of a forest and creating a visually rich, organic architectural model."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_radius=5.0, height_increment=3.0, num_layers=4, seed=42):
    \"""
    Generates a 3D architectural Concept Model based on the 'Stacked forests' metaphor.

    Parameters:
    - base_radius (float): The base radius of the first layer of volumes in meters.
    - height_increment (float): The vertical distance between successive layers in meters.
    - num_layers (int): The number of stacked layers representing different forest levels.
    - seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for i in range(num_layers):
        # Calculate the center height of the current layer
        center_height = i * height_increment

        # Define the number of volumes in the current layer
        num_volumes = random.randint(3, 6)

        for j in range(num_volumes):
            # Randomly position each volume within a circular area
            angle = random.uniform(0, 2 * 3.14159)
            distance = random.uniform(0, base_radius)
            x = distance * math.cos(angle)
            y = distance * math.sin(angle)

            # Randomize the radius and height of each volume
            volume_radius = random.uniform(base_radius * 0.5, base_radius)
            volume_height = random.uniform(height_increment * 0.5, height_increment)

            # Create a cylindrical volume
            base_circle = rg.Circle(rg.Point3d(x, y, center_height), volume_radius)
            cylinder = rg.Cylinder(base_circle, volume_height).ToBrep(True, True)

            geometries.append(cylinder)

        # Add some void spaces to represent clearings
        if random.random() > 0.5:
            clearing_radius = random.uniform(base_radius * 0.3, base_radius * 0.6)
            clearing_center = rg.Point3d(random.uniform(-base_radius, base_radius), 
                                         random.uniform(-base_radius, base_radius), 
                                         center_height + volume_height / 2)
            clearing_sphere = rg.Sphere(clearing_center, clearing_radius).ToBrep()
            geometries.append(clearing_sphere)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(base_radius=6.0, height_increment=4.0, num_layers=5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(base_radius=4.0, height_increment=2.0, num_layers=3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(base_radius=7.0, height_increment=5.0, num_layers=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(base_radius=8.0, height_increment=2.5, num_layers=7, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(base_radius=5.5, height_increment=3.5, num_layers=4, seed=11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
