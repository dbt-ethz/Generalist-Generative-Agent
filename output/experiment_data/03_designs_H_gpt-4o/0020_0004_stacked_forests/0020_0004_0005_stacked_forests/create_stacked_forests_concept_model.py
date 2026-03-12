# Created for 0020_0004_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the metaphor of "Stacked forests." It constructs a lattice-like structure with interwoven horizontal and vertical elements, reflecting the complex interconnections of forest systems. By combining rectilinear and organic shapes, the function captures the organic complexity and layered hierarchy of a forest. Each layer is created with a variety of pathways and spaces, allowing for exploration and interaction, while the varied heights and dynamic silhouette evoke the rich diversity of a forest ecosystem. The result is a visually textured and spatially rich architectural model."""

#! python 3
function_code = """def create_stacked_forests_concept_model(width, depth, num_layers, layer_height, organic_variation, rectilinear_density):
    \"""
    Create an architectural Concept Model based on the 'Stacked forests' metaphor.

    This function generates a lattice-like structure with interwoven horizontal and vertical elements,
    using a combination of rectilinear and organic shapes. The model represents a complex matrix of
    intersecting forms, evoking the interconnected roots and branches of a forest.

    Parameters:
    - width (float): Width of the base of the structure.
    - depth (float): Depth of the base of the structure.
    - num_layers (int): Number of vertical layers in the structure.
    - layer_height (float): Height of each layer.
    - organic_variation (float): Amount of variation for organic shapes (0 to 1).
    - rectilinear_density (int): Number of rectilinear elements per layer.

    Returns:
    - list: A list of Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Seed for replicability

    geometries = []

    # Function to create an organic shape
    def create_organic_shape(center_point, scale, variation):
        circle = rg.Circle(center_point, scale)
        control_points = [circle.PointAt(t / 8.0 * math.tau) for t in range(8)]
        for i in range(len(control_points)):
            offset = rg.Vector3d(random.uniform(-variation, variation),
                                 random.uniform(-variation, variation),
                                 0)
            control_points[i] += offset
        curve = rg.NurbsCurve.Create(False, 3, control_points)
        return rg.Brep.CreatePlanarBreps(curve)[0] if curve and rg.Brep.CreatePlanarBreps(curve) else None

    # Create each layer
    for i in range(num_layers):
        z_offset = i * layer_height

        # Create rectilinear elements
        for _ in range(rectilinear_density):
            x_pos = random.uniform(0, width)
            y_pos = random.uniform(0, depth)
            element_width = random.uniform(1, 3)
            element_depth = random.uniform(1, 3)
            box = rg.Box(rg.Plane(rg.Point3d(x_pos, y_pos, z_offset), rg.Vector3d.ZAxis),
                         rg.Interval(0, element_width),
                         rg.Interval(0, element_depth),
                         rg.Interval(0, layer_height))
            geometries.append(box.ToBrep())

        # Create an organic element
        org_center = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), z_offset + layer_height / 2)
        org_scale = random.uniform(2, 4)
        organic_brep = create_organic_shape(org_center, org_scale, organic_variation)
        if organic_brep:
            geometries.append(organic_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(10.0, 5.0, 3, 2.0, 0.5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(15.0, 10.0, 5, 3.0, 0.3, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(12.0, 6.0, 4, 1.5, 0.7, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(20.0, 8.0, 6, 2.5, 0.4, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(8.0, 4.0, 2, 1.0, 0.6, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
