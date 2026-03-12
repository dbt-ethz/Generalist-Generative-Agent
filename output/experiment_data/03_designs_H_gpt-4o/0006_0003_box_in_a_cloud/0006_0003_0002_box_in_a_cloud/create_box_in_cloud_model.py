# Created for 0006_0003_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model` generates an architectural concept model based on the "Box in a Cloud" metaphor, which contrasts solidity with ethereality. It constructs a central geometric form, or "box," using robust materials to convey permanence. Surrounding this core, it creates multiple translucent "cloud" layers that suggest fluidity and lightness, using random points on a sphere to form amorphous surfaces. This interplay of heavy and soft elements enhances spatial depth, while the strategic use of light and shadow emphasizes the contrast between the defined box and the diffuse cloud, embodying the metaphor's themes of stability and transition."""

#! python 3
function_code = """def create_box_in_cloud_model(box_size=(10, 10, 15), cloud_radius=20, cloud_layer_count=5, seed=42):
    \"""
    Create an architectural Concept Model embodying the 'Box in a Cloud' metaphor.

    This function generates a model where a solid, geometric core ('box') is surrounded by
    a fluid, dynamic outer form ('cloud'). The box is represented as a Brep, while the cloud
    is made of several translucent layers formed by surfaces with varying thickness and shape.

    Parameters:
        box_size (tuple): A tuple (length, width, height) representing the dimensions of the central box.
        cloud_radius (float): The radius within which the cloud layers are generated around the box.
        cloud_layer_count (int): The number of cloud layers to generate.
        seed (int, optional): The seed for random number generation to ensure replicable results. Default is 42.

    Returns:
        list: A list of RhinoCommon Breps and Surfaces representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the central box as a Brep
    box_length, box_width, box_height = box_size
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

    # Create the cloud layers as amorphous surfaces
    cloud_layers = []
    for i in range(cloud_layer_count):
        # Generate random points on a sphere to create each cloud layer
        layer_points = []
        for _ in range(20):  # 20 points per layer
            theta = random.uniform(0, 2 * math.pi)
            phi = random.uniform(0, math.pi)
            x = cloud_radius * random.uniform(0.8, 1) * math.cos(theta) * math.sin(phi)
            y = cloud_radius * random.uniform(0.8, 1) * math.sin(theta) * math.sin(phi)
            z = cloud_radius * random.uniform(0.8, 1) * math.cos(phi)
            point = rg.Point3d(x + box_length / 2, y + box_width / 2, z + box_height / 2)
            layer_points.append(point)

        # Create a closed polyline to form a cloud layer
        if len(layer_points) > 2:
            polyline = rg.Polyline(layer_points)
            polyline.Add(polyline[0])  # Close the polyline
            cloud_surface = rg.NurbsSurface.CreateFromPoints(layer_points, 4, 5, 3, 3)
            cloud_layers.append(cloud_surface)

    return [box_brep] + cloud_layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model(box_size=(12, 12, 18), cloud_radius=25, cloud_layer_count=7, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model(box_size=(8, 8, 10), cloud_radius=15, cloud_layer_count=4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model(box_size=(15, 10, 20), cloud_radius=30, cloud_layer_count=6, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model(box_size=(5, 5, 10), cloud_radius=18, cloud_layer_count=3, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model(box_size=(20, 15, 25), cloud_radius=40, cloud_layer_count=8, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
