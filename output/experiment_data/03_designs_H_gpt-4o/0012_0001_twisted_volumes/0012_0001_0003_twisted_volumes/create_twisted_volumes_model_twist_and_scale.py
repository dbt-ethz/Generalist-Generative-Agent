# Created for 0012_0001_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "Twisted volumes." By creating a series of interlocking geometric forms that are rotated and distorted, the function embodies dynamic spatial relationships and innovative circulation paths. Parameters such as base dimensions, twist angles, and scale factors allow for experimentation with volume manipulation, enhancing the interaction between light and shadow. As the volumes twist and scale, they create varied perspectives and unexpected connections, mirroring the metaphor's essence of movement and transformation. The result is a visually striking model that emphasizes both fluidity and structural tension."""

#! python 3
function_code = """def create_twisted_volumes_model_twist_and_scale(base_length, base_width, base_height, twist_angle, scale_factor, num_volumes):
    \"""
    Create an architectural Concept Model using the 'Twisted volumes' metaphor with a twist and scale approach.

    This function generates a series of abstract, interlocking geometric forms that are rotated, twisted, and scaled
    to explore dynamic spatial relationships, innovative circulation paths, and the interplay of light and shadow.

    Parameters:
    - base_length (float): The length of the base of each volume in meters.
    - base_width (float): The width of the base of each volume in meters.
    - base_height (float): The height of each volume in meters.
    - twist_angle (float): The angle in degrees applied as a twist to each volume.
    - scale_factor (float): The scaling factor applied to each successive volume.
    - num_volumes (int): The number of twisted volumes to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted and scaled volumes.
    \"""
    import Rhino.Geometry as rg
    import math
    import random
    random.seed(42)  # Ensure replicability

    volumes = []
    origin = rg.Point3d(0, 0, 0)

    for i in range(num_volumes):
        # Create a base box
        base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
        brep_box = base_box.ToBrep()

        # Apply a twist transform
        twist_transform = rg.Transform.Rotation(math.radians(twist_angle * (i + 1)), rg.Vector3d.ZAxis, origin + rg.Vector3d(0, 0, base_height / 2))
        twisted_brep = brep_box.DuplicateBrep()
        twisted_brep.Transform(twist_transform)

        # Apply a scaling transform
        scaling_point = origin + rg.Vector3d(base_length / 2, base_width / 2, base_height / 2)
        scale_transform = rg.Transform.Scale(scaling_point, scale_factor ** i)
        twisted_brep.Transform(scale_transform)

        # Add the twisted and scaled volume to the list
        volumes.append(twisted_brep)

        # Move the origin for the next volume
        translation_vector = rg.Vector3d(base_length * 0.6, base_width * 0.6, 0)
        origin += translation_vector

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model_twist_and_scale(2.0, 1.0, 3.0, 45, 1.2, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model_twist_and_scale(1.5, 1.0, 2.5, 30, 1.5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model_twist_and_scale(3.0, 2.0, 4.0, 60, 1.1, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model_twist_and_scale(2.5, 1.5, 3.5, 90, 1.3, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model_twist_and_scale(4.0, 2.0, 5.0, 15, 1.4, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
