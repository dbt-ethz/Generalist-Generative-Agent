# Created for 0007_0004_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model based on the 'rippled grid' metaphor by creating a structured grid of 3D meshes. Each mesh cell's vertices are displaced vertically according to a mathematical sine and cosine function, simulating ripple effects while preserving the underlying grid's order. This approach embodies the metaphor's dynamic and rhythmic quality through undulating surfaces, suggesting fluid movement and spatial flow. By manipulating parameters like ripple amplitude and frequency, the model illustrates how spaces can transition smoothly, thereby exploring the visual impact of the rippled grid on the building's overall form."""

#! python 3
function_code = """def create_rippled_grid_concept_model(rows, columns, cell_size, ripple_amplitude, ripple_frequency):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.

    This function generates a 3D model with a grid structure where each cell is defined by a mesh.
    The mesh vertices are displaced vertically to create a ripple effect across the grid, 
    simulating fluid movement while maintaining an underlying order.

    Parameters:
    rows (int): Number of rows in the grid.
    columns (int): Number of columns in the grid.
    cell_size (float): The size of each cell in the grid in meters.
    ripple_amplitude (float): Maximum vertical displacement of the ripple in meters.
    ripple_frequency (float): Frequency of the ripple effect.

    Returns:
    List[Rhino.Geometry.Mesh]: A list of mesh geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    meshes = []

    # Create the grid of points
    for i in range(rows):
        for j in range(columns):
            x = j * cell_size
            y = i * cell_size

            # Calculate ripple effect for vertices of the mesh
            vertices = []
            for dx in [0, cell_size]:
                for dy in [0, cell_size]:
                    ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + dx) * 0.1) * math.cos(ripple_frequency * (y + dy) * 0.1)
                    vertices.append(rg.Point3d(x + dx, y + dy, ripple_effect))

            # Create a mesh for each grid cell
            mesh = rg.Mesh()
            mesh.Vertices.Add(vertices[0])
            mesh.Vertices.Add(vertices[1])
            mesh.Vertices.Add(vertices[2])
            mesh.Vertices.Add(vertices[3])
            mesh.Faces.AddFace(0, 1, 2, 3)

            mesh.Normals.ComputeNormals()
            mesh.Compact()

            meshes.append(mesh)

    return meshes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(10, 10, 2.0, 1.5, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(5, 8, 1.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(7, 12, 1.5, 2.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(6, 6, 3.0, 2.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(8, 10, 1.0, 1.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
