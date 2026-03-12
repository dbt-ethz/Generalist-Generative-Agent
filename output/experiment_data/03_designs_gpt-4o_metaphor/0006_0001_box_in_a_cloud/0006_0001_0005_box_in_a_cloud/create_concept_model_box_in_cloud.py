# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_concept_model_box_in_cloud` generates an architectural concept model based on the metaphor "Box in a cloud" by creating a solid cubic box to represent the "box" and surrounding it with randomly positioned spheres to symbolize the "cloud." This design captures the contrast between the defined, structured box and the diffuse, ethereal cloud, emphasizing the interplay of solidity and lightness. By adjusting parameters like box size, cloud density, and sphere sizes, the model invites exploration of spatial dynamics, encapsulating the metaphors essence through tangible geometric representations that reflect both stability and transience."""

#! python 3
function_code = """def create_concept_model_box_in_cloud(box_size, cloud_radius, cloud_density, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    This function generates a solid cubic form representing the 'box' and surrounds it 
    with a collection of small spheres representing the 'cloud'. The contrast between 
    the structured box and the diffuse cloud aims to explore the interplay between 
    solidity and ethereality.
    
    Parameters:
    box_size (float): The edge length of the cubic box in meters.
    cloud_radius (float): The radius of the volume within which cloud spheres are distributed.
    cloud_density (int): The number of spheres in the cloud.
    seed (int, optional): A seed for the random number generator to ensure replicability. Default is 42.
    
    Returns:
    list: A list of RhinoCommon Brep objects representing the box and cloud spheres.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)
    
    geometries = []
    
    # Create the box (solid)
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_size, 0, 0),
        rg.Point3d(box_size, box_size, 0),
        rg.Point3d(0, box_size, 0),
        rg.Point3d(0, 0, box_size),
        rg.Point3d(box_size, 0, box_size),
        rg.Point3d(box_size, box_size, box_size),
        rg.Point3d(0, box_size, box_size)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)
    geometries.append(box_brep)
    
    # Create the cloud (voids)
    for _ in range(cloud_density):
        # Random position around the box within the cloud radius
        x = random.uniform(-cloud_radius, cloud_radius)
        y = random.uniform(-cloud_radius, cloud_radius)
        z = random.uniform(-cloud_radius, cloud_radius)
        # Ensure cloud is not interfering with the box
        if x > box_size or x < 0 or y > box_size or y < 0 or z > box_size or z < 0:
            center = rg.Point3d(x, y, z)
            sphere_radius = random.uniform(0.1, 0.3)  # Small, random spheres
            sphere = rg.Sphere(center, sphere_radius)
            sphere_brep = sphere.ToBrep()
            geometries.append(sphere_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_box_in_cloud(5.0, 10.0, 50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_box_in_cloud(3.0, 8.0, 30, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_box_in_cloud(4.0, 12.0, 40, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_box_in_cloud(6.0, 15.0, 60, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_box_in_cloud(2.5, 5.0, 20, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
