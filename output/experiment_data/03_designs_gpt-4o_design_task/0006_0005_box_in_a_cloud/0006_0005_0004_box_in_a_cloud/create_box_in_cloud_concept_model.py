# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the 'Box in a cloud' metaphor by creating a defined geometric 'box' as the central core and surrounding it with multiple concentric 'cloud' layers. The 'box' embodies solidity and structural integrity, while the 'cloud' is represented by spheres with varying radii and random jitter, reflecting dynamic, ethereal qualities. By adjusting the number of layers and their characteristics, the model explores the interaction between the robust core and the fluid outer layer, illustrating the metaphor of integration and spatial transition. The resulting geometries are returned for visualization."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(box_dimensions, cloud_radius, cloud_layer_count, seed):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    This function generates a central 'box' as a solid geometric core and surrounds it with an outer 'cloud' 
    layer that represents a dynamic, interactive space. The 'cloud' is created using a series of concentric 
    layers with varying opacities, suggesting a gradient of experiences and environmental interactions.

    Parameters:
    - box_dimensions (tuple): A tuple of three floats representing the width, depth, and height of the box in meters.
    - cloud_radius (float): The radius of the outermost cloud layer in meters.
    - cloud_layer_count (int): The number of concentric cloud layers.
    - seed (int): A seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Create the 'box'
    box_width, box_depth, box_height = box_dimensions
    box = rg.Box(rg.Plane.WorldXY, rg.Interval(-box_width/2, box_width/2), rg.Interval(-box_depth/2, box_depth/2), rg.Interval(0, box_height))
    box_brep = box.ToBrep()

    # Create the 'cloud'
    cloud_geometries = []
    for i in range(cloud_layer_count):
        layer_radius = cloud_radius * (i + 1) / cloud_layer_count
        jitter = random.uniform(-0.2, 0.2)  # Add some randomness to the cloud shape
        sphere = rg.Sphere(rg.Point3d(0, 0, box_height / 2 + jitter), layer_radius)
        cloud_brep = sphere.ToBrep()
        cloud_geometries.append(cloud_brep)

    # Combine all geometries
    concept_model = [box_brep] + cloud_geometries

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((2.0, 3.0, 4.0), 5.0, 10, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((1.5, 2.5, 3.5), 4.0, 8, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((3.0, 4.0, 5.0), 6.0, 12, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((2.5, 3.5, 4.5), 7.0, 15, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((1.0, 1.0, 1.0), 3.0, 5, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
