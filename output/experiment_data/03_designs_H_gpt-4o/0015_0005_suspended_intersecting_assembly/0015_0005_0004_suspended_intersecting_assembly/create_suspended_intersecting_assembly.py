# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model that embodies the metaphor of "Suspended intersecting assembly." It creates a series of tensioned wires and translucent fabric-like surfaces that represent floating elements, emphasizing lightness and fluidity. By arranging these components at various angles, the function fosters dynamic intersections, promoting visual connections and a sense of movement. The use of randomization in wire placement and fabric orientation ensures variability, while the emphasis on transparency highlights interconnectivity. Ultimately, the model reflects the metaphor's themes of balance, suspension, and spatial dialogue, creating a visually engaging architectural representation."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_wires=8, wire_length=12.0, num_fabrics=4, fabric_size=6.0, seed=24):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly’.
    
    This function generates a series of intersecting tensioned wires and lightweight, translucent planar 
    surfaces to represent floating elements. The geometry emphasizes a light, airy quality with a focus 
    on transparency and fluidity. It returns a list of 3D geometries representing the suspended assembly, 
    promoting dynamic intersections and visual connections.

    Parameters:
    - num_wires (int): Number of tensioned wires to generate.
    - wire_length (float): Length of each tensioned wire in meters.
    - num_fabrics (int): Number of fabric-like planar surfaces to generate.
    - fabric_size (float): Approximate size of each fabric plane in meters.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.GeometryBase]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Helper function to create a random unit vector
    def random_unit_vector():
        vec = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        vec.Unitize()
        return vec

    # Generate tensioned wires
    wires = []
    for _ in range(num_wires):
        start_point = rg.Point3d(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0, 10))
        direction = random_unit_vector()
        end_point = start_point + direction * wire_length
        wire_curve = rg.LineCurve(start_point, end_point)
        wires.append(wire_curve)

    # Generate fabric-like planar surfaces
    fabrics = []
    for _ in range(num_fabrics):
        center_point = rg.Point3d(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0, 10))
        plane_normal = random_unit_vector()
        fabric_plane = rg.Plane(center_point, plane_normal)
        fabric_surface = rg.PlaneSurface(fabric_plane, rg.Interval(-fabric_size / 2, fabric_size / 2), rg.Interval(-fabric_size / 2, fabric_size / 2))
        fabrics.append(fabric_surface)

    # Combine all geometries into a single list
    geometries = wires + fabrics

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_wires=10, wire_length=15.0, num_fabrics=5, fabric_size=8.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_wires=12, wire_length=10.0, num_fabrics=3, fabric_size=5.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_wires=6, wire_length=20.0, num_fabrics=2, fabric_size=10.0, seed=18)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_wires=15, wire_length=25.0, num_fabrics=6, fabric_size=7.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_wires=8, wire_length=18.0, num_fabrics=4, fabric_size=9.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
