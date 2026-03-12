# Created for 0013_0001_split_void.json

""" Summary:
The provided function generates an architectural concept model based on the "Split void" metaphor by creating a structure that features a prominent central void dividing the building into two distinct sections. The function defines the dimensions and volumes for each side, ensuring a clear separation through geometric manipulation. By applying contrasting material ratios, it emphasizes this division visually. The model considers the interaction of light and shadow, allowing for dynamic spatial experiences. Ultimately, this approach encapsulates the metaphor's essence, fostering a duality in function and form while enhancing circulation and visual connectivity within the design."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width_ratio, material_contrast_ratio):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor. This function generates a structure with
    a prominent central void that divides the building into two distinct parts, using contrasting forms or volumes on each
    side to emphasize separation. The model explores the interplay of light and shadow through the space.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_width_ratio (float): Ratio of the void's width to the total width (0 < void_width_ratio < 1).
    - material_contrast_ratio (float): Ratio indicating contrast between the two sides (0 < material_contrast_ratio < 1).

    Returns:
    - List of RhinoCommon Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg

    # Calculate void dimensions
    void_width = width * void_width_ratio
    half_width = (width - void_width) / 2

    # Define the volumes for the two sections
    left_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, half_width), rg.Interval(0, height))
    right_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width + void_width, width), rg.Interval(0, height))

    # Create the central void
    central_void = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width, half_width + void_width), rg.Interval(0, height))

    # Generate breps for the two sections and the void
    left_brep = left_volume.ToBrep()
    right_brep = right_volume.ToBrep()
    void_brep = central_void.ToBrep()

    # Apply material contrast by scaling one of the sections
    material_contrast = 1 + (material_contrast_ratio * 0.2)  # Scale factor based on contrast ratio
    contrast_transform = rg.Transform.Scale(rg.Plane.WorldXY, material_contrast, material_contrast, 1)
    left_brep.Transform(contrast_transform)
    
    # Return the list of geometries
    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 5.0, 3.0, 0.3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15.0, 8.0, 4.0, 0.25, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(12.0, 6.0, 3.5, 0.4, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(20.0, 10.0, 5.0, 0.2, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(8.0, 4.0, 2.5, 0.35, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
