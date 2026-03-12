# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model that embodies the metaphor of a "Perforated vertical landscape." It creates a series of vertical columns with varying radii, simulating tree trunks, interspersed with voids that allow light and air to flow through, enhancing the relationship between interior and exterior spaces. By utilizing random positioning and radius variations within a defined area, the model captures the essence of a vertical forest, promoting dynamic spatial experiences and encouraging movement. This design reflects the metaphor's emphasis on verticality and permeability, inviting exploration of natural elements within the structure."""

#! python 3
function_code = """def create_perforated_vertical_landscape(column_height=15.0, min_radius=0.5, max_radius=1.5, density=0.5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.

    This model features a series of vertical columns with varying radii interspersed with voids, 
    resembling a vertical forest. The columns mimic tree trunks and the voids serve as pathways for 
    light and air, enhancing interaction between internal and external environments.

    Parameters:
    - column_height (float): The height of each column in meters.
    - min_radius (float): The minimum radius of the columns in meters.
    - max_radius (float): The maximum radius of the columns in meters.
    - density (float): The density of columns within the defined space (0 to 1).
    - seed (int): The seed for the random number generator.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the columns.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicable randomness
    random.seed(seed)

    # List to store the generated 3D geometries
    geometries = []

    # Define the bounding area for the columns
    bounding_rect = rg.Rectangle3d(rg.Plane.WorldXY, 20, 20)
    bounding_area = bounding_rect.Area

    # Calculate number of columns based on density
    num_columns = int(density * bounding_area)

    # Create columns with varying radii within the bounding area
    for _ in range(num_columns):
        # Random position within the bounding area
        x = random.uniform(bounding_rect.Corner(0).X, bounding_rect.Corner(2).X)
        y = random.uniform(bounding_rect.Corner(0).Y, bounding_rect.Corner(2).Y)
        
        # Random radius within the specified range
        radius = random.uniform(min_radius, max_radius)

        # Create a vertical column
        column_center = rg.Point3d(x, y, 0)
        column_circle = rg.Circle(column_center, radius)
        column = rg.Cylinder(column_circle, column_height).ToBrep(True, True)

        # Add the column to the geometries list
        geometries.append(column)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(column_height=20.0, min_radius=0.3, max_radius=2.0, density=0.6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(column_height=18.0, min_radius=0.5, max_radius=1.0, density=0.4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(column_height=25.0, min_radius=0.2, max_radius=1.2, density=0.7, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(column_height=22.0, min_radius=0.6, max_radius=1.8, density=0.3, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(column_height=17.0, min_radius=0.4, max_radius=1.4, density=0.8, seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
