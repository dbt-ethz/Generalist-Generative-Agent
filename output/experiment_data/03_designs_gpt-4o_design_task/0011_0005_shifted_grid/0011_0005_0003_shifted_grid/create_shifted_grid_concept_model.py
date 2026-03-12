# Created for 0011_0005_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "Shifted Grid" metaphor by manipulating a standard grid framework. It creates a base grid, then introduces random shifts and rotations to grid points to simulate dynamic movement and fluidity. The function constructs volumes at these shifted points, ensuring they are slightly smaller than the grid to highlight gaps and irregularities. By layering multiple levels with varied shifts and rotations, the model reflects the metaphors emphasis on adaptability, innovative circulation, and engaging spatial experiences. This results in a complex interplay of light and shadow, embodying the intended architectural concept."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, max_shift=2, rotation_angle=15, num_levels=3):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    Parameters:
    - grid_size: The spacing between grid lines in meters. Default is 5 meters.
    - max_shift: The maximum shift distance allowed for grid elements in meters. Default is 2 meters.
    - rotation_angle: The maximum rotation angle for grid elements in degrees. Default is 15 degrees.
    - num_levels: The number of vertical levels in the model. Default is 3.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    geometries = []

    # Base grid
    base_grid_points = []
    for x in range(grid_size):
        for y in range(grid_size):
            base_grid_points.append(rg.Point3d(x * grid_size, y * grid_size, 0))

    # Generate shifted grid elements
    for level in range(num_levels):
        for point in base_grid_points:
            # Apply random shift
            shift_x = random.uniform(-max_shift, max_shift)
            shift_y = random.uniform(-max_shift, max_shift)
            shifted_point = rg.Point3d(point.X + shift_x, point.Y + shift_y, level * grid_size)

            # Create box (volume) at shifted point
            box_width = grid_size * 0.9  # Slightly smaller than grid to create gaps
            box_height = grid_size
            box = rg.Box(rg.Plane(shifted_point, rg.Vector3d.ZAxis), rg.Interval(0, box_width), rg.Interval(0, box_width), rg.Interval(0, box_height))

            # Convert box to Brep for rotation
            brep_box = box.ToBrep()

            # Apply random rotation
            rotation_radians = math.radians(random.uniform(-rotation_angle, rotation_angle))
            rotation_axis = rg.Line(shifted_point, rg.Point3d(shifted_point.X, shifted_point.Y, shifted_point.Z + 1))
            transform = rg.Transform.Rotation(rotation_radians, rotation_axis.Direction, shifted_point)
            brep_box.Transform(transform)

            # Add to geometries
            geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, max_shift=3, rotation_angle=30, num_levels=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=4, max_shift=1, rotation_angle=10, num_levels=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=7, max_shift=5, rotation_angle=20, num_levels=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=8, max_shift=4, rotation_angle=25, num_levels=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, max_shift=2, rotation_angle=45, num_levels=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
