# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The function `create_fractured_monolith` generates an architectural concept model reflecting the metaphor "Porous fractured monolith." It constructs a solid base using specified dimensions, then introduces a series of voids and fractures that embody the metaphor's duality of solidity and permeability. By creating spherical voids and using planes to form fractures, the model achieves a dynamic, fractured appearance. These voids enhance spatial flow and encourage interaction between areas, while varying materials can emphasize contrast between solid and void sections. Ultimately, the design illustrates a balance between enclosure and openness, inviting exploration and engagement."""

#! python 3
function_code = """def create_fractured_monolith(base_length=40, base_width=25, base_height=20, num_voids=7, void_min_size=3, void_max_size=8, fracture_depth=4):
    \"""
    Generates a 3D architectural Concept Model embodying the 'Porous fractured monolith' metaphor.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - num_voids (int): Number of voids to create within the monolith.
    - void_min_size (float): Minimum size of a void in meters.
    - void_max_size (float): Maximum size of a void in meters.
    - fracture_depth (float): Depth of the fractures in meters.

    Returns:
    - List of Rhino.Geometry objects (breps) representing the monolith and its voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(43)  # Ensuring replicability

    # Define the main monolithic block
    monolith = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = monolith.ToBrep()

    # Generate voids
    voids = []
    for _ in range(num_voids):
        size = random.uniform(void_min_size, void_max_size)
        void_origin_x = random.uniform(0, base_length - size)
        void_origin_y = random.uniform(0, base_width - size)
        void_origin_z = random.uniform(0, base_height - size)
        
        # Create a spherical void for more organic fracturing
        sphere = rg.Sphere(rg.Point3d(void_origin_x + size / 2, void_origin_y + size / 2, void_origin_z + size / 2), size / 2)
        voids.append(sphere.ToBrep())

    # Create fractures using planes
    fractures = []
    for i in range(num_voids):
        fracture_plane = rg.Plane(rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), 0), rg.Vector3d(1, 1, random.uniform(-1, 1)))
        fracture_srf = rg.PlaneSurface(fracture_plane, rg.Interval(0, base_length), rg.Interval(0, base_width))
        fracture_curve = fracture_srf.ToBrep().Edges[0]
        extrusion = rg.Brep.CreateFromSurface(fracture_srf).Faces[0].CreateExtrusion(rg.LineCurve(fracture_curve.PointAtStart, rg.Point3d(fracture_curve.PointAtStart.X, fracture_curve.PointAtStart.Y, base_height)), True)
        fractures.append(extrusion)

    # Boolean operations to carve voids and fractures out of the monolith
    all_voids_and_fractures = voids + fractures
    for element in all_voids_and_fractures:
        result = rg.Brep.CreateBooleanDifference(monolith_brep, element, 0.01)
        if result:
            monolith_brep = result[0]

    # Return the final geometry
    return [monolith_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith(base_length=50, base_width=30, base_height=25, num_voids=10, void_min_size=4, void_max_size=10, fracture_depth=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith(base_length=60, base_width=35, base_height=30, num_voids=5, void_min_size=2, void_max_size=6, fracture_depth=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith(base_length=45, base_width=20, base_height=15, num_voids=8, void_min_size=2, void_max_size=7, fracture_depth=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith(base_length=55, base_width=40, base_height=22, num_voids=12, void_min_size=5, void_max_size=9, fracture_depth=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith(base_length=70, base_width=50, base_height=40, num_voids=15, void_min_size=6, void_max_size=12, fracture_depth=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
