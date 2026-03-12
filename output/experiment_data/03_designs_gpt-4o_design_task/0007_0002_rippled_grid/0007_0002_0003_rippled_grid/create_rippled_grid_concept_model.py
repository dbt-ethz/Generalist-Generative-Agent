# Created for 0007_0002_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model inspired by the "rippled grid" metaphor. It establishes a base grid structure, then introduces undulating surfaces to simulate ripple effects, thereby creating a dynamic interplay between order and fluidity. Parameters such as grid size, spacing, ripple amplitude, and frequency dictate the model's geometry. The function calculates ripple effects at each grid point, extrudes lines to form surfaces, and assembles these into Brep objects. The resulting model visually embodies the rhythmic spatial quality, illustrating how structured spaces can flow while adhering to a regular framework."""

#! python 3
function_code = """def create_rippled_grid_concept_model(base_size, grid_spacing, ripple_amplitude, ripple_frequency):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.
    
    The function establishes a base grid structure and introduces undulating surfaces that simulate
    the effect of ripples across this grid. The grid provides a regular structural framework, while 
    the ripple effect adds movement and dynamism. The resulting model explores how spaces can be 
    designed to flow in a rhythmic manner, maintaining a sense of order and suggesting movement.

    Parameters:
    - base_size (tuple): The dimensions of the base grid as (width, depth) in meters.
    - grid_spacing (float): The spacing between grid lines in meters.
    - ripple_amplitude (float): The amplitude of the ripple effect in meters.
    - ripple_frequency (float): The frequency of the ripple effect (higher values increase ripple density).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    width, depth = base_size
    breps = []

    # Create base grid lines
    num_x = int(width / grid_spacing)
    num_y = int(depth / grid_spacing)

    for i in range(num_x + 1):
        for j in range(num_y + 1):
            x = i * grid_spacing
            y = j * grid_spacing

            # Calculate the ripple effect based on the position in the grid
            ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Create vertically undulating curves across the grid
            start_point = rg.Point3d(x, y, 0)
            end_point = rg.Point3d(x, y, ripple_effect)
            line = rg.Line(start_point, end_point)

            # Ensure the line is valid before extrusion
            if line.IsValid:
                # Extrude the line to create a surface
                extrusion_vector = rg.Vector3d(0, 0, 1)
                extrusion = rg.Extrusion.Create(line.ToNurbsCurve(), 1.0, True)

                # Convert extrusion to Brep and add to the list
                brep = extrusion.ToBrep()
                if brep:
                    breps.append(brep)

    # Create a surface to represent the ripple effect across the grid
    undulating_surface_points = []
    for i in range(num_x + 1):
        for j in range(num_y + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + y))
            point = rg.Point3d(x, y, ripple_effect)
            undulating_surface_points.append(point)

    # Create a Nurbs surface from the grid points
    undulating_surface = rg.NurbsSurface.CreateFromPoints(
        undulating_surface_points, num_x + 1, num_y + 1, 3, 3)

    # Convert surface to Brep and add to the list
    surface_brep = undulating_surface.ToBrep()
    breps.append(surface_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1, 0.5, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((15, 20), 0.5, 0.3, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((5, 5), 0.75, 0.8, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((12, 8), 0.6, 0.4, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((20, 15), 2, 1, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
