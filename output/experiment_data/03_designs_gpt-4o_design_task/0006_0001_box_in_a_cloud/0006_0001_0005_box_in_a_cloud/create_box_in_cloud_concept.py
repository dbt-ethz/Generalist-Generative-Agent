# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_concept` generates an architectural concept model based on the "Box in a cloud" metaphor by creating a central geometric "box" and surrounding it with a lighter, ethereal "cloud." It establishes the box using defined dimensions and solid materials, symbolizing stability. The cloud layer is created with a perturbation effect, adding randomness to its shape, representing lightness and movement. This juxtaposition emphasizes the contrast between the solid core and the fluid envelope, facilitating a spatial dialogue. The model's design explores transitions and interactions between these two elements, enhancing the thematic concept of solidity versus ethereality."""

#! python 3
function_code = """def create_box_in_cloud_concept(width, depth, height, cloud_layer_thickness, cloud_perturbation, seed=None):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    Parameters:
    - width (float): The width of the central 'box' in meters.
    - depth (float): The depth of the central 'box' in meters.
    - height (float): The height of the central 'box' in meters.
    - cloud_layer_thickness (float): The thickness of the 'cloud' layer around the box in meters.
    - cloud_perturbation (float): The degree of randomness applied to the 'cloud' layer to simulate ethereal qualities.
    - seed (int, optional): A seed for the random number generator to ensure replicability.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)
    
    # Create the central 'box'
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(width, 0, 0),
        rg.Point3d(width, depth, 0),
        rg.Point3d(0, depth, 0),
        rg.Point3d(0, 0, height),
        rg.Point3d(width, 0, height),
        rg.Point3d(width, depth, height),
        rg.Point3d(0, depth, height)
    ]
    box = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' layer
    cloud_corners = [
        rg.Point3d(-cloud_layer_thickness, -cloud_layer_thickness, -cloud_layer_thickness),
        rg.Point3d(width + cloud_layer_thickness, -cloud_layer_thickness, -cloud_layer_thickness),
        rg.Point3d(width + cloud_layer_thickness, depth + cloud_layer_thickness, -cloud_layer_thickness),
        rg.Point3d(-cloud_layer_thickness, depth + cloud_layer_thickness, -cloud_layer_thickness),
        rg.Point3d(-cloud_layer_thickness, -cloud_layer_thickness, height + cloud_layer_thickness),
        rg.Point3d(width + cloud_layer_thickness, -cloud_layer_thickness, height + cloud_layer_thickness),
        rg.Point3d(width + cloud_layer_thickness, depth + cloud_layer_thickness, height + cloud_layer_thickness),
        rg.Point3d(-cloud_layer_thickness, depth + cloud_layer_thickness, height + cloud_layer_thickness)
    ]
    
    # Perturb the cloud corners to add randomness
    perturbed_cloud_corners = [
        rg.Point3d(
            pt.X + random.uniform(-cloud_perturbation, cloud_perturbation),
            pt.Y + random.uniform(-cloud_perturbation, cloud_perturbation),
            pt.Z + random.uniform(-cloud_perturbation, cloud_perturbation)
        ) for pt in cloud_corners
    ]

    cloud = rg.Brep.CreateFromBox(perturbed_cloud_corners)

    # Return the box and the cloud as a list of Breps
    return [box, cloud]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept(10.0, 5.0, 3.0, 1.0, 0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept(8.0, 4.0, 2.5, 0.8, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept(12.0, 6.0, 4.0, 1.5, 0.7, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept(15.0, 7.0, 5.0, 2.0, 0.9, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept(9.0, 4.5, 3.5, 1.2, 0.4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
