# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The function `create_dynamic_box_in_cloud_model` generates a 3D architectural concept model based on the "Box in a cloud" metaphor. It constructs a solid geometric core, or "box," defined by user-specified dimensions, representing stability and structure. Surrounding this core, multiple interactive "cloud" layers are created using spheres with varying radii, embodying ethereality and dynamism. The function introduces randomness to the placement of these cloud layers, enhancing the organic feel of the design. By combining these elements, the model illustrates the interplay between solidity and fluidity, encouraging exploration of spatial transitions and interactions, and fostering a dialogue between the two forms."""

#! python 3
function_code = """def create_dynamic_box_in_cloud_model(box_dims, cloud_max_radius, cloud_layers, seed=42):
    \"""
    Generates a 3D Concept Model based on the 'Box in a cloud' metaphor.
    
    This model features a rigid core 'box' surrounded by an interactive 'cloud' layer.
    The 'cloud' is designed with multiple layers to emphasize ethereal qualities,
    with an emphasis on spatial transitions and interactions.

    Parameters:
    - box_dims (tuple): Dimensions of the box as (width, depth, height) in meters.
    - cloud_max_radius (float): Maximum radius of the cloud layers around the box.
    - cloud_layers (int): Number of concentric cloud layers surrounding the box.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    # Unpack box dimensions
    box_width, box_depth, box_height = box_dims

    # Create the central 'box' using RhinoCommon
    box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(0, box_width),
        rg.Interval(0, box_depth),
        rg.Interval(0, box_height)
    )
    box_brep = box.ToBrep()

    # Create the 'cloud' layers
    cloud_geometries = []
    for i in range(cloud_layers):
        # Define the radius for the current layer
        layer_radius = cloud_max_radius * (i + 1) / cloud_layers
        # Add randomness to cloud layer placement
        jitter = random.uniform(-0.1, 0.1) * cloud_max_radius

        # Create a cloud layer using an offset sphere
        sphere_center = rg.Point3d(
            box_width / 2 + jitter,
            box_depth / 2 + jitter,
            box_height / 2 + jitter
        )
        sphere = rg.Sphere(sphere_center, layer_radius)

        # Convert the sphere to a Brep for the cloud layer
        cloud_brep = sphere.ToBrep()
        cloud_geometries.append(cloud_brep)

    # Return the combined geometries of the box and cloud
    return [box_brep] + cloud_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_box_in_cloud_model((2, 3, 1), 5.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_box_in_cloud_model((1, 1, 1), 3.0, 2, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_box_in_cloud_model((4, 5, 3), 6.0, 5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_box_in_cloud_model((3, 2, 4), 7.0, 3, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_box_in_cloud_model((5, 5, 5), 10.0, 6, seed=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
