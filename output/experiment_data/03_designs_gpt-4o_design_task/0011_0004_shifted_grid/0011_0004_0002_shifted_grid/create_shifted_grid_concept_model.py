# Created for 0011_0004_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the "Shifted Grid" metaphor by manipulating a conventional grid layout. It introduces random shifts and rotations to grid elements, creating dynamic, non-orthogonal forms that evoke fluidity and movement. Each grid cell is transformed into a 3D volume with varying angles and projections, resulting in an intricate silhouette. This approach encourages innovative spatial arrangements and non-linear circulation paths, allowing for diverse functions and experiences. The model captures the interplay of light and shadow, fostering an environment of exploration and engagement with the architecture."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, shift_amount=2, rotation_angle=15):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. This function generates a series of 
    interconnected volumes with shifts and rotations applied to a conventional grid, resulting in a dynamic and fluid 
    architectural form.

    Inputs:
        grid_size (int): The number of units in the grid (both rows and columns). Default is 5.
        shift_amount (float): The magnitude of shift applied to the grid elements in meters. Default is 2 meters.
        rotation_angle (float): The angle of rotation applied to grid elements in degrees. Default is 15 degrees.

    Outputs:
        List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed for replicability
    random.seed(42)

    # Initialize an empty list to store the Breps
    breps = []

    # Define the base size of each grid cell
    cell_size = 10  # meters

    # Loop through the grid
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the base position of the cell
            base_x = i * cell_size
            base_y = j * cell_size

            # Apply a random shift to the base position
            shift_x = base_x + random.uniform(-shift_amount, shift_amount)
            shift_y = base_y + random.uniform(-shift_amount, shift_amount)

            # Create the base volume as a box
            base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, cell_size), rg.Interval(0, cell_size), rg.Interval(0, cell_size))

            # Move the box to the shifted position
            translation = rg.Transform.Translation(shift_x, shift_y, 0)
            base_box.Transform(translation)

            # Randomly decide to rotate the box
            if random.random() > 0.5:
                rotation_center = base_box.Center
                rotation = rg.Transform.Rotation(math.radians(rotation_angle), rotation_center)
                base_box.Transform(rotation)

            # Convert the box to a Brep and add to the list
            brep_box = base_box.ToBrep()
            breps.append(brep_box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=3, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=1.5, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=2.5, rotation_angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=3, shift_amount=1, rotation_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=4, rotation_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
