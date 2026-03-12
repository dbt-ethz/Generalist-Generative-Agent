# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes` generates an architectural concept model that embodies the metaphor of "Mirrored folded planes." By utilizing parameters such as base length, height, fold angle, and mirror axis, the function creates a series of interlocked, angular surfaces that reflect across specified axes. This approach emphasizes the dynamic interplay of light and shadow while achieving a cohesive yet intricate design. The resulting geometries exemplify the metaphor's traits of symmetry and complexity, inviting exploration of layered forms that embody a rhythmic spatial experience, thereby fulfilling the design task effectively."""

#! python 3
function_code = """def create_mirrored_folded_planes(seed, base_length, height, fold_angle, mirror_axis):
    \"""
    Create an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function generates a series of interlocked, angular folded planes that reflect 
    across specified axes, creating a layered and rhythmic geometry. The planes are 
    configured to form a cohesive yet intricate design, emphasizing the interplay 
    of light and shadow.

    Parameters:
    - seed (int): A seed for the random number generator to ensure replicable results.
    - base_length (float): The base length of each folded plane in the model (in meters).
    - height (float): The height of each folded plane (in meters).
    - fold_angle (float): The angle at which each plane folds (in degrees).
    - mirror_axis (str): The axis across which the planes are mirrored. Options are 'x', 'y', or 'z'.

    Returns:
    - List[Brep]: A list of Brep geometries representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed the random number generator
    random.seed(seed)

    # Helper function to create a folded plane
    def create_folded_plane(base_length, height, fold_angle):
        # Create the base rectangle
        base_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_length, 0, 0),
            rg.Point3d(base_length, height, 0),
            rg.Point3d(0, height, 0)
        ]
        base_polyline = rg.Polyline(base_corners + [base_corners[0]])
        base_surface = rg.Brep.CreatePlanarBreps(base_polyline.ToNurbsCurve())[0]

        # Create the folded geometry by rotating the base surface
        fold_rad = math.radians(fold_angle)
        fold_transform = rg.Transform.Rotation(fold_rad, rg.Vector3d(0, 1, 0), rg.Point3d(base_length / 2, height / 2, 0))
        folded_surface = base_surface.DuplicateBrep()
        folded_surface.Transform(fold_transform)

        return folded_surface

    # Create initial folded plane
    folded_planes = [create_folded_plane(base_length, height, fold_angle)]

    # Mirror the folded plane across the specified axis
    mirror_plane = None
    if mirror_axis == 'x':
        mirror_plane = rg.Plane.WorldZX
    elif mirror_axis == 'y':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis == 'z':
        mirror_plane = rg.Plane.WorldXY

    mirrored_planes = []
    for plane in folded_planes:
        mirrored_plane = plane.DuplicateBrep()
        mirrored_plane.Transform(rg.Transform.Mirror(mirror_plane))
        mirrored_planes.append(mirrored_plane)

    # Combine original and mirrored planes
    all_planes = folded_planes + mirrored_planes

    return all_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes(42, 5.0, 3.0, 30.0, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes(17, 4.0, 2.5, 45.0, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes(99, 6.0, 4.0, 60.0, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes(3, 7.0, 5.0, 15.0, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes(58, 8.0, 6.0, 75.0, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
