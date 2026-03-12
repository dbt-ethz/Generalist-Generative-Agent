# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural model inspired by the metaphor of a subterranean cavern by creating stacked layers that emulate the depth and stratification of a cave. It organizes spaces around a central void or atrium, enhancing vertical movement and exploration. Each layer is formed as a cylinder with a tapered radius, while the central void is subtracted from these layers to create a sense of depth. Randomized offsets introduce a spiraling effect, emphasizing the immersive nature of the design. The result captures the essence of a cavern, fostering an atmosphere of mystery and refuge."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, height, num_layers, central_void_radius, seed=42):
    \"""
    Generates an architectural Concept Model evoking a 'subterranean cavern' metaphor. 
    The model consists of stacked layers with a central void, emphasizing vertical layering, 
    depth, and a sense of exploration. The spaces are organized around a central atrium in 
    a spiraling or cascading manner.

    Parameters:
    - base_radius (float): The radius of the base of the cavern model.
    - height (float): The total height of the cavern model.
    - num_layers (int): The number of stacked layers to create.
    - central_void_radius (float): The radius of the central void or atrium.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D breps representing the cavern model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set seed for randomness
    random.seed(seed)

    # Initialize list to hold the geometry
    geometries = []

    # Calculate layer thickness
    layer_thickness = height / num_layers

    # Create each layer
    for i in range(num_layers):
        # Calculate current layer radius and height
        current_radius = base_radius * (1 - (i / num_layers) * 0.3)  # Tapering effect
        current_height = i * layer_thickness

        # Create the main layer surface as a cylinder
        layer_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius), layer_thickness).ToBrep(True, True)
        
        # Create central void as a cylinder
        void_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, central_void_radius), layer_thickness).ToBrep(True, True)

        # Subtract the central void from the layer
        layer_with_void = rg.Brep.CreateBooleanDifference([layer_cylinder], [void_cylinder], 0.01)
        if layer_with_void:
            geometries.extend(layer_with_void)

        # Introduce a spiral or offset effect
        move_vector = rg.Vector3d(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), layer_thickness)
        offset_transform = rg.Transform.Translation(move_vector)
        for brep in layer_with_void:
            brep.Transform(offset_transform)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 30.0, 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 45.0, 7, 3.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.0, 36.0, 6, 2.5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(20.0, 50.0, 10, 4.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(8.0, 24.0, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
