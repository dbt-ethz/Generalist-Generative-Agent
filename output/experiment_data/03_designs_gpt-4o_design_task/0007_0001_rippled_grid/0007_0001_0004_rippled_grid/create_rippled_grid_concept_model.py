# Created for 0007_0001_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model inspired by the "rippled grid" metaphor. It utilizes a grid framework to create modular elements, each featuring an undulating facade or roof that reflects wave-like patterns. By calculating wave heights based on sine functions influenced by amplitude and frequency, the function produces dynamic surfaces while ensuring structural order. The use of Rhino.Geometry constructs allows for the creation of 3D Breps, illustrating how the ripples impact both external forms and internal spatial relationships. This approach captures the essence of fluidity and rhythm within a structured design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, wave_amplitude, wave_frequency, module_size):
    \"""
    Create a 3D architectural Concept Model based on the 'rippled grid' metaphor.
    
    This function generates a series of modular elements that form an undulating facade or roof
    using a grid system as the underlying framework. The grid is manipulated to create wave-like 
    patterns, suggesting movement while maintaining a structured base.
    
    Parameters:
    - grid_size (tuple): The size of the grid (rows, columns).
    - wave_amplitude (float): The amplitude of the wave, affecting the height of the ripple.
    - wave_frequency (float): The frequency of the wave, affecting the number of ripples.
    - module_size (float): The size of each grid module.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Breps representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Seed randomness for replicability
    random.seed(42)
    
    rows, cols = grid_size
    geometries = []
    
    # Iterate over the grid to create wave-like patterns
    for i in range(rows):
        for j in range(cols):
            # Calculate the height of the wave at this grid point
            wave_height = wave_amplitude * math.sin(wave_frequency * (i + j))
            
            # Define the base of the module
            base_corners = [
                rg.Point3d(i * module_size, j * module_size, 0),
                rg.Point3d((i + 1) * module_size, j * module_size, 0),
                rg.Point3d((i + 1) * module_size, (j + 1) * module_size, 0),
                rg.Point3d(i * module_size, (j + 1) * module_size, 0)
            ]
            
            # Create a planar surface for the base
            base_surface = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.1)
            
            # Create the top surface with a ripple
            top_corners = [
                rg.Point3d(i * module_size, j * module_size, wave_height),
                rg.Point3d((i + 1) * module_size, j * module_size, wave_height),
                rg.Point3d((i + 1) * module_size, (j + 1) * module_size, wave_height),
                rg.Point3d(i * module_size, (j + 1) * module_size, wave_height)
            ]
            top_surface = rg.Brep.CreateFromCornerPoints(top_corners[0], top_corners[1], top_corners[2], top_corners[3], 0.1)
            
            # Create walls between base and top
            walls = []
            for k in range(4):
                wall = rg.Brep.CreateFromCornerPoints(base_corners[k], base_corners[(k + 1) % 4], top_corners[(k + 1) % 4], top_corners[k], 0.1)
                walls.append(wall)
            
            # Join surfaces to form a closed brep
            module_brep = rg.Brep.JoinBreps([base_surface, top_surface] + walls, 0.1)
            
            if module_brep:
                geometries.append(module_brep[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 2.0, 1.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 1.5, 0.5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 12), 3.0, 0.8, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((7, 9), 1.0, 2.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((4, 6), 2.5, 1.5, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
