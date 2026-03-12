# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model based on the "Split void" metaphor by defining a structure with a central void that divides the mass into two distinct sections. It uses specified dimensions to create solid volumes representing the left and right sides of the building, while a central void introduces spatial separation. The function emphasizes contrast through varying dimensions of the void and solids, allowing for dynamic interactions with light and shadow. Ultimately, it returns a list of geometric representations that reflect the duality and movement inherent in the metaphor, enabling diverse spatial experiences."""

#! python 3
function_code = """def create_split_void_concept_model(length=20, width=10, height=10, void_width=2, void_height=8, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor, where a central void divides the structure into two distinct halves.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The total height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - void_height (float): The height of the central void in meters.
    - seed (int): A seed for randomization to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Ensure randomness is consistent
    random.seed(seed)

    # Calculate the positions for the void and the two halves
    half_width = (width - void_width) / 2

    # Create the left and right solid parts of the building
    left_solid = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, half_width), rg.Interval(0, height))
    right_solid = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width + void_width, width), rg.Interval(0, height))

    # Create the central void
    central_void = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width, half_width + void_width), rg.Interval(0, void_height))

    # Convert solids to Breps
    left_brep = left_solid.ToBrep()
    right_brep = right_solid.ToBrep()
    void_brep = central_void.ToBrep()

    # Return a list of Breps representing the concept model
    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=30, width=20, height=15, void_width=5, void_height=10, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=25, width=15, height=12, void_width=3, void_height=6, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=40, width=25, height=20, void_width=4, void_height=12, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=35, width=18, height=14, void_width=6, void_height=9, seed=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=28, width=22, height=18, void_width=7, void_height=11, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
