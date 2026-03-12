# Created for 0007_0005_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model that embodies the "rippled grid" metaphor by creating a structured grid overlaid with undulating surfaces. It uses specified parameters like grid size, spacing, wave amplitude, and frequency to create a series of points that simulate wave-like undulations in the Z-direction. These points form a surface that reflects the dynamic nature of ripples while maintaining an organized grid structure. The resulting 3D geometries emphasize the harmony between fluid movement and structured order, effectively visualizing the interplay between these contrasting qualities in architectural design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, grid_spacing, wave_amplitude, wave_frequency, vertical_extrusion, seed=42):
    \"""
    Generates an architectural Concept Model embodying the 'rippled grid' metaphor by creating undulating surfaces
    overlaying a regular grid structure. The model emphasizes the dynamic interplay between structured order and fluidity.

    Parameters:
    grid_size (tuple): A tuple of two integers (rows, cols) representing the number of grid cells in each direction.
    grid_spacing (float): The spacing between grid lines in meters.
    wave_amplitude (float): The amplitude of the wave undulations in meters.
    wave_frequency (float): The frequency of the wave undulations.
    vertical_extrusion (float): The height to which each undulating surface is extruded to create a solid volume.
    seed (int): Seed for randomness to ensure replicability.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set the random seed for replicability
    random.seed(seed)

    breps = []
    rows, cols = grid_size

    # Create the base grid of points with rippled z-coordinates
    grid_points = []
    for i in range(rows + 1):
        for j in range(cols + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            z = wave_amplitude * math.sin(wave_frequency * (x + y))
            grid_points.append(rg.Point3d(x, y, z))

    # Create surfaces from the grid points and extrude them into solids
    for i in range(rows):
        for j in range(cols):
            # Define the corners of the grid cell
            pt0 = grid_points[i * (cols + 1) + j]
            pt1 = grid_points[i * (cols + 1) + (j + 1)]
            pt2 = grid_points[(i + 1) * (cols + 1) + (j + 1)]
            pt3 = grid_points[(i + 1) * (cols + 1) + j]

            # Create a surface from these points
            surface = rg.NurbsSurface.CreateFromCorners(pt0, pt1, pt2, pt3)
            
            # Extrude the surface to create a volume
            if surface:
                # Use the surface's edges as boundary curves
                boundary_curves = surface.ToBrep().DuplicateEdgeCurves()
                if boundary_curves:
                    for curve in boundary_curves:
                        extrusion = rg.Extrusion.Create(curve, vertical_extrusion, True)
                        brep = extrusion.ToBrep()
                        if brep:
                            breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 7), 0.5, 1.0, 3.0, 2.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((8, 12), 0.75, 0.8, 1.5, 4.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((6, 6), 1.5, 0.3, 4.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((12, 12), 1.2, 0.6, 2.5, 5.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
