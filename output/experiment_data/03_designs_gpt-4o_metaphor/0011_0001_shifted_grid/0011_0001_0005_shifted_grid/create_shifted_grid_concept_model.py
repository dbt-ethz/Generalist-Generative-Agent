# Created for 0011_0001_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "Shifted Grid" metaphor by creating a series of 3D grid-like structures. It dynamically shifts each grid row based on specified parameters, producing varied spatial arrangements that embody movement and fluidity. By randomly deciding to create solid volumes or voids, the function introduces unexpected alignments and intersections, fostering diverse circulation paths and experiences. The resulting model showcases adaptability and flexibility, encouraging exploration and interaction with light and shadow, effectively translating the metaphor into a tangible architectural concept."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size, shift_amount, element_height, grid_count, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    The function generates a series of shifted grid-like structures to create dynamic spatial arrangements.
    It uses solid and void spaces to form a complex interplay of architectural elements.

    Parameters:
    - grid_size: float, the size of each grid cell in meters.
    - shift_amount: float, the amount by which each subsequent grid row is shifted in meters.
    - element_height: float, the height of each architectural element in meters.
    - grid_count: int, number of grid cells along one dimension (the grid is square).
    - seed: int, seed for random number generator to ensure replicability.

    Returns:
    - List of RhinoCommon Brep: A list of 3D breps representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # List to store the resulting breps
    breps = []

    # Create the shifted grid concept model
    for i in range(grid_count):
        for j in range(grid_count):
            # Calculate the base position of each grid cell
            x_offset = i * grid_size + (j * shift_amount)
            y_offset = j * grid_size + (i * shift_amount)

            # Randomly decide whether to create a solid or void
            if random.random() > 0.5:
                # Create a solid box
                base_point = rg.Point3d(x_offset, y_offset, 0)
                box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, grid_size), rg.Interval(0, grid_size), rg.Interval(0, element_height))
                box.Transform(rg.Transform.Translation(base_point - rg.Point3d(0, 0, 0)))
                brep = box.ToBrep()
                breps.append(brep)
            else:
                # Create a void (open space) by not adding a brep
                continue

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(1.0, 0.5, 3.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(2.0, 0.3, 4.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(0.8, 0.4, 2.5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(1.5, 0.2, 2.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(1.2, 0.6, 3.5, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
