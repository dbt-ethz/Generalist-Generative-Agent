# Created for 0020_0005_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept` generates a 3D architectural model inspired by the metaphor of "Stacked forests." It creates a series of cascading terraces or ledges, each representing distinct ecological layers, reflecting the vertical stratification of a forest. The function calculates layer heights and introduces randomness in width and depth to mimic natural variation. By stacking these layers with overlapping heights, it achieves a stepped silhouette reminiscent of a forest hillside. The resulting design emphasizes vertical connectivity, allowing light penetration and shadow play, thereby enriching the spatial experience and embodying the metaphor of organic growth and layered interaction."""

#! python 3
function_code = """def create_stacked_forests_concept(base_width, base_length, height, num_layers, terrace_depth_variation):
    \"""
    Creates a 3D architectural concept model based on the metaphor of 'Stacked forests'.
    
    This function generates a series of cascading terraces or ledges, each representing an ecological layer,
    with varying openness and enclosure. The design captures the silhouette of a stepped form, reminiscent of
    a forest hillside with descending layers.

    Parameters:
    - base_width: float, the width of the base layer in meters.
    - base_length: float, the length of the base layer in meters.
    - height: float, the total height of the structure in meters.
    - num_layers: int, the number of layers or terraces to create.
    - terrace_depth_variation: float, maximum variation in terrace depth in meters for randomness.

    Returns:
    - List of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set seed for randomness to ensure replicable results
    random.seed(42)
    
    # Calculate the height of each layer
    layer_height = height / num_layers
    
    # Initialize the list to store the generated geometries
    concept_model = []
    
    current_z = 0  # Start at the base
    for i in range(num_layers):
        # Calculate the depth of the current layer with some variation
        current_depth = base_length - random.uniform(0, terrace_depth_variation)
        current_width = base_width - random.uniform(0, terrace_depth_variation)
        
        # Create a rectangle for the current layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, current_z))
        
        # Create a box (Brep) at the current layer
        box = rg.Box(base_plane, rg.Interval(0, current_width), rg.Interval(0, current_depth), rg.Interval(0, layer_height))
        brep = box.ToBrep()
        concept_model.append(brep)
        
        # Update z position for the next layer
        current_z += layer_height * 0.9  # Overlapping effect

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(10.0, 15.0, 30.0, 5, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(8.0, 12.0, 25.0, 4, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(12.0, 20.0, 40.0, 6, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(9.0, 14.0, 28.0, 3, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(15.0, 25.0, 50.0, 7, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
