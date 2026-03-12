# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating vertical columns that simulate tree trunks and voids that represent natural pathways. It takes parameters such as the number of columns, their height, radius, and the gaps between them, enabling a varied arrangement that resembles a vertical forest. Using random positioning, the model achieves a natural feel, allowing light and air to penetrate through the voids, fostering interaction between interior and exterior spaces. This design embodies a rhythmic interplay of solid and void, inviting exploration of the architectural landscape."""

#! python 3
function_code = """def create_concept_model(column_count=10, height=30, radius=1.5, void_gap=2.0):
    \"""
    Creates an architectural Concept Model that embodies the 'Perforated vertical landscape' metaphor.
    
    The model consists of vertical columns interspersed with voids, resembling a vertical forest. 
    The columns represent tree trunks, while the voids function as pathways for light and air, promoting 
    interaction with the environment.

    Parameters:
    - column_count (int): The number of vertical columns to create.
    - height (float): The height of each column.
    - radius (float): The radius of each column.
    - void_gap (float): The gap between columns, representing voids.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the columns and voids.
    \"""
    import Rhino
    import random
    random.seed(42)
    from Rhino.Geometry import Point3d, Vector3d, Circle, Cylinder, Brep

    base_point = Point3d(0, 0, 0)
    geometries = []

    for i in range(column_count):
        # Calculate position with randomness for a natural feel
        angle = random.uniform(0, 360)
        x_offset = (radius + void_gap) * i * random.uniform(0.9, 1.1)
        y_offset = (radius + void_gap) * i * random.uniform(0.9, 1.1)

        # Create the base circle of the column
        column_base = Circle(Point3d(x_offset, y_offset, 0), radius)

        # Create the column as a cylinder
        column = Cylinder(column_base, height).ToBrep(True, True)

        # Add the column to the list of geometries
        geometries.append(column)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(column_count=15, height=25, radius=2.0, void_gap=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(column_count=20, height=40, radius=1.0, void_gap=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(column_count=12, height=35, radius=1.2, void_gap=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(column_count=8, height=20, radius=1.8, void_gap=2.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(column_count=18, height=28, radius=1.0, void_gap=2.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
