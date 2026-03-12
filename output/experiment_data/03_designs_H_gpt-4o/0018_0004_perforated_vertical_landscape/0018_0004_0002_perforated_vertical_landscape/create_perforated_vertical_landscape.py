# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor by creating a grid of vertical cylindrical columns. Each column represents the solid elements of the design, while random omissions introduce voids, emphasizing the interplay of solid and void as described in the metaphor. The parameters, such as height, width, depth, and column radius, allow for customization of the models proportions. By varying the density of columns through the void probability, the function captures the essence of verticality and permeability, facilitating light and air flow, while creating a structure that embodies a natural, interconnected landscape."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, column_radius, void_probability, seed=42):
    \"""
    Creates an architectural Concept Model inspired by the 'Perforated vertical landscape' metaphor.
    
    This model features a series of vertical cylindrical columns arranged in a grid, 
    with some columns randomly omitted to create voids, enhancing the interplay of solid and void.

    Parameters:
    - height (float): The total height of the concept model in meters.
    - width (float): The total width of the concept model in meters.
    - depth (float): The total depth of the concept model in meters.
    - column_radius (float): The radius of the cylindrical columns in meters.
    - void_probability (float): The probability (0 to 1) of omitting a column to create a void.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)  # Ensure replicability

    breps = []

    # Define grid spacing based on column diameter
    spacing_x = column_radius * 3  # 3 times the radius for spacing
    spacing_z = column_radius * 3

    # Calculate the number of grid points
    num_x = int(width / spacing_x)
    num_z = int(depth / spacing_z)

    # Create grid of columns
    for i in range(num_x + 1):
        for j in range(num_z + 1):
            # Randomly decide whether to omit this column
            if random.random() > void_probability:
                # Calculate the position of the column's center
                x = i * spacing_x
                z = j * spacing_z

                # Create a vertical column
                base_point = rg.Point3d(x, 0, z)
                top_point = rg.Point3d(x, height, z)
                axis = rg.Line(base_point, top_point)

                # Create a cylindrical column
                circle_base = rg.Circle(rg.Plane(base_point, rg.Vector3d.ZAxis), column_radius)
                cylinder = rg.Cylinder(circle_base, height)
                brep = cylinder.ToBrep(True, True)
                breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 15.0, 5.0, 0.2, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(8.0, 20.0, 10.0, 0.15, 0.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 25.0, 7.0, 0.25, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(15.0, 30.0, 12.0, 0.1, 0.2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(5.0, 10.0, 3.0, 0.1, 0.6, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
