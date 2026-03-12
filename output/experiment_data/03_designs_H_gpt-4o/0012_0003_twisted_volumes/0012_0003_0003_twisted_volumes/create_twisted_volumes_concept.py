# Created for 0012_0003_twisted_volumes.json

""" Summary:
The provided function `create_twisted_volumes_concept` generates an architectural concept model based on the metaphor "Twisted volumes." It creates a series of volumetric elements that exhibit varying degrees of twist and distortion, embodying dynamic forms that suggest movement and transformation. By manipulating parameters like height, radius, twist angle, and the number of volumes and slices, the function constructs a series of lofted geometries that reflect fluidity and unexpected spatial relationships. The design emphasizes light and shadow interactions, enhancing visual and physical connections between interior and exterior spaces, ultimately capturing the essence of the metaphor through architectural form."""

#! python 3
function_code = """def create_twisted_volumes_concept(height, radius, twist_angle, num_volumes, num_slices):
    \"""
    Generates a 3D architectural Concept Model based on the 'Twisted volumes' metaphor. The model consists of
    a series of volumetric elements that exhibit varying degrees of twist and distortion, creating a dynamic and fluid form.

    Parameters:
    - height (float): The height of each twisted volume in meters.
    - radius (float): The base radius of each volume, defining its size.
    - twist_angle (float): The maximum twist angle in degrees applied to the volumes.
    - num_volumes (int): The number of twisted volumes to create.
    - num_slices (int): The number of vertical slices to create the twist effect.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of breps representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a fixed seed for reproducibility
    random.seed(42)

    volumes = []

    for i in range(num_volumes):
        # Create a base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, radius)

        # Compute the angle increment for each slice
        angle_increment = twist_angle / num_slices

        # Create a list to store the loft curves
        loft_curves = []

        for j in range(num_slices + 1):
            # Compute the height of the current slice
            z = j * height / num_slices

            # Compute the rotation angle
            current_angle = j * angle_increment

            # Create a plane for the current slice
            plane = rg.Plane(base_circle.Plane)
            plane.Translate(rg.Vector3d(0, 0, z))
            plane.Rotate(math.radians(current_angle), plane.ZAxis)

            # Create a circle on the current plane and add it to the loft curves
            circle = rg.Circle(plane, radius)
            loft_curves.append(circle.ToNurbsCurve())

        # Create a lofted brep from the curves
        loft_brep = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

        # Add the lofted brep to the list of volumes
        volumes.append(loft_brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_concept(height=5.0, radius=2.0, twist_angle=180.0, num_volumes=10, num_slices=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_concept(height=10.0, radius=3.0, twist_angle=360.0, num_volumes=15, num_slices=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_concept(height=7.0, radius=1.5, twist_angle=90.0, num_volumes=8, num_slices=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_concept(height=6.0, radius=2.5, twist_angle=270.0, num_volumes=12, num_slices=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_concept(height=8.0, radius=4.0, twist_angle=120.0, num_volumes=5, num_slices=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
