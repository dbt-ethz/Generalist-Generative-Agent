# Created for 0007_0002_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_volumes`, generates an architectural concept model that embodies the 'rippled grid' metaphor. It establishes a grid-based framework where each cell's height is modulated by a sine wave, simulating ripples. This creates undulating surfaces that contrast with the underlying grid structure, reflecting a dynamic interplay between order and fluidity. By varying parameters like grid size, cell size, ripple amplitude, and frequency, the function produces a series of volumetric forms that capture the rhythmic spatial quality described in the design task, effectively translating the metaphor into a tangible architectural model."""

#! python 3
function_code = """def create_rippled_grid_volumes(grid_size=10, cell_size=3, ripple_amplitude=1.5, ripple_frequency=1.0):
    \"""
    Generate an architectural Concept Model based on the 'rippled grid' metaphor, using volumetric forms.

    This function constructs a grid-based series of volumes where each volume's height is modulated by
    a ripple effect. The result is a rhythmic and dynamic architectural form that contrasts the regularity
    of a grid with the fluidity of wave-like undulations.

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

    # Iterate over the grid to create volumetric cells
    for i in range(grid_size):
        for j in range(grid_size):
            # Base corner of each cell
            x = i * cell_size
            y = j * cell_size
            z = 0

            # Calculate the ripple effect for the height of the volume
            height = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Define points for the base rectangle of each volume
            base_corners = [
                rg.Point3d(x, y, z),
                rg.Point3d(x + cell_size, y, z),
                rg.Point3d(x + cell_size, y + cell_size, z),
                rg.Point3d(x, y + cell_size, z)
            ]

            # Create a surface for the base
            base_surface = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)

            # Extrude the base surface to create a volume
            if base_surface:
                extrusion_vector = rg.Vector3d(0, 0, height)
                extrusion = rg.Brep.CreateFromOffsetFace(base_surface.Faces[0], height, 0.01, True, True)
                if extrusion:
                    geometries.append(extrusion)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_volumes(grid_size=8, cell_size=2.5, ripple_amplitude=2.0, ripple_frequency=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_volumes(grid_size=6, cell_size=4, ripple_amplitude=1.0, ripple_frequency=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_volumes(grid_size=12, cell_size=1.5, ripple_amplitude=3.0, ripple_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_volumes(grid_size=5, cell_size=3.5, ripple_amplitude=2.5, ripple_frequency=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_volumes(grid_size=10, cell_size=3, ripple_amplitude=1.0, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
