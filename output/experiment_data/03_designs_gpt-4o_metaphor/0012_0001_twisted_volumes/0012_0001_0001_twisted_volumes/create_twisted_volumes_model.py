# Created for 0012_0001_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volumes_model`, generates an architectural concept model by creating a series of twisted volume geometries that embody the metaphor of "Twisted volumes." The function takes parameters such as base dimensions, height, twist angle, and the number of volumes, allowing for flexibility in design. Each volume is extruded from a rectangular base and twisted around a vertical axis, conveying movement and tension. This twisting action enhances the spatial experience, fostering innovative circulation paths and dynamic interactions between interior and exterior spaces. The result is a visually engaging model that plays with light and shadow, reflecting the metaphor's essence."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length, base_width, height, twist_angle, num_volumes):
    \"""
    Generates a list of twisted volume geometries for an architectural Concept Model.
    
    The function creates a series of twisted volumes that convey movement and tension through dynamic and fluid forms.
    The twisting action enhances interaction between spaces and plays with light and shadow.

    Parameters:
    - base_length (float): The length of the base rectangle of each volume in meters.
    - base_width (float): The width of the base rectangle of each volume in meters.
    - height (float): The height of each volume in meters.
    - twist_angle (float): The angle of twist applied to each volume in degrees.
    - num_volumes (int): The number of twisted volumes to create.

    Returns:
    - List of RhinoCommon Brep objects representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    volumes = []

    # Convert twist angle to radians for calculation
    twist_angle_rad = math.radians(twist_angle)

    # Create base curve, a rectangle
    base_curve = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width).ToNurbsCurve()

    for i in range(num_volumes):
        # Create an extrusion from the base curve
        extrusion = rg.Extrusion.Create(base_curve, height, True)

        # Calculate the rotation axis (vertical axis through the center of the base)
        center_point = rg.Point3d(base_length / 2, base_width / 2, 0)
        axis = rg.Line(center_point, rg.Point3d(center_point.X, center_point.Y, height))

        # Calculate the angle of twist for this volume
        current_twist_angle = ((i + 1) / num_volumes) * twist_angle_rad

        # Twist the volume around the axis
        twisted_brep = extrusion.ToBrep()
        twisted_brep.Rotate(current_twist_angle, rg.Vector3d.ZAxis, center_point)

        # Add the twisted volume to the list
        volumes.append(twisted_brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(5.0, 3.0, 10.0, 45.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(4.0, 2.5, 8.0, 30.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(6.0, 4.0, 12.0, 60.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(7.0, 5.0, 15.0, 90.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(3.0, 2.0, 5.0, 75.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
