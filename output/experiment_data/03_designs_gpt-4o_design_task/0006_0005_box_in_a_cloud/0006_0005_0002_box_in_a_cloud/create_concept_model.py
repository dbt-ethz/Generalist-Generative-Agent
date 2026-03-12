# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Box in a cloud" metaphor. It creates a solid geometric 'box' as a central core, symbolizing stability, using specified dimensions. Surrounding this core, the function generates a dynamic 'cloud' layer composed of randomly placed spheres, representing ethereality and interactivity. The spheres vary in size and position, emphasizing the contrast between the defined structure and the fluidity of the cloud. By combining these elements, the model explores the relationship between solidity and lightness, promoting spatial exploration and adaptability, while visually illustrating the metaphor's essence."""

#! python 3
function_code = """def create_concept_model(box_length, box_width, box_height, cloud_radius, cloud_resolution):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    This function generates a central 'box' structure surrounded by an interactive 'cloud' layer.
    The 'box' represents a solid core, while the 'cloud' represents a dynamic, amorphous envelope.

    Inputs:
    - box_length: Length of the box in meters.
    - box_width: Width of the box in meters.
    - box_height: Height of the box in meters.
    - cloud_radius: The radius of the 'cloud' layer surrounding the box.
    - cloud_resolution: The level of detail in the cloud geometry.

    Outputs:
    - A list of 3D geometries (breps or meshes) representing the Concept Model.

    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(42)

    # Create the 'box' as a simple brep
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_length, 0, 0),
        rg.Point3d(box_length, box_width, 0),
        rg.Point3d(0, box_width, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_length, 0, box_height),
        rg.Point3d(box_length, box_width, box_height),
        rg.Point3d(0, box_width, box_height)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' using a series of random spheres
    cloud_geometries = []
    for _ in range(cloud_resolution):
        # Randomly place spheres around the box
        x = random.uniform(-cloud_radius, box_length + cloud_radius)
        y = random.uniform(-cloud_radius, box_width + cloud_radius)
        z = random.uniform(-cloud_radius, box_height + cloud_radius)
        center = rg.Point3d(x, y, z)

        # Randomize the radius of the spheres
        sphere_radius = random.uniform(cloud_radius * 0.1, cloud_radius * 0.3)

        sphere = rg.Sphere(center, sphere_radius)
        cloud_geometries.append(sphere.ToBrep())

    # Combine all geometries into a single list
    concept_model_geometries = [box_brep] + cloud_geometries

    return concept_model_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10, 5, 3, 15, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(8, 4, 2, 10, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(12, 6, 4, 20, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(15, 7, 5, 12, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(9, 3, 2, 8, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
