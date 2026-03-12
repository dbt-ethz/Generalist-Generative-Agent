# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor. It constructs a 3D grid structure, varying the density of solid and void elements based on the specified `void_ratio`. The resulting model features cuboid forms that mimic a lattice, emphasizing verticality and permeability. By adjusting parameters like height, width, depth, and grid size, the function creates diverse spatial configurations that promote light and air flow, fostering interaction between interior and exterior spaces. This design embodies the metaphor's essence, integrating natural elements into a cohesive architectural framework."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=10, grid_size=2, void_ratio=0.5):
    \"""
    Creates an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.
    
    Parameters:
    height (float): The vertical height of the model in meters.
    width (float): The horizontal width of the model in meters.
    depth (float): The depth of the model in meters.
    grid_size (float): The size of the grid cells in meters.
    void_ratio (float): The ratio of voids to solids in the grid structure, between 0 and 1.
    
    Returns:
    List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino
    import random

    # Set a random seed for replicability
    random.seed(42)

    # Create a list to hold the resulting geometries
    geometries = []

    # Calculate the number of elements in each dimension
    num_x = int(width / grid_size)
    num_y = int(depth / grid_size)
    num_z = int(height / grid_size)

    # Create a grid of breps (basic cuboids) with perforated elements
    for i in range(num_x):
        for j in range(num_y):
            for k in range(num_z):
                # Randomly decide if a cell is a void or solid based on void_ratio
                if random.random() > void_ratio:
                    # Create a box at the current grid position
                    base_point = Rhino.Geometry.Point3d(i * grid_size, j * grid_size, k * grid_size)
                    box = Rhino.Geometry.Box(
                        Rhino.Geometry.BoundingBox(
                            base_point,
                            Rhino.Geometry.Point3d((i + 1) * grid_size, (j + 1) * grid_size, (k + 1) * grid_size)
                        )
                    )
                    brep = box.ToBrep()
                    geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=20, depth=15, grid_size=3, void_ratio=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, width=15, depth=5, grid_size=1, void_ratio=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=25, depth=20, grid_size=5, void_ratio=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=50, width=30, depth=10, grid_size=4, void_ratio=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, width=18, depth=12, grid_size=2.5, void_ratio=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
