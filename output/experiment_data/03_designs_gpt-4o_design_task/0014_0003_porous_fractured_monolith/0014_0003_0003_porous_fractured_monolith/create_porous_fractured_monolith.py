# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model embodying the metaphor "Porous fractured monolith." It begins by creating a solid monolithic shape defined by user-specified dimensions. The function then introduces irregular voids within this structure, simulating fractures that contrast the solidity with openings. These voids are randomly positioned and scaled, reflecting the metaphor's emphasis on complexity and movement. By subtracting the void geometries from the monolith, the model achieves a dynamic interplay between mass and space, enhancing light penetration and facilitating interaction while inviting exploration, encapsulating the essence of the proposed architectural concept."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, num_voids, void_scale_range, seed=42):
    \"""
    Creates a conceptual architectural model based on the "Porous fractured monolith" metaphor.
    
    Parameters:
    - base_length (float): The length of the base monolithic form in meters.
    - base_width (float): The width of the base monolithic form in meters.
    - base_height (float): The height of the base monolithic form in meters.
    - num_voids (int): The number of voids or fractures to introduce into the monolith.
    - void_scale_range (tuple): A range for scaling the voids, given as (min_scale, max_scale).
    - seed (int): Seed for random number generation to ensure replicability.
    
    Returns:
    - list: A list of 3D geometries (Breps) representing the monolithic form and its voids.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed
    random.seed(seed)
    
    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = base_box.ToBrep()

    # Generate voids
    voids = []
    for _ in range(num_voids):
        # Randomly position voids within the monolith
        void_center_x = random.uniform(0, base_length)
        void_center_y = random.uniform(0, base_width)
        void_center_z = random.uniform(0, base_height)
        
        # Randomly scale the void size
        scale_factor = random.uniform(*void_scale_range)
        void_length = base_length * scale_factor
        void_width = base_width * scale_factor
        void_height = base_height * scale_factor

        # Create the void box
        void_box = rg.Box(rg.Plane.WorldXY, 
                          rg.Interval(void_center_x - void_length / 2, void_center_x + void_length / 2),
                          rg.Interval(void_center_y - void_width / 2, void_center_y + void_width / 2),
                          rg.Interval(void_center_z - void_height / 2, void_center_z + void_height / 2))
        void_brep = void_box.ToBrep()
        
        # Store the void
        voids.append(void_brep)

    # Subtract voids from the monolith
    fractured_monolith = monolith_brep
    for void in voids:
        difference_result = rg.Brep.CreateBooleanDifference([fractured_monolith], [void], 0.01)
        if difference_result:
            fractured_monolith = difference_result[0]

    # Return the fractured monolith
    return [fractured_monolith] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(10.0, 5.0, 8.0, 3, (0.1, 0.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(15.0, 10.0, 12.0, 5, (0.2, 0.6), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(7.0, 4.0, 6.0, 2, (0.3, 0.7), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(12.0, 6.0, 10.0, 4, (0.15, 0.35), seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(20.0, 15.0, 10.0, 6, (0.05, 0.4), seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
