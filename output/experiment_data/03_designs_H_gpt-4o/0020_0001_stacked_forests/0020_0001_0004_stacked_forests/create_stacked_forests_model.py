# Created for 0020_0001_stacked_forests.json

""" Summary:
The function `create_stacked_forests_model` generates an architectural concept model inspired by the metaphor of "Stacked forests." It constructs a series of vertically stacked, curvilinear layers, each representing distinct forest strata through varying shapes and orientations. By utilizing parameters such as base radius, number of layers, height variation, and curve variance, the model creates organic forms that evoke natural growth patterns. The design emphasizes vertical connectivity by incorporating ramps and stairs, facilitating movement between levels. This approach not only reflects the hierarchical organization of a forest but also enhances spatial experiences, mirroring the interaction found within a natural ecosystem."""

#! python 3
function_code = """def create_stacked_forests_model(base_radius, num_layers, height_variation, curve_variance, seed=42):
    \"""
    Generates an architectural Concept Model embodying the 'Stacked forests' metaphor. The model consists of 
    a series of vertically stacked, curvilinear layers, each representing a 'forest layer' with distinct shapes 
    and orientations. The design uses organic forms and varying dimensions to evoke the natural growth patterns 
    of a forest.

    Inputs:
    - base_radius: Float representing the base radius for the bottom-most circular platform in meters.
    - num_layers: Integer representing the number of vertical layers to create.
    - height_variation: Float representing the maximum variation in height between layers in meters.
    - curve_variance: Float representing the maximum perturbation for the organic curvature of each layer.
    - seed: Integer for the random seed to ensure replicability of the design.

    Outputs:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(seed)

    geometries = []
    current_height = 0
    average_layer_height = 3.0  # Average height for each layer in meters

    for i in range(num_layers):
        # Create a base circle for the current layer
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)

        # Apply random perturbation to create organic shapes
        perturbed_points = []
        for angle in range(0, 360, 10):
            rad_angle = math.radians(angle)
            perturbation = random.uniform(-curve_variance, curve_variance)
            pt = rg.Point3d(base_radius * math.cos(rad_angle), base_radius * math.sin(rad_angle), 0)
            pt += rg.Vector3d(perturbation * math.cos(rad_angle), perturbation * math.sin(rad_angle), 0)
            perturbed_points.append(pt)

        # Create a nurbs curve through the perturbed points
        organic_curve = rg.Curve.CreateInterpolatedCurve(perturbed_points + [perturbed_points[0]], 3)

        # Generate a surface by extruding the curve vertically
        extrusion_vector = rg.Vector3d(0, 0, average_layer_height + random.uniform(-height_variation, height_variation))
        layer_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(organic_curve, extrusion_vector))

        # Translate the layer to its height position
        layer_surface.Transform(rg.Transform.Translation(rg.Vector3d(0, 0, current_height)))
        geometries.append(layer_surface)

        # Update the current height for the next layer
        current_height += extrusion_vector.Z

        # Optionally, add vertical circulation elements (ramps, stairs)
        if i < num_layers - 1:
            ramp_start = rg.Point3d(0, 0, current_height - extrusion_vector.Z)
            ramp_end = rg.Point3d(0, 0, current_height)
            ramp_curve = rg.LineCurve(ramp_start, ramp_end)
            ramp = rg.Brep.CreatePipe(ramp_curve, 0.5, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0]
            geometries.append(ramp)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(5.0, 4, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(7.0, 6, 2.0, 1.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(4.0, 5, 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(6.0, 3, 0.8, 0.2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(8.0, 5, 2.5, 0.7, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
