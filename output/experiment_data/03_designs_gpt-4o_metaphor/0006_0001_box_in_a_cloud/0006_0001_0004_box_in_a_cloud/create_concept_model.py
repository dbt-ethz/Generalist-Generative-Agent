# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Box in a Cloud." It creates a solid geometric box, representing structure and stability, and a collection of spheres that emulate a cloud, symbolizing ethereality and fluidity. The box dimensions and position are defined by the user, while the cloud's density and radius determine its amorphous quality. By incorporating randomness in the sphere placements and sizes, the model emphasizes the contrast between the box's defined boundaries and the cloud's blurred edges. This interplay invites exploration of spatial layers, reflecting the metaphor's key traits."""

#! python 3
function_code = """def create_concept_model(box_size, cloud_radius, box_position=(0, 0, 0), cloud_density=10, randomness_seed=42):
    \"""
    Creates an architectural Concept Model representing a "Box in a Cloud" metaphor.
    
    Parameters:
    - box_size: Tuple of three floats representing the width, depth, and height of the box in meters.
    - cloud_radius: Float representing the radius of the spherical cloud in meters.
    - box_position: Tuple of three floats for the (x, y, z) position of the box's bottom-left corner.
    - cloud_density: Integer representing the number of spheres used to create the cloud.
    - randomness_seed: Integer seed for random number generation to ensure replicable results.
    
    Returns:
    - List of 3D geometries: A list containing the BREP for the box and the spheres for the cloud.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(randomness_seed)
    
    # Create the box (solid, structured element)
    box_corners = [rg.Point3d(box_position[0], box_position[1], box_position[2]),
                   rg.Point3d(box_position[0] + box_size[0], box_position[1], box_position[2]),
                   rg.Point3d(box_position[0] + box_size[0], box_position[1] + box_size[1], box_position[2]),
                   rg.Point3d(box_position[0], box_position[1] + box_size[1], box_position[2]),
                   rg.Point3d(box_position[0], box_position[1], box_position[2] + box_size[2]),
                   rg.Point3d(box_position[0] + box_size[0], box_position[1], box_position[2] + box_size[2]),
                   rg.Point3d(box_position[0] + box_size[0], box_position[1] + box_size[1], box_position[2] + box_size[2]),
                   rg.Point3d(box_position[0], box_position[1] + box_size[1], box_position[2] + box_size[2])]
    
    box_brep = rg.Brep.CreateFromBox(box_corners)
    
    # Create the cloud (ethereal, amorphous element)
    cloud_center = rg.Point3d(box_position[0] + box_size[0] / 2,
                              box_position[1] + box_size[1] / 2,
                              box_position[2] + box_size[2] / 2)
    
    cloud_spheres = []
    for _ in range(cloud_density):
        # Randomly position spheres around the cloud center within the cloud radius
        random_x = cloud_center.X + random.uniform(-cloud_radius, cloud_radius)
        random_y = cloud_center.Y + random.uniform(-cloud_radius, cloud_radius)
        random_z = cloud_center.Z + random.uniform(-cloud_radius, cloud_radius)
        
        random_position = rg.Point3d(random_x, random_y, random_z)
        sphere_radius = random.uniform(0.2, cloud_radius / 4)
        
        sphere = rg.Sphere(random_position, sphere_radius)
        sphere_brep = rg.Brep.CreateFromSphere(sphere)
        cloud_spheres.append(sphere_brep)
    
    # Compile result list
    result_geometries = [box_brep] + cloud_spheres
    
    return result_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(box_size=(2.0, 2.0, 2.0), cloud_radius=5.0, box_position=(1.0, 1.0, 1.0), cloud_density=20, randomness_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(box_size=(3.0, 3.0, 3.0), cloud_radius=7.0, box_position=(0.0, 0.0, 0.0), cloud_density=15, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(box_size=(1.5, 1.5, 1.5), cloud_radius=4.0, box_position=(2.0, 2.0, 2.0), cloud_density=25, randomness_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(box_size=(4.0, 4.0, 4.0), cloud_radius=6.0, box_position=(3.0, 3.0, 3.0), cloud_density=30, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(box_size=(2.5, 2.5, 2.5), cloud_radius=8.0, box_position=(5.0, 5.0, 5.0), cloud_density=12, randomness_seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
