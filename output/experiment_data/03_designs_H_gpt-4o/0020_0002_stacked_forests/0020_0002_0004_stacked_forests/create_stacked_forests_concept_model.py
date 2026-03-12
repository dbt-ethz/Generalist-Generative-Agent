# Created for 0020_0002_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Stacked forests" metaphor by creating a series of interlocking, vertically stacked volumes. Each layer mimics forest growth, incorporating organic shapes and varying heights to reflect the forest's layered ecosystem. The model balances density with openness, integrating solid and void spaces to simulate clearings and pathways. Random geometric variations are introduced to enhance the organic feel, while vertical and horizontal circulation paths provide opportunities for exploration at different levels. The resulting 3D geometries capture the complexity, hierarchy, and dynamic interactions characteristic of a natural forest environment."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_radius=5.0, height_per_layer=3.0, num_layers=5, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Stacked forests' metaphor using a different approach.
    
    This function creates a series of vertically stacked, interlocking volumes that mimic forest layers, emphasizing
    organic growth and spatial hierarchy. The design features both solid and void spaces, creating a dynamic and 
    layered silhouette.

    Parameters:
    - base_radius (float): The base radius of the initial layer in meters.
    - height_per_layer (float): The height of each layer in meters.
    - num_layers (int): The total number of layers in the model.
    - seed (int): Seed for random number generation for replicable randomness.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for i in range(num_layers):
        # Calculate the height for the current layer
        current_height = i * height_per_layer

        # Determine the shape of the current layer using a random polygon
        num_segments = random.randint(5, 8)
        angle_increment = 2 * math.pi / num_segments
        base_polygon = []

        for j in range(num_segments):
            angle = j * angle_increment
            radius_variation = random.uniform(-0.2, 0.2) * base_radius
            x = (base_radius + radius_variation) * math.cos(angle)
            y = (base_radius + radius_variation) * math.sin(angle)
            base_polygon.append(rg.Point3d(x, y, current_height))

        base_polygon.append(base_polygon[0])  # Close the loop
        polygon_curve = rg.Polyline(base_polygon).ToNurbsCurve()

        # Create a vertical extrusion from the base polygon
        extrusion_vector = rg.Vector3d(0, 0, height_per_layer)
        layer_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(polygon_curve, extrusion_vector))
        
        if layer_brep:
            geometries.append(layer_brep)

        # Optionally add voids to create clearings
        if random.random() < 0.5:
            clearing_radius = random.uniform(base_radius * 0.3, base_radius * 0.6)
            clearing_center = rg.Point3d(random.uniform(-base_radius, base_radius),
                                         random.uniform(-base_radius, base_radius),
                                         current_height + height_per_layer / 2)
            clearing = rg.Brep.CreateFromSphere(rg.Sphere(clearing_center, clearing_radius))
            if clearing:
                geometries.append(clearing)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(base_radius=6.0, height_per_layer=2.5, num_layers=4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(base_radius=4.0, height_per_layer=3.5, num_layers=6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(base_radius=7.0, height_per_layer=4.0, num_layers=3, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(base_radius=5.5, height_per_layer=3.0, num_layers=7, seed=78)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(base_radius=8.0, height_per_layer=2.0, num_layers=5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
