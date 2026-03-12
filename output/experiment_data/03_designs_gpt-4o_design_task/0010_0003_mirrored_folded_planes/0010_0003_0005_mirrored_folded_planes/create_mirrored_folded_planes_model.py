# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The provided function, `create_mirrored_folded_planes_model`, generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." By accepting parameters such as base dimensions, height, fold angle, and mirror axis, the function constructs angular, folded forms that create a dynamic visual experience. It employs geometric transformations to mirror these forms across specified axes, ensuring symmetry and balance. The resultant design emphasizes complexity and unity, incorporating light reflection and shadow interplay. This methodical approach to spatial organization fosters a harmonious flow, inviting exploration through the intricately layered geometry, aligning with the metaphor's implications."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, fold_angle, mirror_axis):
    \"""
    Generates an architectural Concept Model based on the 'Mirrored folded planes' metaphor. This function creates a
    series of angular, folded forms that are mirrored across a specified axis to achieve a balanced and dynamic design.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The height of the folds in meters.
    - fold_angle (float): The angle at which the planes are folded in degrees.
    - mirror_axis (str): The axis along which to mirror the geometry ('x', 'y', or 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the mirrored folded planes.

    Note: This function uses RhinoCommon for geometry creation.
    \"""
    import Rhino.Geometry as rg
    import math

    # Helper function to create a folded plane
    def create_folded_plane(length, width, height, angle):
        base_plane = rg.Plane.WorldXY
        points = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(length, 0, 0),
            rg.Point3d(length, width, 0),
            rg.Point3d(0, width, 0),
            rg.Point3d(0, 0, 0)
        ]

        # Fold the plane
        fold_rad = math.radians(angle)
        fold_vector = rg.Vector3d(0, 0, height)
        fold_vector.Rotate(fold_rad, rg.Vector3d(1, 0, 0))
        points[1] += fold_vector
        points[2] += fold_vector

        # Create a polyline and extrude it
        polyline = rg.Polyline(points)
        curve = polyline.ToNurbsCurve()
        extrusion = rg.Extrusion.Create(curve, height, True)

        return extrusion.ToBrep()

    # Create the initial folded plane
    folded_plane_1 = create_folded_plane(base_length, base_width, height, fold_angle)

    # Mirror the folded plane across the specified axis
    if mirror_axis == 'x':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis == 'y':
        mirror_plane = rg.Plane.WorldZX
    elif mirror_axis == 'z':
        mirror_plane = rg.Plane.WorldXY
    else:
        raise ValueError("Invalid mirror axis. Choose 'x', 'y', or 'z'.")

    mirrored_plane = folded_plane_1.DuplicateBrep()
    mirrored_plane.Transform(rg.Transform.Mirror(mirror_plane))

    # Return the list of Breps
    return [folded_plane_1, mirrored_plane]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10, 5, 3, 45, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(8, 4, 2, 30, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12, 7, 5, 60, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(15, 6, 4, 50, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(9, 3, 2, 75, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
