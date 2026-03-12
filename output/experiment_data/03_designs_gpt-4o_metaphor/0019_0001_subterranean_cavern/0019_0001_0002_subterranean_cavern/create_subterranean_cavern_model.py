# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates an immersive space characterized by exploration and refuge by defining a bounding volume representing the cavern's structure. The function also introduces organic voids, which are randomly generated to mimic natural formations, enhancing the sense of mystery. These voids are twisted to add dynamism, reflecting the metaphor's intimate and enveloping qualities. The model employs varied dimensions for the cavern and voids, ensuring a unique and organic architectural representation that aligns with the metaphor's essence."""

#! python 3
function_code = """def create_subterranean_cavern_model(length, width, height, void_count, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of a subterranean cavern.
    
    The model focuses on generating an immersive and enveloping space that suggests exploration, mystery, and refuge.
    It incorporates organic forms and varied lighting conditions to evoke the feeling of a natural, secluded environment.

    Parameters:
    - length (float): The length of the bounding volume of the cavern in meters.
    - width (float): The width of the bounding volume of the cavern in meters.
    - height (float): The height of the bounding volume of the cavern in meters.
    - void_count (int): The number of voids to create within the cavern space.
    - seed (int): Random seed for replicable randomness.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create the bounding volume of the cavern
    cavern_base = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    cavern_brep = cavern_base.ToBrep()
    geometries.append(cavern_brep)

    # Generate organic voids within the cavern
    for _ in range(void_count):
        void_length = random.uniform(0.1 * length, 0.3 * length)
        void_width = random.uniform(0.1 * width, 0.3 * width)
        void_height = random.uniform(0.1 * height, 0.3 * height)

        void_x = random.uniform(0, length - void_length)
        void_y = random.uniform(0, width - void_width)
        void_z = random.uniform(0, height - void_height)

        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), 
                          rg.Interval(void_y, void_y + void_width), 
                          rg.Interval(void_z, void_z + void_height))
        void_brep = void_box.ToBrep()

        # Apply a twist to make the voids more organic
        twist_angle = random.uniform(-0.5, 0.5)
        line_curve = rg.LineCurve(rg.Point3d(void_x, void_y, void_z), rg.Point3d(void_x, void_y, void_z + void_height))
        twisted_void = rg.Brep.CreateFromSweep(
            line_curve,
            rg.Circle(rg.Point3d(void_x + void_length / 2, void_y + void_width / 2, void_z), void_width / 2).ToNurbsCurve(),
            False, 0.1)[0]
        
        twist_transform = rg.Transform.Rotation(twist_angle, rg.Vector3d(0, 0, 1), rg.Point3d(void_x, void_y, void_z))
        twisted_void.Transform(twist_transform)

        geometries.append(twisted_void)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(50.0, 30.0, 20.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(80.0, 60.0, 40.0, 10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(100.0, 50.0, 30.0, 8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(75.0, 45.0, 25.0, 6, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(30.0, 20.0, 15.0, 3, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
