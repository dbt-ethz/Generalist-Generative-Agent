# Created for 0011_0002_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the "Shifted Grid" metaphor by creating a dynamic grid framework. It begins with a standard grid and introduces random shifts and offsets to the grid lines, resulting in interconnected and staggered volumes. This process fosters movement and fluidity, aligning with the metaphor's emphasis on unpredictability. The function incorporates height variations and creates Brep objects that simulate layered structures, enhancing interaction with light and shadow. The output is a series of 3D geometries that embody adaptability and diverse spatial experiences, inviting exploration and discovery within the design."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, grid_count=5, shift_amount=1.0):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    The function creates a regular grid framework and introduces deliberate shifts and offsets in 
    the grid lines to form interconnected volumes and spaces. The model emphasizes movement and 
    fluidity through staggered layers, varied orientations, and dynamic interactions with light 
    and shadow.

    Parameters:
    grid_size (float): The size of each grid cell in meters.
    grid_count (int): The number of grid cells along one axis of the grid.
    shift_amount (float): The amount by which the grid lines are shifted to create the 'shifted grid' effect.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random

    # Seed random number generator for replicability
    random.seed(42)

    breps = []
    base_elevation = 0.0
    
    # Create the initial grid of points
    for i in range(grid_count):
        for j in range(grid_count):
            # Calculate base position
            base_x = i * grid_size
            base_y = j * grid_size

            # Apply a random shift within the specified shift amount
            shift_x = base_x + random.uniform(-shift_amount, shift_amount)
            shift_y = base_y + random.uniform(-shift_amount, shift_amount)

            # Create vertical breps to simulate staggered layers
            height_variation = random.uniform(0.5, 2.0) * grid_size
            box_corners = [
                rg.Point3d(shift_x, shift_y, base_elevation),
                rg.Point3d(shift_x + grid_size, shift_y, base_elevation),
                rg.Point3d(shift_x + grid_size, shift_y + grid_size, base_elevation),
                rg.Point3d(shift_x, shift_y + grid_size, base_elevation),
                rg.Point3d(shift_x, shift_y, base_elevation + height_variation),
                rg.Point3d(shift_x + grid_size, shift_y, base_elevation + height_variation),
                rg.Point3d(shift_x + grid_size, shift_y + grid_size, base_elevation + height_variation),
                rg.Point3d(shift_x, shift_y + grid_size, base_elevation + height_variation)
            ]
            brep = rg.Brep.CreateFromBox(box_corners)
            if brep:
                breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=3, grid_count=4, shift_amount=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=2, grid_count=6, shift_amount=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=4, grid_count=3, shift_amount=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=1, grid_count=8, shift_amount=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=6, grid_count=5, shift_amount=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
