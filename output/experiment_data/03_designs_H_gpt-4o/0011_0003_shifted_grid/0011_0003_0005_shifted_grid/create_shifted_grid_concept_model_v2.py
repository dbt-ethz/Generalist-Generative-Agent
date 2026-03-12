# Created for 0011_0003_shifted_grid.json

""" Summary:
The provided function, `create_shifted_grid_concept_model_v2`, generates an architectural concept model by interpreting the 'Shifted Grid' metaphor. It begins with a traditional grid framework and introduces dynamic shifts and rotations to individual cells, resulting in a non-linear arrangement. By randomly applying shifts and rotations to the grid elements, the function creates overlapping planes and varied silhouettes that embody fluidity and movement. This approach fosters unique spatial experiences and diverse circulation paths, allowing for adaptable spaces. Ultimately, the model invites exploration and interaction, reflecting the metaphor's emphasis on innovative spatial arrangements and playful light manipulation."""

#! python 3
function_code = """def create_shifted_grid_concept_model_v2(grid_width=5, grid_height=5, cell_size=4, shift_distance=1.5, rotation_angle=10):
    \"""
    Creates an architectural Concept Model using the 'Shifted Grid' metaphor, emphasizing a dynamic interplay of
    shifted and rotated elements. The model starts with a conventional grid and applies strategic shifts and rotations
    to create overlapping and intersecting planes, fostering unique spatial experiences and circulation paths.

    Parameters:
    - grid_width (int): The number of grid cells along the x-axis.
    - grid_height (int): The number of grid cells along the y-axis.
    - cell_size (float): The size of each grid cell in meters.
    - shift_distance (float): The maximum distance by which cells are shifted in meters.
    - rotation_angle (float): The maximum angle in degrees by which cells are rotated.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)
    geometries = []

    # Create a function to generate a planar surface with a shift and rotation applied
    def create_shifted_rotated_surface(base_point, size, shift, angle):
        # Define the initial square corners
        corners = [
            rg.Point3d(base_point.X, base_point.Y, 0),
            rg.Point3d(base_point.X + size, base_point.Y, 0),
            rg.Point3d(base_point.X + size, base_point.Y + size, 0),
            rg.Point3d(base_point.X, base_point.Y + size, 0)
        ]

        # Apply random shift
        shift_x = random.uniform(-shift, shift)
        shift_y = random.uniform(-shift, shift)
        shifted_corners = [rg.Point3d(c.X + shift_x, c.Y + shift_y, c.Z) for c in corners]

        # Apply random rotation
        center = rg.Point3d(base_point.X + size / 2, base_point.Y + size / 2, 0)
        rotation_rad = math.radians(random.uniform(-angle, angle))
        rotation_transform = rg.Transform.Rotation(rotation_rad, center)
        rotated_corners = [corner.Transform(rotation_transform) or corner for corner in shifted_corners]

        # Create a planar surface from the transformed corners
        polyline = rg.Polyline(rotated_corners + [rotated_corners[0]])
        polyline_curve = polyline.ToNurbsCurve()
        surface = rg.Brep.CreatePlanarBreps(polyline_curve)

        return surface[0] if surface else None

    # Generate the grid of surfaces with shifts and rotations
    for i in range(grid_width):
        for j in range(grid_height):
            base_pt = rg.Point3d(i * cell_size, j * cell_size, 0)
            brep = create_shifted_rotated_surface(base_pt, cell_size, shift_distance, rotation_angle)
            if brep:
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model_v2(grid_width=6, grid_height=4, cell_size=3, shift_distance=2, rotation_angle=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model_v2(grid_width=8, grid_height=8, cell_size=5, shift_distance=2, rotation_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model_v2(grid_width=7, grid_height=5, cell_size=6, shift_distance=2.5, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model_v2(grid_width=5, grid_height=7, cell_size=4.5, shift_distance=1, rotation_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model_v2(grid_width=10, grid_height=3, cell_size=2, shift_distance=1, rotation_angle=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
