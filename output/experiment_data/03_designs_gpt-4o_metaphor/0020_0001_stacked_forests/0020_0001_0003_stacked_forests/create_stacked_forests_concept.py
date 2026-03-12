# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Stacked Forests," emphasizing a multi-layered, vertical organization akin to a dense forest. It creates cylindrical layers representing the forest's tiers, with variations in base radius and height to mimic organic growth. The function incorporates randomness to enhance spatial diversity, allowing for voids that represent pathways, enriching interaction. By adjusting parameters like the number of layers and randomness, the model reflects hierarchical structures and vertical connectivity, creating a dynamic and immersive experience akin to navigating through a natural forest ecosystem."""

#! python 3
function_code = """def create_stacked_forests_concept(layers=5, base_radius=5.0, height_per_layer=3.0, randomness=0.2, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Stacked Forests'.
    
    The model emphasizes a multi-layered, vertical organization with a sense of hierarchy and organic growth,
    integrating natural elements and offering varied experiences and pathways.

    Parameters:
    - layers (int): Number of vertical layers in the model.
    - base_radius (float): Base radius of the circular footprint for each layer.
    - height_per_layer (float): Height of each layer.
    - randomness (float): Degree of randomness in the placement of elements (0 to 1).
    - seed (int): Random seed for reproducibility.

    Returns:
    - list: A list of RhinoCommon Breps representing the layered structures.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    breps = []

    for i in range(layers):
        # Calculate the center of the current layer
        z = i * height_per_layer
        layer_center = rg.Point3d(0, 0, z)
        
        # Create a circle for the current layer's base footprint
        layer_radius = base_radius * (1 + randomness * (random.random() - 0.5))
        circle = rg.Circle(layer_center, layer_radius)
        
        # Extrude the circle to create a cylindrical layer
        extrusion_vector = rg.Vector3d(0, 0, height_per_layer)
        cylinder = rg.Cylinder(circle, height_per_layer)
        cylinder_brep = cylinder.ToBrep(True, True)
        
        # Optionally subtract voids to represent pathways or open spaces
        void_chance = random.random()
        if void_chance < 0.5:  # 50% chance to create a void
            void_radius = layer_radius * (0.2 + 0.3 * random.random())
            void_circle = rg.Circle(layer_center, void_radius)
            void_cylinder = rg.Cylinder(void_circle, height_per_layer)
            void_brep = void_cylinder.ToBrep(True, True)
            boolean_difference = rg.Brep.CreateBooleanDifference([cylinder_brep], [void_brep], 0.01)
            if boolean_difference:
                cylinder_brep = boolean_difference[0]
        
        breps.append(cylinder_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(layers=7, base_radius=6.0, height_per_layer=4.0, randomness=0.3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(layers=3, base_radius=4.5, height_per_layer=2.5, randomness=0.1, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(layers=10, base_radius=5.5, height_per_layer=2.0, randomness=0.4, seed=27)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(layers=6, base_radius=5.0, height_per_layer=3.5, randomness=0.25, seed=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(layers=4, base_radius=5.5, height_per_layer=2.0, randomness=0.15, seed=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
