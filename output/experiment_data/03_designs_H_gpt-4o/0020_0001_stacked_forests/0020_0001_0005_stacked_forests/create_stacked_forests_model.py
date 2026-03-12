# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Stacked forests." It constructs a series of distinct, vertically-layered platforms, each with organic shapes and irregular forms, reflecting the diverse strata of a forest. The function allows for variations in size and height to create a dynamic silhouette, akin to a forest canopy. Vertical circulation elements like ramps and staircases are integrated, enhancing connectivity between layers and offering diverse spatial experiences. By incorporating random curves and height variations, the model embodies the organic growth patterns found in nature, fulfilling the design task effectively."""

#! python 3
function_code = """def create_stacked_forests_model(base_width, base_depth, num_layers, height_variations, curve_variations, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Stacked forests' metaphor. The model consists of
    a series of layered platforms or blocks that rise vertically. Each layer is distinct in form and orientation,
    interconnected by vertical circulation elements like ramps or staircases. The design emphasizes organic shapes
    and irregular forms to represent the diverse forest strata.

    Inputs:
    - base_width: Float representing the base platform width in meters.
    - base_depth: Float representing the base platform depth in meters.
    - num_layers: Integer representing the number of vertical layers to create.
    - height_variations: Float representing the maximum variation in height between layers in meters.
    - curve_variations: Float representing the maximum deviation for creating organic curves in each layer.
    - seed: Integer for random seed to ensure replicability of the design.

    Outputs:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    current_height = 0

    for i in range(num_layers):
        # Create base plane for the current layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, current_height))

        # Determine dimensions with random variation
        width_variation = base_width * (1 + random.uniform(-0.1, 0.1))
        depth_variation = base_depth * (1 + random.uniform(-0.1, 0.1))

        # Create a base rectangle
        rect = rg.Rectangle3d(base_plane, width_variation, depth_variation)

        # Apply random curves to the corners for organic shapes
        corner_points = [rect.Corner(i) for i in range(4)]
        curve_points = [rg.Point3d(pt.X + random.uniform(-curve_variations, curve_variations),
                                   pt.Y + random.uniform(-curve_variations, curve_variations),
                                   pt.Z) for pt in corner_points]
        curve_points.append(curve_points[0])  # Close the loop

        polyline = rg.Polyline(curve_points)
        polyline_curve = polyline.ToNurbsCurve()

        # Extrude the curve to create a layer volume
        extrusion_vector = rg.Vector3d(0, 0, random.uniform(3, 3 + height_variations))
        extruded_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(polyline_curve, extrusion_vector))
        
        if extruded_surface:
            geometries.append(extruded_surface)

        # Move up for the next layer
        current_height += extrusion_vector.Z

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(5.0, 10.0, 6, 2.0, 1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(7.5, 12.0, 4, 1.5, 2.0, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(6.0, 8.0, 5, 3.0, 1.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(4.0, 9.0, 8, 2.5, 1.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(8.0, 15.0, 3, 2.0, 2.5, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
