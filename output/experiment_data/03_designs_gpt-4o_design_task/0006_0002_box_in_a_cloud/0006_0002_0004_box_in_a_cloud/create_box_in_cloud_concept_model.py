# Created for 0006_0002_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_concept_model`, generates an architectural concept model that embodies the "Box in a cloud" metaphor. It constructs a solid geometric "box" using defined dimensions, representing stability and structure. Surrounding this core, a dynamic "cloud" is formed from randomly positioned spheres, symbolizing lightness and ethereality. The interaction between the rigid box and the amorphous cloud illustrates the contrast between solidity and fluidity, emphasizing spatial transitions. By varying the parameters, the model explores different scales and configurations, ultimately manifesting the metaphors essence through a visual dialogue of form and materiality."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(box_width, box_depth, box_height, cloud_radius, cloud_resolution):
    \"""
    Creates a conceptual architectural model based on the "Box in a cloud" metaphor.
    
    The model consists of a central geometric 'box' symbolizing solidity and structure, encapsulated by a flowing, dynamic 'cloud'
    that represents lightness and ethereality. The 'box' is a defined rectangular prism, while the 'cloud' is generated using 
    a collection of spheres that create an amorphous, enveloping form.

    Parameters:
    - box_width (float): Width of the central box in meters.
    - box_depth (float): Depth of the central box in meters.
    - box_height (float): Height of the central box in meters.
    - cloud_radius (float): Radius of the spheres forming the cloud.
    - cloud_resolution (int): Number of spheres to use for the cloud formation.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the box and the cloud.

    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness
    random.seed(42)

    # Create the 'box' as a Brep (solid)
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
    for _ in range(cloud_resolution):
        # Randomly position spheres around the box
        x = random.uniform(-cloud_radius, box_width + cloud_radius)
        y = random.uniform(-cloud_radius, box_depth + cloud_radius)
        z = random.uniform(-cloud_radius, box_height + cloud_radius)
        center = rg.Point3d(x, y, z)
        sphere = rg.Sphere(center, cloud_radius)
        cloud_breps.append(sphere.ToBrep())

    # Combine all geometries into a single list
    concept_model = [box_brep] + cloud_breps

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model(5.0, 3.0, 2.0, 1.0, 50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model(10.0, 7.0, 4.0, 2.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model(2.5, 1.5, 1.0, 0.5, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model(8.0, 5.0, 3.0, 1.5, 75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model(6.0, 4.0, 3.0, 1.2, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
