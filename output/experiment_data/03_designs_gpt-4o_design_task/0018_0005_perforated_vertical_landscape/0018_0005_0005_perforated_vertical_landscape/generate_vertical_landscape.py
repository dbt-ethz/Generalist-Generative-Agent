# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor. It creates vertical columns with specified radii and heights, arranged in a grid pattern with random offsets for an organic appearance. This design mimics a vertical forest, where columns act as tree trunks and the spaces between them serve as voids or pathways. By allowing light and air to permeate through, the model promotes interaction between interior and exterior spaces. The result is a dynamic structure that embodies the metaphors essence, encouraging exploration and highlighting the interplay between solid and void."""

#! python 3
function_code = """def generate_vertical_landscape(column_radius=0.5, column_height=10, num_columns=10, grid_spacing=3, randomness_seed=42):
    \"""
    Generate a Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    This function creates a series of vertical columns interspersed with voids, representing the metaphor of a
    'Perforated vertical landscape'. The columns are organized in a grid pattern with random offsets to create
    a natural and organic form. The resulting structure encourages interaction between interior and exterior
    spaces, promoting vertical and horizontal movement.

    Parameters:
    - column_radius (float): The radius of each column in meters.
    - column_height (float): The height of each column in meters.
    - num_columns (int): The approximate number of columns to generate.
    - grid_spacing (float): The spacing between columns in the grid, in meters.
    - randomness_seed (int): Seed for random number generator to ensure replicable results.

    Returns:
    - List of Brep: A list of Brep objects representing the columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)
    
    # List to store generated geometries
    geometries = []
    
    # Determine grid size
    grid_size = int(num_columns ** 0.5)
    
    # Generate columns
    for i in range(grid_size):
        for j in range(grid_size):
            # Random offset for organic look
            x_offset = random.uniform(-0.5, 0.5) * grid_spacing
            y_offset = random.uniform(-0.5, 0.5) * grid_spacing
            
            # Calculate column center
            x = i * grid_spacing + x_offset
            y = j * grid_spacing + y_offset
            
            # Create column base point
            base_point = rg.Point3d(x, y, 0)
            
            # Create vertical axis for column
            axis = rg.Line(base_point, rg.Point3d(x, y, column_height))
            
            # Create column as a cylinder
            circle = rg.Circle(rg.Plane(base_point, rg.Vector3d.ZAxis), column_radius)
            column = rg.Cylinder(circle, column_height).ToBrep(True, True)
            
            # Add column to geometries list
            geometries.append(column)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_vertical_landscape(column_radius=0.6, column_height=12, num_columns=16, grid_spacing=4, randomness_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_vertical_landscape(column_radius=0.4, column_height=8, num_columns=25, grid_spacing=2.5, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_vertical_landscape(column_radius=0.3, column_height=15, num_columns=20, grid_spacing=5, randomness_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_vertical_landscape(column_radius=0.7, column_height=9, num_columns=12, grid_spacing=3.5, randomness_seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_vertical_landscape(column_radius=0.5, column_height=5, num_columns=30, grid_spacing=2, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
