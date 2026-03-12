# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the "Box in a cloud" metaphor by creating a defined geometric core ("box") and surrounding it with dynamic, interactive layers ("cloud"). The function takes parameters for the box's size, the number of cloud layers, and the variation in their thickness. It constructs the box using Rhino's geometry tools, ensuring structural integrity, while the cloud layers are represented as toroidal shapes, providing a sense of ethereality. This design integrates solid and fluid forms, promoting interaction and exploration of spatial transitions, embodying the metaphor's essence of juxtaposition between stability and change."""

#! python 3
function_code = """def create_concept_model(box_size, cloud_layers, cloud_variation, random_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    This function generates a central 'box' as a geometric core and envelops it with
    dynamic 'cloud' layers that interact with the environment. The design highlights
    the integration and interaction between the solid and ethereal elements.

    Parameters:
    - box_size: A tuple of three floats (length, width, height) representing the size of the central box in meters.
    - cloud_layers: An integer representing the number of cloud layers surrounding the box.
    - cloud_variation: A float representing the amount of variation in cloud layer thickness.
    - random_seed: An integer seed for the random number generator to ensure replicability.

    Returns:
    - A list of 3D geometries (breps) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Create the box (central core)
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_size[0], 0, 0),
        rg.Point3d(box_size[0], box_size[1], 0),
        rg.Point3d(0, box_size[1], 0),
        rg.Point3d(0, 0, box_size[2]),
        rg.Point3d(box_size[0], 0, box_size[2]),
        rg.Point3d(box_size[0], box_size[1], box_size[2]),
        rg.Point3d(0, box_size[1], box_size[2])
    ]
    box = rg.Brep.CreateFromBox(box_corners)

    # Create the cloud (dynamic outer layer)
    cloud_geometries = []
    for layer in range(1, cloud_layers + 1):
        layer_radius = box_size[0] * 0.6 * layer / cloud_layers
        layer_thickness = layer_radius * (1 + random.uniform(-cloud_variation, cloud_variation))

        # Create a torus as a representation of a cloud layer
        torus_center = rg.Point3d(box_size[0] / 2, box_size[1] / 2, box_size[2] / 2)
        plane = rg.Plane(torus_center, rg.Vector3d.ZAxis)
        torus = rg.Torus(plane, layer_radius, layer_thickness).ToBrep()
        cloud_geometries.append(torus)

    # Return the list of 3D geometries
    return [box] + cloud_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model((5.0, 5.0, 5.0), 3, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model((10.0, 10.0, 10.0), 5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model((3.0, 4.0, 2.0), 2, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model((7.0, 3.0, 4.0), 4, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model((6.0, 6.0, 6.0), 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
