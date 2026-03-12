# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The provided function, `create_fractured_monolith_with_pathways`, generates a 3D architectural model that embodies the metaphor of a "Porous fractured monolith." It begins by creating a solid monolithic base, representing the substantial mass. The function then integrates a specified number of voids, varying in size and orientation, to reflect the metaphor's dynamic and complex nature. Pathways are carved into the structure, enhancing spatial connectivity and encouraging exploration. The result is a model that balances solidity and openness, illustrating the interplay of solid and void spaces while promoting natural light, ventilation, and interaction among different zones."""

#! python 3
function_code = """def create_fractured_monolith_with_pathways(base_length=30, base_width=20, base_height=15, pathway_width=3, num_voids=7, void_size_range=(2, 5), seed=42):
    \"""
    Generates a 3D architectural Concept Model embodying the 'Porous fractured monolith' metaphor
    with integrated pathways that enhance spatial connectivity and exploration.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - pathway_width (float): The width of the pathways carved through the monolith.
    - num_voids (int): Number of voids to create within the monolith.
    - void_size_range (tuple): Min and max size of the voids in meters.
    - seed (int): Random seed for reproducible results.

    Returns:
    - List of Rhino.Geometry objects (breps) representing the monolith with voids and pathways.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)  # Ensuring replicability

    # Define the main monolithic block
    monolith = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = monolith.ToBrep()

    # Generate voids
    voids = []
    for _ in range(num_voids):
        void_size_x = random.uniform(*void_size_range)
        void_size_y = random.uniform(*void_size_range)
        void_size_z = random.uniform(*void_size_range)
        
        void_origin_x = random.uniform(0, base_length - void_size_x)
        void_origin_y = random.uniform(0, base_width - void_size_y)
        void_origin_z = random.uniform(0, base_height - void_size_z)
        
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_origin_x, void_origin_x + void_size_x), rg.Interval(void_origin_y, void_origin_y + void_size_y), rg.Interval(void_origin_z, void_origin_z + void_size_z))
        voids.append(void_box.ToBrep())

    # Create pathways
    pathway_curves = [
        rg.LineCurve(rg.Point3d(pathway_width / 2, 0, 0), rg.Point3d(pathway_width / 2, base_width, base_height)),
        rg.LineCurve(rg.Point3d(base_length - pathway_width / 2, 0, 0), rg.Point3d(base_length - pathway_width / 2, base_width, base_height))
    ]
    pathways = [rg.Extrusion.Create(curve, pathway_width, True).ToBrep() for curve in pathway_curves]

    # Boolean difference to carve voids and pathways out of the monolith
    for void in voids + pathways:
        result = rg.Brep.CreateBooleanDifference(monolith_brep, void, 0.01)
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
    geometry = create_fractured_monolith_with_pathways(base_length=50, base_width=30, base_height=20, pathway_width=5, num_voids=10, void_size_range=(3, 7), seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith_with_pathways(base_length=40, base_width=25, base_height=18, pathway_width=4, num_voids=5, void_size_range=(1, 4), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith_with_pathways(base_length=35, base_width=22, base_height=12, pathway_width=2, num_voids=8, void_size_range=(1, 6), seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith_with_pathways(base_length=45, base_width=35, base_height=25, pathway_width=6, num_voids=12, void_size_range=(2, 8), seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith_with_pathways(base_length=60, base_width=40, base_height=30, pathway_width=7, num_voids=15, void_size_range=(3, 9), seed=2022)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
