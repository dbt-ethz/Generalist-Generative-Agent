# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern by creating a labyrinthine structure composed of interlocking volumes. It employs a combination of angular and organic forms to reflect the rugged and fluid characteristics of natural caves. The function defines parameters for volume dimensions and corridor widths, generating random shapes and arranging them to form narrow passages that lead to larger chambers. By varying the heights and strategically placing voids, the model simulates the interplay of light and shadow, enhancing the immersive experience, exploration, and surprise central to the cavern metaphor."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_length, base_width, height_variation, corridor_width, seed=42):
    \"""
    Generates a conceptual architectural model inspired by the metaphor of a subterranean cavern.
    
    This function creates a labyrinth-like structure composed of interlocking volumes with a mix of angular and organic forms.
    The model incorporates narrow corridors leading to expansive chambers, with varied light and shadow interplay.
    
    Parameters:
    - base_length (float): The base length of the model in meters.
    - base_width (float): The base width of the model in meters.
    - height_variation (float): The maximum variation in height for the volumes in meters.
    - corridor_width (float): The width of the connecting corridors in meters.
    - seed (int): Random seed for reproducibility of the design.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino
    import System
    import random
    from Rhino.Geometry import Point3d, Brep, Box, Plane, Interval

    random.seed(seed)
    cavern_model = []

    # Define the base plane
    base_plane = Plane.WorldXY

    # Create a series of interlocking volumes
    num_volumes = random.randint(3, 6)
    for i in range(num_volumes):
        length = base_length * random.uniform(0.3, 0.6)
        width = base_width * random.uniform(0.3, 0.6)
        height = height_variation * random.uniform(0.5, 1.0)
        
        # Create angular and organic forms
        is_angular = random.choice([True, False])
        
        if is_angular:
            box = Box(base_plane, Interval(0, length), Interval(0, width), Interval(0, height))
            brep = box.ToBrep()
        else:
            center = Point3d(length / 2, width / 2, height / 2)
            sphere = Rhino.Geometry.Sphere(center, min(length, width, height) / 2)
            brep = sphere.ToBrep()
        
        cavern_model.append(brep)
        
        # Move the base plane for the next volume
        offset_x = random.uniform(corridor_width, base_length - length)
        offset_y = random.uniform(corridor_width, base_width - width)
        base_plane.Origin = Point3d(base_plane.Origin.X + offset_x, base_plane.Origin.Y + offset_y, 0)

    # Create corridors (voids) between volumes
    for i in range(num_volumes - 1):
        corridor_length = corridor_width * random.uniform(1.0, 1.5)
        corridor_height = height_variation * random.uniform(0.3, 0.6)
        corridor_box = Box(base_plane, Interval(0, corridor_length), Interval(0, corridor_width), Interval(0, corridor_height))
        corridor_brep = corridor_box.ToBrep()
        cavern_model.append(corridor_brep)

    return cavern_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 5.0, 8.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 10.0, 12.0, 3.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(8.0, 4.0, 6.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(20.0, 15.0, 10.0, 4.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(12.0, 6.0, 9.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
