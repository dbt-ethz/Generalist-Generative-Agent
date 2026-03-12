# Created for 0001_0005_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model that embodies the "House within a house" metaphor by creating concentric, nested volumes. It begins with a central core volume, representing the inner sanctuary, and adds layers that symbolize varying degrees of enclosure and transition. Each layer is articulated with different heights and materials, enhancing the dynamic interaction between open and private spaces. The function incorporates interstitial spaces to guide movement and foster a sense of discovery, effectively illustrating the metaphors themes of nesting, protection, and the unique spatial experiences within the architectural design."""

#! python 3
function_code = """def create_concept_model(core_radius=5.0, layer_count=3, layer_thickness=1.0, interstitial_space=1.5):
    \"""
    Create an architectural Concept Model embodying the 'House within a house' metaphor.
    
    This function generates a series of concentric, layered volumes where each layer represents a transition
    from the external environment to the core sanctuary. The model features a central core surrounded by
    concentric shells with varying heights and forms, creating a dynamic interplay between openness and enclosure.
    
    Parameters:
    - core_radius (float): The radius of the central core volume in meters.
    - layer_count (int): The number of concentric layers surrounding the core.
    - layer_thickness (float): The thickness of each layer in meters.
    - interstitial_space (float): The space between each layer in meters, providing transitional zones.
    
    Returns:
    - List of Breps: A list of 3D geometries representing the concentric layers and core.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicable results with a set seed

    geometries = []
    current_radius = core_radius

    # Create the central core volume
    core_height = core_radius * 2  # Proportional height for the core
    core = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius), core_height).ToBrep(True, True)
    geometries.append(core)

    # Generate concentric layers
    for i in range(layer_count):
        current_radius += interstitial_space + layer_thickness
        layer_height = core_height + random.uniform(0.5, 1.5)  # Randomize height slightly for variation
        
        # Create the outer shell
        outer_shell = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius), layer_height).ToBrep(True, True)
        
        # Create the inner shell
        inner_shell = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius - layer_thickness), layer_height).ToBrep(True, True)
        
        # Subtract inner shell from outer shell to create a hollow layer
        hollow_layer = rg.Brep.CreateBooleanDifference([outer_shell], [inner_shell], 0.01)
        
        if hollow_layer:
            geometries.extend(hollow_layer)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(core_radius=6.0, layer_count=4, layer_thickness=1.5, interstitial_space=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(core_radius=4.0, layer_count=5, layer_thickness=0.8, interstitial_space=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(core_radius=7.0, layer_count=2, layer_thickness=1.0, interstitial_space=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(core_radius=5.5, layer_count=6, layer_thickness=1.2, interstitial_space=1.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(core_radius=8.0, layer_count=3, layer_thickness=2.0, interstitial_space=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
