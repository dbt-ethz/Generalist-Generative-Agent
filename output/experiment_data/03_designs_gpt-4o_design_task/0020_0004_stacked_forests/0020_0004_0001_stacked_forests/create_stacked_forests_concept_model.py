# Created for 0020_0004_stacked_forests.json

""" Summary:
The `create_stacked_forests_concept_model` function generates an architectural model reflecting the 'Stacked forests' metaphor by creating a lattice-like structure of interwoven horizontal and vertical elements. It utilizes specified base dimensions, vertical layers, and horizontal elements to design a dynamic framework that symbolizes the dense interconnectivity of a forest. The function incorporates both rectilinear and curvilinear shapes, influenced by an organic shape factor, to evoke the complexity and harmony of natural ecosystems. By layering these elements, it fosters varied spatial relationships, creating pathways and intersections that promote exploration and interaction, mirroring a forest's rich diversity and growth."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_dims, vertical_layers, horizontal_elements, organic_shape_factor):
    \"""
    Create an architectural Concept Model based on the 'Stacked forests' metaphor.

    This function generates a lattice-like structure with interwoven horizontal and vertical elements,
    evoking a natural forest with diverse pathways and spaces. It combines rectilinear and organic shapes to
    create a dynamic and textured silhouette.

    Parameters:
    - base_dims: tuple of (float, float) representing the base dimensions of the model (width, depth).
    - vertical_layers: int, number of vertical layers to stack, representing different levels of the forest.
    - horizontal_elements: int, number of horizontal elements per layer, representing pathways and spaces.
    - organic_shape_factor: float, a factor influencing the curvilinear nature of organic shapes (0 to 1).

    Returns:
    - List of RhinoCommon breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    width, depth = base_dims
    height_per_layer = 3.0  # Standard height for each vertical layer

    geometries = []

    # Create vertical layers
    for layer in range(vertical_layers):
        base_height = layer * height_per_layer

        # Create horizontal elements within each layer
        for element in range(horizontal_elements):
            element_width = width * (0.2 + 0.6 * random.random())
            element_depth = depth * (0.2 + 0.6 * random.random())

            # Determine position within the layer
            x_pos = width * (0.1 + 0.8 * random.random())
            y_pos = depth * (0.1 + 0.8 * random.random())

            # Create the base rectangle for the element
            base_plane = rg.Plane(rg.Point3d(x_pos, y_pos, base_height), rg.Vector3d.ZAxis)
            rect_corners = [
                rg.Point3d(x_pos, y_pos, base_height),
                rg.Point3d(x_pos + element_width, y_pos, base_height),
                rg.Point3d(x_pos + element_width, y_pos + element_depth, base_height),
                rg.Point3d(x_pos, y_pos + element_depth, base_height)
            ]
            polyline = rg.Polyline(rect_corners + [rect_corners[0]])
            profile_curve = polyline.ToNurbsCurve()

            # Apply organic transformation
            organic_transform = rg.Transform.Identity
            if random.random() < organic_shape_factor:
                organic_transform = rg.Transform.Rotation(
                    random.uniform(-0.1, 0.1), 
                    rg.Vector3d.ZAxis, 
                    rg.Point3d(x_pos + element_width / 2, y_pos + element_depth / 2, base_height)
                )
            profile_curve.Transform(organic_transform)

            # Extrude the profile curve to create 3D geometry
            extrusion_vector = rg.Vector3d(0, 0, height_per_layer)
            extrusion = rg.Extrusion.Create(profile_curve, height_per_layer, True)
            if extrusion:
                brep = extrusion.ToBrep()
                if brep:
                    geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model((10.0, 10.0), 5, 8, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model((20.0, 15.0), 4, 10, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model((15.0, 12.0), 6, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model((25.0, 20.0), 3, 5, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model((30.0, 25.0), 7, 12, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
