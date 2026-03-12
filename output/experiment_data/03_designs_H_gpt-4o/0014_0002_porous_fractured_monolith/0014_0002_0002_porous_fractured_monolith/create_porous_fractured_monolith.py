# Created for 0014_0002_porous_fractured_monolith.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It begins by creating a solid base structure, reflecting the cohesive and dominant mass suggested by the metaphor. The function then introduces a series of voids, which vary in size, depth, and orientation, to emphasize the fractured, porous quality of the design. These voids enhance spatial connectivity, allowing light and airflow to penetrate the structure, thus fostering interaction between interior and exterior spaces. Ultimately, the model visually explores the interplay between solidity and fragmentation, creating a dynamic spatial experience."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length=30, base_width=20, base_height=10, num_voids=5, void_depth_range=(0.2, 0.8), seed=42):
    \"""
    Creates an architectural Concept Model of a 'Porous fractured monolith'.
    
    This function generates a solid monolithic form and introduces a series of interconnected voids 
    that penetrate deeply into the form. The voids are designed to vary in depth and orientation, 
    emphasizing the fractured quality and enhancing spatial connections, light penetration, and airflow.
    
    Parameters:
        base_length (float): Length of the base monolith in meters.
        base_width (float): Width of the base monolith in meters.
        base_height (float): Height of the base monolith in meters.
        num_voids (int): Number of voids to create within the monolith.
        void_depth_range (tuple): Min and max proportion of the base depth that voids can penetrate.
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
    
    # Generate interconnected voids
    for _ in range(num_voids):
        # Randomly determine the size and depth of the voids
        void_length = random.uniform(0.1 * base_length, 0.4 * base_length)
        void_width = random.uniform(0.1 * base_width, 0.4 * base_width)
        void_depth = random.uniform(void_depth_range[0] * base_height, void_depth_range[1] * base_height)
        
        # Randomly position the void within the base
        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_depth)
        
        # Create a box as the void
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), rg.Interval(void_y, void_y + void_width), rg.Interval(void_z, void_z + void_depth))
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
    geometry = create_porous_fractured_monolith(base_length=40, base_width=30, base_height=15, num_voids=10, void_depth_range=(0.3, 0.7), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(base_length=25, base_width=15, base_height=20, num_voids=8, void_depth_range=(0.1, 0.5), seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(base_length=35, base_width=25, base_height=12, num_voids=6, void_depth_range=(0.2, 0.9), seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(base_length=50, base_width=40, base_height=25, num_voids=12, void_depth_range=(0.1, 0.6), seed=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(base_length=45, base_width=35, base_height=18, num_voids=15, void_depth_range=(0.3, 0.8), seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
