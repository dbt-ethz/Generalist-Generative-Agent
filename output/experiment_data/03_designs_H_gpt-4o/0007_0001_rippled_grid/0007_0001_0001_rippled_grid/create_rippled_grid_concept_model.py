# Created for 0007_0001_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a 3D array of modular elements that exhibit undulating surfaces. It uses a defined grid system to establish a structured framework, where each module's height is influenced by sine functions to create wave-like patterns, reflecting both movement and rhythm. The function incorporates parameters such as grid size, module size, and ripple characteristics to manipulate the geometry, ensuring a balance between fluidity and order. This results in a dynamic facade or roofline, enhancing spatial relationships and light interaction within the design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, module_size, ripple_amplitude, ripple_frequency, seed=42):
    \"""
    Create a 3D architectural Concept Model based on the 'rippled grid' metaphor.

    This function generates a series of modular elements that form an undulating facade or roof
    using a grid system as the underlying framework. The grid is manipulated to create wave-like 
    patterns, suggesting movement while maintaining a structured base.

    Parameters:
    - grid_size (tuple): The size of the grid (rows, columns).
    - module_size (float): The size of each grid module.
    - ripple_amplitude (float): The amplitude of the ripple, affecting the height of the undulation.
    - ripple_frequency (float): The frequency of the ripple, affecting the number of undulations.
    - seed (int): Seed for random number generator to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Breps representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed randomness for replicability
    random.seed(seed)

    rows, cols = grid_size
    geometries = []

    # Iterate over the grid to create ripple-like patterns
    for i in range(rows):
        for j in range(cols):
            # Calculate the ripple height at this grid point
            ripple_height = ripple_amplitude * math.sin(ripple_frequency * (i * module_size + j * module_size))

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
                rg.Point3d(i * module_size, j * module_size, ripple_height),
                rg.Point3d((i + 1) * module_size, j * module_size, ripple_height),
                rg.Point3d((i + 1) * module_size, (j + 1) * module_size, ripple_height),
                rg.Point3d(i * module_size, (j + 1) * module_size, ripple_height)
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
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 7), 0.8, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((8, 8), 1.5, 0.4, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((6, 9), 1.2, 0.6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((12, 12), 1.0, 0.7, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
