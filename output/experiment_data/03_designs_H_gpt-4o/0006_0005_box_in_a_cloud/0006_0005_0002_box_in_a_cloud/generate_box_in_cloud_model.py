# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The function `generate_box_in_cloud_model` translates the "Box in a cloud" metaphor into a 3D architectural concept model. It constructs a central solid 'box' using defined dimensions, representing stability and structure. Surrounding this core, the function generates a dynamic 'cloud' layer composed of twisted and undulating surfaces, which evokes fluidity and interaction. By incorporating randomness in the cloud's shape and movement, the model reflects environmental responsiveness. The resulting geometries emphasize the relationship between the defined core and its ethereal envelope, promoting exploration of spatial transitions and the interplay of light and shadow, aligning with the metaphor's essence."""

#! python 3
function_code = """def generate_box_in_cloud_model(box_dimensions, cloud_radius, cloud_layers, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    This function creates a central 'box' as a solid geometric core and surrounds it with a 
    'cloud' layer represented by a series of twisted and undulating surfaces. The 'cloud' 
    interacts with environmental stimuli, such as light or airflow, suggesting a dynamic, adaptable form.

    Parameters:
    - box_dimensions (tuple): A tuple of three floats representing the width, depth, and height of the box in meters.
    - cloud_radius (float): The maximum radius of the outermost cloud layer in meters.
    - cloud_layers (int): The number of twisting layers forming the cloud.
    - seed (int): A seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    
    # Create the 'box'
    box_width, box_depth, box_height = box_dimensions
    box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, box_width), rg.Interval(0, box_depth), rg.Interval(0, box_height))
    box_brep = box.ToBrep()

    # Create the 'cloud' using twisted surfaces
    cloud_geometries = []
    center = rg.Point3d(box_width / 2, box_depth / 2, box_height / 2)
    
    for i in range(cloud_layers):
        # Create a base curve for the twisting surface
        angle_step = 2 * math.pi / 20  # 20 segments
        base_curve_points = []
        
        for j in range(20):
            angle = j * angle_step
            radius_variation = random.uniform(0.8, 1.2)
            x = center.X + cloud_radius * radius_variation * math.cos(angle)
            y = center.Y + cloud_radius * radius_variation * math.sin(angle)
            z = random.uniform(-box_height / 2, box_height / 2)
            base_curve_points.append(rg.Point3d(x, y, z))
        
        base_curve = rg.NurbsCurve.Create(False, 3, base_curve_points)
        
        # Create a twisted surface from the base curve
        twist_angle = random.uniform(0, 2 * math.pi)
        axis = rg.Line(center, rg.Point3d(center.X, center.Y, center.Z + 1))
        twisted_surface = rg.Surface.CreateExtrusion(base_curve, rg.Vector3d(0, 0, box_height))
        twisted_surface.Rotate(twist_angle, rg.Vector3d(0, 0, 1), center)

        cloud_geometries.append(twisted_surface.ToBrep())

    # Return the list of geometries
    return [box_brep] + cloud_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_box_in_cloud_model((5.0, 3.0, 4.0), 2.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_box_in_cloud_model((2.0, 2.0, 2.0), 1.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_box_in_cloud_model((10.0, 5.0, 8.0), 3.0, 5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_box_in_cloud_model((4.0, 4.0, 5.0), 3.0, 8, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_box_in_cloud_model((6.0, 4.0, 3.0), 2.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
