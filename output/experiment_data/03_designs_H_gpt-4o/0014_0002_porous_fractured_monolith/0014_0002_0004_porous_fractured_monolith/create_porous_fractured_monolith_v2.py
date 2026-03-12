# Created for 0014_0002_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith_v2` generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It starts by creating a solid, monolithic base form, then introduces a series of voids that penetrate deeply into this structure, reflecting the metaphor's themes of mass and fragmentation. By varying the size and orientation of these voids, the function emphasizes connections, light penetration, and airflow, thereby fostering interaction between interior and exterior spaces. The resulting model embodies a dynamic interplay between solidity and openness, creating a complex spatial experience that encourages movement and engagement."""

#! python 3
function_code = """def create_porous_fractured_monolith_v2(base_length=30, base_width=20, base_height=10, num_voids=8, void_max_size=5, seed=42):
    \"""
    Creates an architectural Concept Model of a 'Porous fractured monolith'.

    This function generates a monolithic form and introduces a network of voids and cuts 
    that create a porous and fractured appearance. The voids vary in size and orientation, 
    emphasizing spatial connections, light penetration, and airflow. The approach focuses 
    on creating layers of voids to reveal transitions and connections within the structure.

    Parameters:
        base_length (float): Length of the base monolith in meters.
        base_width (float): Width of the base monolith in meters.
        base_height (float): Height of the base monolith in meters.
        num_voids (int): Number of voids to create within the monolith.
        void_max_size (float): Maximum size of the voids in meters.
        seed (int): Seed for randomness to ensure replicability.

    Returns:
        List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the monolithic form with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()
    
    voids = []
    
    # Generate voids using a layered approach
    for layer in range(2):  # Create two layers of voids
        for _ in range(num_voids):
            # Randomly determine the size and position of the voids
            void_length = random.uniform(0.1 * base_length, void_max_size)
            void_width = random.uniform(0.1 * base_width, void_max_size)
            void_height = random.uniform(0.1 * base_height, void_max_size)
            
            void_x = random.uniform(0, base_length - void_length)
            void_y = random.uniform(0, base_width - void_width)
            void_z = random.uniform(0, base_height - void_height)
            
            # Create a void box
            void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), rg.Interval(void_y, void_y + void_width), rg.Interval(void_z, void_z + void_height))
            void_brep = void_box.ToBrep()
            
            # Add the void to the list
            voids.append(void_brep)
    
    # Subtract the voids from the base form
    fractured_monolith = base_brep
    for void in voids:
        result = rg.Brep.CreateBooleanDifference([fractured_monolith], [void], 0.01)
        if result:
            fractured_monolith = result[0]
    
    return [fractured_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith_v2(base_length=40, base_width=25, base_height=15, num_voids=10, void_max_size=6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith_v2(base_length=35, base_width=22, base_height=12, num_voids=5, void_max_size=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith_v2(base_length=50, base_width=30, base_height=20, num_voids=12, void_max_size=8, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith_v2(base_length=45, base_width=28, base_height=18, num_voids=15, void_max_size=7, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith_v2(base_length=32, base_width=24, base_height=14, num_voids=9, void_max_size=5, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
