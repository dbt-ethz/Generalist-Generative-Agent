# Created for 0007_0005_rippled_grid.json

""" Summary:
The provided function creates an architectural concept model inspired by the "rippled grid" metaphor. This metaphor emphasizes a dynamic and rhythmic spatial quality, merging structured grid patterns with fluid, wave-like forms. The function generates a 3D model by defining a grid of points, where each point's height is determined through a sine wave, simulating undulations. By creating lofted surfaces between these points, it achieves smooth transitions that articulate the ripple effect while maintaining an underlying grid order. The output is a series of geometries that visually embody the interplay between structured order and dynamic movement, reflecting the metaphor's essence."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, wave_amplitude, wave_frequency, grid_spacing, surface_smoothness):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor by generating a series of undulating
    surfaces overlaying a regular grid structure. The model emphasizes the ripple effect through smooth transitions
    between wave peaks and troughs, maintaining a balance between fluidity and structural order.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of grid cells in the X and Y directions.
    - wave_amplitude: Float specifying the maximum height of the wave undulations.
    - wave_frequency: Float specifying the frequency of the wave pattern.
    - grid_spacing: Float specifying the distance between grid lines.
    - surface_smoothness: Float defining the smoothness of the transitions between peaks and troughs.

    Returns:
    - List of Rhino.Geometry.Brep representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize the list to hold the geometries
    geometries = []

    # Create the base grid points
    grid_points = []
    for i in range(grid_size[0] + 1):
        for j in range(grid_size[1] + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            z = wave_amplitude * math.sin(wave_frequency * (x + y))
            grid_points.append(rg.Point3d(x, y, z))

    # Create undulating surfaces based on the grid points
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Define the corners of the grid cell
            pt0 = grid_points[i * (grid_size[1] + 1) + j]
            pt1 = grid_points[i * (grid_size[1] + 1) + (j + 1)]
            pt2 = grid_points[(i + 1) * (grid_size[1] + 1) + (j + 1)]
            pt3 = grid_points[(i + 1) * (grid_size[1] + 1) + j]

            # Create a surface using lofted curves for smooth transitions
            curve0 = rg.Curve.CreateInterpolatedCurve([pt0, pt1], surface_smoothness)
            curve1 = rg.Curve.CreateInterpolatedCurve([pt3, pt2], surface_smoothness)
            loft = rg.Brep.CreateFromLoft([curve0, curve1], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            
            # Add the surface to the list of geometries
            if loft:
                geometries.extend(loft)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 5.0, 2.0, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((8, 12), 3.0, 1.5, 0.8, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((15, 15), 4.0, 3.0, 1.2, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((12, 8), 6.0, 2.5, 1.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((5, 5), 2.0, 1.0, 0.5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
