# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The function `generate_cavernous_concept_model` creates an architectural concept model inspired by the metaphor of a subterranean cavern. It generates a labyrinthine structure with interlocking volumes, simulating the complexity of natural caves. The model incorporates both angular and organic forms, allowing for varied chamber shapes that evoke the rugged yet fluid nature of cavern spaces. Corridors connect these chambers, and strategic openings introduce light, enhancing the interplay of shadow and depth. The design prioritizes spatial transitions, fostering a sense of exploration and surprise, reflecting the immersive qualities inherent in subterranean environments."""

#! python 3
function_code = """def generate_cavernous_concept_model(max_length, max_width, max_height, num_chambers, corridor_thickness, seed=42):
    \"""
    Creates an architectural concept model based on the 'subterranean cavern' metaphor.

    This function generates a labyrinthine structure of interlocking volumes, simulating the complexity and mystery of natural caves.
    It combines angular and organic forms with strategic openings to create a dynamic interplay of light and shadow.

    Parameters:
    - max_length (float): The maximum length of the model in meters.
    - max_width (float): The maximum width of the model in meters.
    - max_height (float): The maximum height of the model in meters.
    - num_chambers (int): The number of larger chambers to create within the model.
    - corridor_thickness (float): The thickness of corridors connecting chambers in meters.
    - seed (int): Random seed for reproducibility of the design.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create chambers with varied sizes
    for _ in range(num_chambers):
        chamber_length = random.uniform(max_length * 0.2, max_length * 0.4)
        chamber_width = random.uniform(max_width * 0.2, max_width * 0.4)
        chamber_height = random.uniform(max_height * 0.5, max_height)

        # Determine if the chamber is angular or organic
        is_angular = random.choice([True, False])

        if is_angular:
            # Create angular chamber
            base_plane = rg.Plane.WorldXY
            chamber_box = rg.Box(base_plane, rg.Interval(0, chamber_length), rg.Interval(0, chamber_width), rg.Interval(0, chamber_height))
            chamber_brep = chamber_box.ToBrep()
        else:
            # Create organic chamber
            center = rg.Point3d(chamber_length / 2, chamber_width / 2, chamber_height / 2)
            sphere = rg.Sphere(center, min(chamber_length, chamber_width, chamber_height) / 2)
            chamber_brep = sphere.ToBrep()

        geometries.append(chamber_brep)

    # Create connecting corridors
    for i in range(num_chambers - 1):
        corridor_length = random.uniform(corridor_thickness * 2, corridor_thickness * 4)
        corridor_height = random.uniform(max_height * 0.3, max_height * 0.5)

        corridor_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, corridor_length), rg.Interval(0, corridor_thickness), rg.Interval(0, corridor_height))
        corridor_brep = corridor_box.ToBrep()

        # Randomly transform the corridor to connect chambers
        translation = rg.Transform.Translation(random.uniform(0, max_length - corridor_length), random.uniform(0, max_width - corridor_thickness), 0)
        corridor_brep.Transform(translation)
        
        geometries.append(corridor_brep)

    # Add openings for light
    for brep in geometries[:]:
        opening_size = random.uniform(corridor_thickness, corridor_thickness * 2)
        opening_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-opening_size/2, opening_size/2), rg.Interval(-opening_size/2, opening_size/2), rg.Interval(0, opening_size))
        opening_brep = opening_box.ToBrep()
        
        boolean_result = rg.Brep.CreateBooleanDifference([brep], [opening_brep], 0.001)
        if boolean_result:
            geometries.append(boolean_result[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cavernous_concept_model(50.0, 30.0, 20.0, 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cavernous_concept_model(100.0, 50.0, 30.0, 7, 1.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cavernous_concept_model(75.0, 45.0, 25.0, 4, 3.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cavernous_concept_model(60.0, 40.0, 15.0, 6, 2.5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cavernous_concept_model(80.0, 60.0, 35.0, 3, 4.0, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
