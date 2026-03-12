# Created for 0020_0001_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a series of layered platforms that rise vertically, simulating the tiered organization of a forest. Each layer, with distinct shapes and orientations, embodies the diverse strata of a forest, interconnected by ramps and staircases that enhance vertical connectivity. The function incorporates organic shapes and irregular forms to reflect natural growth patterns, while varying layer sizes and angles introduce visual dynamism. The resulting model emphasizes hierarchical spatial organization and a rich interaction experience, akin to navigating through a forest ecosystem."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_size, layer_count, layer_height, orientation_variance, curve_intensity):
    \"""
    Create a conceptual architectural model based on the 'Stacked forests' metaphor.
    
    This function generates a series of layered platforms or blocks that rise vertically, 
    each representing a forest layer. The layers are distinct in form and orientation, 
    interconnected by vertical circulation elements. The design uses organic shapes and 
    irregular forms to mimic the natural growth patterns found in forests.
    
    Parameters:
    - base_size: A tuple of (width, depth) in meters for the base layer.
    - layer_count: The number of vertical layers to create.
    - layer_height: The height of each layer in meters.
    - orientation_variance: The maximum angle in degrees to randomly orient each layer.
    - curve_intensity: A factor to determine the intensity of curvature for organic shapes.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensures replicable randomness

    def create_layer(center, width, depth, height, angle, curve_factor):
        \"""Create a single layer with organic edges.\"""
        # Create a rough rectangular base for the layer
        base_corners = [
            rg.Point3d(center.X - width / 2, center.Y - depth / 2, center.Z),
            rg.Point3d(center.X + width / 2, center.Y - depth / 2, center.Z),
            rg.Point3d(center.X + width / 2, center.Y + depth / 2, center.Z),
            rg.Point3d(center.X - width / 2, center.Y + depth / 2, center.Z)
        ]

        # Apply random perturbation to create organic edges
        for i in range(len(base_corners)):
            perturbation = rg.Vector3d(random.uniform(-curve_factor, curve_factor),
                                       random.uniform(-curve_factor, curve_factor), 0)
            base_corners[i] += perturbation

        # Create a polyline and a surface from the perturbed corners
        polyline = rg.Polyline(base_corners + [base_corners[0]])
        polyline_curve = polyline.ToNurbsCurve()
        polyline_curve.Rotate(math.radians(angle), rg.Vector3d.ZAxis, center)
        loft_curve = rg.Curve.CreateInterpolatedCurve([point.Location for point in polyline_curve.Points], 3)

        # Extrude the curve to create a layer volume
        extrusion_vector = rg.Vector3d(0, 0, height)
        layer_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(loft_curve, extrusion_vector))
        return layer_brep

    # Start creating the stacked forest model
    geometries = []
    current_center = rg.Point3d(0, 0, 0)

    for i in range(layer_count):
        width = base_size[0] * (1 - 0.1 * i)  # Decrease size for higher layers
        depth = base_size[1] * (1 - 0.1 * i)
        angle_variation = random.uniform(-orientation_variance, orientation_variance)
        layer_brep = create_layer(current_center, width, depth, layer_height, angle_variation, curve_intensity)
        
        # Move center up for the next layer
        current_center.Z += layer_height * 0.8  # Overlap layers slightly for organic stacking

        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model((10, 10), 5, 2, 30, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model((15, 15), 7, 3, 45, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model((12, 12), 6, 2.5, 60, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model((20, 20), 4, 1.5, 15, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model((8, 8), 8, 2, 25, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
