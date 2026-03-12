# Created for 0020_0001_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the "Stacked forests" metaphor by creating a series of vertically layered platforms. Each layer, defined by distinct sizes and orientations, mimics the tiers of a forest, incorporating organic shapes and irregular forms to reflect natural growth patterns. The function includes parameters for controlling the base size, number of layers, height variation, and organic irregularity. By employing randomization within specified constraints, it produces unique geometries that embody vertical connectivity, allowing for diverse spatial experiences akin to navigating through different forest strata."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_size, num_layers, height_variation, organic_factor, seed):
    \"""
    Create an architectural Concept Model based on the 'Stacked forests' metaphor.
    
    This function generates a series of layered platforms or blocks that rise vertically, 
    using organic shapes and irregular forms to represent the diverse forest strata. Each layer 
    is distinct in form and orientation, yet interconnected by vertical circulation elements.
    
    Parameters:
    - base_size: float, the base size of the bottom-most layer in meters.
    - num_layers: int, the number of vertical layers or platforms to create.
    - height_variation: float, the maximum variation in height between the layers in meters.
    - organic_factor: float, a factor influencing the organic irregularity of shapes.
    - seed: int, seed for randomness to ensure replicability.
    
    Returns:
    - list of Rhino.Geometry.Brep objects representing the 3D geometries of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    geometries = []
    current_height = 0.0
    
    for i in range(num_layers):
        # Determine the size and position variation for this layer
        size_variation = base_size * (1 + random.uniform(-organic_factor, organic_factor))
        height_increment = random.uniform(1, height_variation)
        
        # Create a base rectangle for the platform
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, size_variation, size_variation)
        
        # Offset the rectangle to create an organic shape
        offset_distance = size_variation * organic_factor
        offset_curves = base_rect.ToNurbsCurve().Offset(rg.Plane.WorldXY, offset_distance, 0.01, rg.CurveOffsetCornerStyle.Sharp)
        
        if offset_curves:
            # Pick one offset curve if there are multiple
            organic_curve = offset_curves[0]
            
            # Create a surface from the curve
            organic_surface = rg.Brep.CreatePlanarBreps(organic_curve)[0]
            
            # Move the surface up to the current layer height
            translation_vector = rg.Vector3d(0, 0, current_height)
            organic_surface.Transform(rg.Transform.Translation(translation_vector))
            
            # Add to the list of geometries
            geometries.append(organic_surface)
        
        # Update the current height for the next layer
        current_height += height_increment
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(5.0, 10, 3.0, 0.2, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(7.5, 8, 2.5, 0.3, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(4.0, 12, 4.0, 0.1, 77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(6.0, 15, 5.0, 0.25, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(8.0, 5, 2.0, 0.15, 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
