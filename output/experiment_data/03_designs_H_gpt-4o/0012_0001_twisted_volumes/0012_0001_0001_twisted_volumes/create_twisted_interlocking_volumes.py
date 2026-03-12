# Created for 0012_0001_twisted_volumes.json

""" Summary:
The function `create_twisted_interlocking_volumes` generates an architectural concept model inspired by the metaphor "Twisted volumes." It creates a series of interlocking cylindrical forms that are dynamically twisted and distorted to embody fluid architectural expressions. By manipulating parameters like base radius, height, twist angle, and the number of volumes, the function explores innovative spatial relationships and circulation paths. The twisting action enhances the interplay of light and shadow, producing unique visual effects. Ultimately, the model reflects energy and transformation, aligning with the metaphor's emphasis on dynamic forms and their impact on perception and interaction within the space."""

#! python 3
function_code = """def create_twisted_interlocking_volumes(base_radius, height, twist_angle, num_volumes):
    \"""
    Creates an architectural Concept Model inspired by the metaphor 'Twisted volumes'.

    This function generates a series of interlocking cylindrical volumes that are rotated
    and distorted to embody dynamic and fluid architectural forms. The design explores
    spatial relationships, circulation paths, and the interplay of light and shadow.

    Parameters:
    - base_radius (float): The radius of the base of each cylindrical volume in meters.
    - height (float): The height of each volume in meters.
    - twist_angle (float): The maximum angle of twist applied to each volume in degrees.
    - num_volumes (int): The number of twisted volumes to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(42)  # Ensure reproducibility

    volumes = []

    for i in range(num_volumes):
        # Create the base circle for the volume
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        base_curve = base_circle.ToNurbsCurve()

        # Create a series of profiles along the height with varying twist
        profiles = []
        for j in range(10):
            # Calculate the height position of each profile
            profile_height = height * (j / 9.0)
            # Calculate the twist angle at this height
            angle = twist_angle * (j / 9.0) * (math.pi / 180.0)  # Convert to radians
            # Create a transformation for twisting
            twist_transform = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, rg.Point3d(0, 0, profile_height))
            # Transform and translate the profile
            profile_curve = base_curve.DuplicateCurve()
            profile_curve.Transform(twist_transform)
            profile_curve.Translate(rg.Vector3d(0, 0, profile_height))
            profiles.append(profile_curve)

        # Loft the profiles to create a twisted volume
        loft_type = rg.LoftType.Normal
        loft = rg.Brep.CreateFromLoft(profiles, rg.Point3d.Unset, rg.Point3d.Unset, loft_type, False)
        
        if loft:
            twisted_volume = loft[0]
            # Randomly translate the volume for spatial variety
            translation_vector = rg.Vector3d(random.uniform(-2, 2), random.uniform(-2, 2), 0)
            twisted_volume.Translate(translation_vector)
            volumes.append(twisted_volume)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_interlocking_volumes(1.5, 3.0, 45, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_interlocking_volumes(2.0, 4.5, 60, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_interlocking_volumes(1.0, 2.5, 30, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_interlocking_volumes(1.2, 5.0, 90, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_interlocking_volumes(1.8, 3.5, 75, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
