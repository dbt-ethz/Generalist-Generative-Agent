# Created for 0020_0004_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the "Stacked forests" metaphor. It constructs a lattice-like structure with interwoven vertical and horizontal elements, capturing the essence of a forest's growth. By varying parameters like base size, number of layers, and organic shapes, the model reflects the complexity and hierarchy of natural ecosystems. The use of both rectilinear and curvilinear forms represents the unpredictable yet harmonious nature of forests. This approach results in a dynamic silhouette with diverse pathways, promoting exploration and interaction akin to navigating through a forest."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_size, num_layers, layer_height, organic_factor, density_factor):
    \"""
    Generate an architectural Concept Model based on the 'Stacked forests' metaphor.

    This function creates a lattice-like structure with interwoven horizontal and vertical elements,
    evocative of a forest's dense interconnectivity. It combines rectilinear and organic shapes to
    embody the forest's natural complexity and layered hierarchy.

    Parameters:
    - base_size: float, the base dimension of the model's footprint.
    - num_layers: int, the number of vertical layers in the structure.
    - layer_height: float, the height of each layer.
    - organic_factor: float, a factor (0 to 1) that influences the curvilinear nature of the shapes.
    - density_factor: float, a factor influencing the density of elements within each layer.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(123)  # Ensure replicability

    geometries = []

    def create_organic_shape(center, size, organic_factor):
        # Create a base circle and manipulate control points for an organic shape
        circle = rg.Circle(center, size)
        control_points = [circle.PointAt(t) for t in range(0, 360, 45)]
        for i, point in enumerate(control_points):
            offset = rg.Vector3d(random.uniform(-organic_factor, organic_factor),
                                 random.uniform(-organic_factor, organic_factor), 0)
            control_points[i] += offset
        curve = rg.NurbsCurve.Create(False, 3, control_points)
        surface = rg.Brep.CreatePlanarBreps(curve)
        return surface[0] if surface else None

    for layer in range(num_layers):
        z_offset = layer * layer_height
        # Vertical elements as tree trunks
        for i in range(int(base_size * density_factor)):
            x = random.uniform(0, base_size)
            y = random.uniform(0, base_size)
            start_point = rg.Point3d(x, y, z_offset)
            end_point = rg.Point3d(x, y, z_offset + layer_height)
            line = rg.Line(start_point, end_point)
            cylinder = rg.Cylinder(rg.Circle(line.From, base_size * 0.02), line.Length).ToBrep(True, True)
            geometries.append(cylinder)

        # Horizontal elements as branches
        for j in range(int(base_size * density_factor)):
            x1 = random.uniform(0, base_size)
            y1 = random.uniform(0, base_size)
            x2 = random.uniform(0, base_size)
            y2 = random.uniform(0, base_size)
            start_point = rg.Point3d(x1, y1, z_offset + random.uniform(0, layer_height))
            end_point = rg.Point3d(x2, y2, z_offset + random.uniform(0, layer_height))
            line = rg.Line(start_point, end_point)
            pipe = rg.Brep.CreatePipe(line.ToNurbsCurve(), [0.0, 1.0], [0.01, 0.01], True, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]
            geometries.append(pipe)

        # Organic canopy-like shapes
        for k in range(int(base_size * density_factor / 2)):
            center = rg.Point3d(random.uniform(0, base_size), random.uniform(0, base_size), z_offset + layer_height)
            organic_brep = create_organic_shape(center, base_size * 0.15, organic_factor)
            if organic_brep:
                geometries.append(organic_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(10.0, 5, 2.0, 0.3, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(8.0, 4, 1.5, 0.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(12.0, 6, 3.0, 0.4, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(15.0, 3, 2.5, 0.2, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(9.0, 7, 1.0, 0.6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
