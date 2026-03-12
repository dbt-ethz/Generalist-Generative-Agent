# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model by implementing the 'Split void' metaphor, which envisions a structure divided by a central void. It creates two distinct masses on either side of this void, allowing for contrasting materials and shapes that emphasize separation. The function considers the orientation of the void, whether vertical or horizontal, and introduces random perturbations to the shapes to enhance visual interest. This design fosters dynamic interactions with natural light, creating patterns and shadows, while also facilitating circulation and experience within the space, reflecting the duality inherent in the metaphor."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, void_orientation='vertical'):
    \"""
    Create an architectural Concept Model embodying the 'Split void' metaphor. This function generates a structure with 
    a prominent central void that divides the building into two distinct parts. The model explores the interplay between 
    the divided sections, emphasizing separation through contrasting forms and interaction with natural light.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - void_orientation (str): Orientation of the void ('vertical' or 'horizontal').

    Returns:
    - list: A list of RhinoCommon Brep objects representing the building's geometry, including the two split halves and the void.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for reproducibility
    random.seed(42)

    # Create the two building masses
    if void_orientation == 'vertical':
        half_width = (width - void_width) / 2
        mass1 = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, half_width), rg.Interval(0, height))
        mass2 = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width + void_width, width), rg.Interval(0, height))
    else:
        half_length = (length - void_width) / 2
        mass1 = rg.Box(rg.Plane.WorldXY, rg.Interval(0, half_length), rg.Interval(0, width), rg.Interval(0, height))
        mass2 = rg.Box(rg.Plane.WorldXY, rg.Interval(half_length + void_width, length), rg.Interval(0, width), rg.Interval(0, height))

    # Convert boxes to Breps
    brep1 = mass1.ToBrep()
    brep2 = mass2.ToBrep()

    # Simulate contrasting forms using random perturbations
    def perturb_brep(brep, max_perturbation=0.5):
        vertices = brep.DuplicateVertices()
        for vertex in vertices:
            perturbation = rg.Vector3d(
                random.uniform(-max_perturbation, max_perturbation),
                random.uniform(-max_perturbation, max_perturbation),
                random.uniform(-max_perturbation, max_perturbation)
            )
            vertex.Transform(rg.Transform.Translation(perturbation))
        return rg.Brep.CreateFromCornerPoints(vertices[0], vertices[1], vertices[2], vertices[3], 0.01)

    brep1_perturbed = perturb_brep(brep1)
    brep2_perturbed = perturb_brep(brep2)

    # Assemble the final model
    concept_model = [brep1_perturbed, brep2_perturbed]

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(20, 10, 5, 2, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(30, 15, 6, 3, 'horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(25, 12, 8, 4, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(40, 20, 10, 5, 'horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(15, 8, 4, 1, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
