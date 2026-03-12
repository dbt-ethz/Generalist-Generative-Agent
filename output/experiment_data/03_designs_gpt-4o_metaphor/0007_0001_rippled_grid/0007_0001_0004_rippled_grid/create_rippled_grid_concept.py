# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept` generates an architectural concept model inspired by the metaphor "rippled grid." It creates a structured grid of surfaces, where each cell is deformed to reflect a ripple effect, embodying dynamic and rhythmic spatial qualities. The parameters define the grid's size, cell dimensions, ripple amplitude, and frequency. By modifying the z-coordinates of control points with a sinusoidal function, the surfaces achieve an undulating appearance. This method captures the essence of movement and flow while maintaining an organized grid structure, resulting in a visually engaging architectural model that aligns with the metaphor's key traits."""

#! python 3
function_code = """def create_rippled_grid_concept(grid_size, cell_size, ripple_amplitude, ripple_frequency):
    \"""
    Creates a 3D architectural Concept Model based on the 'rippled grid' metaphor.
    
    The function generates a grid of surfaces where each cell is deformed to form a ripple effect.
    This model reflects a dynamic and rhythmic spatial quality, suggesting movement and flow.

    Parameters:
    grid_size (tuple): A tuple (rows, cols) defining the number of cells in the grid.
    cell_size (float): The size of each grid cell in meters.
    ripple_amplitude (float): The maximum height variation of the ripple effect.
    ripple_frequency (float): The frequency of the ripples across the grid.

    Returns:
    list: A list of Brep objects representing the rippled grid surfaces.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    rows, cols = grid_size
    geometries = []

    for i in range(rows):
        for j in range(cols):
            # Define the corner points of the grid cell
            pt0 = rg.Point3d(i * cell_size, j * cell_size, 0)
            pt1 = rg.Point3d((i + 1) * cell_size, j * cell_size, 0)
            pt2 = rg.Point3d((i + 1) * cell_size, (j + 1) * cell_size, 0)
            pt3 = rg.Point3d(i * cell_size, (j + 1) * cell_size, 0)

            # Create curves from the corner points
            edge_curve0 = rg.Line(pt0, pt1).ToNurbsCurve()
            edge_curve1 = rg.Line(pt1, pt2).ToNurbsCurve()
            edge_curve2 = rg.Line(pt2, pt3).ToNurbsCurve()
            edge_curve3 = rg.Line(pt3, pt0).ToNurbsCurve()

            # Create a surface out of the corner curves
            planar_surface = rg.Brep.CreateEdgeSurface([edge_curve0, edge_curve1, edge_curve2, edge_curve3])

            # Create a ripple effect by modifying the control points
            u_divisions = 10
            v_divisions = 10

            # Create a grid of points to form control points for the ripple
            control_points = []
            for u in range(u_divisions + 1):
                for v in range(v_divisions + 1):
                    u_param = u / u_divisions
                    v_param = v / v_divisions
                    point = planar_surface.Surfaces[0].PointAt(u_param, v_param)

                    # Apply a sinusoidal ripple effect to the z-coordinate
                    ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (i * cell_size + point.X)) * math.cos(ripple_frequency * (j * cell_size + point.Y))
                    rippled_point = rg.Point3d(point.X, point.Y, ripple_effect)
                    control_points.append(rippled_point)

            # Create a Nurbs surface using the control points
            nurbs_surface = rg.NurbsSurface.CreateThroughPoints(control_points, u_divisions + 1, v_divisions + 1, 3, 3, False, False)

            # Add the rippled surface to the geometries list
            geometries.append(nurbs_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept((5, 5), 2.0, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept((10, 8), 1.5, 0.75, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept((4, 6), 3.0, 2.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept((6, 4), 1.0, 1.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept((7, 7), 2.5, 1.2, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
