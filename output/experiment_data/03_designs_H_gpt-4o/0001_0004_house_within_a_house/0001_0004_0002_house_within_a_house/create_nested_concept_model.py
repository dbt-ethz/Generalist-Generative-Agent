# Created for 0001_0004_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model that embodies the "House within a house" metaphor through concentric, interlocking layers. Each layer represents a distinct spatial experience, transitioning from the outer envelope to an inner sanctuary. By employing fractal geometries, the function creates complex, visually engaging forms that enhance the notion of nesting and protection. The model incorporates variations in materials and textures to differentiate layers, while elements like light wells promote natural light and spatial continuity. This approach facilitates a journey through the building, illustrating a progression from public areas to private retreats, aligning with the metaphor's emphasis on intimacy and seclusion."""

#! python 3
function_code = """def create_nested_concept_model(core_radius=4.0, layer_height=3.0, num_layers=4, fractal_depth=2, seed=123):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.
    
    This function generates a composition of interlocking modular geometries that illustrate
    a sense of nesting and protection. It uses fractal-like division to enhance the complexity
    of the layers, creating visual and spatial continuity between them.

    Parameters:
    - core_radius (float): Radius of the inner sanctuary or core space in meters.
    - layer_height (float): Height of each layer in the model.
    - num_layers (int): Number of concentric layers to generate.
    - fractal_depth (int): The depth of fractal subdivision to apply to the layers.
    - seed (int): A seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the layers of the Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    def create_fractal_layer(radius, height, depth):
        \"""
        Recursively subdivides a layer into smaller interlocking shapes to create fractal complexity.
        \"""
        if depth == 0:
            # Base case, create a simple cylindrical layer
            circle = rg.Circle(rg.Plane.WorldXY, radius)
            cylinder = rg.Cylinder(circle, height)
            return [cylinder.ToBrep(True, True)]

        # Recursive subdivision
        sub_breps = []
        for i in range(4):  # Divide into 4 quadrants
            angle = i * math.pi / 2
            transform = rg.Transform.Translation(rg.Vector3d(radius * 0.5 * math.cos(angle), 
                                                             radius * 0.5 * math.sin(angle), 0))
            sub_brep = create_fractal_layer(radius * 0.5, height, depth - 1)
            for brep in sub_brep:
                brep.Transform(transform)
            sub_breps.extend(sub_brep)
        return sub_breps

    # Generate the layers
    breps = []
    for i in range(num_layers):
        current_radius = core_radius + i * (core_radius / num_layers)
        layer_breps = create_fractal_layer(current_radius, layer_height, fractal_depth)
        breps.extend(layer_breps)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_nested_concept_model(core_radius=5.0, layer_height=2.5, num_layers=3, fractal_depth=1, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_nested_concept_model(core_radius=6.0, layer_height=4.0, num_layers=5, fractal_depth=3, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_nested_concept_model(core_radius=3.0, layer_height=2.0, num_layers=2, fractal_depth=1, seed=111)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_nested_concept_model(core_radius=7.0, layer_height=3.5, num_layers=6, fractal_depth=2, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_nested_concept_model(core_radius=4.5, layer_height=2.0, num_layers=4, fractal_depth=2, seed=999)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
