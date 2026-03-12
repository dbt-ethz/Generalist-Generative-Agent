# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_concept_model` generates an architectural concept model based on the "Box in a cloud" metaphor by creating a solid, geometric central 'box' and surrounding it with ethereal 'cloud' elements. It takes parameters for the box's dimensions, the cloud's radius, and density, ensuring flexibility in design. The box is constructed using defined points to create a stable structure, while the cloud elements are randomized in position and size, utilizing spheres to convey lightness. This approach emphasizes the contrast between the solid core and the fluid envelope, enhancing the interplay of light, shadow, and space."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(box_dimensions, cloud_radius, cloud_density, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Box in a cloud' metaphor. 
    The model consists of a solid central 'box' enveloped by a lighter, more diffuse 'cloud'.

    Parameters:
    - box_dimensions: Tuple of three floats representing the width, depth, and height of the box in meters.
    - cloud_radius: Float representing the approximate radius of the cloud enveloping the box.
    - cloud_density: Integer representing the number of cloud elements to create around the box.
    - seed: Integer for the random seed to ensure replicable results.

    Returns:
    - A list of RhinoCommon Breps representing the 3D geometries of the box and cloud.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed
    random.seed(seed)

    # Create the central box
    box_width, box_depth, box_height = box_dimensions
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
    box = rg.Brep.CreateFromBox(box_corners)

    # Create the surrounding cloud
    cloud_elements = []
    for _ in range(cloud_density):
        # Random position around the box
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(box_width / 2, cloud_radius)
        height = random.uniform(0, box_height)

        # Random cloud element size and shape
        cloud_element_radius = random.uniform(cloud_radius / 10, cloud_radius / 5)
        cloud_center = rg.Point3d(
            box_width / 2 + distance * random.choice([-1, 1]) * math.cos(angle),
            box_depth / 2 + distance * random.choice([-1, 1]) * math.sin(angle),
            height
        )
        cloud_sphere = rg.Sphere(cloud_center, cloud_element_radius)
        cloud_element = rg.Brep.CreateFromSphere(cloud_sphere)
        cloud_elements.append(cloud_element)

    # Return both the box and the cloud elements
    return [box] + cloud_elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model((2.0, 3.0, 1.5), 5.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model((4.0, 2.0, 3.0), 6.0, 15, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model((1.0, 1.0, 1.0), 3.0, 10, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model((5.0, 5.0, 2.0), 8.0, 30, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model((3.0, 4.0, 2.0), 7.0, 25, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
