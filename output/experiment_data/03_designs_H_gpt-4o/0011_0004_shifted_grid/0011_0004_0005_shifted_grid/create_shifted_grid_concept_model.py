# Created for 0011_0004_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "Shifted Grid" metaphor by creating a dynamic arrangement of interconnected volumes. It begins with a conventional grid, applying random shifts and rotations to each grid cell, promoting a playful and intricate silhouette. The function iteratively constructs polygons at varying heights, extruding them to create three-dimensional forms that embody the metaphor's fluidity. By generating diverse angles and projections, it fosters non-linear circulation paths and enhances light-shadow interactions. The resulting model exemplifies adaptability, encouraging exploration and engagement with its innovative spatial relationships."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, shift_amount=2, rotation_angle=15, level_count=3, level_height=3):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. This function generates a series of 
    interconnected volumes with strategic shifts and rotations, resulting in a dynamic architectural form with varied 
    angles and projections. The design fosters non-linear circulation paths and intricate light-shadow interplay.

    Args:
        grid_size (int): The size of the initial grid defining the number of divisions.
        shift_amount (float): The amount by which each grid cell is shifted.
        rotation_angle (float): The angle by which each grid cell is rotated to create a dynamic form.
        level_count (int): The number of vertical levels in the model.
        level_height (float): The height of each level.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for randomness to ensure replicability
    random.seed(42)

    breps = []

    # Create an initial grid of points
    for level in range(level_count):
        z_base = level * level_height
        for i in range(grid_size):
            for j in range(grid_size):
                x = i * 5.0  # 5 meters spacing
                y = j * 5.0
                point = rg.Point3d(x, y, z_base)

                # Apply shift and rotation
                shift_vector = rg.Vector3d(
                    random.uniform(-shift_amount, shift_amount),
                    random.uniform(-shift_amount, shift_amount),
                    0
                )
                point.Transform(rg.Transform.Translation(shift_vector))

                # Create base polygon
                polygon = rg.Polyline([
                    point,
                    rg.Point3d(point.X + 4, point.Y, point.Z),
                    rg.Point3d(point.X + 4, point.Y + 4, point.Z),
                    rg.Point3d(point.X, point.Y + 4, point.Z),
                    point
                ]).ToNurbsCurve()

                # Rotate around the center of the polygon
                center = rg.Point3d(point.X + 2, point.Y + 2, point.Z)
                rotation = rg.Transform.Rotation(math.radians(rotation_angle), center)
                polygon.Transform(rotation)

                # Scale the polygon to introduce variation
                scale = rg.Transform.Scale(center, random.uniform(0.8, 1.2))
                polygon.Transform(scale)

                # Extrude the polygon to create a box
                extrusion_vector = rg.Vector3d(0, 0, level_height)
                extrusion = rg.Extrusion.Create(polygon, extrusion_vector.Length, True)
                brep = extrusion.ToBrep()
                
                # Add the brep to the list
                if brep:
                    breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=3, rotation_angle=30, level_count=4, level_height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=1.5, rotation_angle=45, level_count=5, level_height=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=2.5, rotation_angle=60, level_count=2, level_height=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=2, rotation_angle=10, level_count=3, level_height=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=4, rotation_angle=20, level_count=3, level_height=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
