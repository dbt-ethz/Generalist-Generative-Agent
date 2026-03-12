# Created for 0007_0003_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model reflecting the 'rippled grid' metaphor by creating a series of layered, undulating surfaces over a structured grid. It employs parameters such as grid size, spacing, and ripple characteristics to define the spatial qualities of the model. The function calculates the height of each layer using a sine wave, simulating the dynamic ripple effect and allowing for variations in elevation across the grid. This interplay of structured order and fluid movement results in a visually harmonious model that embodies the metaphor's essence, illustrating both rhythm and cohesion in architectural design."""

#! python 3
function_code = """def generate_rippled_grid_structure(grid_size, grid_spacing, ripple_amplitude, ripple_frequency, layer_thickness, ripple_phase):
    \"""
    Generates an architectural Concept Model based on the 'rippled grid' metaphor, creating a dynamic interplay between
    structured grid elements and fluid, undulating surfaces.

    Parameters:
    - grid_size (tuple of int): The number of grid units in the x and y directions (rows, columns).
    - grid_spacing (float): The spacing between grid lines in meters.
    - ripple_amplitude (float): The maximum vertical displacement of the ripples in meters.
    - ripple_frequency (float): The frequency of the ripple effect across the grid.
    - layer_thickness (float): The vertical spacing between each layer in meters.
    - ripple_phase (float): The phase shift of the ripple effect.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, cols = grid_size
    breps = []

    # Generate layered surfaces with ripple effect
    for layer in range(-2, 3):  # Five layers for a more complex structure
        for i in range(rows):
            for j in range(cols):
                # Calculate the ripple height using a sine wave with a phase shift
                x = i * grid_spacing
                y = j * grid_spacing
                z = (layer * layer_thickness) + ripple_amplitude * math.sin(ripple_frequency * (x + y) + ripple_phase)

                # Create the four corner points of the grid cell with ripple effect
                pt1 = rg.Point3d(x, y, z)
                pt2 = rg.Point3d(x + grid_spacing, y, z)
                pt3 = rg.Point3d(x + grid_spacing, y + grid_spacing, z)
                pt4 = rg.Point3d(x, y + grid_spacing, z)

                # Create a Nurbs surface from corner points
                surface = rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt4)
                if surface:
                    brep = surface.ToBrep()
                    breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_rippled_grid_structure((10, 10), 1.0, 0.5, 2.0, 0.2, 0.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_rippled_grid_structure((5, 8), 0.5, 1.0, 3.0, 0.1, 1.57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_rippled_grid_structure((15, 15), 0.75, 0.3, 1.5, 0.15, 0.785)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_rippled_grid_structure((8, 12), 0.6, 0.8, 4.0, 0.3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_rippled_grid_structure((12, 12), 0.4, 0.6, 2.5, 0.25, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
