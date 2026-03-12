# Created for 0012_0001_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model by leveraging the metaphor of "Twisted volumes." It creates a series of interlocking geometric forms that are dynamically twisted along their height, reflecting the fluid and tense characteristics of the metaphor. By varying the twist angle and the number of twists, the function explores innovative spatial relationships and circulation paths. The lofting process produces complex shapes that enhance light and shadow interactions, encapsulating the design's energy and transformation. Ultimately, the resulting geometries embody the metaphor while offering a coherent visual and spatial experience."""

#! python 3
function_code = """def create_twisted_volumes_model(base_size=10, height=20, twist_angle=15, twist_count=5):
    \"""
    Creates a conceptual architectural model using the 'Twisted volumes' metaphor.

    Parameters:
    - base_size (float): The base dimension of the volumes in meters.
    - height (float): The height of each volume in meters.
    - twist_angle (float): The angle of twist applied to each volume in degrees.
    - twist_count (int): The number of times the twist is applied along the height.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted volumes.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    random.seed(42)

    # Create a base square as the starting profile
    base_corners = [
        rg.Point3d(-base_size/2, -base_size/2, 0),
        rg.Point3d(base_size/2, -base_size/2, 0),
        rg.Point3d(base_size/2, base_size/2, 0),
        rg.Point3d(-base_size/2, base_size/2, 0)
    ]
    base_curve = rg.Polyline(base_corners + [base_corners[0]]).ToNurbsCurve()

    # Define a lofted twisted volume
    profiles = []
    for i in range(twist_count + 1):
        angle = i * twist_angle * (3.14159 / 180.0)  # Convert to radians
        z_height = i * (height / twist_count)
        twist_transform = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, rg.Point3d(0, 0, z_height))
        moved_curve = base_curve.DuplicateCurve()
        moved_curve.Transform(twist_transform)
        moved_curve.Translate(rg.Vector3d(0, 0, z_height))
        profiles.append(moved_curve)

    # Loft the profiles to create a twisted volume
    loft_type = rg.LoftType.Normal
    breps = rg.Brep.CreateFromLoft(profiles, rg.Point3d.Unset, rg.Point3d.Unset, loft_type, False)

    # Return the twisted volumes as a list of Breps
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_size=15, height=30, twist_angle=20, twist_count=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_size=12, height=25, twist_angle=10, twist_count=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_size=8, height=15, twist_angle=25, twist_count=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_size=18, height=35, twist_angle=30, twist_count=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_size=14, height=22, twist_angle=12, twist_count=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
