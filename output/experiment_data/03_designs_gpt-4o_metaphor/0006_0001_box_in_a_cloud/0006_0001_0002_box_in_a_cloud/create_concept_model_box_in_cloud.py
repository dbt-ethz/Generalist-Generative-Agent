# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_concept_model_box_in_cloud` translates the metaphor "Box in a cloud" into an architectural model by generating a solid geometric box surrounded by a diffuse cloud structure. It emphasizes the contrast between the box's rigidity and the cloud's ethereality through the creation of a defined form and randomly distributed spheres representing the cloud. The function takes parameters for the box's dimensions and cloud characteristics, allowing for exploration of spatial relationships between structured and amorphous elements. This interplay reflects the metaphor's themes of solidity versus fluidity, inviting further exploration of architectural layering and transitions."""

#! python 3
function_code = """def create_concept_model_box_in_cloud(box_dimensions, cloud_radius, cloud_density, seed=42):
    \"""
    Creates a conceptual architectural model based on the metaphor 'Box in a cloud'.
    
    This function generates a defined, geometric form (box) enveloped by a more diffuse, dynamic presence (cloud).
    The design explores the interplay between robust, structured elements and lighter, more amorphous features, 
    emphasizing contrast between opacity and translucency, weight and lightness, defined boundaries and blurred edges.
    
    Parameters:
    - box_dimensions (tuple): A tuple of three floats defining the width, depth, and height of the box in meters.
    - cloud_radius (float): The radius of the spherical cloud surrounding the box.
    - cloud_density (int): The number of points used to generate the cloud, affecting its density.
    - seed (int): Seed for the random number generator to ensure replicable results.
    
    Returns:
    - List of RhinoCommon Brep objects: A list containing the Brep representation of the box and the cloud.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Unpack box dimensions
    box_width, box_depth, box_height = box_dimensions
    
    # Create the box geometry
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
    box = rg.Brep.CreateFromBox(box_corners)
    
    # Set random seed for consistency
    random.seed(seed)
    
    # Create the cloud geometry as a collection of small spheres
    cloud_spheres = []
    for _ in range(cloud_density):
        # Random point generation within a sphere
        u = random.uniform(0, 1)
        v = random.uniform(0, 1)
        theta = u * 2.0 * math.pi
        phi = v * math.pi
        r = cloud_radius * (random.uniform(0.5, 1.0))
        
        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)
        
        point = rg.Point3d(x, y, z)
        
        # Create a small sphere at each random point
        sphere = rg.Sphere(point, cloud_radius * 0.1).ToBrep()
        cloud_spheres.append(sphere)
    
    # Return the box and cloud as a list of Breps
    return [box] + cloud_spheres"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_box_in_cloud((5.0, 3.0, 4.0), 10.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_box_in_cloud((2.0, 2.0, 2.0), 5.0, 50, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_box_in_cloud((6.0, 4.0, 3.0), 12.0, 200, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_box_in_cloud((4.0, 5.0, 2.0), 8.0, 75, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_box_in_cloud((3.0, 3.0, 3.0), 7.0, 150, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
