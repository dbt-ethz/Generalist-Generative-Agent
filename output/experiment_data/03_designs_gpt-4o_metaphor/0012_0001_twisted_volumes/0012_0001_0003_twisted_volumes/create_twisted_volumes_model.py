# Created for 0012_0001_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates dynamic, fluid forms through the manipulation of a rectangular base, applying a twist along its height based on specified parameters (length, width, height, and twist angle). The model consists of multiple sections, each rotated at incremental angles to achieve a visually engaging form. This twisting action fosters innovative spatial relationships, enhances circulation, and plays with light and shadow, reflecting the metaphor's essence of movement and transformation in architecture. The output is a list of 3D geometries representing these twisted volumes."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length=10, base_width=10, height=15, twist_angle=30):
    \"""
    Creates a Concept Model based on the metaphor 'Twisted volumes'. This model consists of dynamic and fluid forms
    that engage with the perception through rotation and distortion.

    Parameters:
    - base_length (float): The length of the base of the volume in meters.
    - base_width (float): The width of the base of the volume in meters.
    - height (float): The height of the volume in meters.
    - twist_angle (float): The maximum angle of twist along the height in degrees.

    Returns:
    - List of Breps: The 3D geometry representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create the base rectangle
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0)
    ]
    base_curve = rg.Polyline(base_corners + [base_corners[0]]).ToNurbsCurve()

    # Create the twisted volume
    twisted_breps = []
    num_sections = 10  # Number of sections to define the twist
    section_height = height / num_sections

    for i in range(num_sections + 1):
        z = i * section_height
        angle = math.radians((twist_angle / num_sections) * i)
        transform = rg.Transform.Rotation(angle, rg.Vector3d(0, 0, 1), rg.Point3d(base_length / 2, base_width / 2, z))
        section_curve = base_curve.Duplicate()
        section_curve.Transform(transform)
        section_curve.Translate(rg.Vector3d(0, 0, z))
        
        if i > 0:  # Skip the first section as it has no previous section to loft from
            loft = rg.Brep.CreateFromLoft([prev_curve, section_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft:
                twisted_breps.extend(loft)
        
        prev_curve = section_curve
    
    return twisted_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_length=12, base_width=8, height=20, twist_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_length=15, base_width=15, height=25, twist_angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_length=5, base_width=10, height=10, twist_angle=90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_length=8, base_width=6, height=12, twist_angle=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_length=20, base_width=10, height=30, twist_angle=90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
