# Created for 0001_0005_house_within_a_house.json

""" Summary:
The function `create_concept_model` translates the "House within a house" metaphor into a 3D architectural concept model by generating concentric, layered volumes. It begins with a central core representing the inner sanctuary, surrounded by multiple layers that vary in height and materiality. Each layer is offset to create interstitial spaces, enhancing exploration and the transition from public to private zones. The varying heights foster a dynamic relationship between openness and enclosure, embodying the metaphor's themes of nesting, protection, and discovery. This results in a visually and spatially rich model that communicates the essence of retreat and encapsulation."""

#! python 3
function_code = """def create_concept_model(core_length=5.0, layer_count=4, layer_offset=1.5, height_variation=(2.5, 4.0)):
    \"""
    Create an architectural Concept Model based on the 'House within a house' metaphor.

    This function generates a series of concentric, layered volumes, each representing different spatial qualities
    transitioning from public to private realms. The central core acts as the innermost sanctuary, surrounded by 
    layers of varied heights and offsets, encouraging exploration and emphasizing the sense of retreat and enclosure.

    Parameters:
    - core_length (float): The side length of the central core cube in meters.
    - layer_count (int): Number of concentric layers surrounding the core.
    - layer_offset (float): Offset distance between each layer in meters, creating interstitial spaces.
    - height_variation (tuple of float): Range of height variation for each layer in meters.

    Returns:
    - List of Rhino.Geometry.Brep: The generated 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for reproducibility
    random.seed(42)

    geometries = []

    # Create the central core volume
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_length / 2, core_length / 2),
                  rg.Interval(-core_length / 2, core_length / 2),
                  rg.Interval(0, core_length))
    geometries.append(core.ToBrep())

    # Generate concentric layers
    for i in range(1, layer_count + 1):
        # Increment dimensions for each layer
        layer_length = core_length + i * layer_offset
        layer_height = random.uniform(*height_variation)

        # Create an outer box for the layer
        outer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-layer_length / 2, layer_length / 2),
                           rg.Interval(-layer_length / 2, layer_length / 2),
                           rg.Interval(0, layer_height))

        # Create an inner box to subtract and form a shell
        inner_length = layer_length - 2 * layer_offset
        inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-inner_length / 2, inner_length / 2),
                           rg.Interval(-inner_length / 2, inner_length / 2),
                           rg.Interval(0, layer_height - layer_offset))

        # Subtract the inner box from the outer box
        shell = rg.Brep.CreateBooleanDifference(outer_box.ToBrep(), inner_box.ToBrep(), 0.01)

        if shell:
            geometries.extend(shell)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(core_length=6.0, layer_count=5, layer_offset=2.0, height_variation=(3.0, 5.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(core_length=4.0, layer_count=3, layer_offset=1.0, height_variation=(2.0, 3.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(core_length=7.0, layer_count=6, layer_offset=1.0, height_variation=(2.0, 4.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(core_length=5.5, layer_count=4, layer_offset=1.0, height_variation=(2.0, 6.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(core_length=8.0, layer_count=5, layer_offset=1.2, height_variation=(3.5, 5.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
