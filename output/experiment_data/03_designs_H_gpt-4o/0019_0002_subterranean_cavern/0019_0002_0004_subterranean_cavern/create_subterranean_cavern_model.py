# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of vertically layered geometries that simulate the stratification found in caves. By defining a central void or atrium, the model invites exploration and immersion, akin to descending into a cavern. Each layer features varied thickness and radius, enhancing the sense of depth and mystery. Randomized offsets introduce a spiraling effect, reflecting the natural, organic forms of caverns. The resulting 3D geometries embody the qualities of exploration, refuge, and the interplay of light and shadow, resonating with the metaphors essence."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, total_height, num_layers, central_void_radius, layer_thickness_variation):
    \"""
    Generates an architectural Concept Model evoking the 'subterranean cavern' metaphor. 
    The model emphasizes vertical layering with a central void, capturing the sense of depth 
    and exploration inherent in a cavern. Each layer features varied heights and textures, 
    organized in a spiraling manner around a central atrium.

    Parameters:
    - base_radius (float): The radius of the base of the model.
    - total_height (float): The total height of the model.
    - num_layers (int): The number of vertical layers to create.
    - central_void_radius (float): The radius of the central void or atrium.
    - layer_thickness_variation (float): The maximum variation in thickness for each layer.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the model.
    \"""
    
    import Rhino.Geometry as rg
    import random

    # Initialize randomness
    random.seed(42)

    # Initialize list for storing geometries
    geometries = []

    # Calculate average layer thickness
    average_layer_thickness = total_height / num_layers

    # Create central void
    central_void = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, central_void_radius), total_height).ToBrep(True, True)

    for i in range(num_layers):
        # Randomize layer thickness
        layer_thickness = average_layer_thickness + random.uniform(-layer_thickness_variation, layer_thickness_variation)

        # Define the current layer's radius (create a tapering effect)
        current_radius = base_radius * (1 - i / num_layers * 0.3)
        
        # Create layer as a cylindrical Brep
        layer_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius), layer_thickness).ToBrep(True, True)

        # Translate layer to its correct vertical position
        translation = rg.Transform.Translation(0, 0, -i * average_layer_thickness)
        layer_cylinder.Transform(translation)

        # Subtract central void from layer
        layer_with_void = rg.Brep.CreateBooleanDifference(layer_cylinder, central_void, 0.01)
        if layer_with_void:
            geometries.extend(layer_with_void)
        
            # Introduce a spiraling offset
            offset_angle = random.uniform(0, 3.1415 / 6)
            offset_transform = rg.Transform.Rotation(offset_angle, rg.Vector3d.ZAxis, rg.Point3d.Origin)
            for brep in layer_with_void:
                brep.Transform(offset_transform)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 50.0, 5, 3.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 60.0, 8, 4.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.0, 40.0, 6, 2.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(20.0, 80.0, 10, 5.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(8.0, 30.0, 4, 2.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
