# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_concept_model` generates an architectural concept model that embodies the 'Box in a cloud' metaphor by creating a distinct geometric core (the 'box') and enveloping it with a dynamic layer (the 'cloud'). It first constructs the core using specified dimensions and robust materials, represented as a solid box. Then, it adds multiple translucent layers around this core, simulating the ethereal quality of the cloud. Random transformations are applied to these layers to enhance the sense of movement and lightness, emphasizing the interplay between solidity and fluidity, thus achieving a cohesive architectural representation of the metaphor."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(core_size, cloud_layers, cloud_extent, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    Parameters:
    core_size (tuple): Dimensions of the core 'box' in meters (width, depth, height).
    cloud_layers (int): Number of translucent 'cloud' layers enveloping the core.
    cloud_extent (float): Maximum extent of the 'cloud' from the core in meters.
    seed (int): Seed for randomness to ensure replicability.
    
    Returns:
    list: A list of RhinoCommon Brep geometries representing the core and cloud layers.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    geometries = []

    # Create the core 'box'
    core_width, core_depth, core_height = core_size
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()
    geometries.append(core_brep)

    # Create the 'cloud' layers
    for i in range(cloud_layers):
        layer_thickness = (random.uniform(0.1, 0.3) * cloud_extent) / cloud_layers
        layer_offset = i * layer_thickness
        cloud_box = rg.Box(rg.Plane.WorldXY,
                           rg.Interval(-cloud_extent/2, core_width + cloud_extent/2),
                           rg.Interval(-cloud_extent/2, core_depth + cloud_extent/2),
                           rg.Interval(-layer_offset, core_height + layer_offset))
        cloud_brep = cloud_box.ToBrep()
        
        # Apply randomness to create a more dynamic cloud appearance
        transformation = rg.Transform.Multiply(
            rg.Transform.Translation(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)),
            rg.Transform.Rotation(random.uniform(-0.1, 0.1), rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)), rg.Point3d(0, 0, 0))
        )
        cloud_brep.Transform(transformation)
        
        geometries.append(cloud_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((5, 5, 10), 3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((10, 8, 6), 5, 3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((4, 4, 8), 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((7, 3, 5), 6, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((6, 6, 12), 2, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
