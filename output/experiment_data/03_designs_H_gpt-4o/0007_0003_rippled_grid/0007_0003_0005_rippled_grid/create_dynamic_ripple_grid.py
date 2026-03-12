# Created for 0007_0003_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a series of undulating surfaces across a structured grid. It defines parameters such as grid size, ripple amplitude, and layers to simulate the dynamic movement of ripples. Using mathematical functions, it calculates the height of each grid point, creating Brep objects that represent the layered surfaces. This approach captures the interplay between order and fluidity, reflecting the rhythmic expansion and contraction of spaces, while maintaining the visibility of the underlying grid structure. The result is a visually dynamic model embodying the metaphor's essence."""

#! python 3
function_code = """def create_dynamic_ripple_grid(grid_size, cell_size, ripple_amplitude, ripple_frequency, layers, material_thickness):
    \"""
    Creates an architectural Concept Model using the 'rippled grid' metaphor with dynamic ripple effects.

    This function generates a series of Brep objects representing layered, undulating surfaces across a grid.
    The ripple effect introduces dynamic movement while maintaining an underlying structured grid, emphasizing
    transitions between compression and openness.

    Parameters:
    - grid_size (tuple): The size of the grid as (rows, columns).
    - cell_size (float): The size of each grid cell in meters.
    - ripple_amplitude (float): The peak height of the ripple effect in meters.
    - ripple_frequency (float): The frequency of the ripple effect.
    - layers (int): The number of ripple layers to generate.
    - material_thickness (float): Thickness of each surface layer in meters, representing material presence.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, cols = grid_size
    breps = []

    for layer in range(layers):
        for i in range(rows):
            for j in range(cols):
                # Calculate ripple height for each corner of the grid cell
                ripple_height = lambda x, y: ripple_amplitude * math.sin(ripple_frequency * (x + y + layer))
                
                pt1 = rg.Point3d(j * cell_size, i * cell_size, ripple_height(j, i) + layer * material_thickness)
                pt2 = rg.Point3d((j + 1) * cell_size, i * cell_size, ripple_height(j + 1, i) + layer * material_thickness)
                pt3 = rg.Point3d((j + 1) * cell_size, (i + 1) * cell_size, ripple_height(j + 1, i + 1) + layer * material_thickness)
                pt4 = rg.Point3d(j * cell_size, (i + 1) * cell_size, ripple_height(j, i + 1) + layer * material_thickness)
                
                # Create a surface from the points
                corners = [pt1, pt2, pt3, pt4, pt1]
                polyline = rg.Polyline(corners)
                surface = rg.Brep.CreateFromCornerPoints(polyline[0], polyline[1], polyline[2], polyline[3], 0.1)
                
                if surface:
                    breps.append(surface)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_ripple_grid((10, 10), 1.0, 0.5, 2.0, 3, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_ripple_grid((5, 8), 0.5, 0.3, 1.5, 4, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_ripple_grid((8, 12), 0.75, 0.4, 3.0, 2, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_ripple_grid((6, 6), 1.5, 0.4, 1.0, 5, 0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_ripple_grid((12, 15), 0.8, 0.6, 2.5, 6, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
