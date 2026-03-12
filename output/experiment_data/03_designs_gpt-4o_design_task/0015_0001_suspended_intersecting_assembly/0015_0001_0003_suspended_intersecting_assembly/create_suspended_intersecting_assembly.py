# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model inspired by the metaphor of "Suspended intersecting assembly." By utilizing parameters like the number of elements and their dimensions, the function randomly creates a series of planar surfaces that mimic floating components. Each surface is translated and rotated within a defined space, creating dynamic intersections that emphasize lightness, fluidity, and structural transparency. The interplay of angles and layering techniques enhances the model's visual complexity, embodying the metaphor's traits of balance, connectivity, and a delicate suspension within the architectural framework."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(seed: int, num_elements: int, max_dimension: float, angle_variation: float) -> list:
    \"""
    Generate an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.
    
    This function creates a series of intersecting planar elements that appear to float and intersect
    within a defined space. The design emphasizes lightness, fluidity, and structural transparency.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability.
    - num_elements (int): Number of planar elements to create.
    - max_dimension (float): Maximum dimension for the bounding box of the elements.
    - angle_variation (float): Maximum angle variation in degrees for the elements.

    Returns:
    - List of Breps: A list of 3D Brep geometries representing the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for repeatability
    random.seed(seed)

    # Initialize a list to hold the resulting Breps
    breps = []

    # Base plane for element creation
    base_plane = rg.Plane.WorldXY

    for _ in range(num_elements):
        # Randomize the size of each element
        width = random.uniform(max_dimension * 0.1, max_dimension * 0.5)
        height = random.uniform(max_dimension * 0.1, max_dimension * 0.5)
        
        # Define a rectangle as the base of the planar element
        rect_corners = [
            rg.Point3d(-width / 2, -height / 2, 0),
            rg.Point3d(width / 2, -height / 2, 0),
            rg.Point3d(width / 2, height / 2, 0),
            rg.Point3d(-width / 2, height / 2, 0)
        ]
        rect_curve = rg.Polyline(rect_corners + [rect_corners[0]]).ToNurbsCurve()

        # Randomize position within the bounding box
        x_translation = random.uniform(-max_dimension / 2, max_dimension / 2)
        y_translation = random.uniform(-max_dimension / 2, max_dimension / 2)
        z_translation = random.uniform(0, max_dimension)

        translation = rg.Transform.Translation(x_translation, y_translation, z_translation)

        # Randomize rotation in 3D space
        x_rotation = math.radians(random.uniform(-angle_variation, angle_variation))
        y_rotation = math.radians(random.uniform(-angle_variation, angle_variation))
        z_rotation = math.radians(random.uniform(-angle_variation, angle_variation))

        rot_x = rg.Transform.Rotation(x_rotation, base_plane.XAxis, rg.Point3d.Origin)
        rot_y = rg.Transform.Rotation(y_rotation, base_plane.YAxis, rg.Point3d.Origin)
        rot_z = rg.Transform.Rotation(z_rotation, base_plane.ZAxis, rg.Point3d.Origin)

        # Combine transformations
        transformation = translation * rot_x * rot_y * rot_z

        # Apply transformation to the base rectangle
        rect_curve.Transform(transformation)

        # Create a planar surface from the transformed rectangle
        planar_surface = rg.Brep.CreatePlanarBreps(rect_curve)[0]

        # Add to the list of Breps
        breps.append(planar_surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(seed=42, num_elements=10, max_dimension=100.0, angle_variation=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(seed=123, num_elements=5, max_dimension=50.0, angle_variation=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(seed=7, num_elements=20, max_dimension=200.0, angle_variation=45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(seed=99, num_elements=15, max_dimension=75.0, angle_variation=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(seed=2023, num_elements=8, max_dimension=150.0, angle_variation=60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
