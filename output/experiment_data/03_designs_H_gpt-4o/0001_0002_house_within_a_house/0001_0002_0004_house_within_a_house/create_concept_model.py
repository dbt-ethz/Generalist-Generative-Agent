# Created for 0001_0002_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a series of interlocking forms that embody nesting and protection. It constructs an outer shell and multiple nested layers, each with decreasing dimensions and varying curvatures to symbolize containment and retreat. By adjusting parameters like layer count and inner spacing, the function explores spatial relationships, facilitating a hierarchy from public to private spaces. The incorporation of curved geometries and transitional voids encourages light penetration and visual interaction, effectively representing the metaphors dynamic interplay between openness and enclosure in the architectural design."""

#! python 3
function_code = """def create_concept_model(length_outer, width_outer, height_outer, layer_count, inner_spacing, curvature, seed=1):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor, using interlocking and nested forms
    to convey a sense of nesting and protection. This version explores the use of curved geometries and transitional voids.

    Parameters:
    - length_outer (float): The length of the outermost shell.
    - width_outer (float): The width of the outermost shell.
    - height_outer (float): The height of the outermost shell.
    - layer_count (int): The number of layers between the outer shell and the inner sanctuary.
    - inner_spacing (float): The spacing between each nested layer.
    - curvature (float): The curvature factor applied to the inner forms, between 0 and 1.
    - seed (int): Random seed for replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Outer shell as a curved box
    outer_base = rg.Plane.WorldXY
    outer_box = rg.Box(outer_base, rg.Interval(0, length_outer), rg.Interval(0, width_outer), rg.Interval(0, height_outer)).ToBrep()

    # Create intermediate layers
    layer_breps = []
    for i in range(layer_count):
        length = length_outer - (i + 1) * inner_spacing
        width = width_outer - (i + 1) * inner_spacing
        height = height_outer - (i + 1) * inner_spacing * curvature
        
        base = rg.Plane.WorldXY
        
        # Apply curvature by scaling along the height
        scale_factor = 1 - curvature * (i + 1) / layer_count
        transformation = rg.Transform.Scale(base, 1, 1, scale_factor)
        
        box = rg.Box(base, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        box.Transform(transformation)
        box_brep = box.ToBrep()
        layer_breps.append(box_brep)

    # Create inner sanctuary as a smaller, curved box
    inner_length = length_outer - (layer_count + 1) * inner_spacing
    inner_width = width_outer - (layer_count + 1) * inner_spacing
    inner_height = height_outer - (layer_count + 1) * inner_spacing * curvature

    inner_base = rg.Plane.WorldXY
    inner_box = rg.Box(inner_base, rg.Interval(0, inner_length), rg.Interval(0, inner_width), rg.Interval(0, inner_height)).ToBrep()

    # Collection of geometries
    concept_model_geometries = [outer_box] + layer_breps + [inner_box]
    
    return concept_model_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10.0, 8.0, 12.0, 5, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(15.0, 10.0, 20.0, 4, 1.5, 0.3, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(12.0, 9.0, 15.0, 6, 0.8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(20.0, 15.0, 18.0, 3, 2.0, 0.7, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(25.0, 20.0, 30.0, 2, 1.2, 0.6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
