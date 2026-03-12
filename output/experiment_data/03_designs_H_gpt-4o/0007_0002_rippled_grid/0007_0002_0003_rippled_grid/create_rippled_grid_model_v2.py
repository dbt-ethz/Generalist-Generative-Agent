# Created for 0007_0002_rippled_grid.json

""" Summary:
The function `create_rippled_grid_model_v2` generates an architectural concept model that embodies the "rippled grid" metaphor by creating a structured grid overlaid with undulating ribbed structures. It establishes a staggered grid layout where each cell's z-coordinate is influenced by a sine wave function, simulating ripples. This dynamic interaction introduces a rhythmic spatial quality, balancing fluidity with the underlying grid's rigidity. The ribbed surfaces derived from these calculations reflect the metaphor's essence, emphasizing movement and order, while varying parameters like ripple amplitude and frequency allow for exploration of different design expressions consistent with the metaphor's themes."""

#! python 3
function_code = """def create_rippled_grid_model_v2(grid_size=10, cell_size=2, ripple_amplitude=1.0, ripple_frequency=2.0):
    \"""
    Create an architectural Concept Model based on the 'rippled grid' metaphor with a different approach.
    
    This function generates a structured grid overlaid with a series of wave-like ribbed structures
    that simulate the effect of ripples. The model emphasizes the spatial rhythm by using a staggered
    grid that introduces undulating ribbed patterns to create a dynamic yet ordered structure.

    Parameters:
    - grid_size (int): The number of cells along one edge of the square grid.
    - cell_size (float): The size of each cell in the grid (in meters).
    - ripple_amplitude (float): The amplitude of the ripple effect (in meters).
    - ripple_frequency (float): The frequency of the ripple effect.
    
    Returns:
    List of 3D geometries (Rhino.Geometry.Brep) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create a list to store the resulting geometries
    geometries = []

    # Define the base grid dimensions
    grid_dim = grid_size * cell_size

    # Create staggered grid points with ripple effect to form ribbed structures
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the base x and y positions with a staggered offset
            x = i * cell_size + (j % 2) * (cell_size / 2)
            y = j * cell_size
            
            # Apply the ripple effect to the z-coordinate
            z = ripple_amplitude * math.sin(ripple_frequency * (x + y))
            
            # Create rib points on either side of the base point
            left_rib_point = rg.Point3d(x - cell_size / 4, y, z)
            right_rib_point = rg.Point3d(x + cell_size / 4, y, z)

            # Create lines representing the ribs
            rib_line = rg.Line(left_rib_point, right_rib_point)
            
            # Create a surface from the rib line to form a ribbed structure
            rib_surface = rg.Surface.CreateExtrusion(rib_line.ToNurbsCurve(), rg.Vector3d(0, 0, cell_size))
            
            # Convert the surface to a Brep and add to the geometries list
            rib_brep = rg.Brep.CreateFromSurface(rib_surface)
            if rib_brep:
                geometries.append(rib_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_model_v2(grid_size=8, cell_size=3, ripple_amplitude=1.5, ripple_frequency=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_model_v2(grid_size=6, cell_size=2.5, ripple_amplitude=2.0, ripple_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_model_v2(grid_size=12, cell_size=1.0, ripple_amplitude=0.5, ripple_frequency=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_model_v2(grid_size=10, cell_size=1.5, ripple_amplitude=2.5, ripple_frequency=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_model_v2(grid_size=5, cell_size=4, ripple_amplitude=1.0, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
