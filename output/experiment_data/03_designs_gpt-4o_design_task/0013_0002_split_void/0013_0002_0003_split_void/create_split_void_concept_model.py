# Created for 0013_0002_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model based on the 'Split void' metaphor by creating two distinct building sections separated by a central void. It takes parameters for dimensions and heights, allowing for dynamic variations in the structure. The left and right sections are represented by boxes, with the void acting as a pivotal element that fosters light interaction and spatial flow. By manipulating the geometry such as applying slight rotations to the right section the model captures the essence of duality, promoting movement and visual dialogue while maintaining a cohesive architectural identity."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, height_left, height_right, void_width, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor, focusing on divided spaces with a central void.
    
    Parameters:
    - base_length: The total length of the building from front to back (meters).
    - base_width: The total width of the building including the void (meters).
    - height_left: The height of the left section of the building (meters).
    - height_right: The height of the right section of the building (meters).
    - void_width: The width of the central void separating the two sections (meters).
    - seed: A seed for random number generation to ensure replicability (default is 42).
    
    Returns:
    - A list of RhinoCommon Brep objects representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Calculate dimensions
    left_width = (base_width - void_width) / 2
    right_width = (base_width - void_width) / 2

    # Create base planes
    base_plane_left = rg.Plane.WorldXY
    base_plane_right = rg.Plane.WorldXY

    # Move the base plane for the right part
    base_plane_right.OriginX += left_width + void_width

    # Create boxes for the left and right sections
    left_box = rg.Box(base_plane_left, rg.Interval(0, left_width), rg.Interval(0, base_length), rg.Interval(0, height_left))
    right_box = rg.Box(base_plane_right, rg.Interval(0, right_width), rg.Interval(0, base_length), rg.Interval(0, height_right))

    # Create a central void as a vertical box
    void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(left_width, left_width + void_width), rg.Interval(0, base_length), rg.Interval(0, max(height_left, height_right)))

    # Convert boxes to Breps
    left_brep = left_box.ToBrep()
    right_brep = right_box.ToBrep()
    void_brep = void_box.ToBrep()

    # Optional: Apply different textures or forms (for conceptual purposes, we'll just modify the geometry slightly)
    # Add a slight rotation to the right section to create a dynamic form
    rotation_angle = random.uniform(-5, 5)  # Degrees
    rotation_axis = rg.Vector3d.ZAxis  # Z-Axis for vertical rotation
    rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, right_box.Center)
    right_brep.Transform(rotation_transform)

    # Return the Breps for the concept model
    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(20, 10, 15, 10, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(30, 12, 18, 12, 3, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(25, 15, 20, 15, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(40, 20, 25, 20, 5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(35, 18, 22, 19, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
