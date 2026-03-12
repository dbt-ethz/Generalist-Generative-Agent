# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The function `create_concept_model` generates an architectural concept model based on the "Box in a cloud" metaphor by creating a solid geometric core (the 'box') and an ethereal, dynamic outer layer (the 'cloud'). The 'box' is defined by its dimensions and constructed using robust materials, while the 'cloud' is formed from randomly positioned spheres that allow for interaction with environmental factors. This design emphasizes the juxtaposition of solidity and fluidity, enabling exploration of spatial transitions. The model captures the metaphor's essence by blending structural integrity with a responsive, changeable outer form, illustrating the interplay between the two elements."""

#! python 3
function_code = """def create_concept_model(box_width, box_depth, box_height, cloud_radius, cloud_resolution, cloud_randomness_seed):
    \"""
    Generates a 3D architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    The model consists of a central 'box' representing a solid, structured core and an 
    encompassing 'cloud' that provides a dynamic, ethereal form. The 'cloud' is designed to 
    interact with environmental factors, suggesting fluidity and adaptability.

    Parameters:
    - box_width (float): The width of the central box in meters.
    - box_depth (float): The depth of the central box in meters.
    - box_height (float): The height of the central box in meters.
    - cloud_radius (float): The approximate radius of the surrounding cloud in meters.
    - cloud_resolution (int): The number of points used to define the cloud's surface.
    - cloud_randomness_seed (int): The seed for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the box and cloud.
    \"""

    import Rhino.Geometry as rg
    import random

    # Create the central 'box' as a Brep
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
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' using a series of spheres around the box
    random.seed(cloud_randomness_seed)
    cloud_spheres = []
    for _ in range(cloud_resolution):
        # Randomly position the spheres around the box
        rand_x = random.uniform(-cloud_radius, box_width + cloud_radius)
        rand_y = random.uniform(-cloud_radius, box_depth + cloud_radius)
        rand_z = random.uniform(-cloud_radius, box_height + cloud_radius)
        radius_variation = random.uniform(0.8, 1.2)
        sphere = rg.Sphere(rg.Point3d(rand_x, rand_y, rand_z), cloud_radius * radius_variation)
        cloud_spheres.append(sphere.ToBrep())

    # Union all spheres to form a cohesive 'cloud'
    cloud_brep = rg.Brep.CreateBooleanUnion(cloud_spheres, 0.01)

    return [box_brep] + list(cloud_brep)"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10.0, 5.0, 3.0, 15.0, 100, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(7.5, 4.0, 2.5, 10.0, 50, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(12.0, 6.0, 4.0, 20.0, 150, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(8.0, 3.0, 2.0, 12.0, 75, 33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(5.0, 5.0, 5.0, 10.0, 200, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
