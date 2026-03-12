# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model` generates an architectural concept model embodying the 'Box in a cloud' metaphor by constructing a solid geometric core, representing the 'box', and surrounding it with a collection of diffuse, lighter spheres that form the 'cloud'. The box is created as a solid rectangular prism, emphasizing structural stability and spatial anchoring. The cloud is represented by randomly positioned spheres, suggesting lightness and ethereality. This juxtaposition highlights the contrast between defined and fluid forms, while varying parameters like dimensions and sphere density allows for exploration of spatial relationships and transitions between the solid and the ephemeral."""

#! python 3
function_code = """def create_box_in_cloud_model(box_width, box_depth, box_height, cloud_radius, cloud_density, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Box in a cloud' metaphor.

    This function constructs a central, geometric form (the 'box') and surrounds it with a secondary layer
    (the 'cloud'). The 'box' is a solid rectangular prism representing structural stability and spatial anchoring.
    The 'cloud' is represented by a collection of lighter, more diffuse spheres that envelop the box, creating a
    sense of lightness and movement.

    Inputs:
    - box_width: Width of the central box in meters.
    - box_depth: Depth of the central box in meters.
    - box_height: Height of the central box in meters.
    - cloud_radius: Average radius of the spheres forming the cloud in meters.
    - cloud_density: Number of spheres used to form the cloud.
    - seed: Random seed for reproducibility.

    Outputs:
    - A list of RhinoCommon Brep objects representing the 'box' and 'cloud'.

    Note:
    - This function uses randomness to distribute the cloud spheres, but results are reproducible with the given seed.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the central 'box' as a solid Brep
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
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' as a collection of spheres
    cloud_breps = []
    for _ in range(cloud_density):
        # Randomly position spheres around the box
        x = random.uniform(-cloud_radius, box_width + cloud_radius)
        y = random.uniform(-cloud_radius, box_depth + cloud_radius)
        z = random.uniform(-cloud_radius, box_height + cloud_radius)
        center = rg.Point3d(x, y, z)
        sphere = rg.Sphere(center, cloud_radius * random.uniform(0.8, 1.2))
        cloud_breps.append(sphere.ToBrep())

    # Combine the box and cloud into a single list of Brep objects
    model_breps = [box_brep] + cloud_breps

    return model_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model(5, 3, 4, 1.5, 50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model(10, 5, 7, 2, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model(8, 6, 5, 2.5, 75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model(12, 8, 10, 3, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model(7, 4, 6, 2, 80)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
