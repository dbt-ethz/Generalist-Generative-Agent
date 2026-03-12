# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_concept_model`, generates an architectural model based on the "Box in a cloud" metaphor by creating a solid core and a dynamic outer layer. The core, represented as a rectangular box, symbolizes stability and strength, constructed from defined dimensions. Surrounding this core, multiple translucent layers are generated to represent the ethereal "cloud," which are designed with varying sizes and slight randomization to create a sense of movement. The interaction between these solid and fluid elements is visually articulated through their contrasting materials and forms, allowing exploration of spatial layers and transitions, reflecting the metaphor's essence."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(core_dimensions, cloud_layers, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    Parameters:
    - core_dimensions (tuple): Dimensions of the core box as (length, width, height) in meters.
    - cloud_layers (int): Number of translucent layers enveloping the core.
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
        # Randomize the dimensions slightly for each layer
        layer_thickness = 0.1  # 10 cm thickness for each layer
        offset_value = 0.5 * (i + 1)  # Gradual increase in layer size
        offset_x = core_length + offset_value + random.uniform(-0.1, 0.1)
        offset_y = core_width + offset_value + random.uniform(-0.1, 0.1)
        offset_z = core_height + offset_value + random.uniform(-0.1, 0.1)
        
        # Create a cloud-like layer around the core
        cloud_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-offset_value, offset_x), rg.Interval(-offset_value, offset_y), rg.Interval(-offset_value, offset_z))
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
    geometry = create_box_in_cloud_concept_model((2, 3, 4), 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((1.5, 2.5, 3.5), 3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((4, 2, 3), 4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((3, 3, 3), 6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((5, 5, 5), 8, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
