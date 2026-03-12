# Created for 0001_0005_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model based on the "House within a house" metaphor by creating a series of concentric, layered volumes. Each layer encapsulates a central core, reflecting the themes of nesting, protection, and privacy. By varying the radius, thickness, and height of these layers, the model embodies a spatial hierarchy that allows for a transition from public to private spaces. This layered design fosters a sense of journey and discovery, as users navigate through the interstitial spaces, experiencing a dynamic interplay of enclosure and openness, reinforcing the metaphor of an internal sanctuary."""

#! python 3
function_code = """def create_concept_model(core_radius=6.0, layer_count=4, layer_thickness=2.0, height_variation=(8.0, 12.0)):
    \"""
    Create an architectural Concept Model that embodies the 'House within a house' metaphor.

    The function generates a series of concentric, layered volumes with varying heights and forms,
    representing transitions from public to private spaces. Each layer is a distinct shell around
    the central core, emphasizing the metaphor of nesting and encapsulation.

    Parameters:
    - core_radius (float): The radius of the central core volume in meters.
    - layer_count (int): The number of concentric layers surrounding the core.
    - layer_thickness (float): The thickness of each layer in meters.
    - height_variation (tuple): A range (min_height, max_height) for random height generation of each layer.

    Returns:
    - List of Rhino.Geometry.Brep: The generated 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a random seed for reproducibility
    random.seed(42)

    geometries = []

    # Create the central core volume
    core_height = random.uniform(*height_variation)
    core = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, core_radius), core_height).ToBrep(True, True)
    geometries.append(core)

    # Generate concentric layers around the core
    for i in range(1, layer_count + 1):
        # Calculate radius and height for the current layer
        outer_radius = core_radius + i * layer_thickness
        inner_radius = outer_radius - layer_thickness
        layer_height = random.uniform(*height_variation)

        # Create the outer and inner cylindrical shells
        outer_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, outer_radius), layer_height).ToBrep(True, True)
        inner_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, inner_radius), layer_height).ToBrep(True, True)

        # Subtract inner cylinder from outer cylinder to create a hollow shell
        hollow_layer = rg.Brep.CreateBooleanDifference([outer_cylinder], [inner_cylinder], 0.01)

        if hollow_layer:
            geometries.extend(hollow_layer)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(core_radius=5.0, layer_count=3, layer_thickness=1.5, height_variation=(10.0, 15.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(core_radius=7.0, layer_count=5, layer_thickness=2.5, height_variation=(9.0, 14.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(core_radius=4.0, layer_count=6, layer_thickness=1.0, height_variation=(7.0, 10.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(core_radius=8.0, layer_count=2, layer_thickness=3.0, height_variation=(6.0, 9.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(core_radius=6.5, layer_count=3, layer_thickness=2.0, height_variation=(5.0, 11.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
