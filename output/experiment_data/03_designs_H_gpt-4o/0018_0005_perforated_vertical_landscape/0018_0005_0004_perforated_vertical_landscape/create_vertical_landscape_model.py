# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The function `create_vertical_landscape_model` generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor. It creates a grid of vertical columns that resemble tree trunks, interspersed with voids to allow light and air to penetrate, fostering a connection between indoor and outdoor environments. Each column's height varies, simulating a natural forest's organic rhythm. The function utilizes parameters such as column count, maximum height, and void percentage to customize the design, ensuring dynamic spatial interactions. This model embodies the metaphor through its verticality and playful integration of solid and void elements, inviting exploration."""

#! python 3
function_code = """def create_vertical_landscape_model(column_count=15, max_height=20.0, base_radius=0.8, void_percentage=0.4, seed=123):
    \"""
    Generates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.

    This function creates a series of vertical columns interspersed with voids in varying heights, 
    evoking the image of a vertical forest. The columns, resembling tree trunks, are arranged in layers 
    with intermittent voids that serve as pathways for light and air, promoting both vertical and horizontal 
    interaction within the structure.

    Parameters:
    - column_count (int): Total number of columns to create.
    - max_height (float): Maximum height for the tallest column in meters.
    - base_radius (float): Base radius of each column in meters.
    - void_percentage (float): Percentage of total height that is void.
    - seed (int): Seed for the random number generator for replicable randomness.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # List to store the generated geometries
    geometries = []

    # Grid size and spacing for positioning columns
    grid_size = int(column_count ** 0.5)
    spacing = 3.0  # meters

    for i in range(grid_size):
        for j in range(grid_size):
            # Determine position with a bit of randomness for a natural appearance
            x = i * spacing + random.uniform(-0.5, 0.5)
            y = j * spacing + random.uniform(-0.5, 0.5)

            # Determine the height of the column
            height = random.uniform(max_height * 0.5, max_height)

            # Create the solid part of the column
            column_base = rg.Point3d(x, y, 0)
            column_circle = rg.Circle(rg.Plane(column_base, rg.Vector3d.ZAxis), base_radius)
            column_cylinder = rg.Cylinder(column_circle, height * (1 - void_percentage)).ToBrep(True, True)
            geometries.append(column_cylinder)

            # Create the void part of the column (above the solid part)
            void_base = rg.Point3d(x, y, height * (1 - void_percentage))
            void_circle = rg.Circle(rg.Plane(void_base, rg.Vector3d.ZAxis), base_radius * 0.8)
            void_cylinder = rg.Cylinder(void_circle, height * void_percentage).ToBrep(True, True)
            geometries.append(void_cylinder)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_vertical_landscape_model(column_count=20, max_height=25.0, base_radius=0.5, void_percentage=0.3, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_vertical_landscape_model(column_count=10, max_height=15.0, base_radius=1.0, void_percentage=0.2, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_vertical_landscape_model(column_count=30, max_height=18.0, base_radius=0.6, void_percentage=0.5, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_vertical_landscape_model(column_count=25, max_height=22.0, base_radius=0.7, void_percentage=0.4, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_vertical_landscape_model(column_count=18, max_height=30.0, base_radius=0.9, void_percentage=0.25, seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
