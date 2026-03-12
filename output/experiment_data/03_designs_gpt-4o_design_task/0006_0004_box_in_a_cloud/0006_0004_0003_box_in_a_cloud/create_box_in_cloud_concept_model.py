# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the "Box in a cloud" metaphor by creating a defined core structure and enveloping it with a dynamic outer layer. The core, represented as a geometric box, is constructed using specified dimensions, symbolizing stability and permanence. Surrounding this core, the function creates multiple random cloud layers in the form of varied spheres, reflecting fluidity and lightness. This juxtaposition allows for interaction between the solid core and the ethereal cloud, visually emphasizing the contrast between defined boundaries and soft, diffuse outlines. The model highlights spatial transitions and dynamic interplay."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(core_size, cloud_layers, cloud_radius, seed=42):
    \"""
    Creates an architectural Concept Model representing the 'Box in a cloud' metaphor.
    
    Parameters:
    - core_size (tuple): Dimensions of the core 'box' as (width, depth, height) in meters.
    - cloud_layers (int): Number of layers for the 'cloud'.
    - cloud_radius (float): Maximum radius of the 'cloud' layer in meters.
    - seed (int, optional): Random seed for reproducibility. Default is 42.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Create the core 'box'
    box_width, box_depth, box_height = core_size
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_width, 0, 0),
        rg.Point3d(box_width, box_depth, 0),
        rg.Point3d(0, box_depth, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_width, 0, box_height),
        rg.Point3d(box_width, box_depth, box_height),
        rg.Point3d(0, box_depth, box_height)
    ]
    core_box = rg.Brep.CreateFromBox(box_corners)
    
    # Create the 'cloud' layers
    cloud_breps = []
    for i in range(cloud_layers):
        # Randomize the position for a dynamic feel
        offset_x = random.uniform(-cloud_radius, cloud_radius)
        offset_y = random.uniform(-cloud_radius, cloud_radius)
        offset_z = random.uniform(-cloud_radius, cloud_radius / 2.0)
        
        # Create a sphere as a base for the cloud layer
        sphere_center = rg.Point3d(box_width / 2 + offset_x, box_depth / 2 + offset_y, box_height / 2 + offset_z)
        sphere_radius = cloud_radius * (0.8 + 0.4 * random.random())  # Vary the size slightly for dynamism
        sphere = rg.Sphere(sphere_center, sphere_radius)
        
        # Convert sphere to a Brep and add to the list
        cloud_breps.append(sphere.ToBrep())
    
    # Return the combined geometry list
    return [core_box] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((3, 2, 1), 5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((5, 3, 2), 7, 6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((4, 4, 2), 6, 5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((2, 2, 2), 4, 3, seed=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((6, 4, 3), 8, 7, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
