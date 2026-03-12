# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model that embodies the 'rippled grid' metaphor by creating a grid of modular elements with wave-like undulations. It utilizes a sinusoidal function to introduce dynamic movement into the structure, resulting in a facade or roof that appears to ripple while maintaining an underlying grid system. Parameters like grid size, spacing, wave amplitude, and frequency allow for the exploration of different spatial relationships and light interactions with the rippled surfaces. This approach balances fluidity and order, reflecting the metaphor's key traits in the architectural design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=10, grid_spacing=5.0, wave_amplitude=2.0, wave_frequency=0.5):
    \"""
    Creates an architectural Concept Model that embodies the 'rippled grid' metaphor.
    
    This function generates a series of modular elements that form an undulating facade or roof.
    It uses a grid system as the underlying framework, manipulating it to create wave-like patterns
    that suggest movement while maintaining a structured base.

    Parameters:
    grid_size (int): The number of modules in one direction of the grid.
    grid_spacing (float): The distance between the centers of adjacent grid modules.
    wave_amplitude (float): The amplitude of the wave pattern applied to the grid.
    wave_frequency (float): The frequency of the wave pattern applied to the grid.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []

    # Calculate grid points
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the base position of the grid point
            x = i * grid_spacing
            y = j * grid_spacing
            
            # Create a wave effect using a sinusoidal function
            z = wave_amplitude * math.sin(wave_frequency * (x + y))

            # Create a box at the grid point
            base_point = rg.Point3d(x, y, z)
            box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(-grid_spacing / 2, grid_spacing / 2), rg.Interval(-grid_spacing / 2, grid_spacing / 2), rg.Interval(0, wave_amplitude))
            breps.append(box.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=15, grid_spacing=4.0, wave_amplitude=3.0, wave_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=8, grid_spacing=6.0, wave_amplitude=1.5, wave_frequency=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=12, grid_spacing=5.0, wave_amplitude=2.5, wave_frequency=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=20, grid_spacing=3.0, wave_amplitude=4.0, wave_frequency=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=10, grid_spacing=5.0, wave_amplitude=2.0, wave_frequency=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
