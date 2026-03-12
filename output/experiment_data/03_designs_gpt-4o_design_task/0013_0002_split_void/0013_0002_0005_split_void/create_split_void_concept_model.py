# Created for 0013_0002_split_void.json

""" Summary:
The `create_split_void_concept_model` function generates an architectural concept model based on the "Split void" metaphor by defining a central void that divides the structure into two distinct halves. This function takes parameters such as building dimensions, void ratio, and varying height levels on either side. It creates the void as a prominent feature, enhancing the interplay of light and shadow while influencing the building's geometry. By manipulating the heights and orientations of the side volumes, the model captures the essence of duality and spatial dynamics, facilitating movement and interaction within the architectural space while maintaining a cohesive identity."""

#! python 3
function_code = """def create_split_void_concept_model(width, depth, height, void_ratio, level_heights, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Split void' metaphor. The model features a central void that splits
    the structure into two halves, each with varying heights or levels, and utilizes the void to enhance natural light and spatial dynamics.

    Parameters:
    - width (float): Total width of the building.
    - depth (float): Total depth of the building.
    - height (float): Maximum height of the building.
    - void_ratio (float): Ratio of the void width to the total width of the building (0 < void_ratio < 1).
    - level_heights (list of floats): Heights of each level on either side of the void.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects: The 3D geometries of the concept model, including floors, walls, and the central void.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for replicability
    random.seed(seed)

    # Define the void width
    void_width = width * void_ratio

    # Calculate the width of each side
    side_width = (width - void_width) / 2

    # Initialize list to store geometries
    geometries = []

    # Create the central void as a box
    void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(side_width, side_width + void_width), rg.Interval(0, depth), rg.Interval(0, height))
    geometries.append(void_box.ToBrep())

    # Create side volumes with varying levels
    for side in [-1, 1]:
        current_x = side * side_width / 2 + side * (side_width + void_width / 2)
        current_height = 0

        for level_height in level_heights:
            # Ensure level height does not exceed total building height
            if current_height + level_height > height:
                level_height = height - current_height

            # Create a box for this level
            level_box = rg.Box(rg.Plane.WorldXY, rg.Interval(current_x - side_width / 2, current_x + side_width / 2), rg.Interval(0, depth), rg.Interval(current_height, current_height + level_height))
            geometries.append(level_box.ToBrep())

            # Move up to the next level
            current_height += level_height

            # Break if the building height is reached
            if current_height >= height:
                break

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 20.0, 30.0, 0.3, [5.0, 7.0, 10.0])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15.0, 25.0, 35.0, 0.25, [6.0, 8.0, 12.0], seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(12.0, 18.0, 24.0, 0.4, [4.0, 6.0, 9.0], seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(8.0, 15.0, 20.0, 0.2, [3.0, 5.0, 7.0], seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(20.0, 30.0, 40.0, 0.15, [8.0, 10.0, 15.0], seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
