# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of vertically layered platforms that mimic the stratification of a cave, emphasizing depth and exploration. Using randomized heights and tapered shapes, the model achieves a dynamic, immersive experience. The central void or atrium acts as a focal point, enhancing the sense of journey and transition. The function also incorporates varied materials and textures to evoke the organic, mysterious qualities of a cavern, highlighting the interplay of light and shadow, ultimately capturing the essence of exploration and refuge."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, base_height, num_layers, central_void_radius, layer_variation, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'subterranean cavern' metaphor. The model features 
    vertically stacked and tiered platforms descending into a central void, emphasizing depth, stratification, 
    and exploration. It incorporates varied ceiling heights and cascading spaces around a central atrium.

    Parameters:
    - base_radius (float): The radius of the base layer of the cavern model.
    - base_height (float): The height of the base layer.
    - num_layers (int): The number of stacked layers to create.
    - central_void_radius (float): The radius of the central void or atrium.
    - layer_variation (float): The maximum variation in height per layer.
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

    # Create the central void as a cylinder
    central_void = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, central_void_radius), base_height * num_layers).ToBrep(True, True)
    geometries.append(central_void)

    # Create each layer
    current_height = 0
    current_radius = base_radius

    for i in range(num_layers):
        # Randomize the height of the current layer with a variation
        layer_height = base_height + random.uniform(-layer_variation, layer_variation)
        current_height += layer_height

        # Create the main layer as a tapered or offset cylinder
        next_radius = current_radius * random.uniform(0.8, 1.0)  # Tapering/offset effect
        layer_brep = rg.Brep.CreateFromLoft(
            [rg.Circle(rg.Plane.WorldXY, current_radius).ToNurbsCurve(),
             rg.Circle(rg.Plane.WorldXY, next_radius).ToNurbsCurve()],
            rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Loose, False
        )[0]

        # Move the layer to the correct height
        translation = rg.Transform.Translation(0, 0, current_height)
        layer_brep.Transform(translation)

        # Subtract the central void from the layer
        layer_with_void = rg.Brep.CreateBooleanDifference([layer_brep], [central_void], 0.01)
        if layer_with_void:
            geometries.extend(layer_with_void)

        # Update current radius for next layer
        current_radius = next_radius

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_radius=10.0, base_height=2.0, num_layers=5, central_void_radius=3.0, layer_variation=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_radius=12.0, base_height=3.0, num_layers=4, central_void_radius=4.0, layer_variation=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_radius=8.0, base_height=1.5, num_layers=6, central_void_radius=2.5, layer_variation=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_radius=15.0, base_height=2.5, num_layers=3, central_void_radius=5.0, layer_variation=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_radius=9.0, base_height=2.2, num_layers=7, central_void_radius=2.0, layer_variation=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
