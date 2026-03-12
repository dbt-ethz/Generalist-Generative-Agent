# Created for 0020_0005_stacked_forests.json

""" Summary:
The provided function `generate_stacked_forests_concept` creates an architectural concept model inspired by the metaphor of "Stacked forests." It generates a series of cascading terraces or ledges, each representing distinct ecological layers, which reflects the vertical stratification found in a forest. By adjusting parameters such as width, depth, and height, the function simulates the dynamic, stepped silhouette of a hillside. The integration of varying degrees of openness and enclosure enhances spatial richness and allows light to interact with the structure, evoking the natural growth patterns of a forest while ensuring vertical connectivity among layers."""

#! python 3
function_code = """def generate_stacked_forests_concept(base_width, base_depth, num_layers, layer_height, offset_factor, random_seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Stacked forests' metaphor.
    
    This function creates a cascading series of terraces or ledges, each representing a unique ecological layer.
    The design emphasizes vertical integration with varying degrees of openness and enclosure, reflecting the 
    natural stratification and growth patterns of a forest.

    Parameters:
    - base_width: The width of the base layer in meters.
    - base_depth: The depth of the base layer in meters.
    - num_layers: The number of terraced layers to create.
    - layer_height: The height of each layer in meters.
    - offset_factor: A factor determining the offset for each successive layer, affecting the cascade.
    - random_seed: A seed for randomness to ensure replicability of results.
    
    Returns:
    - A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set random seed for replicability
    random.seed(random_seed)
    
    geometries = []
    
    # Initial position and size
    current_width = base_width
    current_depth = base_depth
    current_height = 0
    
    for i in range(num_layers):
        # Create a base rectangle for the current layer
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, current_width, current_depth)
        
        # Create a surface from the base rectangle and move it to the current height
        base_surface = rg.Brep.CreateFromSurface(rg.NurbsSurface.CreateFromCorners(
            base_rect.Corner(0), base_rect.Corner(1), base_rect.Corner(2), base_rect.Corner(3)))
        translation = rg.Transform.Translation(0, 0, current_height)
        base_surface.Transform(translation)
        
        # Add to the list of geometries
        geometries.append(base_surface)
        
        # Update dimensions for the next layer
        current_width *= (1 - offset_factor * random.uniform(0.1, 0.3))
        current_depth *= (1 - offset_factor * random.uniform(0.1, 0.3))
        current_height += layer_height
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_stacked_forests_concept(10, 20, 5, 3, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_stacked_forests_concept(15, 25, 4, 2.5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_stacked_forests_concept(12, 15, 6, 4, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_stacked_forests_concept(8, 16, 7, 2, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_stacked_forests_concept(14, 18, 3, 5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
