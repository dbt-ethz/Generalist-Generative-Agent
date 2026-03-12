# Created for 0011_0003_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the 'Shifted Grid' metaphor by starting with a conventional grid structure. It randomly applies shifts and rotations to individual grid cells, creating a dynamic interplay of misaligned volumes. This results in intersecting and overlapping planes that enhance spatial complexity and movement. The model foregrounds adaptability and fluidity, facilitating unique circulation paths and diverse spatial experiences. By intentionally manipulating light and shadow through angled surfaces, the generated model embodies the metaphor's essence, inviting exploration and interaction within the architectural space."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, cell_size=5, shift_amount=2, rotation_angle=15):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    The function generates a grid of cells, applies shifts and rotations to selected cells,
    and returns a list of 3D geometries representing the concept model. The model emphasizes
    dynamic reconfiguration through intersecting and overlapping planes, with non-orthogonal 
    elements to manipulate light and shadow.

    Parameters:
        grid_size (int): The number of cells in each direction of the initial grid.
        cell_size (float): The size of each grid cell in meters.
        shift_amount (float): The amount by which to shift selected grid cells in meters.
        rotation_angle (float): The angle by which to rotate selected grid cells in degrees.

    Returns:
        list: A list of RhinoCommon Brep objects representing the concept model.

    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)

    geometries = []

    # Create initial grid of cells
    for i in range(grid_size):
        for j in range(grid_size):
            # Determine the base position for each cell
            x = i * cell_size
            y = j * cell_size
            z = 0

            # Create a base box for each cell
            base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + cell_size), rg.Interval(y, y + cell_size), rg.Interval(z, z + cell_size))

            # Randomly decide if this cell will be shifted or rotated
            if random.random() > 0.5:
                # Apply a shift
                shift_vector = rg.Vector3d(random.choice([-1, 1]) * shift_amount, random.choice([-1, 1]) * shift_amount, 0)
                base_box.Transform(rg.Transform.Translation(shift_vector))

            if random.random() > 0.5:
                # Apply a rotation
                rotation_center = rg.Point3d(x + cell_size / 2, y + cell_size / 2, 0)
                rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_center)
                base_box.Transform(rotation_transform)

            # Convert the box to a Brep and add to the list
            geometries.append(base_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, cell_size=4, shift_amount=3, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=4, cell_size=6, shift_amount=1, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=7, cell_size=3, shift_amount=5, rotation_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=8, cell_size=2, shift_amount=4, rotation_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, cell_size=5, shift_amount=1, rotation_angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
