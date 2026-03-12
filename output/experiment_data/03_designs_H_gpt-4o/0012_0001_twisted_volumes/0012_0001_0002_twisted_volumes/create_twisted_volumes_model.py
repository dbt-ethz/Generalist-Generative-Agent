# Created for 0012_0001_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates a series of interlocking cylindrical forms that are twisted along their height, embodying the dynamic and fluid characteristics of the metaphor. By varying the twist angle and height for each volume, the model explores innovative spatial relationships and circulation paths. The twisting action enhances the play of light and shadow, creating unique reflections and perspectives. These twisted forms collectively present a cohesive visual impact, aligning with the key traits of energy and transformation, while promoting interaction between interior and exterior spaces."""

#! python 3
function_code = """def create_twisted_volumes_model(base_radius, height, twist_angle, num_volumes):
    \"""
    Generates an architectural Concept Model based on the metaphor 'Twisted volumes'.
    
    This function creates a series of cylindrical forms that are twisted along their height, 
    embodying dynamic and fluid architectural designs. The volumes explore spatial relationships, 
    circulation paths, and the interplay of light and shadow by twisting around their central axis.

    Parameters:
    - base_radius (float): The radius of the base of each cylinder in meters.
    - height (float): The height of each cylinder in meters.
    - twist_angle (float): The total angle in degrees by which each cylinder is twisted from base to top.
    - num_volumes (int): The number of twisted cylindrical volumes to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math
    import random
    random.seed(42)  # Ensure replicable randomness

    breps = []

    for i in range(num_volumes):
        # Create a base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        
        # Create a series of profiles along the height with incremental twists
        profiles = []
        for j in range(6):  # Create 6 profiles along the height
            z_height = j * (height / 5)
            angle = j * (twist_angle / 5) * (math.pi / 180)  # Convert to radians

            # Create a twisted profile at this height
            plane = rg.Plane(rg.Point3d(0, 0, z_height), rg.Vector3d.ZAxis)
            profile_circle = base_circle.ToNurbsCurve()
            profile_circle.Rotate(angle, rg.Vector3d.ZAxis, plane.Origin)
            profiles.append(profile_circle)

        # Loft the profiles to create a twisted volume
        loft_type = rg.LoftType.Normal
        breps.extend(rg.Brep.CreateFromLoft(profiles, rg.Point3d.Unset, rg.Point3d.Unset, loft_type, False))

        # Offset the next volume for visual separation
        offset_vector = rg.Vector3d((i + 1) * base_radius * 2, 0, 0)
        for brep in breps:
            brep.Translate(offset_vector)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(2.0, 10.0, 90.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(1.5, 8.0, 180.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(3.0, 12.0, 45.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(2.5, 15.0, 120.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(1.0, 5.0, 360.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
