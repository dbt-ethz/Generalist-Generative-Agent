# Created for 0020_0001_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept` generates an architectural concept model inspired by the metaphor of "Stacked forests." It constructs vertically layered platforms that mimic the structure of a forest, with distinct sizes, orientations, and organic shapes to represent various forest strata. Each layer is interconnected by ramps or staircases, enhancing vertical connectivity and user experience. The function applies randomness to create irregular edges, reflecting natural growth. By varying layer sizes and heights, the design emphasizes a hierarchy and spatial richness, ultimately encapsulating the dynamic and organic essence of a forest ecosystem in a built form."""

#! python 3
function_code = """def create_stacked_forests_concept(base_size, num_layers, height_variation, organic_factor, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Stacked forests' metaphor.
    
    This function constructs a series of vertically layered platforms with organic and irregular forms 
    to represent the diverse forest strata. Each layer is distinct in size and orientation, yet 
    interconnected by vertical circulation elements.

    Parameters:
    - base_size: tuple of (width, depth) in meters for the base layer.
    - num_layers: int, the number of vertical layers to create.
    - height_variation: float, the maximum variation in height between layers in meters.
    - organic_factor: float, a factor influencing the organic irregularity of layer edges.
    - seed: int, seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    
    def create_irregular_layer(center, width, depth, height, curve_factor):
        \"""Create a single irregular layer with organic edges.\"""
        # Create a rough rectangular base for the layer
        corners = [
            rg.Point3d(center.X - width / 2, center.Y - depth / 2, center.Z),
            rg.Point3d(center.X + width / 2, center.Y - depth / 2, center.Z),
            rg.Point3d(center.X + width / 2, center.Y + depth / 2, center.Z),
            rg.Point3d(center.X - width / 2, center.Y + depth / 2, center.Z)
        ]

        # Apply random perturbation to create organic edges
        for i in range(len(corners)):
            perturbation = rg.Vector3d(random.uniform(-curve_factor, curve_factor),
                                       random.uniform(-curve_factor, curve_factor), 0)
            corners[i] += perturbation

        # Create a polyline and a surface from the perturbed corners
        polyline = rg.Polyline(corners + [corners[0]])
        polyline_curve = polyline.ToNurbsCurve()
        loft_curve = rg.Curve.CreateInterpolatedCurve([point.Location for point in polyline_curve.Points], 3)

        # Extrude the curve to create a layer volume
        extrusion_vector = rg.Vector3d(0, 0, height)
        layer_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(loft_curve, extrusion_vector))
        return layer_brep

    # Start creating the stacked forest model
    geometries = []
    current_center = rg.Point3d(0, 0, 0)

    for i in range(num_layers):
        width = base_size[0] * (1 - 0.1 * i)  # Decrease size for higher layers
        depth = base_size[1] * (1 - 0.1 * i)
        height = random.uniform(2, height_variation)  # Vary the height
        layer_brep = create_irregular_layer(current_center, width, depth, height, organic_factor)
        
        # Move center up for the next layer
        current_center.Z += height * 0.8  # Overlap layers slightly for organic stacking

        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept((10, 10), 5, 3.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept((15, 15), 4, 2.5, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept((12, 12), 6, 4.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept((20, 20), 3, 5.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept((8, 8), 7, 4.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
