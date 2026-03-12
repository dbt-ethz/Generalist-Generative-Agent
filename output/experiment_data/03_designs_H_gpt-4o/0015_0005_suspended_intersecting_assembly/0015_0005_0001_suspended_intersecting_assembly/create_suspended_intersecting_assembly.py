# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model reflecting the metaphor of "Suspended intersecting assembly" by creating a network of intersecting cables and mesh surfaces. The function randomly positions these elements in three-dimensional space, simulating suspension and fluidity. Cables are represented as lines while mesh surfaces are created as spheres intersecting with the cables, forming an intricate web that embodies lightness and transparency. Parameters such as the number of cables, mesh size, and height variation contribute to the models dynamic quality, ultimately encouraging interactive pathways and visual connections that enhance spatial relationships and the model's overall sense of movement."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_cables=7, num_meshes=4, cable_length=15.0, mesh_radius=2.0, height_variation=5.0, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly'.

    This function generates a series of intersecting cable-like elements and mesh surfaces that suggest suspension and
    fluidity. The cables are represented as lines, and the meshes are spheres that intersect with the cables to
    create an intricate web of connections.

    Parameters:
    - num_cables (int): The number of intersecting cables to create.
    - num_meshes (int): The number of mesh surfaces to create.
    - cable_length (float): The length of each cable (in meters).
    - mesh_radius (float): The radius of each spherical mesh (in meters).
    - height_variation (float): Maximum vertical displacement for the elements to create variation in height.
    - seed (int): The seed for random number generation to ensure replicable results.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Breps representing the cables and mesh surfaces.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # List to store the resulting geometries
    geometries = []

    # Generate cables
    for _ in range(num_cables):
        start_pt = rg.Point3d(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0, height_variation))
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        direction.Unitize()
        end_pt = start_pt + direction * cable_length
        cable = rg.LineCurve(start_pt, end_pt)
        geometries.append(cable)

    # Generate meshes
    for _ in range(num_meshes):
        center_pt = rg.Point3d(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0, height_variation))
        mesh = rg.Mesh.CreateFromSphere(rg.Sphere(center_pt, mesh_radius), 10, 10)
        geometries.append(mesh)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_cables=10, num_meshes=5, cable_length=20.0, mesh_radius=3.0, height_variation=10.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_cables=8, num_meshes=6, cable_length=12.0, mesh_radius=2.5, height_variation=7.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_cables=6, num_meshes=3, cable_length=10.0, mesh_radius=1.5, height_variation=4.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_cables=5, num_meshes=2, cable_length=18.0, mesh_radius=4.0, height_variation=8.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_cables=12, num_meshes=8, cable_length=25.0, mesh_radius=2.0, height_variation=6.0, seed=84)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
