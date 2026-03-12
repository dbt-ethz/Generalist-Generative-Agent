# Created for 0011_0005_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the 'Shifted Grid' metaphor by manipulating a standard grid framework. It applies random shifts, rotations, and misalignments to the grid cells, creating dynamic, staggered volumes that embody fluidity and movement. The structure's design encourages innovative circulation paths and unique spatial experiences, reflecting the metaphor's emphasis on adaptability and interaction. By incorporating varying light and shadow patterns through these transformations, the model not only captures visual interest but also fosters exploration and engagement within the space, aligning perfectly with the metaphor's key traits."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_grid_size=10, cell_size=5, vertical_shift=2, horizontal_shift=3, rotation_angle=15):
    \"""
    Generates a 3D architectural Concept Model based on the 'Shifted Grid' metaphor. This function creates a dynamic
    structure by transforming a standard grid framework through shifts, rotations, and misalignments to embody movement 
    and fluidity. The model consists of staggered volumes and intersecting planes to articulate the dynamic nature of the metaphor.

    Parameters:
    - base_grid_size (int): The number of cells in one direction of the grid (both x and y directions).
    - cell_size (float): The size of each cell in the grid in meters.
    - vertical_shift (float): The amount by which cells are vertically shifted to create staggered volumes.
    - horizontal_shift (float): The amount by which cells are horizontally shifted.
    - rotation_angle (float): The angle in degrees by which certain volumes are rotated to create a sense of dynamic movement.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    from math import radians, sin, cos

    random.seed(42)  # Ensures replicability of randomness

    breps = []  # List to store resulting Brep geometries

    for i in range(base_grid_size):
        for j in range(base_grid_size):
            # Calculate base position for each cell
            x_base = i * cell_size
            y_base = j * cell_size

            # Introduce shifts
            x_shift = x_base + (random.choice([-1, 1]) * horizontal_shift * random.random())
            y_shift = y_base + (random.choice([-1, 1]) * vertical_shift * random.random())

            # Define base box geometry
            box = Rhino.Geometry.Box(
                Rhino.Geometry.Plane.WorldXY,
                Rhino.Geometry.Interval(x_shift, x_shift + cell_size),
                Rhino.Geometry.Interval(y_shift, y_shift + cell_size),
                Rhino.Geometry.Interval(0, cell_size)
            )

            # Rotate the box around its center
            center = box.Center
            rotation_rad = radians(random.choice([-1, 1]) * rotation_angle * random.random())
            rotation_axis = Rhino.Geometry.Vector3d(0, 0, 1)  # Rotate around the Z-axis
            rotation_transform = Rhino.Geometry.Transform.Rotation(rotation_rad, rotation_axis, center)
            box.Transform(rotation_transform)

            # Convert the box to a Brep and add to list
            brep = box.ToBrep()
            if brep:
                breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(base_grid_size=8, cell_size=4, vertical_shift=1.5, horizontal_shift=2, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(base_grid_size=12, cell_size=6, vertical_shift=3, horizontal_shift=4, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(base_grid_size=6, cell_size=3, vertical_shift=2.5, horizontal_shift=1, rotation_angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(base_grid_size=10, cell_size=5, vertical_shift=2, horizontal_shift=3, rotation_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(base_grid_size=15, cell_size=7, vertical_shift=4, horizontal_shift=5, rotation_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
