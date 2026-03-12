# Created for 0011_0004_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model that embodies the "Shifted Grid" metaphor by transforming a conventional grid into a dynamic form. It achieves this by introducing random shifts and rotations for each grid cell, creating a playful silhouette characterized by irregular angles and projections. The model incorporates overlapping volumes to establish interconnected spaces with non-linear circulation paths, fostering adaptability and varied spatial experiences. It also emphasizes light and shadow interactions through extruded shapes, enhancing the sense of movement and exploration, thereby reflecting the metaphor's implications of fluidity and discovery in architecture."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, shift_amount=2, rotation_angle=15, height_variation=2):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor. This approach focuses on creating 
    a dynamic and fluid architectural form by systematically shifting and rotating a conventional grid. The model 
    emphasizes interconnected spaces with non-linear circulation paths, varied scales, and intricate light and shadow 
    interactions.

    Parameters:
        grid_size (int): The number of divisions in the grid, defining its size.
        shift_amount (float): The magnitude of shift for each grid cell in meters.
        rotation_angle (float): The rotation angle applied to each grid cell in degrees.
        height_variation (float): The variation in height for the extruded volumes in meters.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed for replicability
    random.seed(42)

    geometries = []

    # Base grid spacing
    cell_size = 10  # meters

    # Generate the grid points
    for i in range(grid_size):
        for j in range(grid_size):
            # Base position for grid cell
            x = i * cell_size
            y = j * cell_size
            z = 0

            # Calculate shift for the grid point
            shift_x = random.uniform(-shift_amount, shift_amount)
            shift_y = random.uniform(-shift_amount, shift_amount)

            # Create a shifted base point
            base_point = rg.Point3d(x + shift_x, y + shift_y, z)

            # Create a polygonal shape (hexagon) to enhance the dynamic form
            hexagon_points = [
                rg.Point3d(base_point.X + math.cos(math.radians(angle)) * 3, 
                           base_point.Y + math.sin(math.radians(angle)) * 3, 
                           base_point.Z) for angle in range(0, 360, 60)
            ]
            hexagon_points.append(hexagon_points[0])  # Closing the polyline
            hexagon = rg.Polyline(hexagon_points)

            # Rotate the shape around its centroid
            centroid = rg.AreaMassProperties.Compute(hexagon.ToNurbsCurve()).Centroid
            rotation = rg.Transform.Rotation(math.radians(rotation_angle), centroid)
            hexagon.Transform(rotation)

            # Extrude the shape to create a solid
            extrusion_vector = rg.Vector3d(0, 0, random.uniform(3, 3 + height_variation))
            extruded_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(hexagon.ToNurbsCurve(), extrusion_vector))

            if extruded_brep:
                geometries.append(extruded_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=3, rotation_angle=30, height_variation=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=1.5, rotation_angle=45, height_variation=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=2.5, rotation_angle=20, height_variation=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=2, rotation_angle=25, height_variation=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=4, rotation_angle=10, height_variation=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
