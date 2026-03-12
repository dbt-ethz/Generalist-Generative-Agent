# Created for 0020_0004_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forest_concept_model`, generates a conceptual architectural model inspired by the metaphor of "Stacked forests." It creates a lattice-like structure by layering vertical and horizontal elements, mimicking the intertwined roots and branches of a forest. By using randomization for placement and dimensions, the model embodies organic growth and complexity, reflecting diverse spatial relationships akin to a forest ecosystem. The function outputs a collection of 3D geometries that showcase varied heights and interconnections, enhancing the exploration and interaction within the space, while the resulting silhouette reflects the textured and dynamic nature of a forest."""

#! python 3
function_code = """def create_stacked_forest_concept_model(num_layers, layer_height, horizontal_span, vertical_span, seed):
    \"""
    Creates a conceptual architectural model inspired by the 'Stacked forests' metaphor.
    
    This function generates a lattice-like structure with interwoven horizontal and vertical elements, 
    using a combination of rectilinear and organic shapes. The model represents a complex matrix of 
    intersecting forms, evoking the interconnected roots and branches of a forest.

    Parameters:
    - num_layers (int): The number of vertical layers in the structure.
    - layer_height (float): The height of each layer in meters.
    - horizontal_span (float): The span of horizontal elements in meters.
    - vertical_span (float): The span of vertical elements in meters.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    geometries = []

    for layer in range(num_layers):
        z_offset = layer * layer_height
        num_verticals = random.randint(2, 5)
        num_horizontals = random.randint(2, 5)
        
        # Create vertical elements with random offsets to simulate organic growth
        for _ in range(num_verticals):
            x_offset = random.uniform(-horizontal_span / 2, horizontal_span / 2)
            y_offset = random.uniform(-horizontal_span / 2, horizontal_span / 2)
            start_point = rg.Point3d(x_offset, y_offset, z_offset)
            end_point = rg.Point3d(x_offset, y_offset, z_offset + vertical_span)
            line = rg.Line(start_point, end_point)
            # Create a circle with a plane perpendicular to the line
            circle = rg.Circle(rg.Plane(start_point, line.Direction), 0.2)
            cylinder = rg.Cylinder(circle, vertical_span).ToBrep(True, True)
            geometries.append(cylinder)

        # Create horizontal elements
        for _ in range(num_horizontals):
            start_x = random.uniform(-horizontal_span / 2, horizontal_span / 2)
            start_y = random.uniform(-horizontal_span / 2, horizontal_span / 2)
            end_x = random.uniform(-horizontal_span / 2, horizontal_span / 2)
            end_y = random.uniform(-horizontal_span / 2, horizontal_span / 2)
            start_point = rg.Point3d(start_x, start_y, z_offset + random.uniform(0, layer_height))
            end_point = rg.Point3d(end_x, end_y, z_offset + random.uniform(0, layer_height))
            line = rg.Line(start_point, end_point)
            # Corrected the Pipe creation
            pipe = rg.Brep.CreatePipe(line.ToNurbsCurve(), [0.0, 1.0], [0.1, 0.1], True, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]
            geometries.append(pipe)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forest_concept_model(5, 2.0, 10.0, 15.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forest_concept_model(3, 1.5, 8.0, 12.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forest_concept_model(4, 3.0, 6.0, 10.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forest_concept_model(6, 2.5, 12.0, 20.0, 28)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forest_concept_model(7, 1.0, 15.0, 25.0, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
