# Created for 0007_0001_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model inspired by the "rippled grid" metaphor. It constructs a grid-based structure where each module undergoes a wave-like transformation, creating dynamic surfaces that suggest movement. The parameters define the grid's dimensions and the amplitude and frequency of the ripples, allowing for variations in the facade's undulation. By manipulating the z-coordinates using a cosine function, the function achieves a balance between fluidity and order. The resulting 3D geometries illustrate how these ripples influence both the exterior form and interior spatial relationships, enhancing the building's rhythmic and structured aesthetic."""

#! python 3
function_code = """def create_rippled_grid_concept_model(rows, columns, module_size, wave_amplitude, wave_frequency):
    \"""
    Generates a 3D architectural Concept Model based on the 'rippled grid' metaphor.
    
    This function creates a series of modules forming an undulating facade or roof by using a grid system 
    as an underlying framework. It manipulates the grid to create wave-like patterns, suggesting movement 
    while maintaining structural base.

    Parameters:
    - rows (int): Number of rows in the grid.
    - columns (int): Number of columns in the grid.
    - module_size (float): Size of each grid module in meters.
    - wave_amplitude (float): Maximum height variation for the ripple effect.
    - wave_frequency (float): Frequency of the ripple effect across the grid.

    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    geometries = []

    # Iterate over the grid to create ripple effect
    for i in range(rows):
        for j in range(columns):
            # Base position for the module
            x = i * module_size
            y = j * module_size
            z_base = 0

            # Calculate the ripple height using a cosine wave
            z_ripple = wave_amplitude * math.cos(wave_frequency * (i + j))

            # Define the corners of the top ripple surface
            top_corners = [
                rg.Point3d(x, y, z_base + z_ripple),
                rg.Point3d(x + module_size, y, z_base + z_ripple),
                rg.Point3d(x + module_size, y + module_size, z_base + z_ripple),
                rg.Point3d(x, y + module_size, z_base + z_ripple)
            ]

            # Create the top surface with the ripple
            top_surface = rg.Brep.CreateFromCornerPoints(top_corners[0], top_corners[1], top_corners[2], top_corners[3], 0.1)

            # Create walls for the module
            walls = []
            for k in range(4):
                start_index = k
                end_index = (k + 1) % 4
                wall = rg.Brep.CreateFromCornerPoints(
                    rg.Point3d(x + (k % 2) * module_size, y + (k // 2) * module_size, z_base),
                    rg.Point3d(x + (end_index % 2) * module_size, y + (end_index // 2) * module_size, z_base),
                    top_corners[end_index],
                    top_corners[start_index],
                    0.1
                )
                if wall:
                    walls.append(wall)

            # Join the top surface and walls into a single brep
            module_brep = rg.Brep.JoinBreps([top_surface] + walls, 0.1)
            if module_brep:
                geometries.append(module_brep[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(5, 5, 2.0, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(10, 10, 1.5, 2.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(4, 6, 1.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(8, 8, 3.0, 1.5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(6, 4, 2.5, 0.8, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
