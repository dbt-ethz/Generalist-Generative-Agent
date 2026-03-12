# Created for 0012_0001_twisted_volumes.json

""" Summary:
The given Python function `create_twisted_volumes_model` generates an architectural concept model based on the metaphor of "Twisted volumes." It creates a series of interlocking geometric forms that are dynamically twisted and distorted, embodying the fluidity and tension suggested by the metaphor. By varying the number of twists and their magnitude, the function explores unique spatial relationships and circulation paths. The resulting volumes enhance interactions between interior and exterior spaces while manipulating light and shadow, producing visually compelling effects. This innovative approach effectively translates the metaphor into a tangible architectural model, showcasing movement and transformation."""

#! python 3
function_code = """def create_twisted_volumes_model(base_size=10, height=20, num_twists=3, twist_magnitude=0.5, num_volumes=5):
    \"""
    Creates an architectural Concept Model using the 'Twisted volumes' metaphor.

    This function generates a series of abstract, interlocking geometric forms that are twisted
    and distorted, embodying the dynamic interplay of twisted volumes. The forms explore spatial
    relationships, circulation paths, and the interplay of light and shadow.

    Parameters:
    - base_size (float): The base dimension of each volume in meters.
    - height (float): The height of each volume in meters.
    - num_twists (int): The number of twists applied along the height of each volume.
    - twist_magnitude (float): The magnitude of the twist as a proportion of base size.
    - num_volumes (int): The number of twisted volumes to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math
    from Rhino.Geometry import Point3d, Polyline, Brep, LoftType, Vector3d, Transform

    # Helper function to create a twisted profile
    def create_twisted_profile(base_curve, height, num_twists, magnitude):
        profiles = []
        for i in range(num_twists + 1):
            z_height = i * (height / num_twists)
            twist_angle = magnitude * base_size * i / num_twists  # Varying twist angle
            twist_transform = Transform.Rotation(math.radians(twist_angle), Vector3d.ZAxis, Point3d(0, 0, z_height))
            moved_curve = base_curve.DuplicateCurve()
            moved_curve.Transform(twist_transform)
            moved_curve.Translate(Vector3d(0, 0, z_height))
            profiles.append(moved_curve)
        return profiles

    geometries = []

    for v in range(num_volumes):
        # Create a base square profile
        base_corners = [
            Point3d(-base_size/2, -base_size/2, 0),
            Point3d(base_size/2, -base_size/2, 0),
            Point3d(base_size/2, base_size/2, 0),
            Point3d(-base_size/2, base_size/2, 0),
            Point3d(-base_size/2, -base_size/2, 0)  # Close the loop
        ]
        base_curve = Polyline(base_corners).ToNurbsCurve()

        # Generate twisted profiles
        profiles = create_twisted_profile(base_curve, height, num_twists, twist_magnitude)

        # Loft the profiles to create a twisted volume
        loft_type = LoftType.Normal
        breps = Brep.CreateFromLoft(profiles, Point3d.Unset, Point3d.Unset, loft_type, False)
        
        # Ensure successful loft creation
        if breps:
            twisted_volume = breps[0]
            geometries.append(twisted_volume)

        # Translate volumes for interlocking effect
        translation_vector = Vector3d(v * base_size * 0.6, v * base_size * 0.6, 0)
        for geom in geometries:
            geom.Translate(translation_vector)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_size=15, height=30, num_twists=5, twist_magnitude=0.7, num_volumes=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_size=12, height=25, num_twists=4, twist_magnitude=0.6, num_volumes=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_size=8, height=15, num_twists=2, twist_magnitude=0.4, num_volumes=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_size=20, height=40, num_twists=6, twist_magnitude=0.8, num_volumes=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_size=18, height=35, num_twists=7, twist_magnitude=0.9, num_volumes=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
