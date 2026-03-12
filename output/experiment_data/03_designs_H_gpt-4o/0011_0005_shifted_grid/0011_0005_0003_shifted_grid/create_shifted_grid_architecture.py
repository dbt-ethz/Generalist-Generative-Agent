# Created for 0011_0005_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model by transforming a standard grid into a dynamic structure that embodies the "Shifted Grid" metaphor. It begins with a grid framework and applies random shifts, rotations, and height variations to create staggered volumes that suggest movement and fluidity. Each grid cell is manipulated to introduce irregularity, resulting in unique intersections and non-linear spatial arrangements that encourage diverse circulation paths. The model emphasizes adaptability and interaction with light and shadow, creating varied patterns that enhance the sense of energy and exploration within the architectural space."""

#! python 3
function_code = """def create_shifted_grid_architecture(base_size=4, height_variation=2, skew_factor=0.2, rotation_variation=10):
    \"""
    Generates a 3D architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    This function begins with a regular grid framework and introduces shifts, skews,
    and rotations to create a dynamic and interactive architectural form. The model
    consists of staggered volumes and intersecting planes, emphasizing movement, fluidity,
    and adaptability.

    Parameters:
    - base_size (int): The number of grid cells along each axis.
    - height_variation (float): The maximum variation in height for each grid cell volume.
    - skew_factor (float): The factor by which each cell is skewed to introduce irregularity.
    - rotation_variation (float): Maximum rotation angle in degrees for grid elements.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensures replicability of randomness

    geometries = []  # List to store resulting Brep geometries
    grid_unit = 5.0  # meters (size of each grid cell)

    for i in range(base_size):
        for j in range(base_size):
            # Base position for each cell
            x_base = i * grid_unit
            y_base = j * grid_unit

            # Height with variation
            height = grid_unit + random.uniform(-height_variation, height_variation)

            # Create a base box
            box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(x_base, x_base + grid_unit),
                rg.Interval(y_base, y_base + grid_unit),
                rg.Interval(0, height)
            )

            # Apply skew transformation
            skew_matrix = rg.Transform.Identity
            skew_x = random.uniform(-skew_factor, skew_factor)
            skew_y = random.uniform(-skew_factor, skew_factor)
            skew_matrix.M03 = skew_x * grid_unit
            skew_matrix.M13 = skew_y * grid_unit
            box.Transform(skew_matrix)

            # Rotate each box around its center
            center = box.Center
            rotation_angle_rad = math.radians(random.uniform(-rotation_variation, rotation_variation))
            rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
            rotation_transform = rg.Transform.Rotation(rotation_angle_rad, rotation_axis, center)
            box.Transform(rotation_transform)

            # Convert box to Brep and add to list
            brep = box.ToBrep()
            if brep:
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_architecture(base_size=5, height_variation=3, skew_factor=0.5, rotation_variation=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_architecture(base_size=6, height_variation=1, skew_factor=0.3, rotation_variation=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_architecture(base_size=7, height_variation=4, skew_factor=0.1, rotation_variation=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_architecture(base_size=8, height_variation=2.5, skew_factor=0.4, rotation_variation=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_architecture(base_size=3, height_variation=5, skew_factor=0.6, rotation_variation=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
