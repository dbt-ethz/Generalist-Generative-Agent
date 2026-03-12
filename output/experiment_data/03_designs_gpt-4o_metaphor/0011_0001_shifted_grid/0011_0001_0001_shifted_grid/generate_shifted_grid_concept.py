# Created for 0011_0001_shifted_grid.json

""" Summary:
The function `generate_shifted_grid_concept` creates an architectural concept model inspired by the "Shifted Grid" metaphor. By defining a grid with adjustable cell sizes and shift amounts, it dynamically reconfigures traditional layouts to introduce movement and fluidity. Each cell's position is altered based on the shift amount, generating innovative spatial arrangements that encourage varied circulation paths and diverse experiences. The resulting geometries, represented as box Breps, embody adaptability, allowing for playful interactions with light and shadow, ultimately fostering a sense of discovery for occupants navigating through the space."""

#! python 3
function_code = """def generate_shifted_grid_concept(grid_size, shift_amount, height, cell_size):
    \"""
    Generates a Concept Model based on the 'Shifted Grid' metaphor, creating a dynamic reconfiguration 
    of a regular pattern to introduce movement and fluidity within the architectural structure.

    Args:
        grid_size (int): The number of cells along one dimension of the grid.
        shift_amount (float): The amount by which each row in the grid is shifted along the x-axis.
        height (float): The height of the blocks created in the grid.
        cell_size (float): The size of each cell in the grid.

    Returns:
        list: A list of Brep geometry objects representing the generated Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Initialize random seed for replicability
    random.seed(42)

    geometries = []

    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the base point of each cell
            base_x = i * cell_size + (j % 2) * shift_amount  # Shift every second row
            base_y = j * cell_size
            base_point = rg.Point3d(base_x, base_y, 0)

            # Create a box brep for each cell
            box_corners = [
                rg.Point3d(base_x, base_y, 0),
                rg.Point3d(base_x + cell_size, base_y, 0),
                rg.Point3d(base_x + cell_size, base_y + cell_size, 0),
                rg.Point3d(base_x, base_y + cell_size, 0),
                rg.Point3d(base_x, base_y, height),
                rg.Point3d(base_x + cell_size, base_y, height),
                rg.Point3d(base_x + cell_size, base_y + cell_size, height),
                rg.Point3d(base_x, base_y + cell_size, height)
            ]
            box = rg.Brep.CreateFromBox(box_corners)
            geometries.append(box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_shifted_grid_concept(5, 2.0, 3.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_shifted_grid_concept(4, 1.5, 2.5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_shifted_grid_concept(6, 3.0, 4.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_shifted_grid_concept(3, 1.0, 2.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_shifted_grid_concept(7, 2.5, 5.0, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
