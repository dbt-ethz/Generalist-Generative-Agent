# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The function `create_cavernous_concept_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of interlocking volumes, combining angular and organic forms to reflect the rugged and fluid nature of cave systems. By varying heights and utilizing both solid and perforated materials, the model emphasizes the exploration and mystery associated with caves. Strategic corridors connect these volumes, facilitating a dynamic interplay of light and shadow that simulates natural cave lighting. Ultimately, the function captures the immersive quality of subterranean environments, promoting a sense of surprise and discovery within the design."""

#! python 3
function_code = """def create_cavernous_concept_model(base_length, base_width, height_variation, corridor_width, seed=42):
    \"""
    Generates a conceptual architectural model inspired by the metaphor of a subterranean cavern.

    This function creates a dynamic interplay of angular and organic forms to simulate the immersive experience of a cavern.
    By arranging interlocking volumes and strategic voids, the model emphasizes exploration and mystery through varied 
    spatial transitions, light, and shadow.

    Parameters:
    - base_length (float): The base length of the model in meters.
    - base_width (float): The base width of the model in meters.
    - height_variation (float): The maximum variation in height for the volumes in meters.
    - corridor_width (float): The width of the connecting corridors in meters.
    - seed (int): Random seed for reproducibility of the design.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    model_geometries = []

    # Create the base plane
    base_plane = rg.Plane.WorldXY

    # Generate interlocking volumes
    num_volumes = random.randint(4, 8)
    for _ in range(num_volumes):
        length = base_length * random.uniform(0.2, 0.5)
        width = base_width * random.uniform(0.2, 0.5)
        height = height_variation * random.uniform(0.5, 1.0)
        
        # Decide on angular or organic form
        is_angular = random.choice([True, False])

        if is_angular:
            # Create a faceted angular box
            box = rg.Box(base_plane, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
            brep = box.ToBrep()
        else:
            # Create a smooth organic blob
            center = rg.Point3d(length / 2, width / 2, height / 2)
            radius = min(length, width, height) / 2
            sphere = rg.Sphere(center, radius)
            brep = sphere.ToBrep()
        
        model_geometries.append(brep)

        # Offset the base plane for the next volume
        offset_x = random.uniform(corridor_width, base_length - length)
        offset_y = random.uniform(corridor_width, base_width - width)
        base_plane.Origin = rg.Point3d(base_plane.Origin.X + offset_x, base_plane.Origin.Y + offset_y, 0)

    # Generate corridors
    for _ in range(num_volumes - 1):
        corridor_length = corridor_width * random.uniform(1.0, 2.0)
        corridor_height = height_variation * random.uniform(0.3, 0.6)
        corridor_box = rg.Box(base_plane, rg.Interval(0, corridor_length), rg.Interval(0, corridor_width), rg.Interval(0, corridor_height))
        corridor_brep = corridor_box.ToBrep()
        model_geometries.append(corridor_brep)

    return model_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cavernous_concept_model(10.0, 5.0, 3.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cavernous_concept_model(15.0, 7.5, 4.0, 2.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cavernous_concept_model(12.0, 6.0, 2.5, 1.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cavernous_concept_model(8.0, 4.0, 2.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cavernous_concept_model(20.0, 10.0, 5.0, 3.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
