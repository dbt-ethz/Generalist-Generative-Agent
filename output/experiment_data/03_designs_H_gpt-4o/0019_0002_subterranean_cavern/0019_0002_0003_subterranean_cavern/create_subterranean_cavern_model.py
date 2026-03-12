# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The provided function `create_subterranean_cavern_model` generates an architectural concept model inspired by the 'subterranean cavern' metaphor. It creates a series of tiered layers that spiral downwards, resembling the stratification of a cavern. Each layer is designed with a hollow central void, promoting vertical movement and exploration. The function utilizes parameters such as base diameter, height, and the number of layers to simulate depth. By applying random rotational shifts to each layer and organizing them around a central atrium, it evokes a sense of immersion and mystery, capturing the essence of a subterranean environment through varied textures and spatial relationships."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_diameter, total_height, num_layers, central_void_diameter, seed=42):
    \"""
    Creates an architectural Concept Model inspired by the 'subterranean cavern' metaphor. The model features 
    tiered platforms that spiral downwards, organizing spaces around a central void, emphasizing depth and exploration.

    Parameters:
    - base_diameter (float): The diameter of the base of the cavern model.
    - total_height (float): The total height of the cavern model from top to bottom.
    - num_layers (int): The number of stacked layers or tiers in the model.
    - central_void_diameter (float): The diameter of the central void or atrium.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D breps representing the cavern model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    import math
    
    # Set seed for random number generation
    random.seed(seed)
    
    # Initialize list to store the resulting geometries
    geometries = []
    
    # Calculate the height and radius decrement per layer
    layer_height = total_height / num_layers
    radius_decrement = (base_diameter - central_void_diameter) / num_layers / 2
    
    # Create layers with a spiraling effect
    for i in range(num_layers):
        # Current layer radius
        current_radius = (base_diameter / 2) - (i * radius_decrement)
        
        # Create a hollow cylinder for the layer
        outer_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius), layer_height).ToBrep(True, True)
        inner_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, central_void_diameter / 2), layer_height).ToBrep(True, True)
        
        # Subtract the central void from the layer
        layer_brep = rg.Brep.CreateBooleanDifference([outer_cylinder], [inner_cylinder], 0.01)
        if layer_brep:
            geometries.extend(layer_brep)
        
        # Apply a spiral shift to the layer
        spiral_angle = random.uniform(5, 15) * (i + 1)
        spiral_transform = rg.Transform.Rotation(math.radians(spiral_angle), rg.Vector3d.ZAxis, rg.Point3d(0, 0, i * layer_height))
        
        for brep in layer_brep:
            brep.Transform(spiral_transform)
            
        # Move the layer to the correct height
        move_transform = rg.Transform.Translation(0, 0, i * layer_height)
        for brep in layer_brep:
            brep.Transform(move_transform)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 30.0, 5, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 45.0, 8, 4.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.0, 36.0, 6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(20.0, 50.0, 10, 5.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(8.0, 24.0, 4, 2.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
