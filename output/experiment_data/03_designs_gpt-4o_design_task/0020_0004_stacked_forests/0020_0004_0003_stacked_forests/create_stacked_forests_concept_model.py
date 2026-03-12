# Created for 0020_0004_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a lattice-like structure composed of interwoven horizontal and vertical elements, symbolizing the interconnectedness of a forest. The model incorporates a mix of rectilinear and curvilinear shapes to reflect the organic complexity of forest ecosystems. Each layer features a matrix of intersecting forms that allow for varied spatial interactions, embodying the natural depth and hierarchy of a forest. This results in a dynamic silhouette with diverse heights, evoking the visual richness of layered forest environments."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_width, base_depth, num_layers, layer_height, curvilinear_factor, rectilinear_density):
    \"""
    Creates an architectural Concept Model embodying the 'Stacked forests' metaphor by generating a lattice-like structure
    composed of interwoven horizontal and vertical elements. The model consists of a matrix of intersecting forms symbolizing
    the dense interconnectivity of a forest, using a combination of rectilinear and organic shapes to capture the natural
    complexity and order found in forest ecosystems.

    Parameters:
    - base_width (float): Width of the base layer of the structure.
    - base_depth (float): Depth of the base layer of the structure.
    - num_layers (int): Number of vertical layers in the structure.
    - layer_height (float): Height of each layer.
    - curvilinear_factor (float): Factor controlling the degree of curvilinear deformation applied to the forms.
    - rectilinear_density (int): Number of rectilinear elements per layer.

    Returns:
    - list: A list of Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness for replicability
    random.seed(42)

    # Initialize list to store resulting geometries
    geometries = []

    # Function to create a curvilinear shape
    def create_curvilinear_shape(center_point, size, curvilinear_factor):
        circle = rg.Circle(center_point, size)
        control_points = [circle.PointAt(t) for t in range(0, 360, 45)]
        for i, point in enumerate(control_points):
            offset = rg.Vector3d(random.uniform(-curvilinear_factor, curvilinear_factor),
                                 random.uniform(-curvilinear_factor, curvilinear_factor),
                                 0)
            control_points[i] += offset
        curve = rg.NurbsCurve.Create(False, 3, control_points)
        breps = rg.Brep.CreatePlanarBreps(curve)
        return breps[0] if breps else None

    # Create each layer
    for i in range(num_layers):
        # Determine the base position for this layer
        z_offset = i * layer_height
        base_point = rg.Point3d(0, 0, z_offset)

        # Create rectilinear elements
        for _ in range(rectilinear_density):
            x_pos = random.uniform(0, base_width)
            y_pos = random.uniform(0, base_depth)
            width = random.uniform(1, 3)
            depth = random.uniform(1, 3)
            rect = rg.Box(rg.Plane(rg.Point3d(x_pos, y_pos, z_offset), rg.Vector3d.ZAxis), rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, layer_height))
            geometries.append(rect.ToBrep())

        # Create a curvilinear element
        curv_center = rg.Point3d(random.uniform(0, base_width), random.uniform(0, base_depth), z_offset + layer_height / 2)
        curv_size = random.uniform(3, 5)
        curvilinear_brep = create_curvilinear_shape(curv_center, curv_size, curvilinear_factor)
        
        if curvilinear_brep is not None:
            geometries.append(curvilinear_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(10.0, 15.0, 5, 2.0, 1.5, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(12.0, 20.0, 4, 3.0, 2.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(8.0, 10.0, 6, 1.5, 1.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(15.0, 25.0, 3, 4.0, 2.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(9.0, 18.0, 7, 2.5, 1.2, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
