# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model by interpreting the metaphor of "Mirrored folded planes." It creates a series of interlocked, angular forms that reflect across multiple axes, achieving dynamic equilibrium between light and shadow. The function constructs folded planes based on specified dimensions and fold angles, then mirrors these geometries to enhance visual symmetry and complexity. This process results in a cohesive design that embodies the metaphor's traits movement, depth, and a rhythmic interplay of shapes. The final output consists of 3D geometries that invite exploration of their intricate, layered spaces, aligning with the design task's requirements."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(width, depth, height, fold_angle, mirror_axis_count):
    \"""
    Creates a Concept Model based on the 'Mirrored folded planes' metaphor using angular forms 
    that reflect across multiple axes. The function generates a series of interlocked, 
    angular planes that are folded and mirrored to achieve a dynamic equilibrium of light and shadow.

    Parameters:
    - width (float): The width of the initial base plane in meters.
    - depth (float): The depth of the initial base plane in meters.
    - height (float): The height of the folded structure in meters.
    - fold_angle (float): The angle in degrees at which the planes are folded.
    - mirror_axis_count (int): The number of axes across which the geometry is mirrored.

    Returns:
    - List of RhinoCommon.Geometry.Brep: A list of Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import math

    def create_folded_plane(base_width, base_depth, fold_height, angle):
        # Create base plane
        base_plane = rg.Plane.WorldXY
        rect_corners = [
            rg.Point3d(0, 0, 0), 
            rg.Point3d(base_width, 0, 0), 
            rg.Point3d(base_width, base_depth, 0),
            rg.Point3d(0, base_depth, 0)
        ]
        base_surface = rg.Brep.CreateFromCornerPoints(rect_corners[0], rect_corners[1], rect_corners[2], rect_corners[3], 0.01)

        # Calculate fold transformation
        angle_radians = math.radians(angle)
        fold_vector = rg.Vector3d(0, fold_height * math.tan(angle_radians), fold_height)
        fold_plane = rg.Plane(base_plane)
        fold_plane.Translate(fold_vector)

        # Create folded surface
        loft_curves = [rg.LineCurve(rect_corners[i], fold_plane.Origin + fold_vector) for i in range(4)]
        folded_surface = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        return folded_surface[0] if folded_surface else None

    def mirror_geometry(geometry, axis_count):
        mirrored_geometries = [geometry]
        for i in range(1, axis_count):
            mirrored_geom = geometry.Duplicate()
            mirror_plane = rg.Plane.WorldXY
            mirror_plane.Rotate(math.pi * i / axis_count, rg.Vector3d.ZAxis, rg.Point3d(0, 0, 0))
            mirrored_geom.Transform(rg.Transform.Mirror(mirror_plane))
            mirrored_geometries.append(mirrored_geom)
        return mirrored_geometries

    # Create initial folded plane
    folded_brep = create_folded_plane(width, depth, height, fold_angle)

    # Mirror geometry across specified number of axes
    mirrored_breps = mirror_geometry(folded_brep, mirror_axis_count)

    return mirrored_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(5.0, 10.0, 3.0, 45.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(7.5, 12.0, 4.0, 30.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(6.0, 8.0, 2.5, 60.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(4.0, 6.0, 2.0, 90.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(8.0, 15.0, 5.0, 75.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
