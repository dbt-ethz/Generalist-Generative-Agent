# Created for 0013_0002_split_void.json

""" Summary:
The provided function, `create_split_void_concept_model`, generates an architectural model based on the 'Split void' metaphor by creating a structure that features a central void acting as a dynamic separator. This void influences the design by dividing the building into two distinct sections with varying heights, promoting an interplay of light and shadow. The function utilizes random height generation for both sides of the void, ensuring each model exhibits unique spatial relationships. The resulting geometry captures the essence of duality and movement, integrating the void as a pivotal element that connects and contrasts the buildings components."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, max_height, void_height_ratio=0.5, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor, emphasizing a vertical division with a multilevel void.

    This function generates a building model where a central void acts as a vertical separator, introducing a dynamic play of levels
    and light. The void splits the building into two sections, each with distinct heights and forms, while maintaining a cohesive
    architectural identity.

    Parameters:
    - length (float): Total length of the building in meters.
    - width (float): Total width of the building in meters.
    - max_height (float): Maximum height of the building in meters.
    - void_height_ratio (float): Ratio of the height of the void to the max height of the building (0 < void_height_ratio < 1).
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the building's sections and the void.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Define void height based on ratio
    void_height = max_height * void_height_ratio

    # Calculate the height of each side
    left_height = random.uniform(void_height, max_height)
    right_height = max_height - (left_height - void_height)

    # Define the central void as a multilevel vertical separator
    void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-width / 2, width / 2), rg.Interval(-length / 4, length / 4), rg.Interval(0, void_height))
    void_brep = void_box.ToBrep()

    # Define the left section with its unique height
    left_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-width / 2, -width / 4), rg.Interval(-length / 2, length / 2), rg.Interval(0, left_height))
    left_brep = left_box.ToBrep()

    # Define the right section with its unique height
    right_box = rg.Box(rg.Plane.WorldXY, rg.Interval(width / 4, width / 2), rg.Interval(-length / 2, length / 2), rg.Interval(0, right_height))
    right_brep = right_box.ToBrep()

    # Return the list of Breps representing the concept model
    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(30, 15, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(40, 20, 25, void_height_ratio=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(50, 25, 30, void_height_ratio=0.4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(35, 18, 22, void_height_ratio=0.7, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(45, 22, 28, void_height_ratio=0.3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
