# Created for 0007_0003_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model by simulating a dynamic 'rippled grid' metaphor. It creates a series of undulating surfaces arranged in a structured grid, introducing a rhythmic pattern that reflects the metaphor's essence. The parameters define the grid's dimensions, the distance between planes, and the characteristics of the ripple effect, such as amplitude and frequency. Using a sine wave, the function calculates the height of each surface, resulting in a visual interplay of peaks and troughs. This approach captures both fluidity and order, embodying the metaphors spatial qualities effectively."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, plane_distance, ripple_amplitude, ripple_frequency, seed):
    \"""
    Creates a 3D architectural Concept Model based on the 'rippled grid' metaphor.
    
    The function generates a series of undulating surfaces arranged in a grid pattern,
    simulating the effect of ripples across a structured grid. This captures the dynamic
    and rhythmic essence of the metaphor, with spaces expanding and contracting to reflect
    the ripple effect.

    Parameters:
    - grid_size (tuple): The dimensions of the grid as (rows, columns).
    - plane_distance (float): The distance between each grid plane.
    - ripple_amplitude (float): The maximum height of the ripple effect.
    - ripple_frequency (float): The frequency of the ripples across the grid.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the rippled surfaces.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    
    rows, cols = grid_size
    base_planes = []
    
    # Create base grid planes
    for i in range(rows):
        for j in range(cols):
            # Calculate the base position for each plane
            origin = rg.Point3d(j * plane_distance, i * plane_distance, 0)
            plane = rg.Plane(origin, rg.Vector3d.ZAxis)
            
            # Add ripple effect using a sine wave pattern
            def ripple_function(x, y):
                return ripple_amplitude * math.sin(ripple_frequency * (x + y))
            
            # Create a surface for each plane with the ripple effect
            corners = [rg.Point3d(j * plane_distance, i * plane_distance, ripple_function(j * plane_distance, i * plane_distance)),
                       rg.Point3d((j+1) * plane_distance, i * plane_distance, ripple_function((j+1) * plane_distance, i * plane_distance)),
                       rg.Point3d((j+1) * plane_distance, (i+1) * plane_distance, ripple_function((j+1) * plane_distance, (i+1) * plane_distance)),
                       rg.Point3d(j * plane_distance, (i+1) * plane_distance, ripple_function(j * plane_distance, (i+1) * plane_distance))]
            
            # Create a Brep surface from corners
            surface = rg.NurbsSurface.CreateFromCorners(corners[0], corners[1], corners[2], corners[3])
            brep = surface.ToBrep()
            base_planes.append(brep)

    return base_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((5, 5), 10.0, 2.0, 1.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((3, 4), 8.0, 1.5, 0.5, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 6), 12.0, 3.0, 2.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((4, 7), 15.0, 2.5, 1.5, 57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((2, 3), 5.0, 1.0, 0.8, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
