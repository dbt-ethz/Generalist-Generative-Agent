# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a series of vertical columns and voids. It uses parameters such as column count, height, and radius to define the structure's dimensions and proportions. The function randomly determines whether each column will be solid or a void, simulating the layered effect of a vertical forest. This design promotes light and air circulation while enhancing interaction between interior and exterior spaces. The resulting geometries visually embody the metaphor, reflecting a dynamic interplay of solid and void that invites exploration and engagement with nature."""

#! python 3
function_code = """def create_perforated_vertical_landscape(column_count=10, height=30.0, radius_range=(0.5, 2.0), void_chance=0.3, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.
    
    This function generates a series of vertical columns interspersed with voids, creating a layered effect that resembles
    a vertical forest. The columns mimic tree trunks and the voids function as pathways for natural elements, promoting
    interaction between interior and exterior spaces.

    Parameters:
    - column_count (int): The number of columns to generate.
    - height (float): The height of the columns in meters.
    - radius_range (tuple): A tuple indicating the minimum and maximum radius of the columns.
    - void_chance (float): The probability (between 0 and 1) that a column will be a void.
    - seed (int): The seed for the random number generator, ensuring replicability.

    Returns:
    - List of RhinoCommon Brep objects representing the solid columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Initialize a list to store the resulting geometries
    geometries = []

    # Define a grid layout for the columns
    grid_spacing = 4.0  # meters
    base_plane = rg.Plane.WorldXY

    for i in range(column_count):
        # Determine the position of the column
        x = (i % 5) * grid_spacing
        y = (i // 5) * grid_spacing
        position = rg.Point3d(x, y, 0)

        # Determine if this column is a void or solid
        if random.random() < void_chance:
            # Create a void as a simple vertical surface
            radius = random.uniform(*radius_range)
            circle = rg.Circle(position, radius)
            extrude_curve = circle.ToNurbsCurve()
            extrusion = rg.Extrusion.Create(extrude_curve, height, True)
            geometries.append(extrusion.ToBrep())
        else:
            # Create a solid column
            radius = random.uniform(*radius_range)
            circle = rg.Circle(position, radius)
            column = rg.Cylinder(circle, height).ToBrep(True, True)
            geometries.append(column)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(column_count=15, height=25.0, radius_range=(1.0, 3.0), void_chance=0.4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(column_count=8, height=40.0, radius_range=(0.8, 2.5), void_chance=0.2, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(column_count=12, height=35.0, radius_range=(0.6, 2.2), void_chance=0.5, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(column_count=20, height=50.0, radius_range=(0.4, 1.5), void_chance=0.6, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(column_count=5, height=20.0, radius_range=(0.7, 1.8), void_chance=0.25, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
