# Created for 0007_0001_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model that embodies the "rippled grid" metaphor by creating a structured yet fluid facade or roof design. It utilizes a grid framework with specified rows and columns, where each grid module's height varies in a wave-like manner, simulating ripples. The function calculates z-offsets using a cosine wave function, producing undulating surfaces that suggest movement while maintaining the underlying order of the grid. This approach allows for dynamic spatial relationships and interactions with light, effectively translating the metaphor into a tangible architectural form."""

#! python 3
function_code = """def create_rippled_grid_concept_model(rows, cols, module_size, wave_amplitude, wave_frequency):
    \"""
    Create an architectural Concept Model that embodies the 'rippled grid' metaphor.
    
    This function generates modular elements that form an undulating facade or roof. It uses a grid
    system as the framework, manipulating it to create wave-like patterns, suggesting movement while
    maintaining structure.
    
    Parameters:
    - rows (int): Number of rows in the grid.
    - cols (int): Number of columns in the grid.
    - module_size (float): Size of each grid module in meters.
    - wave_amplitude (float): Maximum height variation in the wave effect.
    - wave_frequency (float): Frequency of the wave patterns across the grid.
    
    Returns:
    - List of Rhino.Geometry.Brep: A list of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    geometries = []
    
    # Create grid of points with wave-like z-offset
    for i in range(rows):
        for j in range(cols):
            # Calculate the position of the base point
            x = i * module_size
            y = j * module_size
            # Calculate z-offset using a cosine wave for variation
            z_offset = wave_amplitude * math.cos(wave_frequency * (x + y))
            
            # Define the corners of the module
            pt1 = rg.Point3d(x, y, 0)
            pt2 = rg.Point3d(x + module_size, y, 0)
            pt3 = rg.Point3d(x + module_size, y + module_size, z_offset)
            pt4 = rg.Point3d(x, y + module_size, z_offset)
            
            # Create the undulating surface for the module
            surface = rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt4)
            
            if surface:
                geometries.append(surface)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(10, 10, 2.0, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(5, 8, 1.5, 0.8, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(6, 12, 3.0, 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(4, 6, 1.0, 0.3, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(8, 8, 2.5, 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
