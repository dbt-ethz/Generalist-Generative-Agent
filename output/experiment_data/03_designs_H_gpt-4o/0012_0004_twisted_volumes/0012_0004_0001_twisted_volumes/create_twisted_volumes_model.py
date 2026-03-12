# Created for 0012_0004_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volumes_model`, generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates multiple intersecting and twisting volumes, simulating dynamic motion and balance through carefully controlled rotations. Each volume is defined by a base rectangle that is twisted upward, forming a lofted surface between the base and a top rectangle, resulting in a visually striking form. The function incorporates transparency cutouts to enhance interactions of light and shadow, creating a complex interplay between interior and exterior spaces. This approach fosters innovative spatial relationships, embodying the metaphor's transformative energy."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length, base_width, height, num_volumes, max_twist, transparency_cutout_ratio):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor. This model showcases a series
    of intersecting and twisting volumes that reflect dynamic motion and balance.

    Parameters:
    - base_length (float): The base length of each volume in meters.
    - base_width (float): The base width of each volume in meters.
    - height (float): The height of each volume in meters.
    - num_volumes (int): The number of volumes to generate.
    - max_twist (float): The maximum twist angle applied to the volumes in degrees.
    - transparency_cutout_ratio (float): Ratio determining the extent of transparency cutouts (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted volumes of the Concept Model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for consistent results
    random.seed(42)

    # List to store the resulting Breps
    breps = []

    for i in range(num_volumes):
        # Define the base plane and rectangle for each volume
        base_plane = rg.Plane.WorldXY
        base_rect = rg.Rectangle3d(base_plane, base_length, base_width)

        # Define the twist angle for the volume
        twist_angle = random.uniform(-max_twist, max_twist)
        twist_transform = rg.Transform.Rotation(math.radians(twist_angle), base_plane.ZAxis, base_rect.Center)

        # Create the top rectangle with a twist
        top_plane = rg.Plane(base_plane)
        top_plane.Translate(rg.Vector3d(0, 0, height))
        top_rect = rg.Rectangle3d(top_plane, base_length, base_width)
        top_rect.Transform(twist_transform)

        # Create a loft between the base and top rectangles
        loft = rg.Brep.CreateFromLoft([base_rect.ToNurbsCurve(), top_rect.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        if loft:
            brep = loft[0]

            # Add transparency cutout
            if transparency_cutout_ratio > 0:
                cutout_scale = 1 - transparency_cutout_ratio
                cutout_transform = rg.Transform.Scale(base_plane, cutout_scale, cutout_scale, 1)
                base_rect.Transform(cutout_transform)
                cutout_brep = rg.Brep.CreateFromCornerPoints(base_rect.Corner(0), base_rect.Corner(1), top_rect.Corner(2), top_rect.Corner(3), 0.01)
                if cutout_brep:
                    boolean_result = rg.Brep.CreateBooleanDifference(brep, cutout_brep, 0.01)
                    if boolean_result:
                        brep = boolean_result[0]

            # Append the brep to the list
            breps.append(brep)

        # Slightly translate the base plane for the next volume
        translation_vec = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), height * 0.5)
        base_plane.Translate(translation_vec)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(5.0, 3.0, 10.0, 8, 45.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(6.0, 4.0, 12.0, 10, 60.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(4.0, 2.0, 8.0, 5, 30.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(7.0, 5.0, 15.0, 6, 50.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(3.0, 2.5, 7.0, 12, 90.0, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
