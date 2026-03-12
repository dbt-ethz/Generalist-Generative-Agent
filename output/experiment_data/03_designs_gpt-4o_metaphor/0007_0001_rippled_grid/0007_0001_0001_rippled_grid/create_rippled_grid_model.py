# Created for 0007_0001_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a 3D grid of undulating surfaces. It employs sine wave calculations to simulate ripple effects across a defined grid size, producing a dynamic interplay of highs and lows that evoke the metaphor's rhythmic and fluid qualities. Parameters such as grid dimensions, cell size, ripple amplitude, and wave frequency allow for customization of the model's features. The result is a structured yet fluid design, reflecting both order and movement in the architectural form, suitable for visualizing innovative spatial concepts."""

#! python 3
function_code = """def create_rippled_grid_model(grid_size, cell_size, ripple_amplitude, wave_frequency, random_seed=42):
    \"""
    Creates a conceptual architectural model based on the 'rippled grid' metaphor.
    
    This function generates a 3D model consisting of undulating surfaces that form a grid-like structure.
    The surfaces are influenced by a ripple effect, creating a dynamic and rhythmic spatial quality.

    Parameters:
    - grid_size: Tuple (int, int) that defines the number of cells along the x and y axes, respectively.
    - cell_size: Float that specifies the size of each grid cell in meters.
    - ripple_amplitude: Float that determines the height variation of the ripple effect.
    - wave_frequency: Float that controls the frequency of the ripples across the grid.
    - random_seed: Integer for random number generation to ensure replicable results (optional, default is 42).

    Returns:
    - A list of RhinoCommon Brep objects representing the rippled grid surfaces.
    \"""
    import Rhino.Geometry as rg
    import random
    from math import sin, pi

    random.seed(random_seed)
    
    breps = []
    x_count, y_count = grid_size

    # Create control points for the rippled surface
    for i in range(x_count):
        for j in range(y_count):
            # Define the base corner of each grid cell
            x = i * cell_size
            y = j * cell_size

            # Calculate the height using a sine wave function to create ripples
            z = ripple_amplitude * sin(wave_frequency * (x + y) * 2 * pi / cell_size)

            # Define the corners of the current grid cell
            corners = [
                rg.Point3d(x, y, z),
                rg.Point3d(x + cell_size, y, z),
                rg.Point3d(x + cell_size, y + cell_size, z),
                rg.Point3d(x, y + cell_size, z)
            ]

            # Create a nurbs surface from corner points
            nurbs_surface = rg.NurbsSurface.CreateFromCorners(corners[0], corners[1], corners[2], corners[3])

            # Add the surface to the breps list
            if nurbs_surface is not None:
                brep = rg.Brep.CreateFromSurface(nurbs_surface)
                if brep:
                    breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_model((10, 10), 1.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_model((5, 5), 2.0, 1.0, 3.0, random_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_model((8, 8), 0.5, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_model((15, 15), 0.75, 0.8, 1.0, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_model((12, 12), 1.5, 0.6, 4.0, random_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
