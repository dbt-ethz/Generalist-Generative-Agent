# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of vertically stacked layers that mimic the stratification of a cavern, descending into the ground around a central atrium. Each layer features varied heights and decreasing radii to evoke a spiraling descent, enhancing the immersive experience. The use of random height variations and textures reflects the organic qualities of natural caves, emphasizing exploration and mystery. Ultimately, the model captures a balance of open and enclosed spaces, embodying the essence of refuge and the natural environment."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, base_height, num_layers, layer_height_variation):
    \"""
    Creates an architectural Concept Model evoking the 'subterranean cavern' metaphor. The model consists of 
    a series of stacked layers that descend into the ground, organized around a central void or atrium. 
    Spaces spiral or cascade around this core, with varied vertical transitions and ceiling heights.

    Parameters:
    - base_radius: float, the radius of the base layer representing the widest part of the cavern.
    - base_height: float, the height of the first layer, setting the starting point for the vertical descent.
    - num_layers: int, the number of stratified layers in the model.
    - layer_height_variation: float, the maximum variation in height for each subsequent layer.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness to ensure replicability
    random.seed(42)

    geometries = []
    current_radius = base_radius
    current_height = base_height

    # Create a central void or atrium
    atrium_height = base_height * num_layers
    atrium = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, base_radius * 0.2), atrium_height).ToBrep(True, True)
    geometries.append(atrium)

    # Create the stratified layers
    for i in range(num_layers):
        # Randomize the height of each layer
        layer_height = base_height + random.uniform(-layer_height_variation, layer_height_variation)
        current_height -= layer_height

        # Create a tiered platform
        layer = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, current_radius), layer_height).ToBrep(True, True)
        translation = rg.Transform.Translation(0, 0, current_height)
        layer.Transform(translation)
        geometries.append(layer)
        
        # Reduce the radius to create a descending spiral effect
        current_radius *= random.uniform(0.7, 0.9)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10, 5, 8, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15, 10, 5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12, 6, 10, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(8, 4, 6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(20, 7, 4, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
