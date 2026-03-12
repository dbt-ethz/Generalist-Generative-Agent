# Created for 0011_0002_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the 'Shifted Grid' metaphor by manipulating a standard grid framework. It introduces randomness through controlled shifts and offsets in the grid lines to create interconnected volumes that deviate from traditional orthogonal layouts. This approach results in a dynamic model with staggered and misaligned geometries, evoking movement and fluidity. Each generated box represents a building volume at varying elevations, emphasizing adaptability and diverse spatial experiences. The algorithm captures the essence of exploration and interaction with light and shadow, effectively translating the metaphor into a tangible architectural form."""

#! python 3
function_code = """def generate_shifted_grid_concept_model(grid_size=5, shift_factor=0.3, height=3, levels=3):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor. 
    This model introduces deliberate shifts and offsets to a regular grid framework 
    to create interconnected volumes and spaces with non-traditional alignments.

    Parameters:
    - grid_size (int): The size of the base grid in both x and y directions.
    - shift_factor (float): The factor by which the grid lines are shifted to create 
      irregular alignments. It should be between 0 and 1.
    - height (float): The height of each level in meters.
    - levels (int): The number of levels or layers in the model.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for reproducibility
    random.seed(42)

    geometries = []

    # Create the base grid
    for level in range(levels):
        for i in range(grid_size):
            for j in range(grid_size):
                # Calculate offsets
                x_offset = random.uniform(-shift_factor, shift_factor)
                y_offset = random.uniform(-shift_factor, shift_factor)

                # Create base point with shifts
                base_point = rg.Point3d(i + x_offset, j + y_offset, level * height)

                # Create a basic volume (box) at each grid point
                box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis),
                             rg.Interval(0, 1),
                             rg.Interval(0, 1),
                             rg.Interval(0, height))

                # Convert box to Brep
                brep_box = box.ToBrep()
                geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_shifted_grid_concept_model(grid_size=10, shift_factor=0.2, height=4, levels=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_shifted_grid_concept_model(grid_size=7, shift_factor=0.5, height=2, levels=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_shifted_grid_concept_model(grid_size=6, shift_factor=0.1, height=5, levels=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_shifted_grid_concept_model(grid_size=8, shift_factor=0.4, height=3, levels=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_shifted_grid_concept_model(grid_size=4, shift_factor=0.25, height=6, levels=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
