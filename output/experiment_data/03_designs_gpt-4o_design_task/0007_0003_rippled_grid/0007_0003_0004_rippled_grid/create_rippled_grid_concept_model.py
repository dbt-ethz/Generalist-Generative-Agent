# Created for 0007_0003_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model that embodies the 'rippled grid' metaphor by creating a series of undulating surfaces on a structured grid. It takes parameters like grid size, spacing, wave amplitude, and frequency to define the extent of the ripple effect. Using a sine wave function, the function calculates the z-coordinates of grid points, producing a dynamic, wave-like form. It then constructs Nurbs surfaces between these points, ensuring the underlying grid structure remains visible. This approach emphasizes the interplay between order and fluidity, capturing the rhythmic movement inherent in the metaphor while arranging spaces for visual and spatial interest."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=5, grid_spacing=10.0, wave_amplitude=2.0, wave_frequency=2.0):
    \"""
    Creates an architectural Concept Model that embodies the 'rippled grid' metaphor using a series of layered planes
    or surfaces that undulate across a grid. This function captures the rhythmic movement of the ripple effect while 
    ensuring the underlying grid structure is visible. 

    Parameters:
    - grid_size (int): The number of subdivisions in the grid (both horizontally and vertically).
    - grid_spacing (float): The distance between each grid line, measured in meters.
    - wave_amplitude (float): The amplitude of the wave, controlling the height of the ripples.
    - wave_frequency (float): The frequency of the wave, controlling the number of ripples across the grid.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # List to store the generated geometries
    geometries = []

    # Create the base grid of points
    points = []
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * grid_spacing
            y = j * grid_spacing
            # Calculate the z-coordinate using a sine wave function to create a ripple effect
            z = wave_amplitude * math.sin(wave_frequency * (x + y))
            points.append(rg.Point3d(x, y, z))

    # Create surfaces between the grid points
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            # Get the four corner points of the current grid cell
            pt0 = points[i * grid_size + j]
            pt1 = points[i * grid_size + (j + 1)]
            pt2 = points[(i + 1) * grid_size + (j + 1)]
            pt3 = points[(i + 1) * grid_size + j]

            # Create a Nurbs surface from the four corner points
            nurbs_surface = rg.NurbsSurface.CreateFromCorners(pt0, pt1, pt2, pt3)
            if nurbs_surface:
                # Convert surface to Brep and add to the geometries list
                brep = nurbs_surface.ToBrep()
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=10, grid_spacing=5.0, wave_amplitude=3.0, wave_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=7, grid_spacing=8.0, wave_amplitude=1.0, wave_frequency=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=6, grid_spacing=12.0, wave_amplitude=4.0, wave_frequency=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=8, grid_spacing=15.0, wave_amplitude=2.5, wave_frequency=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=12, grid_spacing=6.0, wave_amplitude=1.5, wave_frequency=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
