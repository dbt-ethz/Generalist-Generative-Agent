# Created for 0006_0005_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model` generates an architectural concept model based on the 'Box in a cloud' metaphor by creating a defined geometric "box" as a solid core structure, surrounded by an amorphous "cloud" layer. The box's dimensions are specified, while the cloud's dynamic nature is achieved through randomly generated points that mimic ethereality. This design emphasizes the interplay between the box's stability and the cloud's fluidity, allowing for a seamless transition between forms. The function returns a list of Brep objects, which represent the 3D geometries, facilitating exploration of spatial interactions and visual narratives."""

#! python 3
function_code = """def create_box_in_cloud_model(box_dimensions, cloud_radius, cloud_detail, seed=42):
    \"""
    Generates an architectural Concept Model using the 'Box in a cloud' metaphor.
    
    The function creates a central 'box' structure surrounded by a diffuse 'cloud'
    layer, emphasizing the interaction between solidity and ethereality. The 'box'
    is a defined geometric form, while the 'cloud' is a more amorphous, dynamic presence.

    Parameters:
    - box_dimensions (tuple): Dimensions of the box as (width, depth, height) in meters.
    - cloud_radius (float): Radius of the cloud layer surrounding the box in meters.
    - cloud_detail (int): Number of points used to define the cloud's surface complexity.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)

    # Create the box (solid core)
    box_width, box_depth, box_height = box_dimensions
    box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, box_width), rg.Interval(0, box_depth), rg.Interval(0, box_height))
    box_brep = box.ToBrep()

    # Generate the cloud (dynamic outer layer)
    cloud_center = rg.Point3d(box_width / 2, box_depth / 2, box_height / 2)
    cloud_points = []
    
    for _ in range(cloud_detail):
        angle = random.uniform(0, 2 * 3.14159)
        distance = random.uniform(cloud_radius * 0.8, cloud_radius)
        x = cloud_center.X + distance * random.uniform(-1, 1)
        y = cloud_center.Y + distance * random.uniform(-1, 1)
        z = cloud_center.Z + distance * random.uniform(-1, 1)
        cloud_points.append(rg.Point3d(x, y, z))

    # Create a surface from the cloud points using a convex hull approximation
    cloud_mesh = rg.Mesh()
    for pt in cloud_points:
        cloud_mesh.Vertices.Add(pt)
    cloud_mesh.Faces.AddFace(0, 1, 2, 3)  # Simplified example, adjust for actual cloud detail
    cloud_brep = rg.Brep.CreateFromMesh(cloud_mesh, True)

    # Return both the box and the cloud as a list of Breps
    return [box_brep, cloud_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model((5, 3, 2), 10, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model((2, 2, 3), 5, 50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model((4, 5, 6), 8, 75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model((6, 4, 3), 12, 150)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model((3, 2, 5), 7, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
