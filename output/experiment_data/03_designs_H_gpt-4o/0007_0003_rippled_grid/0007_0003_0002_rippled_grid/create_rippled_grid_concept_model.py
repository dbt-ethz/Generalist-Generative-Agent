# Created for 0007_0003_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model inspired by the 'rippled grid' metaphor. It creates a series of undulating surfaces across a structured grid, reflecting the dynamic interplay of order and fluidity. By calculating z-coordinates using a cosine wave, the function simulates the ripple effect, resulting in a rhythmic pattern of peaks and troughs. The model retains visibility of the underlying grid, while varied layer heights and wave lengths emphasize spatial transitions. This approach effectively captures the essence of movement and flow within a cohesive architectural framework, aligning with the design task's requirements."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, grid_spacing, peak_height, wave_length, num_layers):
    \"""
    Generates an architectural Concept Model embodying the 'rippled grid' metaphor through a series of layered, undulating surfaces.

    The function captures the rhythmic movement of the ripple effect while ensuring the underlying grid structure is visible.
    Each layer is designed to reflect the dynamic interaction between order and movement, emphasizing spatial transitions.

    Parameters:
    - grid_size (tuple): The dimensions of the grid as (rows, columns).
    - grid_spacing (float): The distance between each grid point in meters.
    - peak_height (float): The maximum height of the ripples.
    - wave_length (float): The wavelength of the ripples.
    - num_layers (int): The number of layers of undulating surfaces.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, cols = grid_size
    geometries = []

    for layer in range(num_layers):
        z_offset = layer * (peak_height / num_layers)
        points = []
        
        for i in range(rows + 1):
            row_points = []
            for j in range(cols + 1):
                x = j * grid_spacing
                y = i * grid_spacing
                # Calculate the z-coordinate using a cosine wave with a phase shift for ripple effect
                z = peak_height * math.cos((x + y) / wave_length + layer * math.pi / num_layers) + z_offset
                row_points.append(rg.Point3d(x, y, z))
            points.append(row_points)

        # Create surface from points grid
        for i in range(rows):
            for j in range(cols):
                pt0 = points[i][j]
                pt1 = points[i][j+1]
                pt2 = points[i+1][j+1]
                pt3 = points[i+1][j]
                
                # Create a Nurbs surface from the four corner points
                nurbs_surface = rg.NurbsSurface.CreateFromCorners(pt0, pt1, pt2, pt3)
                if nurbs_surface:
                    brep = nurbs_surface.ToBrep()
                    geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 5.0, 2.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((8, 12), 0.5, 3.0, 1.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 6), 0.8, 4.0, 3.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((12, 15), 0.75, 6.0, 2.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((5, 7), 0.6, 2.5, 1.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
