# Created for 0011_0002_shifted_grid.json

""" Summary:
The `create_shifted_grid_architectural_model` function generates an architectural concept model inspired by the "Shifted Grid" metaphor. It begins with a regular grid, applying random shifts to create staggered and misaligned volumes. This produces interconnected spaces that deviate from traditional layouts, enhancing movement and fluidity. The function incorporates height variations to add complexity and visual interest, fostering diverse spatial experiences. By manipulating light and shadow through varied orientations and projections, the model encourages exploration and adaptability, capturing the essence of the metaphor while allowing for innovative design solutions that invite occupant interaction."""

#! python 3
function_code = """def create_shifted_grid_architectural_model(grid_size=5, cell_size=3.0, shift_factor=0.5, height_range=(2.0, 5.0), levels=3, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor.

    This function starts with a regular grid and introduces shifts to create misaligned and staggered volumes.
    The grid is manipulated to produce interconnected spaces with varied orientations, fostering exploration and
    dynamic interactions with light and shadow.

    Parameters:
    - grid_size (int): The number of grid cells along one axis of the grid.
    - cell_size (float): The size of each grid cell in meters.
    - shift_factor (float): The maximum percentage of the cell size by which grid lines can be shifted.
    - height_range (tuple): The minimum and maximum height variation of the volumes in meters.
    - levels (int): The number of vertical layers.
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed random number generator for replicability
    random.seed(seed)

    geometries = []

    for level in range(levels):
        z_base = level * (height_range[1] + 1)  # Adding a buffer to separate layers

        for i in range(grid_size):
            for j in range(grid_size):
                # Calculate base position with shifts
                x_shift = random.uniform(-shift_factor * cell_size, shift_factor * cell_size)
                y_shift = random.uniform(-shift_factor * cell_size, shift_factor * cell_size)
                x_base = i * cell_size + x_shift
                y_base = j * cell_size + y_shift

                # Random height for each volume
                height = random.uniform(height_range[0], height_range[1])

                # Create box corners
                pt1 = rg.Point3d(x_base, y_base, z_base)
                pt2 = rg.Point3d(x_base + cell_size, y_base, z_base)
                pt3 = rg.Point3d(x_base + cell_size, y_base + cell_size, z_base)
                pt4 = rg.Point3d(x_base, y_base + cell_size, z_base)
                pt5 = rg.Point3d(x_base, y_base, z_base + height)
                pt6 = rg.Point3d(x_base + cell_size, y_base, z_base + height)
                pt7 = rg.Point3d(x_base + cell_size, y_base + cell_size, z_base + height)
                pt8 = rg.Point3d(x_base, y_base + cell_size, z_base + height)
                
                # Create a Brep from the box corners
                box_corners = [pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8]
                brep = rg.Brep.CreateFromBox(box_corners)
                if brep:
                    geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_architectural_model(grid_size=7, cell_size=2.5, shift_factor=0.3, height_range=(3.0, 6.0), levels=4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_architectural_model(grid_size=6, cell_size=4.0, shift_factor=0.2, height_range=(1.5, 4.5), levels=2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_architectural_model(grid_size=8, cell_size=3.5, shift_factor=0.4, height_range=(2.5, 7.0), levels=5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_architectural_model(grid_size=5, cell_size=3.0, shift_factor=0.5, height_range=(2.0, 5.0), levels=3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_architectural_model(grid_size=10, cell_size=2.0, shift_factor=0.1, height_range=(1.0, 3.0), levels=6, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
