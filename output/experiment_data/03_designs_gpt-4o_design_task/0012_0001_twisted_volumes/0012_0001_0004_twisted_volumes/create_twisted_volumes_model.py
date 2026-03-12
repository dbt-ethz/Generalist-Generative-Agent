# Created for 0012_0001_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates interlocking geometric forms by twisting rectangular bases, resulting in dynamic, distorted shapes that reflect the metaphor's essence. The parameters allow for varying dimensions, heights, and angles of twist, facilitating exploration of unique spatial relationships and circulation paths. By manipulating the geometry's orientation, the function also enhances light and shadow interplay, capturing and reflecting light in innovative ways. The final output is a collection of twisted volumes that embody fluidity and tension, showcasing a transformative architectural approach."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length, base_width, height, twist_angle, num_volumes):
    \"""
    Create an architectural Concept Model based on the 'Twisted volumes' metaphor.
    
    This function generates a series of interlocking geometric forms that are rotated and distorted,
    embodying the dynamic interplay of twisted volumes. The model emphasizes fluidity and tension,
    exploring spatial relationships, circulation paths, and the interplay of light and shadow.

    Parameters:
    - base_length (float): The length of the base of each volume in meters.
    - base_width (float): The width of the base of each volume in meters.
    - height (float): The height of each volume in meters.
    - twist_angle (float): The angle in degrees by which each volume is twisted from base to top.
    - num_volumes (int): The number of twisted volumes to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math
    import random
    random.seed(42)  # Ensure replicability
    
    volumes = []

    for i in range(num_volumes):
        # Create the base rectangle for the volume
        base_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_length, 0, 0),
            rg.Point3d(base_length, base_width, 0),
            rg.Point3d(0, base_width, 0),
            rg.Point3d(0, 0, 0)  # Close the polyline
        ]
        base_curve = rg.Polyline(base_corners).ToNurbsCurve()

        # Create a twisted lofted surface
        top_curve = base_curve.Duplicate()
        top_curve.Translate(rg.Vector3d(0, 0, height))
        top_curve.Rotate(math.radians(twist_angle * (i + 1)), rg.Vector3d.ZAxis, rg.Point3d(0, 0, height / 2))

        loft_curves = [base_curve, top_curve]
        twisted_surface = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

        # Add volume to the list
        volumes.append(twisted_surface)

        # Randomly translate the volume for spatial variety
        translation_vector = rg.Vector3d(random.uniform(-5, 5), random.uniform(-5, 5), 0)
        twisted_surface.Translate(translation_vector)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(2.0, 1.0, 3.0, 30.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(1.5, 2.0, 4.0, 45.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(3.0, 2.0, 5.0, 60.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(2.5, 1.5, 6.0, 15.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(4.0, 3.0, 2.0, 90.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
