# Created for 0007_0004_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model based on the 'rippled grid' metaphor by creating a 3D grid structure that features rhythmic undulations. It employs sine and cosine functions to simulate the ripple effect, ensuring that the underlying grid maintains order while introducing fluid, wavy surfaces. The model's parameters grid size, cell size, ripple amplitude, ripple frequency, and base height allow for diverse expressions of the metaphor. Each generated surface is then extruded to give it volume, culminating in a cohesive design that visually and spatially embodies the dynamic interaction between structure and fluidity."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, ripple_amplitude, ripple_frequency, base_height):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.

    This function generates a 3D model that features a regular grid structure with undulating surfaces. 
    The ripple effect is applied via a combination of sine and cosine functions to create a dynamic interaction 
    between fluidity and structure, emphasizing the 'rippled grid' metaphor.

    Parameters:
    grid_size (int): Number of cells along one dimension of the grid.
    cell_size (float): Size of each grid cell in meters.
    ripple_amplitude (float): Maximum displacement of the ripple effect in meters.
    ripple_frequency (float): Frequency of the ripple effect.
    base_height (float): Base height of the grid in meters.

    Returns:
    List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []

    # Create grid points
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * cell_size
            y = j * cell_size
            z = base_height + ripple_amplitude * (math.sin(ripple_frequency * x) * math.cos(ripple_frequency * y))

            # Create a base point with ripple effect
            base_point = rg.Point3d(x, y, z)

            # Create the four corners of the cell
            pt1 = base_point
            pt2 = rg.Point3d(x + cell_size, y, z)
            pt3 = rg.Point3d(x + cell_size, y + cell_size, z)
            pt4 = rg.Point3d(x, y + cell_size, z)

            # Create a surface with the ripple effect
            surface = rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt4)

            if surface:
                # Extrude the surface to give volume
                extrusion_vector = rg.Vector3d(0, 0, -base_height)
                extruded_brep = surface.ToBrep().Faces[0].CreateExtrusion(rg.LineCurve(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, -base_height)), True)

                if extruded_brep:
                    breps.append(extruded_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(10, 1.0, 0.5, 2.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(5, 2.0, 1.0, 1.5, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(8, 1.5, 0.3, 3.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(6, 0.8, 0.4, 2.5, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(12, 1.2, 0.6, 2.2, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
