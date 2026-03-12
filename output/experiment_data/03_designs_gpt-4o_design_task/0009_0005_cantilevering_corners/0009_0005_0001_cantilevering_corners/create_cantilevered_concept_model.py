# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model that embodies the metaphor of "Cantilevering corners." It begins by creating a central core, serving as the structure's anchor, and extends multiple cantilevered sections outward, symbolizing motion and tension. Through randomization, the function varies the angles and lengths of these cantilevers, enhancing the dynamic interplay between stability and movement. The design highlights contrasts between solid and void by incorporating negative spaces and experimenting with materials to emphasize light and shadow, ultimately resulting in engaging spaces that invite exploration and interaction, reflecting the metaphor's essence of defying traditional architectural expectations."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_height=6, core_width=4, core_length=4, num_cantilevers=3, cantilever_length_range=(3, 6), cantilever_height=2, seed=42):
    \"""
    Generates a conceptual architectural model embodying 'Cantilevering corners'.
    
    The model features a central core with cantilevered sections extending outward,
    creating a dynamic interplay between stability and motion. The design emphasizes
    the contrast between solid and void, and highlights the interaction of light and shadow.

    Parameters:
    - core_height (float): The height of the central core.
    - core_width (float): The width of the central core.
    - core_length (float): The length of the central core.
    - num_cantilevers (int): The number of cantilevered sections.
    - cantilever_length_range (tuple): The range of lengths for the cantilevers.
    - cantilever_height (float): The height of the cantilevered sections.
    - seed (int): The seed for random number generation, ensuring reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Create the central core as a box
    core_origin = rg.Point3d(0, 0, 0)
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_length), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]
    
    # Define cantilevered sections
    for i in range(num_cantilevers):
        # Randomly select an axis and direction for cantilever
        axis = random.choice(['X', 'Y'])
        direction = random.choice([-1, 1])
        
        # Determine the cantilever's origin
        if axis == 'X':
            cantilever_origin = rg.Point3d(direction * core_width / 2, random.uniform(-core_length / 2, core_length / 2), random.uniform(0, core_height))
            cantilever_plane = rg.Plane(cantilever_origin, rg.Vector3d(1 if direction > 0 else -1, 0, 0))
        else:
            cantilever_origin = rg.Point3d(random.uniform(-core_width / 2, core_width / 2), direction * core_length / 2, random.uniform(0, core_height))
            cantilever_plane = rg.Plane(cantilever_origin, rg.Vector3d(0, 1 if direction > 0 else -1, 0))
        
        # Define cantilever dimensions
        cantilever_length = random.uniform(*cantilever_length_range)
        cantilever_width = core_width / 2
        
        # Create cantilever box
        if axis == 'X':
            cantilever_box = rg.Box(cantilever_plane, rg.Interval(0, direction * cantilever_length), rg.Interval(-cantilever_width / 2, cantilever_width / 2), rg.Interval(0, cantilever_height))
        else:
            cantilever_box = rg.Box(cantilever_plane, rg.Interval(-cantilever_width / 2, cantilever_width / 2), rg.Interval(0, direction * cantilever_length), rg.Interval(0, cantilever_height))
        
        geometries.append(cantilever_box.ToBrep())
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_height=8, core_width=5, core_length=5, num_cantilevers=4, cantilever_length_range=(4, 7), cantilever_height=3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_height=10, core_width=6, core_length=8, num_cantilevers=2, cantilever_length_range=(2, 5), cantilever_height=4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_height=7, core_width=3, core_length=6, num_cantilevers=5, cantilever_length_range=(2, 8), cantilever_height=1, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_height=9, core_width=7, core_length=3, num_cantilevers=6, cantilever_length_range=(1, 4), cantilever_height=2.5, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_height=5, core_width=4, core_length=7, num_cantilevers=3, cantilever_length_range=(3, 8), cantilever_height=2, seed=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
