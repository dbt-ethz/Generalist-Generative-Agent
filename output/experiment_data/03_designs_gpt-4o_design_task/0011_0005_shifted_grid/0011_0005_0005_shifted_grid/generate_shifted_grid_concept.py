# Created for 0011_0005_shifted_grid.json

""" Summary:
The function `generate_shifted_grid_concept` creates an architectural concept model based on the 'Shifted Grid' metaphor by starting with a standard grid framework. It applies random shifts and rotations to grid elements, resulting in a dynamic arrangement that embodies movement and fluidity. Each grid cell is extruded into a 3D volume, incorporating variations in height to enhance visual complexity. This approach fosters innovative spatial arrangements and diverse circulation paths, while the shifting elements create intriguing light and shadow interactions. The adaptability of the spaces encourages exploration, aligning with the metaphor's emphasis on transformation and engagement in architecture."""

#! python 3
function_code = """def generate_shifted_grid_concept(base_grid_size, shift_amount, max_rotation):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor. 
    The model begins with a standard grid framework and applies shifts, rotations, 
    and alignments to create a dynamic and interactive form.

    Parameters:
    base_grid_size (int): The size of the base grid in terms of number of units per side.
    shift_amount (float): The maximum amount by which grid elements can be shifted.
    max_rotation (float): The maximum rotation angle (in degrees) that can be applied to grid elements.

    Returns:
    list: A list of Rhino.Geometry.Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed the random number generator for replicability
    random.seed(42)

    # Initialize a list to store the resulting geometries
    geometries = []

    # Define the base grid dimensions
    grid_unit_size = 5.0  # meters (each grid cell is 5x5 meters)
    height_variation = 2.0  # meters (variation in height of each volume)

    # Generate the base grid points
    for i in range(base_grid_size):
        for j in range(base_grid_size):
            # Calculate base position
            base_x = i * grid_unit_size
            base_y = j * grid_unit_size

            # Apply shifts
            shift_x = random.uniform(-shift_amount, shift_amount)
            shift_y = random.uniform(-shift_amount, shift_amount)

            # Calculate the new shifted position
            new_x = base_x + shift_x
            new_y = base_y + shift_y

            # Create a base plane at the new position
            base_plane = rg.Plane(rg.Point3d(new_x, new_y, 0), rg.Vector3d.ZAxis)

            # Apply rotation
            rotation_angle = random.uniform(-max_rotation, max_rotation)
            rotated_plane = base_plane
            rotated_plane.Rotate(math.radians(rotation_angle), base_plane.Normal)

            # Create the volume (extruded surface)
            height = grid_unit_size + random.uniform(-height_variation, height_variation)
            base_surface = rg.Rectangle3d(rotated_plane, grid_unit_size, grid_unit_size).ToNurbsCurve()
            extrusion_vector = rg.Vector3d(0, 0, height)
            brep_volume = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_surface, extrusion_vector))

            if brep_volume:
                geometries.append(brep_volume)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_shifted_grid_concept(10, 2.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_shifted_grid_concept(8, 1.5, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_shifted_grid_concept(12, 3.0, 60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_shifted_grid_concept(6, 2.5, 90.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_shifted_grid_concept(5, 1.0, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
