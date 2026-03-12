# Created for 0020_0005_stacked_forests.json

""" Summary:
The function `generate_cascading_terraces` creates an architectural concept model inspired by the "Stacked forests" metaphor. It generates a series of terraces that symbolize ecological layers within a forest, emphasizing vertical integration and light interplay. Each layer is crafted with varying openness, allowing for a dynamic interaction of enclosed and open spaces. The function employs randomness to introduce organic variations in shape, simulating natural growth patterns. By iteratively constructing layers with specified dimensions and thickness, the model evolves into a stepped silhouette, reminiscent of cascading forest formations, enriching the spatial experience and connectivity akin to a living ecosystem."""

#! python 3
function_code = """def generate_cascading_terraces(base_size, num_layers, layer_thickness, openness_factor, organic_factor, seed=42):
    \"""
    Generates an architectural concept model based on the 'Stacked forests' metaphor.

    This model features a cascading series of terraces or ledges, each representing different ecological layers.
    It emphasizes vertical integration, light penetration, and shadow play, using a combination of linear and organic shapes.

    Parameters:
    - base_size: Tuple[float, float], the base dimensions (length, width) of the model in meters.
    - num_layers: int, the number of cascading layers or terraces to create.
    - layer_thickness: float, the thickness of each layer in meters.
    - openness_factor: float, a factor between 0 and 1 determining the openness of each layer (0 being completely enclosed, 1 fully open).
    - organic_factor: float, a factor to introduce organic variation in layer shapes.
    - seed: int, random seed for replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    random.seed(seed)
    
    base_length, base_width = base_size
    geometries = []
    current_z = 0

    for i in range(num_layers):
        # Calculate the openness of the current layer
        layer_openness = openness_factor * random.uniform(0.5, 1.0)

        # Create a base rectangle for the current layer
        length_variation = base_length * (1 - i * layer_openness / num_layers)
        width_variation = base_width * (1 - i * layer_openness / num_layers)

        # Introduce organic shapes using the organic_factor
        organic_variation = organic_factor * random.uniform(-0.5, 0.5)
        
        # Create a non-uniform rectangle to simulate organic growth
        corners = [
            rg.Point3d(0, 0, current_z),
            rg.Point3d(length_variation, 0, current_z),
            rg.Point3d(length_variation + organic_variation, width_variation, current_z),
            rg.Point3d(organic_variation, width_variation, current_z)
        ]

        # Generate a planar surface from the corners
        surface = rg.Brep.CreateFromCornerPoints(corners[0], corners[1], corners[2], corners[3], 0.01)
        
        if surface:
            # Extrude the surface to create a solid layer
            extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
            extrusion_curve = rg.LineCurve(rg.Point3d(0, 0, current_z), rg.Point3d(0, 0, current_z + layer_thickness))
            extrusion = rg.Brep.CreateFromSurface(surface.Faces[0].DuplicateSurface())
            if extrusion:
                extrusion = extrusion.Faces[0].CreateExtrusion(extrusion_curve, True)
                if extrusion:
                    geometries.append(extrusion)
        
        current_z += layer_thickness
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cascading_terraces((10, 5), 5, 0.5, 0.8, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cascading_terraces((15, 8), 4, 0.3, 0.6, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cascading_terraces((12, 6), 6, 0.4, 0.7, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cascading_terraces((20, 10), 3, 0.6, 0.9, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cascading_terraces((8, 4), 7, 0.2, 0.5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
