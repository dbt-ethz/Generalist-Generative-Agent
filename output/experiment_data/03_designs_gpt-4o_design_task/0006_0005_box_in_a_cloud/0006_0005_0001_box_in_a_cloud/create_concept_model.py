# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The provided function, `create_concept_model`, generates an architectural concept model based on the "Box in a cloud" metaphor. It constructs a solid, geometric "box" as the central core using defined dimensions, emphasizing structural integrity. Surrounding this core, it creates a dynamic "cloud" layer composed of randomly positioned spheres that symbolize the ethereal, interactive outer space. The number and size of these spheres are influenced by parameters such as cloud density and radius, capturing the metaphor's essence of solidity versus fluidity. The model reflects a harmonious relationship between the stable core and the adaptable outer layer, facilitating exploration of spatial transitions."""

#! python 3
function_code = """def create_concept_model(box_size, cloud_radius, cloud_density, random_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    Parameters:
    - box_size: A tuple of three floats (length, width, height) representing the size of the central box in meters.
    - cloud_radius: A float representing the radius of the cloud sphere around the box in meters.
    - cloud_density: An integer representing the number of cloud elements surrounding the box.
    - random_seed: An integer seed for the random number generator to ensure replicability.
    
    Returns:
    - A list of 3D geometries (breps, surfaces, or meshes) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Create the box (central core)
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_size[0], 0, 0),
        rg.Point3d(box_size[0], box_size[1], 0),
        rg.Point3d(0, box_size[1], 0),
        rg.Point3d(0, 0, box_size[2]),
        rg.Point3d(box_size[0], 0, box_size[2]),
        rg.Point3d(box_size[0], box_size[1], box_size[2]),
        rg.Point3d(0, box_size[1], box_size[2])
    ]
    box = rg.Brep.CreateFromBox(box_corners)
    
    # Create the cloud (dynamic outer layer)
    cloud_elements = []
    for _ in range(cloud_density):
        # Random position around the box
        position = rg.Point3d(
            random.uniform(-cloud_radius, box_size[0] + cloud_radius),
            random.uniform(-cloud_radius, box_size[1] + cloud_radius),
            random.uniform(-cloud_radius, box_size[2] + cloud_radius)
        )
        # Create a sphere to represent a part of the cloud
        sphere = rg.Sphere(position, random.uniform(0.1, 0.5))
        cloud_elements.append(sphere.ToBrep())
    
    # Return the list of 3D geometries
    return [box] + cloud_elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model((5.0, 3.0, 2.0), 10.0, 50, random_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model((4.0, 4.0, 4.0), 8.0, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model((6.0, 2.0, 3.0), 12.0, 100, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model((3.0, 5.0, 1.0), 15.0, 75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model((2.0, 2.0, 2.0), 5.0, 20, random_seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
