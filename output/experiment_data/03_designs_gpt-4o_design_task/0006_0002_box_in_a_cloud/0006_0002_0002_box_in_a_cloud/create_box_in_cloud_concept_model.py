# Created for 0006_0002_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_concept_model`, generates an architectural concept model that visually represents the metaphor of "Box in a cloud." It creates a solid geometric "box" using specified dimensions to symbolize stability and permanence. This box is then enveloped by a dynamic, cloud-like form, generated from a sphere that simulates lightness through a mesh, incorporating random vertex offsets to enhance its ethereal quality. The model emphasizes the contrast between the defined edges of the box and the soft contours of the cloud, illustrating the interplay of solidity and ambiguity, and inviting exploration of spatial transitions."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(box_length=10, box_width=10, box_height=10, cloud_radius=15, cloud_resolution=20):
    \"""
    Creates a 'Box in a Cloud' architectural concept model using RhinoCommon. The model consists of a central box 
    representing stability and structure, enveloped by a cloud-like form suggesting lightness and ethereality.

    Inputs:
    - box_length: The length of the box (in meters).
    - box_width: The width of the box (in meters).
    - box_height: The height of the box (in meters).
    - cloud_radius: The radius of the spherical 'cloud' (in meters).
    - cloud_resolution: The number of divisions for constructing the cloud's surface.

    Outputs:
    - A list of RhinoCommon Breps representing the box and the cloud geometry.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set a seed for randomness
    random.seed(42)
    
    # Create the central 'box'
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_length, 0, 0),
        rg.Point3d(box_length, box_width, 0),
        rg.Point3d(0, box_width, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_length, 0, box_height),
        rg.Point3d(box_length, box_width, box_height),
        rg.Point3d(0, box_width, box_height)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)
    
    # Create the 'cloud' using a sphere base
    cloud_center = rg.Point3d(box_length / 2, box_width / 2, box_height / 2)
    cloud_sphere = rg.Sphere(cloud_center, cloud_radius)
    
    # Convert the sphere to a mesh with desired resolution
    cloud_mesh = rg.Mesh.CreateFromSphere(cloud_sphere, cloud_resolution, cloud_resolution)
    
    # Add some randomness to vertices to simulate the 'cloud' effect
    for i in range(cloud_mesh.Vertices.Count):
        vertex = cloud_mesh.Vertices[i]
        new_x = vertex.X + random.uniform(-1, 1) * 0.5  # Small random offset
        new_y = vertex.Y + random.uniform(-1, 1) * 0.5
        new_z = vertex.Z + random.uniform(-1, 1) * 0.5
        cloud_mesh.Vertices.SetVertex(i, new_x, new_y, new_z)
    
    # Convert the mesh to a Brep for consistency in output
    cloud_brep = rg.Brep.CreateFromMesh(cloud_mesh, True)
    
    return [box_brep, cloud_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model(box_length=15, box_width=10, box_height=8, cloud_radius=20, cloud_resolution=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model(box_length=12, box_width=12, box_height=6, cloud_radius=18, cloud_resolution=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model(box_length=8, box_width=5, box_height=10, cloud_radius=12, cloud_resolution=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model(box_length=20, box_width=15, box_height=10, cloud_radius=25, cloud_resolution=35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model(box_length=5, box_width=5, box_height=5, cloud_radius=10, cloud_resolution=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
