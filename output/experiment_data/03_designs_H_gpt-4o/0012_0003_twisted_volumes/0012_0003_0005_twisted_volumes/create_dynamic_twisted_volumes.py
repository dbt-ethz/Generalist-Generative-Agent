# Created for 0012_0003_twisted_volumes.json

""" Summary:
The function `create_dynamic_twisted_volumes` generates an architectural concept model that embodies the metaphor of "Twisted volumes" by creating a series of interconnected volumetric elements. Each volume exhibits varying degrees of twist and distortion, achieved through a parameterized approach that adjusts twisting angles based on a sine function. This manipulation of form results in dynamic shapes that evoke energy and movement, enhancing spatial relationships and creating unexpected adjacencies. The model also emphasizes light and shadow play through its twisted surfaces, ensuring a visually engaging experience that reflects the metaphor's themes of transformation and interaction between spaces."""

#! python 3
function_code = """def create_dynamic_twisted_volumes(base_length, base_width, height, num_volumes, twist_factor, seed=42):
    \"""
    Generates a series of interconnected volumetric elements that embody twisting and distortion, 
    evoking the 'Twisted volumes' metaphor in an architectural concept model.

    Parameters:
    - base_length (float): The base length of each volume in meters.
    - base_width (float): The base width of each volume in meters.
    - height (float): The height of each volume in meters.
    - num_volumes (int): The number of volumetric elements to create.
    - twist_factor (float): A scaling factor for the twist intensity, influencing the overall distortion.
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

    for i in range(num_volumes):
        # Create a base rectangle for the volume
        base_rect = rg.Rectangle3d(base_plane, base_length, base_width)
        base_curve = base_rect.ToNurbsCurve()

        # Define height and twist parameters
        volume_height = height
        twist_angle = twist_factor * (i + 1) * 10  # increasing twist with each volume

        # Generate a dynamic twist axis using a sine function for curvature
        twist_axis = rg.Line(base_plane.Origin, rg.Point3d(0, 0, volume_height))
        sinusoidal_twist = math.sin(math.radians(twist_angle)) * twist_factor

        # Create top plane with twist and rotation
        top_plane = base_plane.Clone()
        top_plane.Translate(rg.Vector3d(0, 0, volume_height))
        top_plane.Rotate(sinusoidal_twist, top_plane.ZAxis)

        # Create the top rectangle and loft to create the twisted volume
        top_rect = rg.Rectangle3d(top_plane, base_length, base_width).ToNurbsCurve()
        loft_brep = rg.Brep.CreateFromLoft([base_curve, top_rect], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        
        volumes.append(loft_brep)

        # Move the base plane up for the next volume
        base_plane.Translate(rg.Vector3d(0, 0, volume_height))
    
    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_twisted_volumes(5.0, 3.0, 10.0, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_twisted_volumes(4.0, 2.0, 8.0, 5, 2.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_twisted_volumes(6.0, 4.0, 12.0, 3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_twisted_volumes(7.0, 5.0, 15.0, 6, 1.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_twisted_volumes(3.0, 2.5, 9.0, 7, 1.2, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
