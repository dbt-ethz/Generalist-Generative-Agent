# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model that embodies the metaphor of a "Porous fractured monolith" by creating a solid block with strategic voids. It begins by defining dimensions for a monolithic base and then introduces a specified number of voids, which are represented as random boxes subtracted from the base. This process captures the essence of solidity and fragmentation, while the irregular shapes of the voids enhance the model's dynamic quality. The result is a 3D representation that emphasizes light, shadow, and spatial connectivity, aligning with the metaphor's themes of permeability and interaction."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, cut_count, seed):
    \"""
    Creates an architectural Concept Model that embodies the 'Porous fractured monolith' metaphor.
    
    Parameters:
    - base_length (float): The length of the monolithic block.
    - base_width (float): The width of the monolithic block.
    - base_height (float): The height of the monolithic block.
    - cut_count (int): Number of voids to introduce into the block.
    - seed (int): Seed for random generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D breps representing the fractured monolithic form with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for reproducibility
    random.seed(seed)
    
    # Create the base monolithic block
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []
    
    # Create voids by subtracting random boxes from the base block
    for _ in range(cut_count):
        # Random dimensions and location for the voids
        void_length = random.uniform(base_length * 0.1, base_length * 0.5)
        void_width = random.uniform(base_width * 0.1, base_width * 0.5)
        void_height = random.uniform(base_height * 0.1, base_height * 0.5)
        
        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)
        
        # Create the void box
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), rg.Interval(void_y, void_y + void_width), rg.Interval(void_z, void_z + void_height))
        void_brep = void_box.ToBrep()
        
        voids.append(void_brep)
    
    # Subtract voids from the base block
    fractured_monolith = base_brep
    for void in voids:
        boolean_difference = rg.Brep.CreateBooleanDifference([fractured_monolith], [void], 0.001)
        if boolean_difference:  # Check if the operation succeeded
            fractured_monolith = boolean_difference[0]
    
    return [fractured_monolith] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(10.0, 5.0, 15.0, 3, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(12.5, 6.0, 20.0, 5, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(8.0, 4.0, 12.0, 4, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(15.0, 7.0, 10.0, 2, 77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(9.0, 3.5, 18.0, 6, 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
