# Created for 0007_0002_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a structured grid foundation that incorporates dynamic, undulating surfaces. It uses mathematical sine functions to simulate ripple effects, resulting in a visual interplay between fluidity and order. The function initializes a grid of points, applying a ripple effect to their heights, and constructs vertical lines to represent the undulating surfaces. Additionally, a NURBS surface is created from these control points to encapsulate the rhythmic spatial quality. This approach emphasizes the contrast between the rigid grid and the organic ripples, fulfilling the design task effectively."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=10, grid_spacing=5, ripple_amplitude=2, ripple_frequency=0.5):
    \"""
    Creates a 3D architectural Concept Model based on the 'rippled grid' metaphor.

    The model features a structured grid foundation with undulating surfaces or layers
    that simulate the effect of ripples. This approach emphasizes the contrast between 
    the rigid grid and fluid ripples, exploring rhythmic spatial qualities.

    Inputs:
        grid_size (int): The number of grid cells in each dimension (e.g., 10x10 grid).
        grid_spacing (float): The distance between grid lines (in meters).
        ripple_amplitude (float): The maximum height of the ripple effect (in meters).
        ripple_frequency (float): The frequency of the ripple pattern (controls the number of ripples).

    Outputs:
        List of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.

    \"""

    import Rhino.Geometry as rg
    import math

    # Initialize list to hold the resulting geometries
    geometries = []

    # Create the base grid lines
    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            # Calculate the base point on the grid
            x = i * grid_spacing
            y = j * grid_spacing
            z = 0  # Base height

            # Apply a ripple effect to the height, based on a sine wave
            ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Create a point with the ripple effect applied to the z-coordinate
            point = rg.Point3d(x, y, z + ripple_effect)

            # Create a vertical line from the base grid to the ripple point
            base_point = rg.Point3d(x, y, z)
            line = rg.Line(base_point, point)

            # Add the line to the geometries list
            geometries.append(rg.Brep.CreateFromCornerPoints(base_point, point, point, base_point, 0.01))

    # Create a surface that flows over these grid points
    control_points = []
    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            z = ripple_amplitude * math.sin(ripple_frequency * (x + y))
            control_points.append(rg.Point3d(x, y, z))

    # Create nurbs surface from control points
    nurbs_surface = rg.NurbsSurface.CreateFromPoints(control_points, grid_size + 1, grid_size + 1, 3, 3)

    # Add the ripple surface to the geometries list
    geometries.append(nurbs_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=15, grid_spacing=4, ripple_amplitude=3, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=12, grid_spacing=6, ripple_amplitude=1.5, ripple_frequency=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=8, grid_spacing=3, ripple_amplitude=2.5, ripple_frequency=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=20, grid_spacing=2, ripple_amplitude=4, ripple_frequency=0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=10, grid_spacing=5, ripple_amplitude=1, ripple_frequency=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
