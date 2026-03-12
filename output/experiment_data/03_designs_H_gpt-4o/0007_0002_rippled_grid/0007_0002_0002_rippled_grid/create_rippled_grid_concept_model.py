# Created for 0007_0002_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model that embodies the "rippled grid" metaphor by combining structured grid elements with dynamic, undulating surfaces. It establishes a grid of points in 3D space, where the z-coordinates are modified to create a ripple effect based on sine wave calculations. These points are then used to create lofted surfaces between adjacent rows, enhancing the visual interplay of order (the grid) and fluidity (the rippling surface). The model effectively translates the metaphor into a physical form, illustrating rhythmic spatial qualities and dynamic movement within a structured framework."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=8, grid_spacing=4, ripple_amplitude=1.5, ripple_frequency=1.2):
    \"""
    Generates a concept model based on the 'rippled grid' metaphor. This model features a structured grid influenced by
    undulating, ripple-like surfaces, which create dynamic spatial qualities and a rhythmic interplay between order and
    movement. The approach employs a lofted surface between ripple points to enhance the ripple effect.

    Parameters:
    grid_size (int): The number of grid cells along one dimension of the grid.
    grid_spacing (float): The distance between grid lines in meters.
    ripple_amplitude (float): The height amplitude of the ripple effect in meters.
    ripple_frequency (float): The frequency of the ripples across the grid surface.

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import math

    # List to store the resulting geometries
    geometries = []

    # Create a 2D grid of points with ripple effect applied to the z-axis
    points = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            x = i * grid_spacing
            y = j * grid_spacing
            z = ripple_amplitude * math.sin(ripple_frequency * (x + y))
            row.append(rg.Point3d(x, y, z))
        points.append(row)

    # Create lofted surfaces between adjacent rows to form the ripple effect
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            # Define points for lofting
            pt1 = points[i][j]
            pt2 = points[i+1][j]
            pt3 = points[i+1][j+1]
            pt4 = points[i][j+1]

            # Create interpolated curves between consecutive points
            curve1 = rg.NurbsCurve.CreateInterpolatedCurve([pt1, pt2], 3)
            curve2 = rg.NurbsCurve.CreateInterpolatedCurve([pt4, pt3], 3)

            # Loft the curves to create the surface
            loft_surfaces = rg.Brep.CreateFromLoft([curve1, curve2], rg.Point3d.Unset, rg.Point3d.Unset, 
                                                   rg.LoftType.Normal, False)
            if loft_surfaces:
                geometries.extend(loft_surfaces)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=10, grid_spacing=5, ripple_amplitude=2.0, ripple_frequency=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=6, grid_spacing=3, ripple_amplitude=1.0, ripple_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=12, grid_spacing=2, ripple_amplitude=3.0, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=8, grid_spacing=4, ripple_amplitude=2.5, ripple_frequency=1.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=5, grid_spacing=6, ripple_amplitude=1.0, ripple_frequency=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
