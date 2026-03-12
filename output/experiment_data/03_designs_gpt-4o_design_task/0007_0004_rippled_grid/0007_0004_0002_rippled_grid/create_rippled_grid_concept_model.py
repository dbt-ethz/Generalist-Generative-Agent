# Created for 0007_0004_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model that embodies the 'rippled grid' metaphor by creating a structured yet fluid grid of surfaces. It takes parameters for grid size and ripple characteristics to produce a 3D model with undulating elements. Each grid cell's position is influenced by sine functions, introducing rhythmic displacements that simulate ripples while maintaining an underlying organized grid structure. The result is a visually dynamic model that emphasizes fluidity and movement, reflecting the metaphors essence while ensuring spatial continuity and order in the architectural design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, ripple_amplitude, ripple_frequency):
    \"""
    Create an architectural Concept Model embodying the 'rippled grid' metaphor.
    
    This function generates a 3D model based on a regular grid structure with undulating elements
    that introduce a sense of movement and fluidity while maintaining architectural order.
    
    Parameters:
    - grid_size: Tuple[int, int], the number of cells in the grid (rows, columns).
    - cell_size: float, the size of each grid cell in meters.
    - ripple_amplitude: float, maximum displacement of the ripple in meters.
    - ripple_frequency: float, frequency of the ripple pattern.
    
    Returns:
    - List[Rhino.Geometry.Brep], a list of 3D geometries representing the concept model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(42)  # Set seed for reproducibility
    
    rows, cols = grid_size
    breps = []
    
    for i in range(rows):
        for j in range(cols):
            # Calculate base position of each grid cell
            x = j * cell_size
            y = i * cell_size
            
            # Determine ripple displacement
            displacement = ripple_amplitude * math.sin(ripple_frequency * i) * math.sin(ripple_frequency * j)
            
            # Create base surface for each grid cell with rippled effect
            pt1 = rg.Point3d(x, y, displacement)
            pt2 = rg.Point3d(x + cell_size, y, displacement)
            pt3 = rg.Point3d(x + cell_size, y + cell_size, displacement)
            pt4 = rg.Point3d(x, y + cell_size, displacement)
            
            polyline = rg.Polyline([pt1, pt2, pt3, pt4, pt1])
            surface = rg.Brep.CreatePlanarBreps(polyline.ToNurbsCurve())[0]
            
            # Add the surface to the list of breps
            breps.append(surface)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 0.5, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 12), 0.75, 0.4, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((8, 8), 1.5, 0.7, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((7, 9), 1.2, 0.6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
