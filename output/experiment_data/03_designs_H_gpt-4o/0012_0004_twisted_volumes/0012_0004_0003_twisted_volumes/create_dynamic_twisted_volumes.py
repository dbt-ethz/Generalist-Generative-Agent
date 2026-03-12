# Created for 0012_0004_twisted_volumes.json

""" Summary:
The provided function creates an architectural concept model inspired by the metaphor "Twisted volumes." It generates a series of intersecting, twisting forms that embody dynamic balance and spatial interplay. Each volume is defined by parameters like base dimensions, height, and twist angles, contributing to a multifaceted structure. The function incorporates transparency, allowing light to interact with the volumes, enhancing visual complexity through cutouts. By manipulating the geometry and arrangement of these twisted forms, the model reflects movement, tension, and innovative spatial relationships while emphasizing the transformative qualities of light and shadow in the architectural experience."""

#! python 3
function_code = """def create_dynamic_twisted_volumes(base_length, base_width, height, num_volumes, max_twist_angle, transparency_factor):
    \"""
    Creates an architectural Concept Model that embodies the 'Twisted volumes' metaphor. 
    The function generates a set of twisting and intersecting volumes that capture dynamic balance and light interaction.

    Parameters:
    - base_length (float): The base length of each volume in meters.
    - base_width (float): The base width of each volume in meters.
    - height (float): The height of each volume in meters.
    - num_volumes (int): The number of twisting volumes to generate.
    - max_twist_angle (float): The maximum twist angle in degrees for each volume.
    - transparency_factor (float): Proportion of surfaces that will allow light to pass through (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the twisted volumes.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    from random import seed, uniform
    import math

    seed(42)  # Ensuring reproducibility

    breps = []

    for i in range(num_volumes):
        # Create base rectangle
        base_plane = rg.Plane.WorldXY
        base_rect = rg.Rectangle3d(base_plane, base_length, base_width)

        # Extrusion vector and twist
        extrusion_vector = rg.Vector3d(0, 0, height)
        twist_angle = uniform(-max_twist_angle, max_twist_angle)
        
        # Create twisted extrusion
        path_curve = rg.LineCurve(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height))
        shape_curve = base_rect.ToNurbsCurve()
        twisted_brep = rg.Brep.CreateFromSweep(path_curve, shape_curve, True, 0.01)[0]
        twist_transform = rg.Transform.Rotation(math.radians(twist_angle), extrusion_vector, rg.Point3d(0, 0, height / 2))
        twisted_brep.Transform(twist_transform)

        # Apply transparency cutouts
        if transparency_factor > 0:
            cutout_scale = 1 - transparency_factor
            cutout_transform = rg.Transform.Scale(rg.Plane.WorldXY, cutout_scale, cutout_scale, 1)
            cutout_brep = twisted_brep.Duplicate()
            cutout_brep.Transform(cutout_transform)
            boolean_diff = rg.Brep.CreateBooleanDifference(twisted_brep, cutout_brep, 0.01)
            if boolean_diff:
                twisted_brep = boolean_diff[0]

        # Append the final twisted and cutout volume
        breps.append(twisted_brep)

        # Offset base for next volume
        base_plane.Origin += rg.Vector3d(uniform(-1, 1), uniform(-1, 1), height * 0.5)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_twisted_volumes(5.0, 3.0, 10.0, 4, 45.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_twisted_volumes(4.0, 2.5, 8.0, 6, 30.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_twisted_volumes(6.0, 4.0, 12.0, 5, 60.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_twisted_volumes(7.0, 3.5, 15.0, 3, 90.0, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_twisted_volumes(3.0, 2.0, 5.0, 8, 75.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
