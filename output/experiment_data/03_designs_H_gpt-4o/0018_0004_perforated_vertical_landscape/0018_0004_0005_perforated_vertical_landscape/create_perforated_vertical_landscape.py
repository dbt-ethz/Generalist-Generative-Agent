# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model based on the "Perforated Vertical Landscape" metaphor by creating a vertical grid structure composed of columns and voids. By defining parameters such as height, width, and spacing, the function uses randomization to determine where to place columns or voids, ensuring a dynamic interplay between solid and void. This design enhances light and air flow, achieving the metaphor's essence of openness and connectivity. The varying densities and arrangements of columns mimic a natural lattice, promoting interaction between interior and exterior spaces, ultimately reflecting the metaphor's vision of a vertical landscape."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, column_radius, grid_spacing, void_probability, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Perforated Vertical Landscape' metaphor.
    
    This function generates a vertical columnar grid structure with varying densities,
    allowing for an interplay of solid and void to promote light and air flow through the model.

    Parameters:
    - height (float): Total height of the model in meters.
    - width (float): Total width of the model in meters.
    - depth (float): Total depth of the model in meters.
    - column_radius (float): Radius of the columns in the grid.
    - grid_spacing (float): The spacing between columns in meters.
    - void_probability (float): Probability of creating a void at each grid point.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    breps = []

    # Calculate the number of columns in each direction
    num_x = int(width / grid_spacing)
    num_y = int(depth / grid_spacing)
    num_z = int(height / grid_spacing)

    # Iterate over the grid positions
    for i in range(num_x):
        for j in range(num_y):
            for k in range(num_z):
                # Determine if this position should have a column or be a void
                if random.random() > void_probability:
                    # Calculate the center of the column
                    x = i * grid_spacing
                    y = j * grid_spacing
                    z = k * grid_spacing

                    # Create a vertical cylinder (column)
                    base_point = rg.Point3d(x, y, z)
                    axis = rg.Line(base_point, rg.Point3d(x, y, z + grid_spacing)).ToNurbsCurve()
                    circle = rg.Circle(rg.Plane(base_point, rg.Vector3d.ZAxis), column_radius)
                    column = rg.Cylinder(circle, grid_spacing).ToBrep(True, True)
                    
                    breps.append(column)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=10.0, width=5.0, depth=5.0, column_radius=0.1, grid_spacing=1.0, void_probability=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=15.0, width=10.0, depth=8.0, column_radius=0.2, grid_spacing=0.5, void_probability=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=12.0, width=6.0, depth=4.0, column_radius=0.15, grid_spacing=0.75, void_probability=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=20.0, width=8.0, depth=10.0, column_radius=0.25, grid_spacing=1.5, void_probability=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=18.0, width=7.0, depth=6.0, column_radius=0.3, grid_spacing=1.2, void_probability=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
