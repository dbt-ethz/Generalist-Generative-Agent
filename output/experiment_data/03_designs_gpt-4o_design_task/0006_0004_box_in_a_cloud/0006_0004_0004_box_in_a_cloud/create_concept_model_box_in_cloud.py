# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the "Box in a Cloud" metaphor by creating a solid core and a surrounding ethereal layer. It takes parameters for the core's dimensions, the number of cloud layers, and their transparency. The function constructs a geometric "box" representing the core, emphasizing stability with robust materials. It then creates multiple scaled cloud layers that envelop the core, suggesting movement and lightness. This interplay between the defined core and the fluid cloud layer embodies the metaphor's contrast, allowing exploration of their spatial relationships and interactions through varying densities and transparency."""

#! python 3
function_code = """def create_concept_model_box_in_cloud(core_size, cloud_layers, cloud_transparency, seed=42):
    \"""
    Generates an architectural concept model representing the 'Box in a Cloud' metaphor.

    Parameters:
    - core_size (tuple of float): Dimensions of the core box as (width, depth, height).
    - cloud_layers (int): Number of layers in the cloud-like envelope.
    - cloud_transparency (float): Transparency value for the cloud layers, between 0 (opaque) and 1 (completely transparent).
    - seed (int, optional): Seed for random number generation to ensure replicable results. Default is 42.

    Returns:
    - List of RhinoCommon Breps: A list containing the 3D geometries of the core and cloud layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicable results
    random.seed(seed)

    # Create the core 'box'
    core_width, core_depth, core_height = core_size
    box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = box.ToBrep()

    # Create the cloud layers
    cloud_breps = []
    cloud_height_increment = core_height / (cloud_layers * 2)
    for i in range(cloud_layers):
        scale_factor = 1.2 + (i * 0.1)  # Gradually increase scale for each layer
        cloud_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(-core_width * scale_factor / 2, core_width * scale_factor / 2),
            rg.Interval(-core_depth * scale_factor / 2, core_depth * scale_factor / 2),
            rg.Interval(core_height + i * cloud_height_increment, core_height + (i + 1) * cloud_height_increment)
        )
        cloud_brep = cloud_box.ToBrep()
        cloud_breps.append(cloud_brep)

    # Combine all geometry into a single list
    concept_model = [core_brep] + cloud_breps

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_box_in_cloud((10.0, 5.0, 3.0), 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_box_in_cloud((15.0, 10.0, 4.0), 3, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_box_in_cloud((8.0, 4.0, 2.0), 4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_box_in_cloud((12.0, 6.0, 5.0), 6, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_box_in_cloud((20.0, 10.0, 6.0), 7, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
