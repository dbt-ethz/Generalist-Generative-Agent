# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Mirrored folded planes." It creates a series of dynamic, angular surfaces arranged symmetrically around a central axis, emphasizing movement and depth. By utilizing parameters like axis length, plane count, and fold variation, the function introduces variations in width and height to create visually engaging folded planes. Each plane is mirrored across the central axis, enhancing the reflective symmetry and complexity. The resulting model showcases a rhythmic repetition of forms and interconnected spaces, inviting exploration and highlighting the balance between intricacy and coherence in spatial organization."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(axis_length=10.0, plane_count=6, max_height=5.0, max_width=4.0, fold_variation=0.5):
    \"""
    This function creates an architectural Concept Model that embodies the 'Mirrored folded planes' metaphor.
    It generates a series of dynamic, folded surfaces arranged symmetrically around a central axis,
    with variations in folding to emphasize movement and depth.

    Parameters:
    - axis_length (float): The length of the central axis around which the planes are mirrored (in meters).
    - plane_count (int): The number of folded planes on each side of the axis.
    - max_height (float): The maximum height of each plane (in meters).
    - max_width (float): The maximum width of each plane (in meters).
    - fold_variation (float): The variation factor for folds to create dynamic forms (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure the randomness is replicable

    # List to store the generated geometries
    geometries = []

    # Central axis line
    central_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(axis_length, 0, 0))

    # Create folded planes
    for i in range(plane_count):
        # Position of the plane along the central axis
        offset = (i + 0.5) * (axis_length / plane_count)
        
        # Define the base point
        base_point = rg.Point3d(offset, 0, 0)
        
        # Randomly vary the width and height for dynamic folds
        width_variation = max_width * random.uniform(1 - fold_variation, 1 + fold_variation)
        height_variation = max_height * random.uniform(1 - fold_variation, 1 + fold_variation)
        
        # Create four corners of the folded plane
        corner1 = base_point + rg.Vector3d(width_variation, 0, 0)
        corner2 = corner1 + rg.Vector3d(0, 0, height_variation)
        corner3 = base_point + rg.Vector3d(0, 0, height_variation)
        
        # Create the folded plane surface
        folded_plane = rg.Brep.CreateFromCornerPoints(base_point, corner1, corner2, corner3, 0.001)

        # Mirror the plane across the central axis
        mirror_transform = rg.Transform.Mirror(rg.Plane(rg.Point3d(offset, 0, 0), rg.Vector3d(0, 1, 0)))
        mirrored_plane = folded_plane.DuplicateBrep()
        mirrored_plane.Transform(mirror_transform)

        # Add both the original and mirrored plane to the geometries list
        geometries.append(folded_plane)
        geometries.append(mirrored_plane)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(axis_length=15.0, plane_count=8, max_height=6.0, max_width=3.0, fold_variation=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(axis_length=12.0, plane_count=5, max_height=4.0, max_width=2.0, fold_variation=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(axis_length=20.0, plane_count=10, max_height=7.0, max_width=5.0, fold_variation=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(axis_length=18.0, plane_count=7, max_height=8.0, max_width=5.0, fold_variation=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(axis_length=25.0, plane_count=4, max_height=3.0, max_width=6.0, fold_variation=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
