# Created for 0012_0003_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volumes_model`, generates an architectural concept model based on the metaphor of "Twisted volumes." It creates a series of cylindrical volumes that exhibit varying degrees of twist and distortion, reflecting dynamic movement and spatial fluidity. By manipulating the twist angle and height of each volume, the model captures a sense of energy and transformation. The function employs iterative geometry creation, lofting twisted circles to form the volumes and ensuring unique spatial relationships. This approach emphasizes the interplay of light and shadow, enhancing visual depth and perspective, thus embodying the metaphor in a coherent architectural form."""

#! python 3
function_code = """def create_twisted_volumes_model(radius, height, twist_angle, num_volumes, seed=42):
    \"""
    Generates a Concept Model of twisted volumetric elements, evoking the 'Twisted volumes' metaphor.
    The model features a series of cylindrical volumes that exhibit varying degrees of twist and distortion,
    emphasizing dynamic movement and spatial fluidity.

    Parameters:
    - radius (float): The base radius of each cylindrical volume in meters.
    - height (float): The height of each cylindrical volume in meters.
    - twist_angle (float): The maximum twist angle in degrees applied across the height of the volume.
    - num_volumes (int): The number of cylindrical volumes to create.
    - seed (int): Optional seed for randomness to ensure replicability.

    Returns:
    - List of RhinoCommon.Geometry.Brep: A list of 3D geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    volumes = []
    for i in range(num_volumes):
        # Create a base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, radius)
        
        # Create a series of planes along the height, each twisted incrementally
        curves = []
        for j in range(10):  # Divide the height into segments
            factor = j / 9.0
            z = factor * height
            angle = factor * math.radians(random.uniform(-twist_angle, twist_angle))
            
            # Create and rotate plane
            plane = rg.Plane.WorldXY
            plane.Translate(rg.Vector3d(0, 0, z))
            plane.Rotate(angle, plane.ZAxis)
            
            # Create circle on the plane
            twisted_circle = rg.Circle(plane, radius)
            curves.append(twisted_circle.ToNurbsCurve())
        
        # Loft the circles to form a twisted volume
        loft_brep = rg.Brep.CreateFromLoft(curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        volumes.append(loft_brep)
        
        # Optionally, translate the volume to avoid overlap
        translation_vector = rg.Vector3d(i * radius * 2.5, 0, 0)
        translation_transform = rg.Transform.Translation(translation_vector)
        loft_brep.Transform(translation_transform)
    
    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(1.0, 5.0, 45.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(0.5, 3.0, 90.0, 8, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(2.0, 4.0, 30.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(1.5, 6.0, 60.0, 12, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(3.0, 8.0, 75.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
