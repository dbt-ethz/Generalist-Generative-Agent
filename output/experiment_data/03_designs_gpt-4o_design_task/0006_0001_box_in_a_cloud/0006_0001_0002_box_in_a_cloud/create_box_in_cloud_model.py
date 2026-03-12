# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model` generates an architectural concept model based on the "Box in a Cloud" metaphor by creating a solid geometric core, referred to as the "box," and surrounding it with a lighter, ethereal "cloud" of elements. The model starts by defining the dimensions of the box using specified parameters, constructing a defined central volume that symbolizes structural stability. Next, it generates multiple random cloud elements around the box, utilizing lighter materials (like spheres) to represent the diffuse envelope. This design emphasizes the contrast between the solidity of the box and the fluidity of the cloud, creating a spatial dialogue that embodies the metaphor effectively."""

#! python 3
function_code = """def create_box_in_cloud_model(box_length, box_width, box_height, cloud_radius, cloud_density):
    \"""
    Creates a conceptual architectural model following the "Box in a Cloud" metaphor.
    
    The model comprises a central, solid 'box' representing the primary programmatic space,
    surrounded by a 'cloud' of lighter, more diffuse elements. This design emphasizes the 
    contrast between structured solidity and ephemeral lightness. The 'cloud' is realized 
    through a series of perforated or translucent elements that envelop the 'box'.

    Parameters:
    - box_length (float): The length of the central box in meters.
    - box_width (float): The width of the central box in meters.
    - box_height (float): The height of the central box in meters.
    - cloud_radius (float): The radius of the cloud envelope around the box in meters.
    - cloud_density (int): The number of elements used to create the cloud.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries 
      of the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for reproducibility
    random.seed(42)

    # Create the central box
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

    # Create the cloud
    cloud_elements = []
    for _ in range(cloud_density):
        # Generate random position around the box
        random_angle = random.uniform(0, 2 * math.pi)
        random_distance = random.uniform(box_length / 2, cloud_radius)
        random_height = random.uniform(0, box_height)

        # Calculate position for cloud element
        x = box_length / 2 + random_distance * math.cos(random_angle)
        y = box_width / 2 + random_distance * math.sin(random_angle)
        position = rg.Point3d(x, y, random_height)

        # Create a cloud element
        cloud_element = rg.Sphere(position, random.uniform(0.5, 1.5))
        cloud_brep = rg.Brep.CreateFromSphere(cloud_element)
        cloud_elements.append(cloud_brep)

    # Combine all elements into the final model
    model_elements = [box_brep] + cloud_elements

    return model_elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model(10.0, 5.0, 3.0, 15.0, 50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model(8.0, 4.0, 2.5, 12.0, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model(12.0, 6.0, 4.0, 20.0, 40)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model(15.0, 7.0, 5.0, 25.0, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model(9.0, 4.5, 3.5, 14.0, 45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
