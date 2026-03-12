# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It begins by creating a solid base structure that symbolizes the monolithic aspect. The function then introduces a series of voids and fractures, varying in size and orientation, to represent the complexity and dynamic nature of the metaphor. These voids enhance light penetration and airflow, promoting spatial connectivity. The model balances solidity and openness, encouraging interaction and exploration within the space, while visually illustrating the tension between a cohesive mass and fragmented elements."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length=30, base_width=20, base_height=15, num_voids=5, void_min_size=2, void_max_size=5, fracture_depth=3):
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

    random.seed(42)  # Ensuring replicability

    # Define the main monolithic block
    monolith = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = monolith.ToBrep()

    # Generate voids
    voids = []
    for _ in range(num_voids):
        void_size_x = random.uniform(void_min_size, void_max_size)
        void_size_y = random.uniform(void_min_size, void_max_size)
        void_size_z = random.uniform(void_min_size, void_max_size)
        
        void_origin_x = random.uniform(0, base_length - void_size_x)
        void_origin_y = random.uniform(0, base_width - void_size_y)
        void_origin_z = random.uniform(0, base_height - void_size_z)
        
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_origin_x, void_origin_x + void_size_x), rg.Interval(void_origin_y, void_origin_y + void_size_y), rg.Interval(void_origin_z, void_origin_z + void_size_z))
        voids.append(void_box.ToBrep())

    # Create fractures
    fractures = []
    for _ in range(num_voids):
        fracture_size_x = random.uniform(void_min_size, void_max_size)
        fracture_size_y = random.uniform(void_min_size, void_max_size)
        
        fracture_origin_x = random.uniform(0, base_length - fracture_size_x)
        fracture_origin_y = random.uniform(0, base_width - fracture_size_y)
        
        fracture_curve = rg.LineCurve(rg.Point3d(fracture_origin_x, fracture_origin_y, 0), rg.Point3d(fracture_origin_x, fracture_origin_y, base_height))
        fracture_srf = rg.Extrusion.Create(fracture_curve, fracture_depth, True).ToBrep()
        fractures.append(fracture_srf)

    # Boolean difference to carve voids and fractures out of the monolith
    for void in voids:
        result = rg.Brep.CreateBooleanDifference(monolith_brep, void, 0.01)
        if result:
            monolith_brep = result[0]

    for fracture in fractures:
        result = rg.Brep.CreateBooleanDifference(monolith_brep, fracture, 0.01)
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
    geometry = create_porous_fractured_monolith(base_length=40, base_width=30, base_height=20, num_voids=10, void_min_size=3, void_max_size=7, fracture_depth=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(base_length=25, base_width=15, base_height=10, num_voids=7, void_min_size=1, void_max_size=4, fracture_depth=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(base_length=35, base_width=25, base_height=18, num_voids=6, void_min_size=2.5, void_max_size=6, fracture_depth=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(base_length=50, base_width=40, base_height=30, num_voids=8, void_min_size=4, void_max_size=10, fracture_depth=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(base_length=45, base_width=35, base_height=25, num_voids=12, void_min_size=3, void_max_size=8, fracture_depth=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
