# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a "subterranean cavern." By defining parameters such as radius, height variation, and the number of voids, it constructs a main cavern and intimate spaces that evoke exploration and mystery. The use of organic forms and varied ceiling heights creates an enveloping environment, while randomly placed voids enhance the sense of refuge and shelter. The geometries produced, represented as 3D models, encapsulate the key traits of the metaphor, allowing for an immersive and atmospheric architectural design."""

#! python 3
function_code = """def create_subterranean_cavern_model(cavern_radius=10, height_variation=5, num_voids=3):
    \"""
    Creates a conceptual architectural model based on the metaphor of a subterranean cavern.

    The design aims to evoke exploration, mystery, and refuge, using organic forms and varied lighting conditions. 
    The model consists of a main cavern volume with smaller voids that represent intimate, sheltered spaces.

    Parameters:
        cavern_radius (float): The average radius of the main cavern space in meters.
        height_variation (float): Maximum variation in height of the cavern ceiling and floor in meters.
        num_voids (int): Number of smaller voids within the cavern.

    Returns:
        List[Rhino.Geometry.Brep]: A list of 3D geometries representing the cavern and voids.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Vector3d, Brep, NurbsSurface
    
    # Set a seed for randomness to ensure replicability
    random.seed(42)
    
    # Create the main cavern volume
    base_point = Point3d(0, 0, 0)
    ceiling_points = []
    floor_points = []
    
    # Generate points for ceiling and floor
    for i in range(-cavern_radius, cavern_radius + 1, 2):
        for j in range(-cavern_radius, cavern_radius + 1, 2):
            # Calculate distance from center to create an organic shape
            dist = (i**2 + j**2) ** 0.5
            
            # Calculate height variation based on distance
            height_offset = (1 - dist / cavern_radius) * height_variation
            
            # Create ceiling and floor points
            ceiling_points.append(Point3d(i, j, cavern_radius + height_offset))
            floor_points.append(Point3d(i, j, -cavern_radius - height_offset))
    
    # Calculate the number of points in U and V directions
    u_count = (2 * cavern_radius) // 2 + 1
    v_count = (2 * cavern_radius) // 2 + 1
    
    # Create surfaces for ceiling and floor
    ceiling_surface = NurbsSurface.CreateFromPoints(ceiling_points, u_count, v_count, 3, 3)
    floor_surface = NurbsSurface.CreateFromPoints(floor_points, u_count, v_count, 3, 3)
    
    # Create breps from surfaces
    ceiling_brep = Brep.CreateFromSurface(ceiling_surface)
    floor_brep = Brep.CreateFromSurface(floor_surface)
    
    # Create a list to store all geometries
    geometry_list = [ceiling_brep, floor_brep]
    
    # Create voids within the cavern
    for _ in range(num_voids):
        void_center = Point3d(
            random.uniform(-cavern_radius, cavern_radius),
            random.uniform(-cavern_radius, cavern_radius),
            random.uniform(-cavern_radius, cavern_radius)
        )
        void_radius = random.uniform(1, cavern_radius / 3)
        sphere = Rhino.Geometry.Sphere(void_center, void_radius)
        void_brep = sphere.ToBrep()
        geometry_list.append(void_brep)
    
    return geometry_list"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(cavern_radius=15, height_variation=10, num_voids=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(cavern_radius=12, height_variation=7, num_voids=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(cavern_radius=20, height_variation=8, num_voids=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(cavern_radius=8, height_variation=3, num_voids=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(cavern_radius=18, height_variation=6, num_voids=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
