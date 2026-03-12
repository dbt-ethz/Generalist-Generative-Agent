# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor of a "Suspended intersecting assembly." It creates a series of intersecting planes, each appearing to float and dynamically connect within three-dimensional space. By utilizing random orientations and heights for these planes, the model captures a sense of movement and fluidity, while lightweight materials and transparent geometries emphasize transparency and interconnectivity. The resulting structure embodies the metaphor's key traits of lightness and delicate balance, inviting interaction and enhancing visual dialogues through its intricate web of spatial relationships."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(seed, num_planes=5, plane_size=5.0, height_variation=3.0):
    \"""
    Generates an architectural Concept Model exemplifying the 'Suspended intersecting assembly' metaphor.
    
    The function creates a series of intersecting planar elements that are elevated and appear to float,
    forming a complex web of spatial relationships. The design focuses on transparency, fluidity, and
    dynamic intersections, suggesting movement and continuity.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability of results.
    - num_planes (int): Number of planar elements to generate.
    - plane_size (float): Size of each plane. Assumes a square plane with sides of length `plane_size`.
    - height_variation (float): Maximum vertical displacement for the planes to create variation in height.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the intersecting planes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # List to store the resulting Breps
    breps = []

    for i in range(num_planes):
        # Random orientation for each plane
        angle = random.uniform(0, 2 * 3.14159)  # Random rotation angle in radians
        rotation_axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        rotation_axis.Unitize()

        # Create a base plane
        base_plane = rg.Plane.WorldXY

        # Rotate the plane by the random angle around a random axis
        base_plane.Rotate(angle, rotation_axis)

        # Random height for each plane
        height = random.uniform(-height_variation, height_variation)

        # Translate the plane to a random height
        translation = rg.Vector3d(0, 0, height)
        base_plane.Translate(translation)

        # Create a rectangular surface on the base plane
        rect_corners = [
            base_plane.PointAt(-plane_size / 2, -plane_size / 2),
            base_plane.PointAt(plane_size / 2, -plane_size / 2),
            base_plane.PointAt(plane_size / 2, plane_size / 2),
            base_plane.PointAt(-plane_size / 2, plane_size / 2),
            base_plane.PointAt(-plane_size / 2, -plane_size / 2)  # Close the polyline by repeating the first point
        ]
        rect = rg.Polyline(rect_corners)
        surface = rg.Brep.CreateFromCornerPoints(rect[0], rect[1], rect[2], rect[3], 0.01)

        # Add the surface to the list of Breps
        breps.append(surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(seed=42, num_planes=8, plane_size=6.0, height_variation=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(seed=100, num_planes=10, plane_size=4.0, height_variation=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(seed=7, num_planes=6, plane_size=7.0, height_variation=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(seed=21, num_planes=12, plane_size=3.5, height_variation=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(seed=15, num_planes=9, plane_size=5.5, height_variation=3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
