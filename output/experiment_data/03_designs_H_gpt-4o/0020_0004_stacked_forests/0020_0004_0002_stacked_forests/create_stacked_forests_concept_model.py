# Created for 0020_0004_stacked_forests.json

""" Summary:
The provided Python function, `create_stacked_forests_concept_model`, generates an architectural concept model inspired by the metaphor of 'Stacked forests.' It achieves this by creating a complex lattice structure composed of interwoven vertical and horizontal elements, mimicking the interconnectedness of forest ecosystems. The function defines various parameters, including layer count, dimensions, and organic variations, to produce a diverse assortment of geometries. By combining rectilinear and curvilinear forms, the model embodies the organic growth and spatial richness of a forest, fostering layered interactions and pathways that encourage exploration, ultimately reflecting the metaphor's essence."""

#! python 3
function_code = """def create_stacked_forests_concept_model(num_layers, layer_height, base_width, base_depth, organic_variation, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Stacked forests' metaphor.

    This function generates a complex matrix of interwoven horizontal and vertical elements,
    using a combination of rectilinear and organic shapes to evoke the natural complexity
    and interconnectedness of a forest ecosystem.

    Parameters:
    - num_layers: int, number of vertical layers to stack.
    - layer_height: float, height of each layer in meters.
    - base_width: float, width of the base area in meters.
    - base_depth: float, depth of the base area in meters.
    - organic_variation: float, factor influencing the curvilinear nature of organic shapes (0 to 1).
    - seed: int, seed for random number generation to ensure replicability.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)  # Ensure replicability

    geometries = []

    # Define a function to create a curvilinear form
    def create_curvilinear_form(center, radius, height):
        circle = rg.Circle(center, radius)
        curve = circle.ToNurbsCurve()
        if random.random() < organic_variation:
            offset = rg.Vector3d(random.uniform(-radius * organic_variation, radius * organic_variation),
                                 random.uniform(-radius * organic_variation, radius * organic_variation), 0)
            curve.Translate(offset)
        extrusion = rg.Extrusion.Create(curve, height, True)
        if extrusion:
            return extrusion.ToBrep()
        return None

    # Create vertical layers
    for layer in range(num_layers):
        z_height = layer * layer_height
        
        # Create vertical elements
        for _ in range(3):  # Fixed number for simplicity
            x = random.uniform(0, base_width)
            y = random.uniform(0, base_depth)
            start_point = rg.Point3d(x, y, z_height)
            end_point = rg.Point3d(x, y, z_height + layer_height)
            line = rg.Line(start_point, end_point)
            pipe = rg.Brep.CreatePipe(line.ToNurbsCurve(), [0.0, 1.0], [0.1, 0.1], True, rg.PipeCapMode.Round, True, 0.01, 0.01)
            if pipe:
                geometries.append(pipe[0])

        # Create horizontal and curvilinear organic elements
        for _ in range(2):  # Fixed number for simplicity
            center = rg.Point3d(random.uniform(0, base_width), random.uniform(0, base_depth), z_height + layer_height / 2)
            radius = random.uniform(2, 4)
            brep = create_curvilinear_form(center, radius, layer_height)
            if brep:
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(5, 3.0, 10.0, 10.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(7, 2.5, 12.0, 15.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(4, 4.0, 8.0, 8.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(6, 2.0, 15.0, 10.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(3, 5.0, 20.0, 25.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
