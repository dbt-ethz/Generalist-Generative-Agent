# Created for 0001_0005_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model that embodies the "House within a house" metaphor by creating concentric, layered volumes. Each layer varies in height and transparency, symbolizing the transition from the external environment to an inner sanctuary. The model's structure facilitates a journey through interstitial spaces, enhancing the exploration of the design. By manipulating the radius and applying random translations, it creates a dynamic interplay between openness and enclosure. This approach effectively communicates the protective nature of the design while highlighting the spatial hierarchy and the experiential quality of moving through nested spaces."""

#! python 3
function_code = """def create_concept_model(base_radius=10, num_layers=3, height_increment=5, transparency_values=None):
    \"""
    Creates an architectural Concept Model embodying the 'House within a house' metaphor.
    
    This function generates a series of concentric, layered volumes with varying heights and transparency levels,
    simulating the transition from the external environment to a core sanctuary. The design highlights the journey
    and discovery through interstitial spaces and dynamic spatial relationships.

    Parameters:
    - base_radius (float): The radius of the outermost layer in meters.
    - num_layers (int): The number of concentric layers or shells.
    - height_increment (float): The incremental height difference between each successive layer in meters.
    - transparency_values (list of float): A list representing transparency levels for each layer, 
                                           ranging from 0 (opaque) to 1 (fully transparent). If None, default values are used.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    if transparency_values is None:
        transparency_values = [i / num_layers for i in range(num_layers)]
    random.seed(42)  # Ensure replicability of any randomness

    geometries = []
    current_radius = base_radius

    for i in range(num_layers):
        # Create a cylindrical layer
        height = (i + 1) * height_increment
        cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius), height).ToBrep(True, True)
        
        # Adjust transparency (simulated here by assigning a material index, not visible in geometry)
        material_index = int(transparency_values[i] * 100)  # Not used directly, but would inform material setup in practice
        # Apply transformation for staggered effect
        translate_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 0)
        translation = rg.Transform.Translation(translate_vector)
        cylinder.Transform(translation)
        
        geometries.append(cylinder)
        
        # Reduce the radius for the next inner layer
        current_radius *= 0.8
        
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(base_radius=15, num_layers=5, height_increment=4, transparency_values=[0, 0.25, 0.5, 0.75, 1])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(base_radius=12, num_layers=4, height_increment=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(base_radius=20, num_layers=6, height_increment=3, transparency_values=[0.1, 0.3, 0.5, 0.7, 0.9, 1])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(base_radius=8, num_layers=3, height_increment=7, transparency_values=[0.2, 0.5, 0.8])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(base_radius=18, num_layers=2, height_increment=10, transparency_values=[0.4, 0.6])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
