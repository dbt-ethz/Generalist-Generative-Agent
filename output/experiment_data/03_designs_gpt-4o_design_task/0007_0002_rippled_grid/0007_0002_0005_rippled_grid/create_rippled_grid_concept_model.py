# Created for 0007_0002_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model based on the "rippled grid" metaphor by establishing a structured grid that serves as a foundation. It employs mathematical sine functions to create undulating surfaces, simulating the ripple effect across the grid. The model contrasts rigid grid lines with fluid, dynamic curves, reflecting the interplay of order and movement. By defining parameters like grid size, spacing, ripple amplitude, and frequency, the function allows for the exploration of various spatial qualities, ultimately producing 3D geometries that embody the rhythmic and dynamic essence of the metaphor."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=10, grid_spacing=5, ripple_amplitude=2, ripple_frequency=3):
    \"""
    Generates a concept model based on the 'rippled grid' metaphor. This model features a structured grid that is 
    influenced by undulating, ripple-like surfaces, which create dynamic spatial qualities and a rhythmic interplay 
    between order and movement.

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
    import random

    # Seed for reproducibility
    random.seed(42)
    
    geometries = []

    # Create base grid points
    points = []
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * grid_spacing
            y = j * grid_spacing
            z = 0
            points.append(rg.Point3d(x, y, z))

    # Create ripple surfaces
    for point in points:
        x, y, z = point.X, point.Y, point.Z
        ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + y))
        ripple_point = rg.Point3d(x, y, ripple_effect)
        
        # Create a simple undulating surface using a circle for simplicity
        circle = rg.Circle(ripple_point, grid_spacing / 2)
        circle_surface = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]
        
        # Add to list of geometries
        geometries.append(circle_surface)

    # Optionally, create connecting ribs or structural elements
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            # Create vertical ribs
            pt1 = points[i * grid_size + j]
            pt2 = points[i * grid_size + (j + 1)]
            pt3 = points[(i + 1) * grid_size + j]
            
            line1 = rg.Line(pt1, pt2)
            line2 = rg.Line(pt1, pt3)
            
            geometries.append(rg.Brep.CreateFromSurface(rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt1)))

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=12, grid_spacing=4, ripple_amplitude=3, ripple_frequency=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=8, grid_spacing=6, ripple_amplitude=1.5, ripple_frequency=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=15, grid_spacing=3, ripple_amplitude=5, ripple_frequency=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=10, grid_spacing=7, ripple_amplitude=2.5, ripple_frequency=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=5, grid_spacing=10, ripple_amplitude=4, ripple_frequency=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
