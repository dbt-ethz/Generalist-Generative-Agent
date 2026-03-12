# Created for 0012_0003_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model based on the metaphor "Twisted volumes" by creating a series of interconnected volumetric elements that exhibit varying degrees of twist and distortion. Each volume is defined by a base rectangle, which is twisted using a randomized angle along its height, resulting in dynamic forms that evoke movement and fluidity. The model emphasizes innovative spatial relationships and transitions, enhancing interaction between interior and exterior spaces. By manipulating light and shadow through the twisted surfaces, the design animates the structure, capturing the essence of continuous evolution and transformation inherent in the metaphor."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length, base_width, height, twist_angle, num_volumes, seed=42):
    \"""
    Generates a series of interconnected volumetric elements that exhibit varying degrees of twist and distortion,
    reflecting the 'Twisted volumes' metaphor in an architectural concept model.

    Parameters:
    - base_length (float): The base length of each volume in meters.
    - base_width (float): The base width of each volume in meters.
    - height (float): The height of each volume in meters.
    - twist_angle (float): The maximum twist angle in degrees for the volumetric elements.
    - num_volumes (int): The number of volumetric elements to create.
    - seed (int): Optional seed for randomness to ensure replicability.

    Returns:
    - List of RhinoCommon.Geometry.Brep: A list of 3D geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    volumes = []
    base_plane = rg.Plane.WorldXY
    current_z = 0

    for i in range(num_volumes):
        # Create a base rectangle for the volume
        base_rect = rg.Rectangle3d(base_plane, base_length, base_width)
        base_curve = base_rect.ToNurbsCurve()

        # Define height and angle of twist for each volume
        volume_height = height
        angle_of_twist = random.uniform(0, twist_angle)

        # Create a series of sections for a smoother twist
        sections = []
        for j in range(6):  # Increase the number of sections for smoother twisting
            t = j / 5.0
            section_plane = base_plane.Clone()
            section_plane.Translate(rg.Vector3d(0, 0, t * volume_height))
            section_plane.Rotate(math.radians(angle_of_twist * t), section_plane.ZAxis)
            section_rect = rg.Rectangle3d(section_plane, base_length, base_width)
            sections.append(section_rect.ToNurbsCurve())

        # Loft between the sections to create a smoothly twisted volume
        loft_brep = rg.Brep.CreateFromLoft(sections, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft_brep:
            volumes.append(loft_brep[0])

        # Move the base plane up for the next volume
        base_plane.Translate(rg.Vector3d(0, 0, volume_height))

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(5.0, 3.0, 10.0, 180.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(4.0, 2.5, 8.0, 90.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(6.0, 4.0, 12.0, 270.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(3.0, 2.0, 6.0, 360.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(7.0, 5.0, 15.0, 150.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
