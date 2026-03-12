# Created for 0013_0002_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model based on the "Split void" metaphor by defining a central void that divides the building into two distinct sections. It constructs two halves of varying heights, reflecting the duality and dynamic tension suggested by the metaphor. The void not only separates but also connects these halves, promoting interaction and movement. The model emphasizes the interplay of light and shadow as the void becomes a channel for natural light, enhancing spatial experience. This design approach captures the essence of divided yet cohesive architectural identity."""

#! python 3
function_code = """def create_split_void_concept_model(base_length=30, base_width=20, height_variation=10, void_width=5):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor, where a central void
    divides the structure into two distinct parts. The void acts as a dynamic separator, influencing
    the building's geometry and spatial relationships.

    Parameters:
    - base_length (float): The overall length of the building in meters.
    - base_width (float): The width of the building in meters.
    - height_variation (float): The difference in height between the two halves of the building in meters.
    - void_width (float): The width of the central void in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg

    # Create the base profile
    half_width = (base_width - void_width) / 2

    # First half of the building
    base1 = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, half_width), rg.Interval(0, height_variation))
    brep1 = base1.ToBrep()

    # Second half of the building with different height
    base2 = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(base_width - half_width, base_width), rg.Interval(0, height_variation * 1.5))
    brep2 = base2.ToBrep()

    # Create the void
    void = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(half_width, base_width - half_width), rg.Interval(0, height_variation * 1.5))
    void_brep = void.ToBrep()

    # Subtract the void from the building halves
    brep1_diff = rg.Brep.CreateBooleanDifference([brep1], [void_brep], 0.01)
    brep2_diff = rg.Brep.CreateBooleanDifference([brep2], [void_brep], 0.01)

    # Collect the final geometry
    final_geometry = []
    if brep1_diff:
        final_geometry.extend(brep1_diff)
    if brep2_diff:
        final_geometry.extend(brep2_diff)

    return final_geometry"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(base_length=40, base_width=25, height_variation=12, void_width=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(base_length=50, base_width=30, height_variation=15, void_width=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(base_length=35, base_width=22, height_variation=9, void_width=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(base_length=45, base_width=28, height_variation=11, void_width=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(base_length=60, base_width=35, height_variation=20, void_width=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
