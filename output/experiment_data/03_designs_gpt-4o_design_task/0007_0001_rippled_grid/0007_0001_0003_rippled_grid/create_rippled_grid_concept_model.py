# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model that embodies the "rippled grid" metaphor by creating a grid-based structure with undulating surfaces. It defines a grid of modular elements, where each cell's height is influenced by sine wave calculations, introducing wave-like variations in the facade or roof. The parameters grid size, cell size, wave amplitude, and wave frequency allow for customization of the design's fluidity and order. The output consists of 3D geometries that reflect the dynamic and rhythmic qualities of ripples while adhering to an underlying grid framework, balancing structure and movement."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, wave_amplitude, wave_frequency):
    \"""
    Create an architectural Concept Model that embodies the 'rippled grid' metaphor.
    
    This function generates a series of modular elements that form an undulating facade or roof.
    The model explores how ripple patterns can influence both exterior form and interior spatial 
    relationships, maintaining a balance between fluidity and order.

    :param grid_size: Tuple (int, int) representing the number of cells in the grid (rows, columns).
    :param cell_size: Float representing the size of each grid cell in meters.
    :param wave_amplitude: Float representing the amplitude of the wave effect in meters.
    :param wave_frequency: Float representing the frequency of the wave effect.
    :return: List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    rows, cols = grid_size
    geometries = []
    
    for i in range(rows):
        for j in range(cols):
            # Calculate the base point of the cell
            base_point = rg.Point3d(i * cell_size, j * cell_size, 0)
            
            # Calculate the offset in the Z direction to create the ripple effect
            z_offset = wave_amplitude * math.sin(wave_frequency * (i + j))
            
            # Create the ripple surface for the current cell
            pt1 = base_point
            pt2 = rg.Point3d(base_point.X + cell_size, base_point.Y, z_offset)
            pt3 = rg.Point3d(base_point.X + cell_size, base_point.Y + cell_size, z_offset)
            pt4 = rg.Point3d(base_point.X, base_point.Y + cell_size, 0)
            
            # Create a surface from the points
            surface = rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt4)
            
            # Add the surface to the geometry list
            if surface:
                geometries.append(surface)
    
    return geometries"""

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
    geometry = create_rippled_grid_concept_model((5, 15), 0.8, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((8, 8), 1.5, 0.4, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((12, 6), 1.2, 0.6, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((6, 12), 1.0, 0.7, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
