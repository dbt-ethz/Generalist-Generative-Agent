# Created for 0012_0003_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volumes_model`, generates an architectural concept model by creating a series of volumetric elements that embody the metaphor of "Twisted volumes." It takes parameters such as base dimensions, height, and twist angle to produce boxes that are rotated around a defined axis, simulating a dynamic and fluid architectural form. Each volumes twist fosters unexpected spatial relationships and enhances interaction with light and shadow, creating a visually engaging structure. By adjusting the number of volumes and their respective twists, the model embodies movement and transformation, aligning with the design task's emphasis on fluidity and discovery."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length, base_width, height, twist_angle, num_volumes):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor. This function generates a series of
    volumetric elements that are twisted and distorted to evoke dynamic movement and transformation.

    Inputs:
    - base_length (float): The length of the base of the volumes in meters.
    - base_width (float): The width of the base of the volumes in meters.
    - height (float): The height of each volume in meters.
    - twist_angle (float): The maximum angle of twist applied to the volumes in degrees.
    - num_volumes (int): The number of volumetric elements to create.

    Outputs:
    - A list of RhinoCommon Breps representing the twisted volumes.

    \"""
    import Rhino.Geometry as rg
    import random
    from math import radians

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    volumes = []

    for i in range(num_volumes):
        # Create the base rectangle
        base_rectangle = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)

        # Extrude the rectangle to create a box
        extrusion_vector = rg.Vector3d(0, 0, height)
        box = rg.Brep.CreateFromBox([base_rectangle.Corner(0), base_rectangle.Corner(1),
                                     base_rectangle.Corner(2), base_rectangle.Corner(3),
                                     base_rectangle.Corner(0) + extrusion_vector,
                                     base_rectangle.Corner(1) + extrusion_vector,
                                     base_rectangle.Corner(2) + extrusion_vector,
                                     base_rectangle.Corner(3) + extrusion_vector])

        # Determine the twist axis (z-axis) and the twist angle
        twist_axis_line = rg.Line(base_rectangle.Corner(0), base_rectangle.Corner(0) + extrusion_vector)
        twist_axis_curve = twist_axis_line.ToNurbsCurve()
        angle = radians(random.uniform(0, twist_angle))

        # Apply rotation to the box directly
        if box:
            box.Rotate(angle, rg.Vector3d(0, 0, 1), rg.Point3d(0, 0, 0))

            # Add the twisted box to the list of volumes
            volumes.append(box)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(5.0, 3.0, 10.0, 45.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(4.0, 2.5, 8.0, 30.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(6.0, 4.0, 12.0, 60.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(7.0, 3.5, 15.0, 75.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(3.5, 2.0, 7.0, 90.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
