# Created for 0001_0002_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model based on the "House within a house" metaphor by creating nested cylindrical forms. It models an outer protective shell and an inner sanctuary, representing the idea of containment and retreat. The function utilizes parameters such as radii and heights to define the geometry of these layers, while creating transitional layers in between that vary in size and orientation, enhancing the interplay between openness and enclosure. The result is a collection of 3D geometries that visually translate the metaphor into a layered spatial hierarchy, inviting exploration and interaction within the design."""

#! python 3
function_code = """def create_concept_model(radius_outer, radius_inner, height_outer, height_inner, layer_distance):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor, using interlocking 
    and nested forms to convey a sense of nesting and protection.

    Parameters:
    - radius_outer (float): The radius of the outer shell.
    - radius_inner (float): The radius of the inner sanctuary.
    - height_outer (float): The height of the outer shell.
    - height_inner (float): The height of the inner sanctuary.
    - layer_distance (float): The distance between the outer shell and the inner sanctuary.

    Returns:
    - List of Breps: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for randomness
    random.seed(0)

    # Create the outer shell as a larger cylinder
    outer_shell = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, radius_outer), height_outer).ToBrep(True, True)

    # Create the inner sanctuary as a smaller, nested cylinder
    inner_sanctuary = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, radius_inner), height_inner).ToBrep(True, True)

    # Move the inner sanctuary upwards by layer_distance
    translation_vector = rg.Vector3d(0, 0, layer_distance)
    inner_sanctuary.Transform(rg.Transform.Translation(translation_vector))

    # Create a series of transitional layers between the outer and inner forms
    layer_count = 3
    layer_breps = []
    for i in range(layer_count):
        # Calculate transition radius and height
        transition_radius = radius_outer - (radius_outer - radius_inner) * (i + 1) / (layer_count + 1)
        transition_height = height_outer - (height_outer - height_inner) * (i + 1) / (layer_count + 1)
        
        # Create the transitional layer as a cylinder
        transition_layer = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, transition_radius), transition_height).ToBrep(True, True)
        
        # Slightly rotate each layer for dynamic interplay
        angle = random.uniform(-5, 5)  # Random rotation angle between -5 and 5 degrees
        rotation_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, 1)).Direction
        rotation_transform = rg.Transform.Rotation(math.radians(angle), rotation_axis, rg.Point3d(0, 0, 0))
        transition_layer.Transform(rotation_transform)

        # Move each layer upwards by a fraction of layer_distance
        transition_translation = rg.Vector3d(0, 0, layer_distance * (i + 1) / (layer_count + 1))
        transition_layer.Transform(rg.Transform.Translation(transition_translation))

        layer_breps.append(transition_layer)

    # Collect all geometries in a list
    concept_model_geometries = [outer_shell] + layer_breps + [inner_sanctuary]

    return concept_model_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(5.0, 3.0, 10.0, 6.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(7.0, 4.0, 12.0, 8.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(6.0, 2.5, 15.0, 9.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(8.0, 5.0, 14.0, 7.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(10.0, 6.0, 20.0, 12.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
