# Created for 0007_0005_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model by simulating the metaphor of a "rippled grid." It creates a structured grid while applying wave-like undulations to the surfaces, embodying the dynamic interplay between order and fluidity. The parameters, including grid size, wave amplitude, and frequency, dictate the extent and nature of the ripples. By calculating z-coordinates through a sine function, it generates undulating surfaces over a rotated grid layout. This approach allows for visually engaging designs that reflect the rhythmic qualities of waves while maintaining an underlying grid structure, facilitating fluid spatial transitions in the model."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, wave_amplitude, wave_frequency, grid_spacing, grid_angle=0):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor by developing a series of undulating
    surfaces overlaid on a rotated grid structure. The model emphasizes the ripple effect in contrast with the grid.

    Parameters:
    grid_size (tuple): A tuple of two integers (rows, cols) representing the number of grid cells in each direction.
    wave_amplitude (float): The amplitude of the wave undulations in meters.
    wave_frequency (float): The frequency of the wave undulations.
    grid_spacing (float): The spacing between grid lines in meters.
    grid_angle (float): The angle in degrees to rotate the grid, introducing a dynamic orientation.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    breps = []

    # Convert grid angle to radians for rotation calculations
    angle_rad = math.radians(grid_angle)

    # Create the base grid structure
    rows, cols = grid_size
    for i in range(rows):
        for j in range(cols):
            # Calculate the position of each grid point with rotation
            x = i * grid_spacing * math.cos(angle_rad) - j * grid_spacing * math.sin(angle_rad)
            y = i * grid_spacing * math.sin(angle_rad) + j * grid_spacing * math.cos(angle_rad)

            # Calculate the z-coordinate using a wave function to create the ripple effect
            z = wave_amplitude * math.sin(wave_frequency * (x + y))

            # Create a point at the calculated position
            point = rg.Point3d(x, y, z)

            # Create a grid cell surface with wave effects
            if i < rows - 1 and j < cols - 1:
                pt1 = rg.Point3d(x + grid_spacing * math.cos(angle_rad), y + grid_spacing * math.sin(angle_rad), wave_amplitude * math.sin(wave_frequency * ((x + grid_spacing) + y)))
                pt2 = rg.Point3d(x + grid_spacing * math.cos(angle_rad) - grid_spacing * math.sin(angle_rad), y + grid_spacing * math.sin(angle_rad) + grid_spacing * math.cos(angle_rad), wave_amplitude * math.sin(wave_frequency * ((x + grid_spacing) + (y + grid_spacing))))
                pt3 = rg.Point3d(x - grid_spacing * math.sin(angle_rad), y + grid_spacing * math.cos(angle_rad), wave_amplitude * math.sin(wave_frequency * (x + (y + grid_spacing))))
                
                # Create a surface from these points
                surface = rg.NurbsSurface.CreateFromCorners(point, pt1, pt2, pt3)
                if surface:
                    breps.append(rg.Brep.CreateFromSurface(surface))

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 2.0, 1.0, 1.0, 45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 1.5, 0.5, 2.0, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 12), 3.0, 2.0, 1.5, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((7, 9), 1.0, 1.5, 2.5, 90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((8, 8), 2.5, 1.2, 1.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
