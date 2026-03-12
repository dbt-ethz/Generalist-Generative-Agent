# Created for 0002_0004_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Cubic nest" metaphor by creating a 3D matrix of cubic volumes. Each cube's size and position are slightly randomized to enhance the layered, interconnected quality of the design, reflecting a sense of shelter and complexity. The function iterates through specified rows, columns, and layers, ensuring that the cubes vary in size and orientation, which aligns with the metaphor's emphasis on individuality and collective harmony. The interplay of solid and void within this arrangement fosters dynamic spatial experiences, inviting exploration and interaction throughout the architectural composition."""

#! python 3
function_code = """def create_cubic_nest_matrix(base_size=3.0, rows=3, columns=3, layers=3, randomness_seed=42):
    \"""
    Generates a 3D architectural Concept Model based on the 'Cubic nest' metaphor using a grid of cubic volumes.
    
    Args:
        base_size (float): The base size of each cube in meters.
        rows (int): Number of rows in the matrix of cubes.
        columns (int): Number of columns in the matrix of cubes.
        layers (int): Number of vertical layers in the matrix of cubes.
        randomness_seed (int): Seed for random number generator to ensure replicability.
        
    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness to ensure replicability
    random.seed(randomness_seed)

    # List to store the generated Brep (Boundary Representation) geometries
    cubic_nest = []

    # Iterate over the grid to create the matrix of cubes
    for i in range(rows):
        for j in range(columns):
            for k in range(layers):
                # Randomize cube size slightly to add variation
                variation_factor = random.uniform(0.8, 1.2)
                cube_size = base_size * variation_factor

                # Calculate cube center based on grid position and add random offset
                x_offset = random.uniform(-0.5, 0.5) * base_size
                y_offset = random.uniform(-0.5, 0.5) * base_size
                z_offset = random.uniform(-0.5, 0.5) * base_size
                center = rg.Point3d(i * base_size + x_offset, j * base_size + y_offset, k * base_size + z_offset)

                # Create a cube as a box
                box = rg.Box(rg.Plane(center, rg.Vector3d.ZAxis), rg.Interval(-0.5 * cube_size, 0.5 * cube_size), rg.Interval(-0.5 * cube_size, 0.5 * cube_size), rg.Interval(-0.5 * cube_size, 0.5 * cube_size))
                
                # Convert box to Brep and add to list
                cubic_nest.append(box.ToBrep())

    return cubic_nest"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_matrix(base_size=2.0, rows=4, columns=4, layers=2, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_matrix(base_size=1.5, rows=5, columns=3, layers=4, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_matrix(base_size=2.5, rows=3, columns=5, layers=3, randomness_seed=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_matrix(base_size=3.5, rows=2, columns=2, layers=2, randomness_seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_matrix(base_size=4.0, rows=3, columns=3, layers=1, randomness_seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
