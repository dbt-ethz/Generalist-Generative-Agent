# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The function `generate_concept_model_box_in_cloud` creates an architectural model embodying the "Box in a cloud" metaphor. It generates a solid core, or "box," defined by geometric dimensions and robust materials, representing stability. Surrounding this core, multiple translucent "cloud" layers are created, which vary in size and thickness to suggest lightness and movement. The function uses random rotation for each layer to enhance dynamism, emphasizing the contrast between the solid, structured core and the ethereal, flowing cloud. This interaction illustrates the interplay between permanence and fluidity, capturing the essence of the metaphor in a tangible model."""

#! python 3
function_code = """def generate_concept_model_box_in_cloud(core_dimensions, cloud_layers, cloud_thickness, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    Parameters:
    - core_dimensions (tuple): Dimensions of the core 'box' as (length, width, height) in meters.
    - cloud_layers (int): Number of layers representing the 'cloud'.
    - cloud_thickness (float): Thickness of each cloud layer in meters.
    - seed (int, optional): Seed for random number generation to ensure replicable results. Default is 42.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the core and the cloud layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Create the core 'box'
    core_length, core_width, core_height = core_dimensions
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_length), rg.Interval(0, core_width), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    # Create the cloud layers
    cloud_breps = []
    for i in range(cloud_layers):
        layer_scale = 1 + (i + 1) * 0.1  # Gradually increasing scale
        cloud_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(-cloud_thickness * layer_scale / 2, core_length + cloud_thickness * layer_scale / 2),
            rg.Interval(-cloud_thickness * layer_scale / 2, core_width + cloud_thickness * layer_scale / 2),
            rg.Interval(-cloud_thickness * layer_scale / 2, core_height + cloud_thickness * layer_scale / 2)
        )
        cloud_brep = cloud_box.ToBrep()

        # Apply a slight rotation to each layer for dynamic appearance
        rotation_angle = random.uniform(-0.1, 0.1)  # In radians
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation_center = rg.Point3d(core_length / 2, core_width / 2, core_height / 2)
        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, rotation_center)
        cloud_brep.Transform(rotation_transform)

        cloud_breps.append(cloud_brep)

    # Return the core and the cloud layers
    return [core_brep] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_concept_model_box_in_cloud((5, 3, 2), 4, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_concept_model_box_in_cloud((10, 8, 6), 3, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_concept_model_box_in_cloud((7, 5, 4), 5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_concept_model_box_in_cloud((4, 4, 4), 6, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_concept_model_box_in_cloud((3, 2, 1), 2, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
