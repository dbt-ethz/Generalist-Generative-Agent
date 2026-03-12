# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a central mass with dynamically extending sections. It accepts parameters for base dimensions, cantilever specifications, and void ratios. The function constructs a stable core and incorporates cantilevers that project outward at varying heights and orientations, emphasizing the contrast between the solid base and lighter extensions. Voids are introduced beneath these cantilevers, enhancing the feeling of suspension and tension. The model explores spatial dynamics, engaging with light and shadows, thereby fostering a sense of movement and interaction with the environment."""

#! python 3
function_code = """def create_cantilevering_corners_model(base_dimensions, cantilever_specs, void_height_ratio):
    \"""
    Create an architectural Concept Model embodying the 'Cantilevering corners' metaphor. This function generates a 3D 
    model with a stable central mass and dynamically cantilevered sections, incorporating voids to enhance the sense 
    of suspension.

    Parameters:
    - base_dimensions (tuple): A tuple of three floats (width, depth, height) representing the central base dimensions.
    - cantilever_specs (list of tuples): Each tuple contains three elements:
        * length (float): The length of the cantilever.
        * height (float): The height from the base at which the cantilever starts.
        * orientation (float): The angle in degrees at which the cantilever is oriented from the base.
    - void_height_ratio (float): The ratio of the void height to the cantilever height to create voids beneath cantilevers.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model with cantilevered sections.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create central base
    base_width, base_depth, base_height = base_dimensions
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
    
    geometries = [base_box]

    for length, height, orientation in cantilever_specs:
        # Define cantilever corners in local space
        cantilever_corners = [
            rg.Point3d(base_width / 2, base_depth / 2, height),
            rg.Point3d(base_width / 2 + length, base_depth / 2, height),
            rg.Point3d(base_width / 2 + length, base_depth / 2 + length, height),
            rg.Point3d(base_width / 2, base_depth / 2 + length, height),
            rg.Point3d(base_width / 2, base_depth / 2, height + base_height),
            rg.Point3d(base_width / 2 + length, base_depth / 2, height + base_height),
            rg.Point3d(base_width / 2 + length, base_depth / 2 + length, height + base_height),
            rg.Point3d(base_width / 2, base_depth / 2 + length, height + base_height)
        ]
        cantilever_box = rg.Brep.CreateFromBox(cantilever_corners)

        # Rotate the cantilever
        rotation_center = rg.Point3d(base_width / 2, base_depth / 2, height)
        rotation_transform = rg.Transform.Rotation(math.radians(orientation), rg.Vector3d.ZAxis, rotation_center)
        cantilever_box.Transform(rotation_transform)
        
        geometries.append(cantilever_box)

        # Create void beneath cantilever
        void_height = height * void_height_ratio
        void_corners = [
            rg.Point3d(base_width / 2, base_depth / 2, height - void_height),
            rg.Point3d(base_width / 2 + length, base_depth / 2, height - void_height),
            rg.Point3d(base_width / 2 + length, base_depth / 2 + length, height - void_height),
            rg.Point3d(base_width / 2, base_depth / 2 + length, height - void_height),
            rg.Point3d(base_width / 2, base_depth / 2, height),
            rg.Point3d(base_width / 2 + length, base_depth / 2, height),
            rg.Point3d(base_width / 2 + length, base_depth / 2 + length, height),
            rg.Point3d(base_width / 2, base_depth / 2 + length, height)
        ]
        void_box = rg.Brep.CreateFromBox(void_corners)
        void_box.Transform(rotation_transform)
        
        geometries.append(void_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model((10.0, 5.0, 3.0), [(4.0, 2.0, 30.0), (3.0, 1.5, -15.0)], 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model((12.0, 6.0, 4.0), [(5.0, 3.0, 45.0), (2.5, 2.0, -30.0)], 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model((15.0, 7.0, 5.0), [(6.0, 4.0, 60.0), (3.5, 2.5, -25.0)], 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model((8.0, 4.0, 2.5), [(3.0, 1.0, 75.0), (2.0, 1.5, -45.0)], 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model((9.0, 4.5, 3.5), [(4.5, 2.5, 15.0), (2.5, 1.0, 0.0)], 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
