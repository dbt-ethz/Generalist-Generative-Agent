# Created for 0001_0004_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the 'House within a house' metaphor by creating a series of concentric, overlapping layers. Each layer represents distinct spatial functions, transitioning from public to private realms, thus embodying the principles of nesting and protection. The model incorporates varying heights and radii to create a cascading effect, enhancing visual and spatial continuity. Openings simulate light wells, promoting natural light penetration and connection between layers. Ultimately, this approach fosters an experiential journey through the layered spaces, reflecting the dynamic interplay of exposure and seclusion inherent in the metaphor."""

#! python 3
function_code = """def generate_concept_model(concentric_layers=4, base_layer_height=3.0, height_increment=1.0, seed=1):
    \"""
    Generates an architectural Concept Model embodying the 'House within a house' metaphor.

    This function creates a series of nested and overlapping layers, each representing a distinct spatial
    function or level of intimacy. The design emphasizes a layered spatial hierarchy, transitioning from
    public to private spaces, while incorporating elements such as voids and light wells to enhance
    natural light penetration and visual connections.

    Parameters:
    - concentric_layers (int): Number of concentric layers in the model.
    - base_layer_height (float): The height of the innermost layer.
    - height_increment (float): Incremental height added to each successive layer to create a cascading effect.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the layers of the Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set random seed for replicability
    random.seed(seed)

    # Initialize list to store the resulting geometries
    geometries = []

    # Base radius for the innermost space
    base_radius = 5.0

    # Generate concentric layers
    for i in range(concentric_layers):
        # Calculate the radius and height for each layer
        radius = base_radius + i * 2.0
        height = base_layer_height + i * height_increment

        # Create base cylinder
        base_circle = rg.Circle(rg.Plane.WorldXY, radius)
        base_cylinder = rg.Cylinder(base_circle, height).ToBrep(True, True)

        # Create openings in the layers to simulate light wells
        opening_radius = random.uniform(radius * 0.2, radius * 0.3)
        opening_circle = rg.Circle(rg.Plane.WorldXY, opening_radius)
        opening_cylinder = rg.Cylinder(opening_circle, height).ToBrep(False, False)

        # Subtract opening from the layer
        light_well = rg.Brep.CreateBooleanDifference([base_cylinder], [opening_cylinder], 0.01)
        if light_well:
            geometries.extend(light_well)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_concept_model(concentric_layers=5, base_layer_height=2.5, height_increment=1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_concept_model(concentric_layers=3, base_layer_height=4.0, height_increment=0.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_concept_model(concentric_layers=6, base_layer_height=3.5, height_increment=2.0, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_concept_model(concentric_layers=7, base_layer_height=3.0, height_increment=1.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_concept_model(concentric_layers=4, base_layer_height=2.0, height_increment=0.8, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
