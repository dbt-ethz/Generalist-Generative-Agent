# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The function `create_fractured_monolith_with_pathways` generates a 3D architectural concept model inspired by the metaphor of a "Porous fractured monolith." It begins by creating a solid monolithic block, representing the substantial mass. The function then incorporates a specified number of voids, which are randomly sized and positioned, reflecting the metaphor's complexity and dynamic nature. Additionally, pathways are generated to connect these voids, emphasizing permeability and spatial flow. The combination of solid and void elements illustrates a balance between enclosure and openness, promoting interaction and exploration while embodying the metaphor's key traits of connectivity and engagement."""

#! python 3
function_code = """def create_fractured_monolith_with_pathways(base_length=30, base_width=20, base_height=15, void_count=5, pathway_width=2, seed=42):
    \"""
    Generates a 3D architectural Concept Model based on the 'Porous fractured monolith' metaphor.
    
    The model consists of a solid monolithic base with integrated voids and pathways that create a sense of permeability
    and connectivity. The pathways interconnect voids and spaces, emphasizing exploration and flow.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - void_count (int): Number of voids to create within the monolith.
    - pathway_width (float): The width of the pathways connecting voids in meters.
    - seed (int): Random seed for reproducibility.

    Returns:
    - List of Rhino.Geometry objects (breps) representing the monolith, voids, and pathways.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)  # Ensuring replicability

    # Define the main monolithic block
    monolith = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = monolith.ToBrep()

    # Generate voids
    voids = []
    for _ in range(void_count):
        void_size_x = random.uniform(base_length * 0.1, base_length * 0.3)
        void_size_y = random.uniform(base_width * 0.1, base_width * 0.3)
        void_size_z = random.uniform(base_height * 0.1, base_height * 0.3)

        void_origin_x = random.uniform(0, base_length - void_size_x)
        void_origin_y = random.uniform(0, base_width - void_size_y)
        void_origin_z = random.uniform(0, base_height - void_size_z)

        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_origin_x, void_origin_x + void_size_x), 
                          rg.Interval(void_origin_y, void_origin_y + void_size_y), 
                          rg.Interval(void_origin_z, void_origin_z + void_size_z))
        voids.append(void_box.ToBrep())

    # Create pathways connecting voids
    pathways = []
    for i in range(void_count - 1):
        start_point = rg.Point3d(voids[i].GetBoundingBox(True).Center)
        end_point = rg.Point3d(voids[i+1].GetBoundingBox(True).Center)

        pathway_curve = rg.LineCurve(start_point, end_point)
        pathway_srf = rg.Extrusion.Create(pathway_curve, pathway_width, True).ToBrep()
        pathways.append(pathway_srf)

    # Boolean difference to carve voids and pathways out of the monolith
    for void in voids:
        result = rg.Brep.CreateBooleanDifference([monolith_brep], [void], 0.01)
        if result:
            monolith_brep = result[0]

    for pathway in pathways:
        result = rg.Brep.CreateBooleanDifference([monolith_brep], [pathway], 0.01)
        if result:
            monolith_brep = result[0]

    # Return the final geometry
    return [monolith_brep] + voids + pathways"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith_with_pathways(base_length=40, base_width=25, base_height=20, void_count=7, pathway_width=3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith_with_pathways(base_length=35, base_width=15, base_height=10, void_count=4, pathway_width=1.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith_with_pathways(base_length=50, base_width=30, base_height=25, void_count=6, pathway_width=2.5, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith_with_pathways(base_length=45, base_width=22, base_height=18, void_count=5, pathway_width=2, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith_with_pathways(base_length=60, base_width=35, base_height=30, void_count=8, pathway_width=4, seed=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
