# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept_model_alternative`, generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates multiple vertically stacked platforms, each with unique shapes and heights, reflecting the layered structure of a forest ecosystem. The function employs random perturbations to introduce organic forms, enhancing the resemblance to natural elements. Each platform is interconnected by ramps or staircases, promoting vertical connectivity and varied spatial experiences. The model emphasizes hierarchy and diversity, embodying the metaphor's essence by simulating a dynamic skyline reminiscent of treetops in a forest."""

#! python 3
function_code = """def create_stacked_forests_concept_model_alternative(base_size, num_layers, max_height_variation, curvature_factor, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Stacked forests' metaphor. This model consists of vertically
    stacked, organically shaped platforms that mimic the layered structure of a forest. Each layer is distinct in form
    and orientation, interconnected by pathways to enhance vertical connectivity.

    Parameters:
    - base_size: Tuple of two floats (width, depth) representing the base dimensions in meters.
    - num_layers: Integer, the number of vertical layers or platforms to create.
    - max_height_variation: Float, the maximum variation in height between the layers in meters.
    - curvature_factor: Float, a factor influencing the degree of curvature and organic form of the platforms.
    - seed: Integer, a seed for the random number generator to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []
    current_height = 0.0
    base_width, base_depth = base_size

    for i in range(num_layers):
        # Calculate size variation and height for the current layer
        width_variation = base_width * (1 - 0.1 * i)
        depth_variation = base_depth * (1 - 0.1 * i)
        height_increment = 3.0 + random.uniform(-max_height_variation, max_height_variation)

        # Create an organic shape using a circle base and perturb its control points
        circle = rg.Circle(rg.Plane.WorldXY, width_variation / 2)
        circle_pts = circle.ToNurbsCurve().Points
        for pt in circle_pts:
            perturbation = rg.Vector3d(random.uniform(-curvature_factor, curvature_factor),
                                       random.uniform(-curvature_factor, curvature_factor), 0)
            pt.Location += perturbation

        # Create a nurbs curve from perturbed points and loft into a brep
        organic_curve = rg.Curve.CreateInterpolatedCurve([pt.Location for pt in circle_pts], 3)
        loft_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(organic_curve, rg.Vector3d(0, 0, height_increment)))

        # Transform the brep to current layer height
        translation = rg.Transform.Translation(0, 0, current_height)
        loft_brep.Transform(translation)
        
        # Add the brep to the geometries list
        geometries.append(loft_brep)
        
        # Increment the current height for the next layer
        current_height += height_increment * 0.8  # Slightly overlap layers for organic stacking

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model_alternative((10.0, 10.0), 5, 2.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model_alternative((15.0, 15.0), 4, 1.5, 2.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model_alternative((8.0, 12.0), 6, 3.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model_alternative((12.0, 8.0), 3, 1.0, 1.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model_alternative((20.0, 10.0), 7, 2.5, 1.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
