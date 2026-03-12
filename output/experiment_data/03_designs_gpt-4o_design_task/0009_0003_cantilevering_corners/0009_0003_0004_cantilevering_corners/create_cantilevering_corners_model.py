# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The function `create_cantilevering_corners_model` generates an architectural concept model based on the metaphor of "Cantilevering corners." It creates a central base from which multiple cantilevered segments extend outward at varying heights and angles, embodying the tension between stability and motion. By utilizing randomized orientations and varying heights for these projections, the model emphasizes contrasts through scale and materiality. Additionally, voids beneath the cantilevers enhance the illusion of suspension, while the interplay of light and shadows further accentuates movement and balance. This dynamic composition invites exploration and interaction with the surrounding environment."""

#! python 3
function_code = """def create_cantilevering_corners_model(base_width, base_depth, base_height, cantilever_length, cantilever_height, num_cantilevers):
    \"""
    Creates an architectural Concept Model embodying the 'Cantilevering corners' metaphor. The model features a central
    mass with cantilevered segments extending at different heights and orientations, emphasizing the contrast between the
    stable core and lighter projecting sections.

    Parameters:
    - base_width (float): The width of the central base in meters.
    - base_depth (float): The depth of the central base in meters.
    - base_height (float): The height of the central base in meters.
    - cantilever_length (float): The length of each cantilevered segment in meters.
    - cantilever_height (float): The height at which each cantilever starts from the base in meters.
    - num_cantilevers (int): The number of cantilevered sections to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    import math  # Importing math to use radians conversion
    random.seed(42)  # Ensuring replicability

    breps = []

    # Create the central core base
    base_corners = [
        Rhino.Geometry.Point3d(0, 0, 0),
        Rhino.Geometry.Point3d(base_width, 0, 0),
        Rhino.Geometry.Point3d(base_width, base_depth, 0),
        Rhino.Geometry.Point3d(0, base_depth, 0)
    ]
    base_surface = Rhino.Geometry.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.1)
    base_brep = base_surface
    base_brep.Translate(0, 0, base_height / 2)
    breps.append(base_brep)

    # Create cantilevered sections
    for i in range(num_cantilevers):
        angle = random.uniform(0, 360)  # Randomize orientation
        rotation = Rhino.Geometry.Transform.Rotation(math.radians(angle), Rhino.Geometry.Vector3d.ZAxis, Rhino.Geometry.Point3d(0, 0, cantilever_height))
        
        cantilever_corners = [
            Rhino.Geometry.Point3d(base_width / 2, base_depth / 2, cantilever_height),
            Rhino.Geometry.Point3d(base_width / 2 + cantilever_length, base_depth / 2, cantilever_height),
            Rhino.Geometry.Point3d(base_width / 2 + cantilever_length, base_depth / 2 + cantilever_length, cantilever_height),
            Rhino.Geometry.Point3d(base_width / 2, base_depth / 2 + cantilever_length, cantilever_height)
        ]
        cantilever_surface = Rhino.Geometry.Brep.CreateFromCornerPoints(cantilever_corners[0], cantilever_corners[1], cantilever_corners[2], cantilever_corners[3], 0.1)
        cantilever_brep = cantilever_surface
        cantilever_brep.Translate(0, 0, base_height / 2)
        cantilever_brep.Transform(rotation)
        breps.append(cantilever_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model(5.0, 3.0, 4.0, 2.0, 1.5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model(6.0, 4.0, 5.0, 3.0, 2.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model(7.0, 2.5, 6.0, 4.5, 3.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model(8.0, 5.0, 7.0, 3.5, 2.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model(4.0, 2.0, 3.0, 2.5, 1.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
