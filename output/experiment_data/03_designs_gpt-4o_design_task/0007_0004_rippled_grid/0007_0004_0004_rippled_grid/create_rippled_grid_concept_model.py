# Created for 0007_0004_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a base grid structure and applying a ripple effect to it. The function takes parameters for grid size, ripple characteristics, and height to construct a series of undulating surfaces that suggest movement while adhering to an organized grid layout. It calculates ripple heights using a sine function, creating dynamic, curved surfaces for each grid cell. The resulting Brep geometries represent the undulating structure, facilitating smooth spatial transitions and visual impact, embodying the metaphor's essence of fluidity and order."""

#! python 3
function_code = """def create_rippled_grid_concept_model(base_grid_size, ripple_amplitude, ripple_frequency, height, ripple_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor. This model features a base grid
    structure with undulating elements that ripple across, suggesting movement and fluidity while maintaining an
    organized grid structure.

    Parameters:
    base_grid_size (int): The size of the base grid (number of cells in one row/column).
    ripple_amplitude (float): The maximum height deviation for the ripple effect.
    ripple_frequency (float): The frequency of the ripple across the grid.
    height (float): The height of the building model.
    ripple_seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the rippled surfaces over the grid.
    \"""
    
    import Rhino.Geometry as rg
    import System
    from System.Collections.Generic import List
    import random
    
    random.seed(ripple_seed)
    
    grid_spacing = 5.0  # meters, spacing between grid lines
    ripple_offset = grid_spacing / (2 * System.Math.PI * ripple_frequency)
    
    breps = List[rg.Brep]()
    
    for i in range(base_grid_size):
        for j in range(base_grid_size):
            # Calculate the base point of the grid cell
            base_point = rg.Point3d(i * grid_spacing, j * grid_spacing, 0)
            
            # Calculate the ripple effect at this grid point
            ripple_height = ripple_amplitude * System.Math.Sin(i * ripple_frequency + j * ripple_frequency)
            
            # Create the base surface for the grid cell, offset by the ripple height
            surface_corners = [
                rg.Point3d(base_point.X, base_point.Y, base_point.Z + ripple_height),
                rg.Point3d(base_point.X + grid_spacing, base_point.Y, base_point.Z + ripple_height),
                rg.Point3d(base_point.X + grid_spacing, base_point.Y + grid_spacing, base_point.Z + ripple_height),
                rg.Point3d(base_point.X, base_point.Y + grid_spacing, base_point.Z + ripple_height)
            ]
            
            surface = rg.NurbsSurface.CreateFromCorners(*surface_corners)
            
            if surface:
                # Create a volume by extruding the surface to the specified height
                extrusion_vector = rg.Vector3d(0, 0, height)
                extrusion_path = rg.LineCurve(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height))
                brep = surface.ToBrep().Faces[0].CreateExtrusion(extrusion_path, True)
                
                if brep:
                    breps.Add(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(10, 2.0, 0.5, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(8, 1.5, 1.0, 10.0, ripple_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(12, 3.0, 0.8, 20.0, ripple_seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(5, 1.0, 0.3, 8.0, ripple_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(15, 4.0, 0.2, 12.0, ripple_seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
