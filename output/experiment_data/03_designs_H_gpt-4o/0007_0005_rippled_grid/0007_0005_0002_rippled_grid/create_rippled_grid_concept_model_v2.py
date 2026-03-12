# Created for 0007_0005_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model_v2` generates an architectural concept model by creating a 3D representation that embodies the metaphor of a "rippled grid". It constructs a grid of points where each point's elevation (z-value) is defined by a sine wave function, creating undulating surfaces that mimic the dynamic qualities of waves. By lofting curves between these points, the function produces fluid surfaces that contrast with the underlying regular grid structure, thus illustrating the interplay between order and movement. The result is a visually engaging model that reflects the metaphor's principles of rhythm and spatial fluidity."""

#! python 3
function_code = """def create_rippled_grid_concept_model_v2(grid_size=(10, 10), grid_spacing=5.0, wave_amplitude=2.0, wave_frequency=0.4):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor. This version uses a lofted surface
    approach to create continuous undulating forms overlaying a regular grid structure. It aims to convey a
    dynamic interplay between structured grid and wave-like forms with fluid transitions between the elements.

    Parameters:
    grid_size (tuple): A tuple of two integers (rows, cols) representing the number of grid divisions.
    grid_spacing (float): The spacing between grid lines in meters.
    wave_amplitude (float): The amplitude of the wave undulations in meters.
    wave_frequency (float): The frequency of the wave undulations.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create a list to store the lofted Brep geometries
    breps = []

    # Generate the base grid points with undulating z-values
    grid_points = []
    for i in range(grid_size[0] + 1):
        row_points = []
        for j in range(grid_size[1] + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            z = wave_amplitude * math.sin(wave_frequency * (x ** 2 + y ** 2))
            point = rg.Point3d(x, y, z)
            row_points.append(point)
        grid_points.append(row_points)

    # Create lofted surfaces from the grid points
    for j in range(grid_size[1]):
        curves = []
        for i in range(grid_size[0]):
            # Create a polyline from the vertical sequence of points
            polyline_points = [grid_points[i][j], grid_points[i][j+1], grid_points[i+1][j+1], grid_points[i+1][j]]
            polyline = rg.Polyline(polyline_points)
            curve = polyline.ToNurbsCurve()
            curves.append(curve)

        # Create a lofted surface through the curves
        loft = rg.Brep.CreateFromLoft(curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            breps.extend(loft)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model_v2(grid_size=(15, 15), grid_spacing=3.0, wave_amplitude=1.5, wave_frequency=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model_v2(grid_size=(20, 10), grid_spacing=4.0, wave_amplitude=3.0, wave_frequency=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model_v2(grid_size=(12, 12), grid_spacing=6.0, wave_amplitude=2.5, wave_frequency=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model_v2(grid_size=(8, 8), grid_spacing=2.0, wave_amplitude=4.0, wave_frequency=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model_v2(grid_size=(5, 5), grid_spacing=10.0, wave_amplitude=1.0, wave_frequency=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
