# Created for 0011_0005_shifted_grid.json

""" Summary:
The function `create_shifted_grid_architecture` generates an architectural concept model inspired by the 'Shifted Grid' metaphor. It begins with a standard grid framework, applying random shifts and rotations to each grid point, simulating dynamic movement and fluidity. By creating staggered volumes and intersecting planes, the model embodies a non-linear spatial arrangement that fosters innovative circulation paths. This design accentuates light and shadow interactions, casting varied patterns and enhancing the overall energy of the structure. Additionally, the adaptable nature of the spaces allows for flexible functions, promoting exploration and discovery within the architectural experience."""

#! python 3
function_code = """def create_shifted_grid_architecture(grid_size=5, num_layers=3, shift_magnitude=1.0, rotation_angle=10):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor.

    This function creates a series of intersecting planes and staggered volumes
    by starting with a standard grid and applying shifts and rotations to simulate
    dynamic movement and fluidity within the structure. The resulting model exhibits
    non-linear spatial arrangements and innovative circulation paths, enhancing
    interaction with light and shadow.

    Parameters:
    - grid_size (float): The base size of each grid cell in meters.
    - num_layers (int): The number of vertical layers in the model.
    - shift_magnitude (float): Maximum distance to shift grid points in meters.
    - rotation_angle (float): Maximum angle in degrees for rotating grid planes.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the architectural model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure reproducibility

    # Initialize list to store the resulting geometries
    geometries = []

    # Create base grid points
    base_points = []
    for i in range(grid_size):
        for j in range(grid_size):
            base_points.append(rg.Point3d(i * grid_size, j * grid_size, 0))

    # Generate shifted and rotated planes
    for layer in range(num_layers):
        height = layer * grid_size  # Layer height
        for point in base_points:
            # Apply random shift
            shift_x = random.uniform(-shift_magnitude, shift_magnitude)
            shift_y = random.uniform(-shift_magnitude, shift_magnitude)
            shifted_point = rg.Point3d(point.X + shift_x, point.Y + shift_y, height)

            # Create a plane at the shifted point
            plane = rg.Plane(shifted_point, rg.Vector3d.ZAxis)

            # Apply random rotation
            rotation_rad = math.radians(random.uniform(-rotation_angle, rotation_angle))
            rotation_axis = rg.Line(shifted_point, rg.Point3d(shifted_point.X, shifted_point.Y, shifted_point.Z + 1))
            rotation_transform = rg.Transform.Rotation(rotation_rad, rotation_axis.Direction, shifted_point)
            plane.Transform(rotation_transform)

            # Create a rectangular surface on the plane
            rect = rg.Rectangle3d(plane, grid_size * 0.9, grid_size * 0.9)  # Slightly smaller to show gaps
            surface = rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), rg.Vector3d(0, 0, grid_size))

            # Convert to Brep and add to geometries
            brep = rg.Brep.CreateFromSurface(surface)
            if brep:
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_architecture(grid_size=6, num_layers=4, shift_magnitude=2.0, rotation_angle=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_architecture(grid_size=7, num_layers=5, shift_magnitude=1.5, rotation_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_architecture(grid_size=4, num_layers=2, shift_magnitude=0.5, rotation_angle=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_architecture(grid_size=8, num_layers=6, shift_magnitude=3.0, rotation_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_architecture(grid_size=5, num_layers=3, shift_magnitude=1.0, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
