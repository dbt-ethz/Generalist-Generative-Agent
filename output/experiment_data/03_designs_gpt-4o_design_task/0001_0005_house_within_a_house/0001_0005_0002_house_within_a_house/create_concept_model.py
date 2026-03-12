# Created for 0001_0005_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a series of concentric, layered volumes. Each layer represents varying degrees of enclosure and intimacy, reflecting a spatial hierarchy. The parameters allow for customization of the base radius, number of layers, height variations, and transparency levels, signifying transitions from public to private spaces. The function utilizes geometric constructs to form solid and void relationships, enhancing the experiential qualities of movement and discovery throughout the nested layers, ultimately embodying the metaphor of retreat and encapsulation in architectural design."""

#! python 3
function_code = """def create_concept_model(base_radius, layer_count, height_variation, transparency_levels):
    \"""
    Creates a series of concentric, layered volumes to embody the 'House within a house' metaphor.
    
    Parameters:
    - base_radius: The radius of the innermost core volume (in meters).
    - layer_count: The number of concentric layers surrounding the core.
    - height_variation: A list of height values (in meters) for each layer, indicating varying heights.
    - transparency_levels: A list of transparency values for each layer, indicating different material or transparency levels.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set seed for reproducibility
    random.seed(42)
    
    # List to store the resulting breps
    breps = []
    
    # Create the core central volume
    core_height = height_variation[0]
    core = rg.Cylinder(rg.Circle(rg.Point3d(0, 0, 0), base_radius), core_height).ToBrep(True, True)
    breps.append(core)
    
    # Generate concentric layers
    for i in range(1, layer_count + 1):
        layer_radius = base_radius + i * 2  # Increment radius for each layer
        layer_height = height_variation[i % len(height_variation)]  # Cycle through the provided heights
        # Create each layer as a hollow cylinder
        outer_cylinder = rg.Cylinder(rg.Circle(rg.Point3d(0, 0, 0), layer_radius), layer_height).ToBrep(True, True)
        inner_cylinder = rg.Cylinder(rg.Circle(rg.Point3d(0, 0, 0), layer_radius - 1), layer_height).ToBrep(True, True)
        layer = rg.Brep.CreateBooleanDifference([outer_cylinder], [inner_cylinder], 0.01)[0]
        breps.append(layer)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(5, 3, [10, 15, 20], [0.2, 0.5, 0.8])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(4, 5, [8, 12, 16, 20, 24], [0.1, 0.3, 0.6, 0.9, 0.4])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(6, 4, [5, 10, 15, 20], [0.3, 0.7, 0.4, 0.9])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(3, 2, [12, 18], [0.1, 0.5])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(7, 6, [9, 14, 19, 24, 29, 34], [0.4, 0.6, 0.2, 0.8, 0.5, 0.3])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
