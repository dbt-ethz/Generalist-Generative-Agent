# Created for 0007_0002_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a structured grid and overlaying undulating surfaces that simulate ripples. It establishes a 3D grid of points influenced by sine wave calculations, which determine the vertical displacement (z-coordinates) to create the ripple effect. The function constructs mesh faces from these points, resulting in geometries that embody the interplay between fluidity and order. By adjusting parameters like grid size, spacing, ripple amplitude, and frequency, the model explores spatial dynamics, ensuring a harmonious balance between the rigid grid framework and the organic rippling forms."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=10, grid_spacing=5, ripple_amplitude=2, ripple_frequency=1.5):
    \"""
    Generates an architectural Concept Model based on the 'rippled grid' metaphor.
    
    This function constructs a base grid structure and superimposes a series of undulating mesh surfaces
    that simulate ripple effects, achieving a dynamic and rhythmic spatial form. The design explores the
    tension between the rigid grid and fluid ripple patterns.

    Parameters:
    - grid_size (int): The number of cells along the edge of the grid.
    - grid_spacing (float): The distance between each grid point (in meters).
    - ripple_amplitude (float): The maximum deviation of the ripple effect (in meters).
    - ripple_frequency (float): The number of ripple cycles across the grid.

    Returns:
    List of 3D geometries (Rhino.Geometry.Brep) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize the list to hold the geometries
    geometries = []

    # Create a 3D grid of points
    points = []
    for i in range(grid_size + 1):
        row = []
        for j in range(grid_size + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            # Calculate the ripple effect on the z-coordinate
            z = ripple_amplitude * math.sin(ripple_frequency * (x + y))
            row.append(rg.Point3d(x, y, z))
        points.append(row)

    # Create mesh faces based on the points
    for i in range(grid_size):
        for j in range(grid_size):
            # Define the corners of each mesh face
            p1 = points[i][j]
            p2 = points[i + 1][j]
            p3 = points[i + 1][j + 1]
            p4 = points[i][j + 1]

            # Create a mesh face and add it to the list
            mesh = rg.Mesh()
            mesh.Vertices.Add(p1)
            mesh.Vertices.Add(p2)
            mesh.Vertices.Add(p3)
            mesh.Vertices.Add(p4)
            mesh.Faces.AddFace(0, 1, 2, 3)
            mesh.Normals.ComputeNormals()
            mesh.Compact()
            geometries.append(mesh)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=8, grid_spacing=4, ripple_amplitude=3, ripple_frequency=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=12, grid_spacing=6, ripple_amplitude=1.5, ripple_frequency=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=5, grid_spacing=2, ripple_amplitude=4, ripple_frequency=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=15, grid_spacing=3, ripple_amplitude=2.5, ripple_frequency=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=10, grid_spacing=5, ripple_amplitude=3, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
