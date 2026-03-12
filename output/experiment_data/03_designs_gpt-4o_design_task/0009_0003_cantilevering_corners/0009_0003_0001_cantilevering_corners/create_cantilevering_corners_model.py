# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The function `create_cantilevering_corners_model` generates an architectural concept model that embodies the metaphor of "Cantilevering corners" by creating a stable central mass from which various sections extend outward. It utilizes parameters such as base dimensions and cantilever characteristics to define the structure. The function constructs the central base and adds cantilevered sections at varying heights and angles, enhancing visual dynamism and spatial tension. By incorporating voids beneath the cantilevers, the design emphasizes suspension and interaction with light, creating intriguing spaces that invite exploration while balancing stability and motion, in line with the provided design task."""

#! python 3
function_code = """def create_cantilevering_corners_model(base_width, base_depth, base_height, cantilever_length, cantilever_height, cantilever_rotation):
    \"""
    Create an architectural Concept Model embodying the 'Cantilevering corners' metaphor. This function generates a 3D model with a stable central mass and dynamically cantilevered sections.

    Parameters:
    - base_width (float): Width of the central base mass.
    - base_depth (float): Depth of the central base mass.
    - base_height (float): Height of the central base mass.
    - cantilever_length (float): The length of each cantilevered section.
    - cantilever_height (float): The height at which each cantilevered section is positioned above the base.
    - cantilever_rotation (float): The rotation angle in degrees applied to each cantilevered section.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model with cantilevered sections.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for reproducibility
    random.seed(42)

    # Create the central base mass
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_width, 0, 0),
        rg.Point3d(base_width, base_depth, 0),
        rg.Point3d(0, base_depth, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_width, 0, base_height),
        rg.Point3d(base_width, base_depth, base_height),
        rg.Point3d(0, base_depth, base_height)
    ]
    base_box = rg.Brep.CreateFromBox(base_corners)

    # Create cantilevered sections
    cantilevered_sections = []
    for i in range(4):
        offset_x = random.choice([0, base_width - cantilever_length])
        offset_y = random.choice([0, base_depth - cantilever_length])
        rotation_angle = cantilever_rotation * (i + 1)

        cantilever_corners = [
            rg.Point3d(offset_x, offset_y, cantilever_height),
            rg.Point3d(offset_x + cantilever_length, offset_y, cantilever_height),
            rg.Point3d(offset_x + cantilever_length, offset_y + cantilever_length, cantilever_height),
            rg.Point3d(offset_x, offset_y + cantilever_length, cantilever_height),
            rg.Point3d(offset_x, offset_y, cantilever_height + base_height),
            rg.Point3d(offset_x + cantilever_length, offset_y, cantilever_height + base_height),
            rg.Point3d(offset_x + cantilever_length, offset_y + cantilever_length, cantilever_height + base_height),
            rg.Point3d(offset_x, offset_y + cantilever_length, cantilever_height + base_height)
        ]
        cantilever_box = rg.Brep.CreateFromBox(cantilever_corners)

        # Rotate the cantilever around the center of the base
        rotation_center = rg.Point3d(base_width / 2, base_depth / 2, cantilever_height)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_center)
        cantilever_box.Transform(rotation_transform)

        cantilevered_sections.append(cantilever_box)

    # Compile all geometries
    all_geometries = [base_box] + cantilevered_sections

    return all_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model(10.0, 5.0, 3.0, 4.0, 2.0, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model(15.0, 7.0, 4.0, 5.0, 3.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model(12.0, 6.0, 5.0, 3.0, 2.5, 60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model(8.0, 4.0, 2.5, 2.0, 1.5, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model(20.0, 10.0, 6.0, 6.0, 4.0, 90.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
