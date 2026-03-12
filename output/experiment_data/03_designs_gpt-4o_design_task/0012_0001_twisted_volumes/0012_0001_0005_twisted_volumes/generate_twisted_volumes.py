# Created for 0012_0001_twisted_volumes.json

""" Summary:
The provided function, `generate_twisted_volumes`, creates an architectural concept model inspired by the metaphor "Twisted volumes." It generates a series of interlocking, twisted geometric forms by applying a rotation transformation to basic box shapes. Each volume is defined by its dimensions and a specified twist angle, resulting in dynamic silhouettes that suggest movement and transformation. The model emphasizes innovative spatial relationships and circulation paths while enhancing light and shadow interactions. This approach captures the essence of the metaphor, showcasing a fluid and tense architectural expression that fosters unexpected connections between interior and exterior spaces."""

#! python 3
function_code = """def generate_twisted_volumes(base_length, base_width, base_height, twist_angle, num_volumes):
    \"""
    Generates a series of twisted, interlocking geometric forms to embody the 'Twisted volumes' metaphor
    in an architectural concept model.

    Parameters:
        base_length (float): The base length of each volume in meters.
        base_width (float): The base width of each volume in meters.
        base_height (float): The base height of each volume in meters.
        twist_angle (float): The angle of twist applied to each volume in degrees.
        num_volumes (int): The number of volumes to generate.

    Returns:
        list: A list of Brep objects representing the twisted volumes.

    The function uses RhinoCommon to create and manipulate 3D geometry, specifically Breps. The twisting 
    of volumes creates dynamic forms that redefine spatial relationships and enhance the interaction 
    between interior and exterior spaces.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)  # Ensure replicable randomness

    volumes = []

    # Starting point for the first volume
    origin = rg.Point3d(0, 0, 0)

    for i in range(num_volumes):
        # Create a box as the base geometry
        base_box = rg.Box(rg.Plane(origin, rg.Vector3d.ZAxis), rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
        brep_box = base_box.ToBrep()

        # Apply a twist transform
        twist_transform = rg.Transform.Rotation(math.radians(twist_angle), rg.Vector3d.ZAxis, origin)
        twisted_brep = brep_box.DuplicateBrep()
        twisted_brep.Transform(twist_transform)

        # Add the twisted volume to the list
        volumes.append(twisted_brep)

        # Move the origin for the next volume to create interlocking effect
        translation_vector = rg.Vector3d(base_length * 0.8, base_width * 0.8, 0)
        origin += translation_vector

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_twisted_volumes(5.0, 3.0, 2.0, 30, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_twisted_volumes(4.0, 2.0, 3.0, 45, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_twisted_volumes(6.0, 4.0, 1.5, 60, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_twisted_volumes(7.0, 5.0, 4.0, 15, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_twisted_volumes(3.5, 2.5, 3.0, 90, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
