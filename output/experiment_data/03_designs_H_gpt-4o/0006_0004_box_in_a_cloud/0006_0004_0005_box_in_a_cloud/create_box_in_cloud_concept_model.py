# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_concept_model`, generates an architectural concept model based on the "Box in a cloud" metaphor by creating a defined geometric core ("box") and enveloping it with dynamic, layered cloud-like forms. The core's dimensions are specified, ensuring a solid and stable structure, while multiple cloud layers are added, each varying in size to evoke movement and lightness. This interplay between the rigid core and the fluid cloud captures the essence of solidity versus ethereality, allowing for exploration of spatial transitions. The model emphasizes contrast through shape, texture, and light interaction."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(core_dimensions, cloud_layers, cloud_thickness, layer_variation, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    Parameters:
    - core_dimensions (tuple): Dimensions of the core box as (length, width, height) in meters.
    - cloud_layers (int): Number of cloud layers enveloping the core.
    - cloud_thickness (float): Thickness of each cloud layer in meters.
    - layer_variation (float): Degree of variation in cloud layer dimensions to create dynamism.
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
        # Calculate the base size for this layer
        layer_offset = cloud_thickness * (i + 1)
        base_length = core_length + layer_offset
        base_width = core_width + layer_offset
        base_height = core_height + layer_offset

        # Introduce variation to layer dimensions
        varied_length = base_length + random.uniform(-layer_variation, layer_variation)
        varied_width = base_width + random.uniform(-layer_variation, layer_variation)
        varied_height = base_height + random.uniform(-layer_variation, layer_variation)

        # Create a cloud-like layer around the core
        cloud_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-layer_offset/2, varied_length), rg.Interval(-layer_offset/2, varied_width), rg.Interval(-layer_offset/2, varied_height))
        cloud_brep = cloud_box.ToBrep()
        
        # Add to cloud breps
        cloud_breps.append(cloud_brep)
    
    # Return the core and the cloud layers
    return [core_brep] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((5, 3, 2), 4, 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((10, 8, 6), 3, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((7, 5, 4), 5, 0.8, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((4, 2, 3), 6, 0.6, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((6, 4, 5), 2, 0.7, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
