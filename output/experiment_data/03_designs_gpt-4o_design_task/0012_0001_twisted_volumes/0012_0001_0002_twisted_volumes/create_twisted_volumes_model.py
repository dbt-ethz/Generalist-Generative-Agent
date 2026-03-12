# Created for 0012_0001_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates a series of interlocking geometric forms that are dynamically twisted and distorted to embody movement and transformation. By applying varying twist angles, the function explores innovative spatial relationships and circulation paths, enhancing interaction between interior and exterior spaces. The model emphasizes light and shadow interplay, as the twisted shapes capture and reflect light differently. This approach results in a visually striking silhouette that conveys energy and fluidity, aligning with the metaphor's core traits."""

#! python 3
function_code = """def create_twisted_volumes_model(base_dimensions, primary_twist_angle, secondary_twist_angle, twist_variation, num_volumes):
    \"""
    Creates a conceptual architectural model based on the metaphor of 'Twisted volumes'.
    
    This function generates a series of interlocking geometric forms that are rotated and
    distorted to embody dynamic and fluid architectural forms. The volumes are designed
    to explore different spatial relationships and the interplay of light and shadow.

    Parameters:
    - base_dimensions: A tuple of floats (width, depth, height) representing the base dimensions of each volume.
    - primary_twist_angle: A float representing the primary twist angle in degrees applied to each volume.
    - secondary_twist_angle: A float representing the secondary twist angle in degrees for additional distortion.
    - twist_variation: A float representing the degree of variation in the twist angles between volumes.
    - num_volumes: An integer specifying the number of volumes to generate.

    Returns:
    - A list of 3D geometries (breps) representing the twisted volumes.

    \"""
    import Rhino.Geometry as rg
    import math
    import random
    random.seed(42)

    width, depth, height = base_dimensions
    geometries = []

    for i in range(num_volumes):
        # Create a base box
        base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height)).ToBrep()
        
        # Calculate twist angles with some variation
        current_primary_twist = primary_twist_angle + random.uniform(-twist_variation, twist_variation)
        current_secondary_twist = secondary_twist_angle + random.uniform(-twist_variation, twist_variation)
        
        # Create twisting transformations
        primary_twist = rg.Transform.Rotation(math.radians(current_primary_twist), rg.Vector3d.ZAxis, rg.Point3d(0, 0, height / 2))
        secondary_twist = rg.Transform.Rotation(math.radians(current_secondary_twist), rg.Vector3d.YAxis, rg.Point3d(width / 2, 0, height / 2))
        
        # Apply transformations
        twisted_box = base_box.DuplicateBrep()
        twisted_box.Transform(primary_twist)
        twisted_box.Transform(secondary_twist)
        
        # Offset and move the volume to create interlocking forms
        translation_vector = rg.Vector3d(i * width * 0.5, i * depth * 0.5, 0)
        translation = rg.Transform.Translation(translation_vector)
        twisted_box.Transform(translation)
        
        geometries.append(twisted_box)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model((2.0, 1.0, 3.0), 45, 30, 10, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model((1.5, 2.0, 4.0), 60, 15, 5, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model((3.0, 2.0, 5.0), 90, 45, 15, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model((4.0, 3.0, 2.0), 30, 60, 20, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model((2.5, 2.5, 2.5), 75, 20, 8, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
