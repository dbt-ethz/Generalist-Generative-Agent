# Created for 0013_0002_split_void.json

""" Summary:
The provided function `create_split_void_concept_model` generates an architectural concept model based on the "Split void" metaphor. It creates a central void that acts as a dynamic separator, influencing the buildings geometry and light interplay. The function takes parameters like building dimensions and level variations to design volumes on either side of the void, allowing for differences in height and spatial relationships. By integrating varying heights, the model emphasizes duality and promotes movement through the void, ensuring it serves as a cohesive, unifying architectural feature while enhancing the spatial experience with light and shadow dynamics."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, level_variations, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Split void' metaphor, emphasizing the division and connection
    between spaces through a central void. This model explores the interplay of spaces with varying levels and the role of 
    natural light within the void.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The maximum height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - level_variations (list of tuples): A list where each tuple contains two floats representing the height variation 
      for the left and right sections at a particular level.
    - seed (int): A seed for random number generation to ensure replicability (default is 42).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for replicability
    random.seed(seed)
    
    # Calculate the width of each side excluding the void
    side_width = (width - void_width) / 2

    # Initialize list to store geometries
    geometries = []

    # Create the central void as a vertical brep
    void_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(side_width, side_width + void_width),
        rg.Interval(0, length),
        rg.Interval(0, height)
    )
    geometries.append(void_box.ToBrep())

    # Create the side volumes with varying levels
    for side in [-1, 1]:  # Left (-1) and right (1) sides
        base_x = side * (side_width / 2 + void_width / 2)
        current_height = 0

        for left_variation, right_variation in level_variations:
            # Determine the height for this level on each side
            level_height = height * (0.2 + random.uniform(-0.05, 0.05))
            if side == -1:
                level_height += left_variation
            else:
                level_height += right_variation

            # Ensure level height does not exceed total building height
            if current_height + level_height > height:
                level_height = height - current_height

            # Create a box for this level
            level_box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(base_x - side_width / 2, base_x + side_width / 2),
                rg.Interval(0, length),
                rg.Interval(current_height, current_height + level_height)
            )
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
    geometry = create_split_void_concept_model(30.0, 20.0, 15.0, 5.0, [(2.0, 3.0), (1.5, 2.5), (1.0, 1.0)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(40.0, 25.0, 20.0, 6.0, [(3.0, 4.0), (2.0, 3.5), (1.5, 2.0)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(50.0, 30.0, 25.0, 7.0, [(4.0, 5.0), (3.0, 4.5), (2.0, 2.5)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(35.0, 22.0, 18.0, 4.0, [(2.5, 3.5), (1.8, 2.3), (1.2, 1.7)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(45.0, 28.0, 22.0, 5.5, [(3.5, 4.5), (2.5, 3.0), (1.0, 1.5)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
