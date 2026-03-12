# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The function `create_concept_model` generates an architectural concept model inspired by the "Box in a cloud" metaphor. It creates a solid geometric "box" representing the core structure, defined by specified dimensions. Surrounding this core, it generates multiple cloud layers using randomized offsets and varying sizes, embodying the dynamic, ethereal characteristics of a cloud. This integration of the box and cloud reflects the interaction between stability and fluidity, allowing for exploration of spatial transitions. The result is a collection of 3D geometries that visually express the contrast and dialogue between the rigid core and the soft, adaptable outer layer."""

#! python 3
function_code = """def create_concept_model(box_width, box_depth, box_height, cloud_density, cloud_layer_thickness, random_seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    The model consists of a central 'box' symbolizing a solid, structured core and a 'cloud'
    formed by layered, interconnected sheets that represent a dynamic, ethereal form.

    Parameters:
    - box_width (float): The width of the central box in meters.
    - box_depth (float): The depth of the central box in meters.
    - box_height (float): The height of the central box in meters.
    - cloud_density (int): The number of layers used to represent the cloud's form.
    - cloud_layer_thickness (float): The thickness of each cloud layer in meters.
    - random_seed (int): The seed for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the box and cloud.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Create the central 'box' as a Brep
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

    # Create the 'cloud' using layered surfaces with varying positions
    cloud_geometries = []
    base_plane = rg.Plane(rg.Point3d(box_width / 2, box_depth / 2, box_height / 2), rg.Vector3d.ZAxis)
    for i in range(cloud_density):
        # Offset the base plane with some randomness to create dynamic layers
        offset_distance = random.uniform(-cloud_layer_thickness, cloud_layer_thickness)
        cloud_layer_plane = base_plane.Clone()
        cloud_layer_plane.Translate(rg.Vector3d(0, 0, offset_distance * i))

        # Create a rectangle on this plane with some variation in size
        layer_width = box_width + random.uniform(-1.0, 1.0)
        layer_depth = box_depth + random.uniform(-1.0, 1.0)
        rectangle = rg.Rectangle3d(cloud_layer_plane, layer_width, layer_depth)
        
        # Create a Brep from the offset and add to the cloud geometries
        cloud_brep = rg.Brep.CreatePlanarBreps([rectangle.ToNurbsCurve()])[0]
        cloud_geometries.append(cloud_brep)

    # Return the list of 3D geometries
    return [box_brep] + cloud_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(5.0, 3.0, 2.0, 10, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(4.0, 2.5, 3.0, 8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(6.0, 4.0, 5.0, 12, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(7.0, 5.0, 4.0, 15, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(3.0, 2.0, 1.5, 5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
