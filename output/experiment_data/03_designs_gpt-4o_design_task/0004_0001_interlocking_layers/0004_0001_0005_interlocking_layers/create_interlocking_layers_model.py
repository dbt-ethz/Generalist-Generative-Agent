# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the metaphor of "Interlocking Layers." It constructs a series of interconnected planes or volumes, each representing a layer that overlaps and shifts in orientation. By varying dimensions, thickness, and rotation angles, the function captures the dynamic interplay between openness and enclosure, reflecting the metaphor's essence. The use of color differentiation enhances the visual complexity of the structure, while ensuring distinct yet connected spaces. Overall, the model embodies structural and spatial intricacy, aligning with the design task's requirements for a rich architectural experience."""

#! python 3
function_code = """def create_interlocking_layers_model(base_width, base_depth, height, num_layers, layer_thickness, color_variation_seed):
    \"""
    Creates an architectural Concept Model embodying the 'Interlocking Layers' metaphor.
    
    This function generates a series of interconnected planes or volumes that are interlocked,
    demonstrating the dynamic and visually complex nature of the design task. The model is
    characterized by overlapping layers with varied orientations and angles to create both
    open and closed spaces, capturing the essence of structural complexity and spatial variety.

    Parameters:
    - base_width (float): The width of the base plane of the model in meters.
    - base_depth (float): The depth of the base plane of the model in meters.
    - height (float): The height of the entire model in meters.
    - num_layers (int): The number of interlocking layers to create.
    - layer_thickness (float): The thickness of each interlocking layer in meters.
    - color_variation_seed (int): A seed value for random color variation to differentiate layers.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import System.Drawing as sd
    import random
    import math  # Import the math module to use the radians conversion

    random.seed(color_variation_seed)

    geometries = []
    layer_height = height / num_layers

    for i in range(num_layers):
        # Define the base rectangle for each layer
        width_variation = random.uniform(0.8, 1.2)
        depth_variation = random.uniform(0.8, 1.2)
        
        layer_width = base_width * width_variation
        layer_depth = base_depth * depth_variation

        # Create the base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_rect = rg.Rectangle3d(base_plane, rg.Interval(-layer_width / 2, layer_width / 2), rg.Interval(-layer_depth / 2, layer_depth / 2))
        
        # Extrude the rectangle to create a solid layer
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        extrude_curve = base_rect.ToNurbsCurve()
        extrusion = rg.Extrusion.Create(extrude_curve, layer_thickness, True)
        layer_brep = extrusion.ToBrep()

        # Rotate the layer to create interlocking effect
        rotation_angle = random.uniform(-30, 30)
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation_center = rg.Point3d(0, 0, i * layer_height)
        transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, rotation_center)
        layer_brep.Transform(transform)
        
        # Translate the layer to its position in the stack
        translation_vector = rg.Vector3d(0, 0, i * layer_height)
        move_transform = rg.Transform.Translation(translation_vector)
        layer_brep.Transform(move_transform)
        
        # Assign a random color for differentiation (handled outside of geometry)
        color = sd.Color.FromArgb(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        # Typically, colors are applied in the visualization layer, not directly in geometry

        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 8, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 20.0, 10, 0.4, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 12.0, 6, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(15.0, 7.0, 25.0, 5, 0.6, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(9.0, 4.5, 18.0, 7, 0.4, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
