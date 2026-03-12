# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model inspired by the metaphor of a "rippled grid." It creates a grid of undulating surfaces using sine wave calculations to simulate the dynamic, rhythmic quality of ripples. By defining grid size, cell size, ripple amplitude, and frequency, the function creates a variety of surface geometries that reflect both structured order and fluid movement. The resulting Brep objects represent the concept model, embodying the metaphor's essence through a visually engaging and spatially dynamic design, suitable for exploration in architectural contexts."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=10, cell_size=5, ripple_amplitude=2, ripple_frequency=2):
    \"""
    Generates a concept model based on the 'rippled grid' metaphor. This model consists of a grid of undulating surfaces
    that mimic the effect of ripples propagating across a uniform grid. The undulations are generated using sine waves 
    to create a dynamic and rhythmic spatial quality.

    Parameters:
    grid_size (int): The number of cells along one axis of the grid. The grid is square, so this applies to both axes.
    cell_size (float): The size of each cell in the grid in meters.
    ripple_amplitude (float): The maximum height variation of the ripples in meters.
    ripple_frequency (float): The frequency of the ripple pattern, affecting the number of peaks and troughs across the grid.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the surfaces of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Initialize random seed for replicability
    random.seed(42)

    breps = []
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the center of the cell
            x = i * cell_size
            y = j * cell_size

            # Create the corners of the cell
            corners = []
            for u in range(2):
                for v in range(2):
                    # Calculate the ripple effect on the z coordinate
                    z = ripple_amplitude * math.sin(ripple_frequency * (x + u * cell_size) / grid_size) * \
                        math.sin(ripple_frequency * (y + v * cell_size) / grid_size)
                    corners.append(rg.Point3d(x + u * cell_size, y + v * cell_size, z))

            # Create a surface from the corner points
            surface = rg.NurbsSurface.CreateFromCorners(corners[0], corners[1], corners[3], corners[2])
            if surface:
                brep = rg.Brep.CreateFromSurface(surface)
                if brep:
                    breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=15, cell_size=3, ripple_amplitude=1, ripple_frequency=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=8, cell_size=4, ripple_amplitude=1.5, ripple_frequency=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=12, cell_size=6, ripple_amplitude=3, ripple_frequency=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=20, cell_size=2, ripple_amplitude=0.5, ripple_frequency=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=10, cell_size=5, ripple_amplitude=4, ripple_frequency=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
