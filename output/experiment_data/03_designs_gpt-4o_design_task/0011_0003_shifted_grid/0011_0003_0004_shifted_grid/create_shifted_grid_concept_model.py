# Created for 0011_0003_shifted_grid.json

""" Summary:
The provided function creates an architectural concept model based on the "Shifted Grid" metaphor by manipulating a conventional grid structure. It generates a series of 3D geometries through randomized shifts and rotations of grid cells, creating misaligned volumes that emphasize dynamic intersections. This approach results in a layered silhouette and unique spatial arrangements, encouraging fluid circulation paths and varied experiences within the space. The model's adaptability is enhanced by allowing configurations that support multiple functions, while angled surfaces play with light and shadow, inviting exploration and interaction in line with the metaphors implications of movement and discovery."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_grid_size=5, shift_amount=2, rotation_angle=15, height=3):
    \"""
    Creates an architectural Concept Model using the 'Shifted Grid' metaphor, 
    resulting in a dynamic interplay of shifted and rotated architectural elements.

    Parameters:
    - base_grid_size (float): The size of the initial grid cells in meters.
    - shift_amount (float): The amount by which grid elements are shifted in meters.
    - rotation_angle (float): The angle in degrees to rotate selected elements.
    - height (float): The height of the architectural volumes in meters.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)

    geometries = []
    
    # Create the base grid
    grid_points = []
    for i in range(4):
        for j in range(4):
            grid_points.append(rg.Point3d(i * base_grid_size, j * base_grid_size, 0))

    # Define a helper function to shift and rotate a given base cell
    def create_shifted_rotated_cell(base_pt, shift, angle, height):
        # Create the base rectangle
        rect_corners = [
            base_pt,
            rg.Point3d(base_pt.X + base_grid_size, base_pt.Y, 0),
            rg.Point3d(base_pt.X + base_grid_size, base_pt.Y + base_grid_size, 0),
            rg.Point3d(base_pt.X, base_pt.Y + base_grid_size, 0)
        ]
        
        # Shift the rectangle
        shift_vector = rg.Vector3d(shift, shift, 0)
        shifted_corners = [corner + shift_vector for corner in rect_corners]

        # Rotate the rectangle around its center
        center_pt = sum(shifted_corners, rg.Point3d(0, 0, 0)) / len(shifted_corners)
        rotation_transform = rg.Transform.Rotation(math.radians(angle), center_pt)
        rotated_corners = [corner.Transform(rotation_transform) or corner for corner in shifted_corners]

        # Create a Brep from the shifted and rotated rectangle
        polyline = rg.Polyline(rotated_corners + [rotated_corners[0]])
        polyline_curve = polyline.ToNurbsCurve()
        brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(polyline_curve, rg.Vector3d(0, 0, height)))

        return brep

    # Apply shifts and rotations to selected grid cells
    for i, pt in enumerate(grid_points):
        if i % 2 == random.randint(0, 1):  # Randomly decide if this cell should be shifted/rotated
            brep = create_shifted_rotated_cell(pt, shift_amount, rotation_angle, height)
            if brep:
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(base_grid_size=10, shift_amount=3, rotation_angle=30, height=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(base_grid_size=7, shift_amount=4, rotation_angle=45, height=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(base_grid_size=8, shift_amount=1, rotation_angle=60, height=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(base_grid_size=6, shift_amount=2.5, rotation_angle=90, height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(base_grid_size=12, shift_amount=5, rotation_angle=75, height=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
