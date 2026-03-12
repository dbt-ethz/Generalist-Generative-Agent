# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor of a "Suspended intersecting assembly." It utilizes random parameters to create multiple intersecting planes that simulate floating structures and dynamic intersections, embodying a sense of lightness and fluidity. By employing a series of rectangular surfaces defined by random start and end points, the model captures the intricate spatial network suggested by the metaphor. The planes' arrangement emphasizes transparency and the interplay of negative spaces, reflecting the delicate balance and gravity-defying nature of the architectural concept, while allowing for multiple viewpoints and pathways."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length=25, base_width=15, height=20, num_planes=6, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Suspended intersecting assembly' metaphor.
    
    This function generates a model using a series of intersecting planes that simulate the suspended
    and floating nature of architectural elements. The planes are arranged in a dynamic and crisscrossing
    manner to emphasize lightness and fluidity, incorporating reflective surfaces to enhance perception.
    
    Parameters:
    - base_length (float): Length of the base area in meters.
    - base_width (float): Width of the base area in meters.
    - height (float): Maximum height of the assembly in meters.
    - num_planes (int): Number of intersecting planes to generate.
    - seed (int): Seed for random number generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    geometries = []
    
    # Create a base plane
    base_plane = rg.Plane.WorldXY
    
    # Generate intersecting planes
    for _ in range(num_planes):
        # Random start and end points for each plane's defining line
        start_x = random.uniform(0, base_length)
        start_y = random.uniform(0, base_width)
        start_z = random.uniform(height * 0.2, height)
        
        end_x = random.uniform(0, base_length)
        end_y = random.uniform(0, base_width)
        end_z = random.uniform(height * 0.2, height)
        
        # Create line to define plane
        line = rg.Line(rg.Point3d(start_x, start_y, start_z), rg.Point3d(end_x, end_y, end_z))
        
        # Create a plane perpendicular to the line
        plane_origin = line.PointAt(0.5)
        plane_normal = rg.Vector3d.CrossProduct(line.Direction, rg.Vector3d.ZAxis)
        intersect_plane = rg.Plane(plane_origin, plane_normal)
        
        # Create a rectangular surface on the plane
        plane_width = random.uniform(base_width * 0.2, base_width * 0.5)
        plane_length = line.Length
        rect_corners = [
            intersect_plane.PointAt(-plane_length / 2, -plane_width / 2),
            intersect_plane.PointAt(plane_length / 2, -plane_width / 2),
            intersect_plane.PointAt(plane_length / 2, plane_width / 2),
            intersect_plane.PointAt(-plane_length / 2, plane_width / 2),
        ]
        
        surface = rg.Brep.CreateFromCornerPoints(rect_corners[0], rect_corners[1], rect_corners[2], rect_corners[3], 0.01)
        if surface:
            geometries.append(surface)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_length=30, base_width=20, height=25, num_planes=8, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_length=40, base_width=30, height=15, num_planes=10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_length=35, base_width=25, height=18, num_planes=5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_length=28, base_width=18, height=22, num_planes=7, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_length=50, base_width=35, height=30, num_planes=12, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
