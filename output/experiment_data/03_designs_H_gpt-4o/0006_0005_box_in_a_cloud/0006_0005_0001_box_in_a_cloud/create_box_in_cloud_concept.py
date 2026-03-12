# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The provided function `create_box_in_cloud_concept` generates an architectural concept model by embodying the "Box in a Cloud" metaphor. It constructs a solid, geometric 'box' as the central element, representing structural integrity. Surrounding this core, the function creates a layered 'cloud' composed of dynamic, ethereal surfaces that evoke interaction and adaptability. By varying the dimensions and positions of the cloud layers, the model explores the contrast between the rigid box and the fluid cloud, emphasizing spatial transitions and the interplay of light and shadow. This approach encourages a dialogue between solid and ephemeral forms, enhancing the architectural narrative."""

#! python 3
function_code = """def create_box_in_cloud_concept(box_length, box_width, box_height, cloud_radius, cloud_layers, seed=0):
    \"""
    Generates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    This function creates a central 'box' as a solid and defined geometric form, 
    surrounded by a 'cloud' composed of layered, interconnected surfaces. The 'cloud' 
    emulates an ethereal and dynamic outer layer, transitioning smoothly from the core.

    Parameters:
    - box_length (float): The length of the central box in meters.
    - box_width (float): The width of the central box in meters.
    - box_height (float): The height of the central box in meters.
    - cloud_radius (float): The maximum extent of the cloud layer in meters.
    - cloud_layers (int): Number of layers to form the cloud.
    - seed (int): Random seed for reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the box and cloud geometries.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create the central 'box' Brep
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_length, 0, 0),
        rg.Point3d(box_length, box_width, 0),
        rg.Point3d(0, box_width, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_length, 0, box_height),
        rg.Point3d(box_length, box_width, box_height),
        rg.Point3d(0, box_width, box_height)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' as layered surfaces
    cloud_breps = []
    for i in range(cloud_layers):
        angle = 2 * 3.14159 * i / cloud_layers
        offset_x = cloud_radius * random.uniform(0.8, 1.2)
        offset_y = cloud_radius * random.uniform(0.8, 1.2)
        cloud_plane = rg.Plane(rg.Point3d(offset_x, offset_y, box_height / 2),
                               rg.Vector3d(0, 0, 1))
        cloud_circle = rg.Circle(cloud_plane, cloud_radius * random.uniform(0.8, 1.2))
        cloud_surface = rg.Brep.CreatePlanarBreps(cloud_circle.ToNurbsCurve())
        if cloud_surface:
            cloud_breps.append(cloud_surface[0])

    # Combine geometries
    concept_model = [box_brep] + cloud_breps

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept(5.0, 3.0, 2.0, 4.0, 10, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept(6.0, 4.0, 3.0, 5.0, 8, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept(7.0, 5.0, 4.0, 6.0, 12, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept(4.0, 2.5, 1.5, 3.0, 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept(8.0, 6.0, 5.0, 7.0, 15, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
