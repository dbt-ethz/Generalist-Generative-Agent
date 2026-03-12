# Created for 0012_0003_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes` generates an architectural concept model by creating a series of twisted volumetric elements that embody the metaphor of "Twisted volumes." By defining parameters such as height, radius, twist angle, and the number of twists, the function constructs dynamic forms through a process of lofting curves that undergo rotation and distortion. Each volume captures the essence of movement and transformation, resulting in fluid spatial connections and varying light conditions. This approach allows for innovative interior arrangements and enhances the interaction between spaces, fulfilling the design task while visually expressing energy and evolution."""

#! python 3
function_code = """def create_twisted_volumes(height, radius, twist_angle, num_twists):
    \"""
    Creates a series of twisted volumetric elements as an architectural Concept Model.

    Parameters:
    - height (float): The height of each twisted volume in meters.
    - radius (float): The base radius of each volume, dictating its size.
    - twist_angle (float): The maximum twist angle in degrees applied to each volume.
    - num_twists (int): The number of twisted volumes to generate.

    Returns:
    - List of Breps: A list of twisted Brep surfaces representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    from math import radians, sin, cos, pi

    # Set seed for reproducibility
    random.seed(42)

    breps = []

    for i in range(num_twists):
        # Calculate twist for each volume
        angle = radians(twist_angle * random.uniform(0.5, 1.5))

        # Create base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, radius)

        # Create twisted surface by lofting between offset circles
        twisted_curve = []
        for j in range(10):  # Number of segments in height
            factor = j / 9.0
            z = factor * height
            rotation = factor * angle

            # Create plane for each segment
            plane = rg.Plane.WorldXY
            plane.Translate(rg.Vector3d(0, 0, z))
            plane.Rotate(rotation, plane.ZAxis)

            # Create rotated circle at each height segment
            twisted_circle = rg.Circle(plane, radius * (1 + 0.2 * sin(factor * pi)))
            twisted_curve.append(twisted_circle.ToNurbsCurve())

        # Loft the curves to create the twisted volume
        loft_brep = rg.Brep.CreateFromLoft(twisted_curve, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        breps.append(loft_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes(10.0, 2.0, 45.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes(15.0, 3.0, 60.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes(8.0, 1.5, 30.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes(12.0, 2.5, 90.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes(20.0, 4.0, 75.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
