# Created for 0013_0002_split_void.json

""" Summary:
The `create_split_void_concept_model` function generates an architectural concept model based on the "Split void" metaphor by defining a structural layout that incorporates a central void. The function takes parameters for building dimensions and void characteristics, allowing for vertical or horizontal splits. It calculates the dimensions of two distinct halves of the structure, creating spatial separation while maintaining a cohesive design. The void acts as a dynamic element, facilitating light and shadow interplay, and enhances movement through the building. The resulting geometries illustrate the duality and unity of spaces, embodying the metaphor's essence."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_ratio=0.3, split_orientation='vertical'):
    \"""
    Generate an architectural Concept Model based on the 'Split void' metaphor, focusing on the spatial
    separation and connection through a central void. This model explores the interplay of light, shadow,
    and movement within divided spaces, capturing the essence of duality and unity.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The overall height of the building in meters.
    - void_ratio (float): The ratio of the void width/height to the total width/height of the building.
    - split_orientation (str): The orientation of the void, either 'vertical' or 'horizontal'.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the building and the void.
    \"""
    import Rhino.Geometry as rg

    # Calculate void dimensions
    void_dimension = (width if split_orientation == 'vertical' else height) * void_ratio

    # Define side dimensions based on split orientation
    if split_orientation == 'vertical':
        side_dimension = (width - void_dimension) / 2
        lower_left_a = rg.Point3d(0, 0, 0)
        upper_right_a = rg.Point3d(length, side_dimension, height)
        lower_left_b = rg.Point3d(0, side_dimension + void_dimension, 0)
        upper_right_b = rg.Point3d(length, width, height)
    else:
        side_dimension = (height - void_dimension) / 2
        lower_left_a = rg.Point3d(0, 0, 0)
        upper_right_a = rg.Point3d(length, width, side_dimension)
        lower_left_b = rg.Point3d(0, 0, side_dimension + void_dimension)
        upper_right_b = rg.Point3d(length, width, height)

    # Create Breps for the two halves
    box_a = rg.Box(rg.BoundingBox(lower_left_a, upper_right_a))
    box_b = rg.Box(rg.BoundingBox(lower_left_b, upper_right_b))

    # Create the void space
    if split_orientation == 'vertical':
        void_lower_left = rg.Point3d(0, side_dimension, 0)
        void_upper_right = rg.Point3d(length, side_dimension + void_dimension, height)
    else:
        void_lower_left = rg.Point3d(0, 0, side_dimension)
        void_upper_right = rg.Point3d(length, width, side_dimension + void_dimension)

    void_box = rg.Box(rg.BoundingBox(void_lower_left, void_upper_right))

    # Convert boxes to Breps
    brep_a = box_a.ToBrep()
    brep_b = box_b.ToBrep()
    void_brep = void_box.ToBrep()

    # Return the list of Breps representing the concept model
    return [brep_a, brep_b, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(20, 10, 5, void_ratio=0.2, split_orientation='horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15, 8, 6, void_ratio=0.4, split_orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(30, 15, 10, void_ratio=0.3, split_orientation='horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(25, 12, 8, void_ratio=0.5, split_orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(18, 9, 4, void_ratio=0.25, split_orientation='horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
