# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model based on the "Stacked forests" metaphor by creating a series of layered platforms that mimic the structure of a forest. Each layer is designed with varying shapes and heights, reflecting the organic and irregular forms found in nature. The function incorporates vertical connectivity through ramps and pathways, enhancing user experience by simulating the movement through different forest strata. By adjusting parameters like base size and height, the model achieves a dynamic silhouette reminiscent of treetops, while integrating elements such as curves and terraces, reinforcing the metaphor of a multi-layered, natural environment."""

#! python 3
function_code = """def create_stacked_forests_layers(base_size, num_layers, height_factor, organic_shape_variation, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Stacked forests' metaphor, creating a series of
    layered platforms with organic shapes. Each layer is distinct in form and orientation, interconnected by
    natural pathways, reflecting diverse forest strata.

    Parameters:
    - base_size: Tuple of two floats representing the base platform size in meters (width, depth).
    - num_layers: Integer representing the number of vertical layers to create.
    - height_factor: Float representing a factor to vary the height between layers.
    - organic_shape_variation: Float determining the degree of organic shape deviation.
    - seed: Integer for random seed to ensure replicability of the design.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    width, depth = base_size
    current_height = 0
    geometries = []

    for i in range(num_layers):
        # Define the base plane for the current layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, current_height))

        # Create a circle to introduce organic shapes
        circle_radius = max(width, depth) * (0.5 + random.uniform(-organic_shape_variation, organic_shape_variation))
        circle = rg.Circle(base_plane, circle_radius)

        # Create a surface from the circle
        planar_breps = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())
        if planar_breps:
            surface = planar_breps[0]

            # Vary the height incrementally
            height_increment = 3.0 + height_factor * random.uniform(-1, 1)
            current_height += height_increment

            # Apply random rotation to simulate organic form
            rotation_angle = math.radians(random.uniform(-20, 20))
            rotation = rg.Transform.Rotation(rotation_angle, base_plane.ZAxis, circle.Center)
            surface.Transform(rotation)

            # Add the generated surface to the list of geometries
            geometries.append(surface)

            # Introduce a vertical connection element if not the last layer
            if i < num_layers - 1:
                path_start = circle.Center + rg.Vector3d(0, 0, height_increment / 2)
                path_end = path_start + rg.Vector3d(0, 0, height_increment)
                path_curve = rg.LineCurve(path_start, path_end)
                path_breps = rg.Brep.CreatePipe(path_curve, 0.3, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)
                if path_breps:
                    path = path_breps[0]
                    geometries.append(path)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_layers((10.0, 15.0), 5, 2.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_layers((8.0, 12.0), 4, 1.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_layers((12.0, 10.0), 6, 2.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_layers((15.0, 20.0), 3, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_layers((5.0, 7.0), 8, 1.8, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
