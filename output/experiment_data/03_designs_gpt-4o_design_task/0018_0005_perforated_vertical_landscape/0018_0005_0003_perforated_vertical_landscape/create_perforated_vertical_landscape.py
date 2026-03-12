# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a series of vertical columns and voids. Each column symbolizes tree trunks, while the voids represent natural pathways, embodying a vertical forest aesthetic. Parameters such as the number of columns, height, and spacing are adjustable, allowing for variation in design. The use of geometries like cylinders for columns and voids facilitates a layered effect, promoting light and air flow. This interplay between solid and void enhances spatial interaction, reflecting the metaphors essence of integrating nature with architectural form."""

#! python 3
function_code = """def create_perforated_vertical_landscape(num_columns, height, column_radius, void_radius, spacing, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    The model consists of vertical columns interspersed with voids to create a layered effect, 
    allowing light and air to pass through while offering privacy. The structure resembles a 
    vertical forest with columns as tree trunks and voids as natural pathways.

    Parameters:
    - num_columns: int, the number of columns to create.
    - height: float, the height of each column in meters.
    - column_radius: float, the radius of each column in meters.
    - void_radius: float, the radius of the voids in meters.
    - spacing: float, the distance between the centers of adjacent columns in meters.
    - seed: int, the seed for randomness to ensure replicability.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    geometries = []

    for i in range(num_columns):
        # Calculate position for the column
        angle = (2 * 3.14159 / num_columns) * i
        x = spacing * i
        y = spacing * random.uniform(-0.5, 0.5)

        # Create the column (solid)
        column_center = rg.Point3d(x, y, 0)
        column = rg.Cylinder(rg.Circle(column_center, column_radius), height).ToBrep(True, True)
        geometries.append(column)

        # Create the void (subtractive geometry)
        void_center = rg.Point3d(x, y, height / 2)
        void = rg.Cylinder(rg.Circle(void_center, void_radius), height).ToBrep(True, True)
        geometries.append(void)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(num_columns=10, height=5.0, column_radius=0.2, void_radius=0.1, spacing=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(num_columns=15, height=8.0, column_radius=0.3, void_radius=0.15, spacing=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(num_columns=20, height=6.0, column_radius=0.25, void_radius=0.12, spacing=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(num_columns=12, height=7.0, column_radius=0.15, void_radius=0.05, spacing=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(num_columns=8, height=10.0, column_radius=0.4, void_radius=0.2, spacing=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
