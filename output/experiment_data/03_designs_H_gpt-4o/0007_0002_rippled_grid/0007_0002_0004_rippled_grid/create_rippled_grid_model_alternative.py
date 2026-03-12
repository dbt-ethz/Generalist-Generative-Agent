# Created for 0007_0002_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a structured grid and introducing undulating surfaces that simulate ripples. It establishes a grid of control points and applies a mathematical sine function to manipulate the z-coordinates, resulting in a dynamic, fluid form that contrasts with the underlying grid structure. The function produces 3D geometries that visually represent this interplay between order and movement, embodying the metaphor's essence. By varying parameters such as grid size, cell size, ripple amplitude, and frequency, the function explores diverse spatial configurations that maintain rhythmic qualities."""

#! python 3
function_code = """def create_rippled_grid_model_alternative(grid_size=10, cell_size=2, ripple_amplitude=1.0, ripple_frequency=2.0):
    \"""
    Generate an architectural Concept Model based on the 'rippled grid' metaphor.

    This function establishes a grid structure and introduces undulating curves that simulate
    ripples across the grid. The resulting model emphasizes the dynamic interplay between
    structured order and fluid movement.

    Parameters:
    - grid_size (int): The number of cells along one dimension of the grid.
    - cell_size (float): The size of each cell in the grid (in meters).
    - ripple_amplitude (float): The amplitude of the ripple effect (in meters).
    - ripple_frequency (float): The frequency of the ripple effect.

    Returns:
    List of 3D geometries (Rhino.Geometry.Brep) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create a list to store the resulting geometries
    geometries = []

    # Iterate over the grid to create control points for the curves
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the position of each grid point
            x = i * cell_size
            y = j * cell_size

            # Apply the ripple effect to the z-coordinate
            z = ripple_amplitude * math.sin(ripple_frequency * math.sqrt(x**2 + y**2))

            # Create a polyline to visualize the ripple effect in 3D
            polyline_points = []
            for k in range(5):
                z_offset = z * math.cos(math.pi * k / 4)
                point = rg.Point3d(x, y, z_offset)
                polyline_points.append(point)
            polyline = rg.Polyline(polyline_points)

            # Create a curve from the polyline and add it to the geometries
            curve = polyline.ToNurbsCurve()
            breps = rg.Brep.CreateFromSweep(curve, rg.LineCurve(rg.Point3d(x, y, 0), rg.Point3d(x, y, z)), True, 0.01)
            if breps:
                geometries.append(breps[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_model_alternative(grid_size=15, cell_size=3, ripple_amplitude=2.0, ripple_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_model_alternative(grid_size=8, cell_size=1.5, ripple_amplitude=0.5, ripple_frequency=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_model_alternative(grid_size=12, cell_size=2.5, ripple_amplitude=1.2, ripple_frequency=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_model_alternative(grid_size=20, cell_size=1.0, ripple_amplitude=1.5, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_model_alternative(grid_size=10, cell_size=2.0, ripple_amplitude=3.0, ripple_frequency=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
