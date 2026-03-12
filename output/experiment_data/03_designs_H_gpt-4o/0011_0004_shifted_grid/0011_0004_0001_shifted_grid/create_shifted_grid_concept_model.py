# Created for 0011_0004_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model by implementing the 'Shifted Grid' metaphor. It begins with a conventional grid, introducing random shifts and rotations to each grid unit, resulting in varied configurations that challenge traditional orthogonal forms. The model's design emphasizes non-linear circulation paths and interconnected spaces, allowing for dynamic spatial experiences. By varying heights and applying transformations, it creates a playful silhouette that enhances interaction between light and shadow. The output is a collection of 3D geometries that embody adaptability and exploration, aligning closely with the design task's goals of fluidity and discovery in architectural form."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, shift_amount=3, rotation_angle=10, height_variability=2, floor_count=3):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor. The design introduces strategic
    shifts and rotations across a conventional grid to form a dynamic silhouette with varied angles and projections.
    The model emphasizes non-linear circulation paths, interconnected spaces, and intricate light-shadow interactions.

    Parameters:
        grid_size (int): The number of units in the grid (both rows and columns).
        shift_amount (float): Maximum shift applied to each grid unit in meters.
        rotation_angle (float): Maximum rotation angle applied to each grid unit in degrees.
        height_variability (float): Maximum variation in height for the volumes in meters.
        floor_count (int): Number of floors or layers in the concept model.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed for replicability
    random.seed(42)

    breps = []
    cell_size = 10  # meters, base size of grid cell

    for floor in range(floor_count):
        base_z = floor * (cell_size + height_variability / 2)
        
        for i in range(grid_size):
            for j in range(grid_size):
                # Calculate base position of each grid cell
                x = i * cell_size
                y = j * cell_size

                # Apply random shift and rotation
                shift_x = random.uniform(-shift_amount, shift_amount)
                shift_y = random.uniform(-shift_amount, shift_amount)
                rotation = random.uniform(-rotation_angle, rotation_angle)

                # Create a base box for each grid cell
                box = rg.Box(
                    rg.Plane.WorldXY,
                    rg.Interval(x, x + cell_size),
                    rg.Interval(y, y + cell_size),
                    rg.Interval(base_z, base_z + random.uniform(4, 8) + height_variability)
                )

                # Transform the box
                translation = rg.Transform.Translation(shift_x, shift_y, 0)
                box.Transform(translation)
                
                center = box.Center
                rotation_transform = rg.Transform.Rotation(math.radians(rotation), center)
                box.Transform(rotation_transform)

                # Convert to Brep and add to list
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
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=4, rotation_angle=15, height_variability=3, floor_count=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=2, rotation_angle=20, height_variability=1, floor_count=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=5, rotation_angle=25, height_variability=4, floor_count=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=3.5, rotation_angle=30, height_variability=2.5, floor_count=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=6, rotation_angle=12, height_variability=3.5, floor_count=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
