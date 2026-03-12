# Created for 0007_0002_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by establishing a grid structure that serves as a foundation. It introduces undulating surfaces simulating ripples, calculated using sine wave functions to create varying heights. The parameters (grid size, ripple amplitude, and frequency) allow for diverse geometric variations, emphasizing the interplay between the rigid grid and fluid forms. The output consists of a list of 3D Brep objects that visually communicate the rhythmic spatial quality, reflecting both order and dynamism, capturing the essence of the metaphor in a tangible architectural representation."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=5, ripple_amplitude=2, ripple_frequency=0.5):
    \"""
    Creates a 3D architectural Concept Model based on the 'rippled grid' metaphor.
    
    The model features a grid-based structure overlaid with a series of undulating surfaces 
    to simulate the effect of ripples. This model explores the tension between a structured 
    grid and organic ripple patterns, emphasizing rhythmic spatial quality.

    Parameters:
    - grid_size (int): The number of grid cells along one axis of the base grid.
    - ripple_amplitude (float): The maximum height of the ripples.
    - ripple_frequency (float): The frequency of the ripple undulations.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    geometries = []
    grid_spacing = 10  # Space between grid lines in meters

    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the center of the grid cell
            x = i * grid_spacing
            y = j * grid_spacing

            # Create the base grid point
            base_point = rg.Point3d(x, y, 0)

            # Calculate the ripple effect using a sine wave function
            ripple_height = ripple_amplitude * math.sin(ripple_frequency * (x + y))
            
            # Create a ripple point above the base grid point
            ripple_point = rg.Point3d(x, y, ripple_height)

            # Create a vertical line between the base point and ripple point
            line = rg.Line(base_point, ripple_point)
            line_curve = rg.LineCurve(line)

            # Create a surface by extruding the line curve along the Y-axis
            extrusion_vector = rg.Vector3d(0, grid_spacing, 0)
            surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(line_curve, extrusion_vector))

            if surface:
                geometries.append(surface)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=10, ripple_amplitude=3, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=8, ripple_amplitude=1.5, ripple_frequency=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=6, ripple_amplitude=4, ripple_frequency=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=12, ripple_amplitude=2.5, ripple_frequency=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=7, ripple_amplitude=5, ripple_frequency=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
