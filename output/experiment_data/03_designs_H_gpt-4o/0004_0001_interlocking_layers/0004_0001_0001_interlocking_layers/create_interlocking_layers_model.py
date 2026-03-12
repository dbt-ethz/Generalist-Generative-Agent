# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model reflecting the metaphor of "Interlocking Layers." It creates multiple overlapping planes by defining the base dimensions, the number of layers, and their heights. Each layer is represented as a volume that is extruded from a rectangular base, incorporating random rotations to illustrate the interlocking nature of the design. The function captures the dynamic interplay between layers, allowing for varying spatial relationships, openness, and privacy. Ultimately, the resulting model embodies structural complexity and a rich architectural experience aligned with the design task's requirements."""

#! python 3
function_code = """def create_interlocking_layers_model(base_size, num_layers, layer_height, angle_variation, seed):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function generates a dynamic model of interconnected volumes and planes that interlock,
    embodying the idea of layers shifting and overlapping to create complex spatial relationships.

    Parameters:
    - base_size (tuple): A tuple (width, depth) specifying the size of the base footprint in meters.
    - num_layers (int): The number of interlocking layers to create.
    - layer_height (float): The height of each layer in meters.
    - angle_variation (float): The maximum angle variation for layer rotation in degrees.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the interlocking layers of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for consistent results
    random.seed(seed)

    # Unpack base dimensions
    width, depth = base_size

    # Initialize a list to store the created layers
    layers = []

    # Iterate to create each layer
    for i in range(num_layers):
        # Create a base rectangle for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = i * layer_height
        rect_corners = [
            rg.Point3d(-width / 2, -depth / 2, 0),
            rg.Point3d(width / 2, -depth / 2, 0),
            rg.Point3d(width / 2, depth / 2, 0),
            rg.Point3d(-width / 2, depth / 2, 0),
            rg.Point3d(-width / 2, -depth / 2, 0)  # Closing the polyline
        ]
        rectangle = rg.Polyline(rect_corners)

        # Create a surface from the rectangle
        surface = rg.Brep.CreateFromCornerPoints(
            rect_corners[0], rect_corners[1], rect_corners[2], rect_corners[3], 0.01)

        # Extrude the surface to create volume
        extrusion_vec = rg.Vector3d(0, 0, layer_height)
        extrusion_path = rg.Line(rect_corners[0], rect_corners[0] + extrusion_vec).ToNurbsCurve()
        layer_brep = surface.Faces[0].CreateExtrusion(extrusion_path, True)

        # Apply rotation to simulate interlocking
        angle = random.uniform(-angle_variation, angle_variation)
        rotation = rg.Transform.Rotation(math.radians(angle), base_plane.ZAxis, base_plane.Origin)
        layer_brep.Transform(rotation)

        # Apply a translation in Z to position the layer correctly
        translation = rg.Transform.Translation(0, 0, i * layer_height)
        layer_brep.Transform(translation)

        # Add the layer to the list
        layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model((10, 5), 5, 2, 15, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((8, 4), 3, 1.5, 10, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((12, 6), 4, 3, 20, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((15, 10), 6, 2.5, 25, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((20, 10), 7, 1, 30, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
