# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Box in a cloud" by creating a solid geometric box encompassed by a diffuse cloud structure. It accepts parameters defining the box's dimensions, the cloud's size and density, and the number of layers, emphasizing the contrast between the box's defined edges and the cloud's amorphous presence. By utilizing randomness, the function generates cloud points that create a dynamic, ethereal atmosphere around the robust box, effectively exploring spatial relationships and transitions between solidity and lightness, thus embodying the metaphor's essence in the resulting architectural model."""

#! python 3
function_code = """def create_concept_model(box_size, cloud_radius, cloud_density, cloud_layers, randomness_seed=42):
    \"""
    Create a Concept Model based on the metaphor 'Box in a cloud'.
    
    This function generates a defined, geometric box form enveloped by a more diffuse, 
    dynamic presence represented by a cloud-like structure. The design explores the interplay 
    between the robust structure of the box and the lighter, amorphous features of the cloud.

    Parameters:
    - box_size: tuple of three floats (width, depth, height) representing the size of the box in meters.
    - cloud_radius: float, the radius of the spherical volume representing the 'cloud' around the box.
    - cloud_density: int, the number of points making up the cloud.
    - cloud_layers: int, the number of layers in the cloud structure.
    - randomness_seed: int, seed for randomness to ensure reproducibility.

    Returns:
    - List of 3D geometries (breps and points) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Set the random seed
    random.seed(randomness_seed)
    
    # Create the box
    box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, box_size[0]), rg.Interval(0, box_size[1]), rg.Interval(0, box_size[2]))
    box_brep = box.ToBrep()
    
    # Create the cloud
    cloud_points = []
    for layer in range(cloud_layers):
        layer_radius = cloud_radius * (1 - (layer / cloud_layers))
        for _ in range(cloud_density):
            # Random point in spherical coordinates
            theta = random.uniform(0, 2 * 3.14159)
            phi = random.uniform(0, 3.14159)
            r = random.uniform(layer_radius * 0.8, layer_radius)
            
            x = r * math.sin(phi) * math.cos(theta)
            y = r * math.sin(phi) * math.sin(theta)
            z = r * math.cos(phi)
            
            point = rg.Point3d(x, y, z)
            cloud_points.append(point)
    
    # Return the geometries
    return [box_brep] + cloud_points"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model((5.0, 3.0, 2.0), 10.0, 100, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model((2.0, 2.0, 2.0), 5.0, 50, 3, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model((4.0, 4.0, 4.0), 8.0, 80, 4, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model((6.0, 4.0, 3.0), 12.0, 120, 6, randomness_seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model((3.0, 5.0, 1.0), 7.0, 60, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
