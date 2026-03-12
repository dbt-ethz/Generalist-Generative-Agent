# Created for 0011_0002_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the 'Shifted Grid' metaphor by creating a regular grid framework that is dynamically altered through random shifts. By iterating through layers and introducing deliberate offsets in both x and y directions, the function forms interconnected volumes that deviate from traditional layouts, embodying movement and fluidity. Each layer's geometry is defined by staggered boxes, emphasizing varied orientations and interactions with light and shadow. This approach fosters adaptability and exploration, aligning with the metaphor's essence of creating unexpected spatial experiences and diverse circulation paths within the structure."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, spacing=4, shift_amount=1.5, height=3, layers=4):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor.

    This function creates a regular grid framework and introduces deliberate shifts to form interconnected
    volumes and spaces with non-traditional alignments. The model emphasizes movement and fluidity through
    staggered layers, varied orientations, and dynamic interactions with light and shadow.

    Parameters:
    - grid_size (int): The number of grid cells along each axis.
    - spacing (float): The distance between grid lines in meters.
    - shift_amount (float): The maximum amount by which the grid lines are shifted.
    - height (float): The height of each layer in meters.
    - layers (int): The total number of vertical layers.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed random number generator for replicability
    random.seed(42)

    geometries = []

    # Iterate through each layer
    for layer in range(layers):
        z_height = layer * height
        
        # Create the grid with shifted points
        for i in range(grid_size):
            for j in range(grid_size):
                # Base grid points
                x_base = i * spacing
                y_base = j * spacing

                # Shift grid points to create the 'shifted grid' effect
                x_shift = random.uniform(-shift_amount, shift_amount)
                y_shift = random.uniform(-shift_amount, shift_amount)

                # Define base point for each volume
                base_point = rg.Point3d(x_base + x_shift, y_base + y_shift, z_height)

                # Create a box for each shifted point
                box = rg.Box(
                    rg.Plane(base_point, rg.Vector3d.ZAxis),
                    rg.Interval(0, spacing * 0.8),
                    rg.Interval(0, spacing * 0.8),
                    rg.Interval(0, height)
                )

                # Convert box to Brep and add to the list
                brep_box = box.ToBrep()
                geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, spacing=5, shift_amount=2, height=4, layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=4, spacing=3, shift_amount=1, height=2, layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=7, spacing=6, shift_amount=2.5, height=3.5, layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=5, spacing=4.5, shift_amount=1, height=2.5, layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=8, spacing=7, shift_amount=3, height=5, layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
