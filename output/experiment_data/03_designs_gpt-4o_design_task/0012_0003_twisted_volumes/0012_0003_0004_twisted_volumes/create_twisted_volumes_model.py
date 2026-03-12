# Created for 0012_0003_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates a series of interconnected volumetric elements that exhibit varying twists and distortions, reflecting dynamic movement and spatial fluidity. By defining parameters such as base dimensions, height, twist angle, and divisions, the function constructs a series of planes that are progressively rotated. This results in a lofted surface that embodies the metaphor's essence, fostering unexpected spatial relationships and enhancing light and shadow interplay. The model ultimately conveys a sense of energy and transformation, aligning with the metaphor's implications for architectural design."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length=10, base_width=10, height=30, twist_angle=45, divisions=5):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Twisted volumes'. This model features a composition
    of interconnected volumetric elements that exhibit varying degrees of twist and distortion, emphasizing dynamic
    movement and spatial fluidity.

    Parameters:
    - base_length (float): The length of the base of each volume in meters.
    - base_width (float): The width of the base of each volume in meters.
    - height (float): The height of the volumes in meters.
    - twist_angle (float): The total angle of twist applied to the volumes in degrees.
    - divisions (int): The number of divisions or segments along the height to create the twist effect.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the twisted volumes.
    \"""

    import Rhino.Geometry as rg
    import random
    import math  # Corrected import for math functions
    random.seed(42)  # Ensure replicability

    breps = []
    base_plane = rg.Plane.WorldXY

    # Create a base rectangle
    base_rect = rg.Rectangle3d(base_plane, base_length, base_width)

    # Create a series of planes along the height of the volume
    planes = [base_plane]
    for i in range(1, divisions + 1):
        plane = base_plane.Clone()
        plane.Translate(rg.Vector3d(0, 0, height * i / divisions))
        plane.Rotate(math.radians(twist_angle * i / divisions), plane.ZAxis)
        planes.append(plane)

    # Create a lofted surface between the planes
    curves = [rg.PolylineCurve(base_rect.ToPolyline())]
    for plane in planes[1:]:
        transformed_rect = base_rect.ToNurbsCurve()
        transformed_rect.Transform(rg.Transform.PlaneToPlane(base_plane, plane))
        curves.append(transformed_rect)

    loft = rg.Brep.CreateFromLoft(curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
    if loft:
        breps.extend(loft)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_length=15, base_width=10, height=40, twist_angle=60, divisions=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_length=12, base_width=15, height=25, twist_angle=90, divisions=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_length=8, base_width=8, height=20, twist_angle=30, divisions=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_length=20, base_width=15, height=35, twist_angle=75, divisions=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_length=18, base_width=12, height=50, twist_angle=120, divisions=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
