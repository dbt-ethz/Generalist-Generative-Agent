# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_concept_model`, generates an architectural concept model by interpreting the "Box in a cloud" metaphor. It creates a robust core represented as a geometric box using specified dimensions, symbolizing stability and solidity. Surrounding this core, multiple translucent layers are generated, mimicking a cloud-like presence. The layers are slightly rotated and offset to convey movement and lightness, enhancing the interaction between the solid core and the ethereal envelope. This interplay emphasizes contrast in opacity and translucency, encapsulating the metaphor's essence while allowing for dynamic spatial exploration within the model."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(core_dimensions, cloud_layers, cloud_material_thickness, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    Parameters:
    - core_dimensions (tuple): Dimensions of the core box as (length, width, height) in meters.
    - cloud_layers (int): Number of translucent layers enveloping the core.
    - cloud_material_thickness (float): Thickness of each cloud layer in meters.
    - seed (int, optional): Seed for random number generator for reproducibility. Default is 42.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the core and the cloud layers.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Create the core box
    core_length, core_width, core_height = core_dimensions
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_length), rg.Interval(0, core_width), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()
    
    # Create the cloud layers
    cloud_breps = []
    for i in range(cloud_layers):
        # Calculate the base size for the cloud layer
        offset_value = cloud_material_thickness * (i + 1)
        base_x = core_length + offset_value
        base_y = core_width + offset_value
        base_z = core_height + offset_value

        # Create a cloud-like layer around the core
        layer_profile = rg.Rectangle3d(rg.Plane.WorldXY, base_x, base_y)
        cloud_layer = rg.Extrusion.Create(layer_profile.ToNurbsCurve(), base_z, True)

        # Apply slight random rotation to create a more dynamic cloud appearance
        rotation_angle = random.uniform(-0.1, 0.1)  # Random angle in radians
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        rotation_center = rg.Point3d(core_length / 2, core_width / 2, core_height / 2)
        rotation = rg.Transform.Rotation(rotation_angle, rotation_axis, rotation_center)
        cloud_layer.Transform(rotation)

        # Convert to Brep and add to the list
        cloud_breps.append(cloud_layer.ToBrep())
    
    # Return the core and the cloud layers
    return [core_brep] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((5, 3, 2), 4, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((10, 6, 4), 3, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((7, 4, 3), 5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((8, 5, 3), 6, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((12, 8, 5), 2, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
