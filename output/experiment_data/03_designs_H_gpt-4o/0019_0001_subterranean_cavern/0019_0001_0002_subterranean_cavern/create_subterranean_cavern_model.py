# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern by creating a series of interconnected, organic shapes that reflect the metaphor's themes of exploration and refuge. It creates a base surface and multiple chambers with varied heights using ellipsoidal forms to evoke natural cavern characteristics. Randomized dimensions and placements promote an irregular, undulating landscape, while tunnels connect these chambers, enhancing spatial discovery. This approach, combined with the potential use of translucent materials or strategic openings for lighting, embodies the essence of a secluded, immersive environment that mirrors the mystery of a cavern."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_length=20.0, base_width=15.0, height_variation=4.0, chamber_count=6, seed=123):
    \"""
    Create an Architectural Concept Model inspired by the 'subterranean cavern' metaphor. The model
    features organic shapes, interconnected spaces, and varied spatial qualities to evoke a sense of
    exploration and mystery.

    Parameters:
    - base_length (float): The length of the model's base in meters, representing the horizontal extent.
    - base_width (float): The width of the model's base in meters.
    - height_variation (float): Maximum variation in vertical height to create an undulating ceiling.
    - chamber_count (int): Number of main chambers, each representing an occupiable volume.
    - seed (int): Random seed for consistent results across multiple executions.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create the base surface for the cavern
    base_plane = rg.Plane.WorldXY
    base_rect = rg.Rectangle3d(base_plane, base_length, base_width).ToNurbsCurve()
    base_surface = rg.Brep.CreatePlanarBreps(base_rect)[0]
    geometries.append(base_surface)

    # Generate chambers with varied heights
    for _ in range(chamber_count):
        # Randomly position each chamber within the base area
        center_x = random.uniform(0.1 * base_length, 0.9 * base_length)
        center_y = random.uniform(0.1 * base_width, 0.9 * base_width)
        center_z = random.uniform(0.0, height_variation)

        # Create an irregular ellipsoid shape for each chamber
        ellipsoid_center = rg.Point3d(center_x, center_y, center_z)
        radius_x = random.uniform(1.0, 3.0)
        radius_y = random.uniform(1.0, 3.0)
        radius_z = random.uniform(1.0, 3.0)

        ellipsoid = rg.Ellipse(rg.Plane(ellipsoid_center, rg.Vector3d.ZAxis), radius_x, radius_y).ToNurbsCurve()
        ellipsoid_surface = rg.Brep.CreateFromSurface(rg.RevSurface.Create(ellipsoid, rg.Line(ellipsoid_center, rg.Vector3d(0, 0, radius_z))))
        
        if ellipsoid_surface:
            geometries.append(ellipsoid_surface)

    # Create tunnels between chambers
    for i in range(chamber_count - 1):
        start = geometries[i].GetBoundingBox(True).Center
        end = geometries[i + 1].GetBoundingBox(True).Center

        # Create a tunnel using a cylinder between chambers
        tunnel_vector = end - start
        tunnel_length = tunnel_vector.Length
        tunnel_direction = tunnel_vector / tunnel_length

        tunnel_radius = random.uniform(0.3, 0.5)
        tunnel = rg.Cylinder(rg.Circle(rg.Plane(start, tunnel_direction), tunnel_radius), tunnel_length)
        tunnel_brep = tunnel.ToBrep(True, True)

        if tunnel_brep:
            geometries.append(tunnel_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_length=25.0, base_width=20.0, height_variation=5.0, chamber_count=8, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_length=30.0, base_width=10.0, height_variation=3.0, chamber_count=4, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_length=15.0, base_width=25.0, height_variation=6.0, chamber_count=5, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_length=18.0, base_width=18.0, height_variation=2.0, chamber_count=7, seed=999)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_length=22.0, base_width=12.0, height_variation=4.5, chamber_count=10, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
