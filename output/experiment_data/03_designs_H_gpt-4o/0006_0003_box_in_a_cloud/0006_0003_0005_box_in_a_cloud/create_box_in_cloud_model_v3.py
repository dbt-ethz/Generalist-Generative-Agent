# Created for 0006_0003_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model_v3` generates an architectural concept model based on the "Box in a Cloud" metaphor by constructing a solid geometric core (the "box") and enveloping it with a fluid, translucent outer layer (the "cloud"). It creates the box using defined dimensions and robust materials, ensuring a sense of stability. The cloud is formed through multiple layered extrusions, using varying offsets to achieve a dynamic, wavy appearance that suggests lightness and movement. This interplay between the rigid box and soft cloud highlights contrasts in solidity and ethereality, inviting exploration of spatial transitions and interactions."""

#! python 3
function_code = """def create_box_in_cloud_model_v3(box_length=10, box_width=10, box_height=15, cloud_thickness=5, cloud_segments=30):
    \"""
    Creates an architectural Concept Model embodying the 'Box in a Cloud' metaphor.

    This version of the function constructs a central solid box and surrounds it with an amorphous 'cloud'
    composed of a series of translucent layers that create a dynamic, diffuse envelope.

    Parameters:
        box_length (float): The length of the box in meters.
        box_width (float): The width of the box in meters.
        box_height (float): The height of the box in meters.
        cloud_thickness (float): The thickness of the cloud-like envelope.
        cloud_segments (int): The number of segments to form the cloud layers.

    Returns:
        list: A list of RhinoCommon Breps and Surfaces representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness
    random.seed(42)

    # Create the box (core structure)
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

    # Create the cloud (amorphous envelope)
    cloud_layers = []
    for i in range(cloud_segments):
        # Calculate a variable offset for each layer, creating a wavy cloud effect
        angle_offset = (2 * math.pi / cloud_segments) * i
        layer_points = []
        for j in range(cloud_segments):
            angle = (2 * math.pi / cloud_segments) * j + angle_offset
            radius = (box_length + box_width) / 4 + cloud_thickness * (0.5 + 0.5 * math.sin(angle * 3))
            x = math.cos(angle) * radius
            y = math.sin(angle) * radius
            z = random.uniform(0, box_height)
            layer_points.append(rg.Point3d(x + box_length / 2, y + box_width / 2, z))

        # Create closed polyline and extrude to form a cloud layer
        polyline = rg.Polyline(layer_points + [layer_points[0]])
        cloud_curve = polyline.ToNurbsCurve()
        extrusion_direction = rg.Vector3d(0, 0, cloud_thickness / cloud_segments)
        cloud_surface = rg.Surface.CreateExtrusion(cloud_curve, extrusion_direction)
        cloud_layers.append(cloud_surface)

    return [box_brep] + cloud_layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model_v3(box_length=12, box_width=8, box_height=10, cloud_thickness=6, cloud_segments=40)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model_v3(box_length=15, box_width=15, box_height=20, cloud_thickness=4, cloud_segments=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model_v3(box_length=5, box_width=10, box_height=12, cloud_thickness=3, cloud_segments=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model_v3(box_length=20, box_width=10, box_height=15, cloud_thickness=7, cloud_segments=35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model_v3(box_length=10, box_width=15, box_height=18, cloud_thickness=8, cloud_segments=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
