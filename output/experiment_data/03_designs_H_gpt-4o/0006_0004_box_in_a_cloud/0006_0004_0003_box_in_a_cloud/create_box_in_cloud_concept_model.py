# Created for 0006_0004_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_concept_model`, generates an architectural concept model based on the "Box in a cloud" metaphor. It constructs a solid, geometric core (the "box") using specified dimensions and creates a series of randomized, spherical cloud elements around it, representing the ethereal "cloud." By varying the density and extent of these cloud elements, the function captures the dynamic interplay between the robust core and its surrounding fluidity. The resulting model showcases a visual contrast between solidity and lightness, reflecting the metaphor's emphasis on the interaction between defined structures and more amorphous forms, while allowing for exploration of spatial relationships."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(core_dimensions, cloud_density, cloud_extent, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    Parameters:
    - core_dimensions (tuple): Dimensions of the core box as (length, width, height) in meters.
    - cloud_density (int): The density or number of cloud elements enveloping the core.
    - cloud_extent (float): The extent of the cloud envelope from the core in meters.
    - seed (int, optional): Seed for random number generator for reproducibility. Default is 42.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the core and cloud elements.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the core box
    core_length, core_width, core_height = core_dimensions
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_length), rg.Interval(0, core_width), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    # Create the cloud elements
    cloud_breps = []
    for _ in range(cloud_density):
        # Randomize positions and sizes to create a cloud-like appearance
        cloud_center = rg.Point3d(
            random.uniform(-cloud_extent, core_length + cloud_extent),
            random.uniform(-cloud_extent, core_width + cloud_extent),
            random.uniform(0, core_height + cloud_extent)
        )
        cloud_radius = random.uniform(0.1, 0.5) * cloud_extent
        cloud_sphere = rg.Sphere(cloud_center, cloud_radius)
        cloud_brep = cloud_sphere.ToBrep()
        cloud_breps.append(cloud_brep)

    # Return the core and cloud elements
    return [core_brep] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((5, 5, 5), 20, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((10, 8, 6), 15, 4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((7, 3, 2), 10, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((12, 10, 8), 25, 5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((15, 10, 10), 30, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
