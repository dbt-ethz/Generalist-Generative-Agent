# Created for 0001_0004_house_within_a_house.json

""" Summary:
The provided function, `create_concept_model_house_within_house`, generates an architectural concept model based on the 'House within a house' metaphor. It creates a series of concentric or interwoven layers, symbolizing nesting and protection. The function uses parameters like inner and outer radii, height, and the number of layers to define the model's dimensions. Each layer is represented as a cylinder, with variations in height to enhance the interwoven effect. This approach embodies the design task by visually illustrating the transition from the outer protective layer to the inner sanctuary, emphasizing spatial hierarchy and experiential qualities."""

#! python 3
function_code = """def create_concept_model_house_within_house(inner_radius, outer_radius, height, layers, seed=None):
    \"""
    Creates a conceptual architectural model embodying the 'House within a house' metaphor.
    
    This function generates a composition of concentric or interwoven layers that illustrate
    a sense of nesting and protection, using modular geometries to evoke a layered spatial hierarchy.

    Parameters:
    - inner_radius (float): The radius of the innermost core representing the sanctuary.
    - outer_radius (float): The radius of the outermost layer representing the protective envelope.
    - height (float): The height of each layer in the model.
    - layers (int): The number of concentric layers to generate.
    - seed (int, optional): A seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the layers of the Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random
    
    if seed is not None:
        random.seed(seed)

    # Ensure valid input
    if outer_radius <= inner_radius or layers < 1 or height <= 0:
        raise ValueError("Invalid input parameters for concept model.")

    # Calculate the increment in radius for each layer
    radius_increment = (outer_radius - inner_radius) / layers

    # Generate the layers
    breps = []
    for i in range(layers):
        # Calculate the radius for this layer
        layer_radius = inner_radius + i * radius_increment

        # Create a cylinder for the layer
        circle = rg.Circle(rg.Plane.WorldXY, layer_radius)
        cylinder = rg.Cylinder(circle, height)

        # Convert to Brep
        brep = cylinder.ToBrep(True, True)
        
        # Randomly offset the layer's height to create interwoven effect
        if i % 2 == 0:
            offset = random.uniform(-height * 0.1, height * 0.1)
            translation = rg.Vector3d(0, 0, offset)
            brep.Transform(rg.Transform.Translation(translation))
        
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_house_within_house(inner_radius=2.0, outer_radius=5.0, height=3.0, layers=4, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_house_within_house(inner_radius=1.5, outer_radius=6.0, height=2.5, layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_house_within_house(inner_radius=3.0, outer_radius=7.0, height=4.0, layers=5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_house_within_house(inner_radius=2.5, outer_radius=8.0, height=3.5, layers=3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_house_within_house(inner_radius=1.0, outer_radius=4.0, height=2.0, layers=8, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
