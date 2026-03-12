# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model based on the "Split void" metaphor by defining a building structure with a central void that divides it into two distinct parts. It creates a bounding box representing the overall building dimensions and a void box to signify the central division. By applying Boolean operations, the function subtracts the void from the building mass, resulting in two separate sections. It also introduces randomness in the positioning of one part for visual distinction, enhancing spatial dynamics and interaction with light, thereby embodying the metaphor's themes of duality and contrast."""

#! python 3
function_code = """def create_split_void_concept_model(length=20.0, width=10.0, height=10.0, void_width=2.0, void_height=8.0, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor.
    
    Parameters:
    - length: The total length of the building form in meters (default is 20).
    - width: The total width of the building form in meters (default is 10).
    - height: The total height of the building form in meters (default is 10).
    - void_width: The width of the central void in meters (default is 2).
    - void_height: The height of the central void in meters (default is 8).
    - seed: Random seed for replicable randomness (default is 42).

    Returns:
    - A list of 3D geometries (breps) representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the overall bounding box
    total_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    
    # Define the central void as a box
    void_box = rg.Box(
        rg.Plane.WorldXY, 
        rg.Interval((length - void_width) / 2, (length + void_width) / 2), 
        rg.Interval(0, width), 
        rg.Interval(0, void_height)
    )
    
    # Create the two distinct parts by subtracting the void from the total box
    part1 = total_box.ToBrep()
    part2 = total_box.ToBrep()
    
    void_brep = void_box.ToBrep()
    
    part1 = rg.Brep.CreateBooleanDifference([part1], [void_brep], 0.01)[0]
    part2 = rg.Brep.CreateBooleanDifference([part2], [void_brep], 0.01)[0]
    
    # Shift part2 to create the visual distinction
    translation_vector = rg.Vector3d(random.uniform(0.5, 1.5), 0, 0)
    part2.Transform(rg.Transform.Translation(translation_vector))
    
    # Return the list of breps representing the two parts and the void
    return [part1, part2, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=25.0, width=15.0, height=12.0, void_width=3.0, void_height=9.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=30.0, width=20.0, height=15.0, void_width=4.0, void_height=10.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=22.0, width=12.0, height=9.0, void_width=2.5, void_height=7.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=18.0, width=8.0, height=10.0, void_width=1.5, void_height=6.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=24.0, width=14.0, height=11.0, void_width=3.5, void_height=8.0, seed=88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
