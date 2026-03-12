# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_concept_model` generates an architectural concept model that embodies the "Box in a cloud" metaphor. It defines a solid core (the "box") using specified dimensions and robust materials, reflecting permanence. Surrounding this core, it creates multiple translucent cloud layers that vary in height and size, symbolizing ethereality and fluidity. The approach emphasizes the interaction between the structured core and the dynamic cloud layers, allowing glimpses of the core while manipulating light and shadow. This interplay highlights the contrast between solidity and softness, capturing the essence of the metaphor in a cohesive architectural model."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(core_dimensions, cloud_layers, cloud_height_variation, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    Parameters:
    - core_dimensions (tuple): Dimensions of the core box as (length, width, height) in meters.
    - cloud_layers (int): Number of translucent layers enveloping the core.
    - cloud_height_variation (float): Maximum variation in height for cloud layers in meters.
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
    base_cloud_height = core_height * 0.5  # Start at half the core height
    for i in range(cloud_layers):
        # Calculate the base position for the cloud layer
        base_height = base_cloud_height + i * (cloud_height_variation / cloud_layers)
        # Determine random variation for dynamic cloud effect
        height_variation = random.uniform(-cloud_height_variation, cloud_height_variation)
        layer_height = base_height + height_variation
        
        # Create a cloud-like offset layer around the core
        offset_value = 0.5 * (i + 1)  # Gradual increase in layer size
        offset_x = core_length + offset_value
        offset_y = core_width + offset_value
        offset_z = layer_height
        
        cloud_box = rg.Box(
            rg.Plane.WorldXY, 
            rg.Interval(-offset_value, offset_x), 
            rg.Interval(-offset_value, offset_y), 
            rg.Interval(0, offset_z)
        )
        cloud_brep = cloud_box.ToBrep()
        
        # Subtract the core from the cloud to create a hollow layer
        cloud_difference = rg.Brep.CreateBooleanDifference([cloud_brep], [core_brep], 0.001)
        if cloud_difference:
            cloud_breps.append(cloud_difference[0])
    
    # Return the core and the cloud layers
    return [core_brep] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((5, 3, 2), 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((10, 6, 3), 6, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((7, 4, 2.5), 3, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((8, 5, 4), 5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((12, 8, 5), 7, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
