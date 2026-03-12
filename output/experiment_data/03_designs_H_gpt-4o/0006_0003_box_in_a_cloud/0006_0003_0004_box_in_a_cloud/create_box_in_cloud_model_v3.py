# Created for 0006_0003_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the "Box in a Cloud" metaphor by creating a solid geometric core (the "box") and an enveloping, amorphous outer layer (the "cloud"). It constructs the box using defined dimensions and rigid materials, ensuring a sense of stability. Surrounding this core are multiple semi-transparent layers that represent the cloud, each varying in thickness and offset to evoke fluidity and lightness. The function incorporates randomness in angles and offsets to enhance the dynamic quality of the cloud. Ultimately, the model visually contrasts solidity with ethereality, embodying the metaphor's essence."""

#! python 3
function_code = """def create_box_in_cloud_model_v3(box_length=12, box_width=12, box_height=20, cloud_radius=25, cloud_layers=5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Box in a Cloud' metaphor.

    This function generates a concept model where a solid, geometric core ('box') is enveloped by a series of layered,
    semi-transparent surfaces ('cloud'). The box is represented by a Brep and the cloud by concentric, offset
    surfaces, which create a diffuse, dynamic outer form.

    Parameters:
        box_length (float): The length of the box in meters.
        box_width (float): The width of the box in meters.
        box_height (float): The height of the box in meters.
        cloud_radius (float): The maximum radius of the cloud-like envelope.
        cloud_layers (int): The number of semi-transparent layers forming the cloud.
        seed (int, optional): The seed for random number generation to ensure replicable results.

    Returns:
        list: A list of RhinoCommon Breps and Surfaces representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness
    random.seed(seed)

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

    # Create the cloud layers (amorphous envelope)
    cloud_surfaces = []
    for layer in range(cloud_layers):
        offset = (layer + 1) * (cloud_radius / cloud_layers)
        random_angle = random.uniform(0, 2 * math.pi)
        x_offset = offset * math.cos(random_angle)
        y_offset = offset * math.sin(random_angle)

        # Create an elliptical cloud layer
        cloud_ellipse = rg.Ellipse(rg.Plane(rg.Point3d(box_length / 2 + x_offset, box_width / 2 + y_offset, box_height / 2), rg.Vector3d.ZAxis), 
                                   box_length / 2 + offset, box_width / 2 + offset)
        
        cloud_curve = cloud_ellipse.ToNurbsCurve()
        cloud_surface = rg.RevSurface.Create(cloud_curve, rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, 1)))
        cloud_surfaces.append(cloud_surface.ToBrep())

    return [box_brep] + cloud_surfaces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model_v3(box_length=15, box_width=10, box_height=25, cloud_radius=30, cloud_layers=6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model_v3(box_length=10, box_width=10, box_height=15, cloud_radius=20, cloud_layers=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model_v3(box_length=8, box_width=8, box_height=10, cloud_radius=15, cloud_layers=3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model_v3(box_length=20, box_width=15, box_height=30, cloud_radius=40, cloud_layers=8, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model_v3(box_length=14, box_width=14, box_height=22, cloud_radius=35, cloud_layers=7, seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
