# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern. It constructs layered volumes that incorporate both angular and organic forms, simulating the rugged yet fluid characteristics of natural caves. By creating a series of interlocking spheres and boxes, the model emphasizes spatial transitions through narrow passages leading into expansive chambers. Strategic openings enhance the interplay of light and shadow, mimicking the natural lighting found in caverns. This design approach captures a sense of exploration and surprise, evoking an immersive experience reflective of a subterranean environment, aligning with the metaphor's essence."""

#! python 3
function_code = """def create_subterranean_cavern_model_with_layers(base_length, base_width, height, num_layers, seed=42):
    \"""
    Generates a conceptual architectural model inspired by the metaphor of a subterranean cavern with layered spaces.

    This function creates a complex structure composed of a series of layered volumes, 
    integrating angular and organic forms. The model emphasizes spatial transitions through 
    narrow passages leading into larger volumes, with an interplay of light and shadow.

    Parameters:
    - base_length (float): The base length of the model in meters.
    - base_width (float): The base width of the model in meters.
    - height (float): The height of each layer in meters.
    - num_layers (int): Number of vertical layers to stack.
    - seed (int): Random seed for reproducibility of the design.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    cavern_model = []

    # Define base plane and starting point
    base_plane = rg.Plane.WorldXY

    # Parameters for organic and angular forms
    max_offset = min(base_length, base_width) / 4
    max_radius = min(base_length, base_width) / 8

    # Create layers
    for layer in range(num_layers):
        # Determine the offset for the layer
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        offset_z = layer * height

        # Create organic and angular forms for each layer
        for _ in range(2):
            if random.choice([True, False]):
                # Organic form: Sphere
                center = rg.Point3d(
                    random.uniform(offset_x, offset_x + base_length),
                    random.uniform(offset_y, offset_y + base_width),
                    offset_z + random.uniform(0, height)
                )
                sphere = rg.Sphere(center, random.uniform(max_radius / 2, max_radius))
                cavern_model.append(sphere.ToBrep())
            else:
                # Angular form: Box
                box = rg.Box(
                    rg.Plane(rg.Point3d(offset_x, offset_y, offset_z), rg.Vector3d.ZAxis),
                    rg.Interval(0, random.uniform(max_radius, base_length / 2)),
                    rg.Interval(0, random.uniform(max_radius, base_width / 2)),
                    rg.Interval(0, height)
                )
                cavern_model.append(box.ToBrep())

        # Create strategic openings
        for brep in cavern_model[:]:
            if isinstance(brep, rg.Brep):
                void = rg.Box(base_plane, rg.Interval(-1, 1), rg.Interval(-1, 1), rg.Interval(-1, 1)).ToBrep()
                boolean_difference = rg.Brep.CreateBooleanDifference([brep], [void], 0.001)
                if boolean_difference:  # Check if the operation was successful
                    cavern_model.append(boolean_difference[0])

    return cavern_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model_with_layers(10.0, 8.0, 3.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model_with_layers(15.0, 10.0, 4.0, 7, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model_with_layers(12.0, 9.0, 2.5, 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model_with_layers(20.0, 15.0, 5.0, 4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model_with_layers(18.0, 12.0, 3.5, 8, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
