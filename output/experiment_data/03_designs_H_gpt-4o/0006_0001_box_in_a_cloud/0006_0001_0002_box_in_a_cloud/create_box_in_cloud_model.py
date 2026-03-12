# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the "Box in a cloud" metaphor by creating a central solid geometric form (the "box") surrounded by layers of translucent materials (the "cloud"). It constructs the box using specified dimensions to represent stability and permanence. Surrounding it, the function generates multiple cloud layers with incremental thickness and random perturbations to simulate lightness and ethereality. This design emphasizes the contrast between the defined, structured core and the flowing, organic envelope, facilitating a spatial dialogue between solidity and fluidity, as well as exploring the interplay of opacity and translucency."""

#! python 3
function_code = """def create_box_in_cloud_model(box_dims, cloud_layers, cloud_variability, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Box in a cloud' metaphor.

    This function builds a central geometric 'box' of specified dimensions and surrounds it with a series of
    'cloud' layers. The 'box' is a solid, stable structure, while the 'cloud' is composed of layered translucent
    surfaces with varying opacity and perturbation to simulate ethereality and movement.

    Parameters:
    - box_dims (tuple of floats): Dimensions of the box (width, depth, height) in meters.
    - cloud_layers (int): Number of layers in the cloud envelope.
    - cloud_variability (float): Degree of shape perturbation for cloud layers.
    - seed (int, optional): Seed for random number generation to ensure replicability, default is 42.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the box and cloud layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    # Unpack box dimensions
    box_width, box_depth, box_height = box_dims

    # Create the central box
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
    box = rg.Brep.CreateFromBox(box_corners)

    # Create cloud layers surrounding the box
    cloud_breps = []
    for i in range(cloud_layers):
        layer_thickness = (i + 1) * 0.5  # Incremental layer thickness
        cloud_corners = [
            rg.Point3d(-layer_thickness, -layer_thickness, -layer_thickness),
            rg.Point3d(box_width + layer_thickness, -layer_thickness, -layer_thickness),
            rg.Point3d(box_width + layer_thickness, box_depth + layer_thickness, -layer_thickness),
            rg.Point3d(-layer_thickness, box_depth + layer_thickness, -layer_thickness),
            rg.Point3d(-layer_thickness, -layer_thickness, box_height + layer_thickness),
            rg.Point3d(box_width + layer_thickness, -layer_thickness, box_height + layer_thickness),
            rg.Point3d(box_width + layer_thickness, box_depth + layer_thickness, box_height + layer_thickness),
            rg.Point3d(-layer_thickness, box_depth + layer_thickness, box_height + layer_thickness)
        ]

        # Perturb cloud corners to simulate organic shape
        perturbed_corners = [
            rg.Point3d(
                pt.X + random.uniform(-cloud_variability, cloud_variability),
                pt.Y + random.uniform(-cloud_variability, cloud_variability),
                pt.Z + random.uniform(-cloud_variability, cloud_variability)
            ) for pt in cloud_corners
        ]

        # Create layer as a Brep
        cloud_layer = rg.Brep.CreateFromBox(perturbed_corners)
        cloud_breps.append(cloud_layer)

    return [box] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model((2.0, 3.0, 4.0), 5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model((1.0, 1.0, 1.0), 3, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model((5.0, 2.0, 3.0), 4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model((3.0, 4.0, 2.0), 6, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model((4.0, 5.0, 6.0), 2, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
