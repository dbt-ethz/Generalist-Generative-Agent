# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor by creating a series of staggered, layered platforms. It employs parameters such as base dimensions, height, number of layers, and a perforation factor to shape the model. The function creates each layer with varying widths and depths, incorporating perforations that mimic natural light and airflow pathways. By extruding rectangles and subtracting circular perforations, the model achieves a dynamic interplay of solid and void, embodying verticality and spatial connection, thus reflecting the metaphor's essence of permeability and interaction with the environment."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_dimension, height, number_of_layers, perforation_factor):
    \"""
    Creates an architectural Concept Model inspired by the 'Perforated vertical landscape' metaphor.
    
    This function generates a 3D model consisting of staggered, layered platforms with varying degrees of perforation,
    designed to allow light, air, and views to permeate through the structure. It embodies the concept of a vertical
    landscape with a rhythmic interplay between solid and void.

    Parameters:
    - base_dimension: float, the base dimension of the model (length of the ground plane).
    - height: float, the total height of the structure.
    - number_of_layers: int, the number of staggered layers/platforms.
    - perforation_factor: float, a value between 0 and 1 indicating the degree of perforation (0 for solid, 1 for fully perforated).

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    layers = []
    layer_height = height / number_of_layers

    for i in range(number_of_layers):
        # Calculate the current layer's position and size
        x_offset = random.uniform(-0.5, 0.5) * base_dimension * 0.1
        y_offset = random.uniform(-0.5, 0.5) * base_dimension * 0.1
        z_offset = i * layer_height

        # Base plane of the layer
        plane = rg.Plane.WorldXY
        plane.Origin = rg.Point3d(x_offset, y_offset, z_offset)

        # Create a base rectangle for the layer
        width = base_dimension * (0.8 + random.uniform(0, 0.2))
        depth = base_dimension * (0.8 + random.uniform(0, 0.2))
        rectangle = rg.Rectangle3d(plane, width, depth)

        # Extrude the rectangle to create a box
        extrusion = rg.Extrusion.Create(rectangle.ToNurbsCurve(), layer_height * (0.9 + random.uniform(0, 0.1)), True)
        
        # Create perforations
        perforations = []
        perforation_count = int(perforation_factor * 10)
        for _ in range(perforation_count):
            p_x = random.uniform(rectangle.Corner(0).X, rectangle.Corner(2).X)
            p_y = random.uniform(rectangle.Corner(0).Y, rectangle.Corner(2).Y)
            p_radius = random.uniform(0.1, 0.2) * base_dimension
            perforation_circle = rg.Circle(rg.Point3d(p_x, p_y, z_offset + layer_height / 2), p_radius)
            perforation = rg.Extrusion.Create(perforation_circle.ToNurbsCurve(), layer_height, True)
            perforations.append(perforation.ToBrep())

        # Subtract perforations from the layer
        solid_brep = extrusion.ToBrep()
        for perf in perforations:
            boolean_difference = rg.Brep.CreateBooleanDifference([solid_brep], [perf], 0.001)
            if boolean_difference:
                solid_brep = boolean_difference[0]

        layers.append(solid_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 20.0, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 30.0, 8, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 25.0, 6, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(8.0, 15.0, 4, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(20.0, 40.0, 10, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
