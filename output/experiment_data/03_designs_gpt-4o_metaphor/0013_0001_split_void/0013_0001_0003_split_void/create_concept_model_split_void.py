# Created for 0013_0001_split_void.json

""" Summary:
The function `create_concept_model_split_void` generates a 3D architectural model based on the metaphor "Split void," which emphasizes division within a central open space. It defines a base volume and calculates a split void, creating distinct zones that enhance interactions with light and shadow. The model's dimensions and the degree of separation are adjustable through parameters like `length`, `width`, `height`, and `split_ratio`. By subtracting the void from the base volume and adding pathways, the design embodies dynamic tension and duality, resulting in an architectural form that evokes openness and movement while retaining a cohesive identity."""

#! python 3
function_code = """def create_concept_model_split_void(length, width, height, split_ratio=0.5):
    \"""
    Creates a 3D architectural concept model based on the 'Split Void' metaphor.
    
    This function generates a model with a central open space divided by a void,
    creating distinct zones that interact with light and shadow. The design 
    emphasizes duality and movement within a structured form.
    
    Parameters:
    - length (float): The total length of the concept model in meters.
    - width (float): The total width of the concept model in meters.
    - height (float): The total height of the concept model in meters.
    - split_ratio (float, optional): Ratio (0-1) determining the proportion of space
      allocated to the split void. Default is 0.5 for an equal split.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set randomness seed for replicability
    random.seed(42)

    # Calculate dimensions for the split void
    void_length = length * split_ratio
    void_width = width * split_ratio

    # Create the base volume
    base_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

    # Create the split void as a bounding box
    void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(length * (1-split_ratio)/2, length * (1+split_ratio)/2),
                      rg.Interval(width * (1-split_ratio)/2, width * (1+split_ratio)/2), rg.Interval(0, height))

    # Subtract the void from the base volume
    base_brep = base_volume.ToBrep()
    void_brep = void_box.ToBrep()
    split_brep = rg.Brep.CreateBooleanDifference(base_brep, void_brep, 0.001)

    # Ensure the result is valid
    if not split_brep:
        return []

    # Create additional geometry to emphasize the split
    path_width = width * 0.1
    path_length = length * 0.1
    path_plane = rg.Plane(rg.Point3d(length/2, width/2, 0), rg.Vector3d.ZAxis)
    path_box = rg.Box(path_plane, rg.Interval(-path_length/2, path_length/2), rg.Interval(-path_width/2, path_width/2), rg.Interval(0, height))

    # Merge the path with the split brep
    path_brep = path_box.ToBrep()
    final_brep = rg.Brep.CreateBooleanUnion(list(split_brep) + [path_brep], 0.001)

    if final_brep is None:
        return []

    return list(final_brep)"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_split_void(10, 5, 3, split_ratio=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_split_void(12, 8, 4, split_ratio=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_split_void(15, 10, 5, split_ratio=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_split_void(20, 15, 6, split_ratio=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_split_void(18, 9, 7, split_ratio=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
