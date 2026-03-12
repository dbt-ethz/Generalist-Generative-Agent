# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model inspired by the metaphor "Porous fractured monolith." It begins by creating a robust, unified mass representing the monolithic form. The function then introduces various voids and fractures of differing sizes and orientations, reflecting the metaphor's complexity. This design emphasizes the contrast between solid mass and open space, enhancing lightness and permeability. By strategically placing voids, the model promotes natural ventilation and guides movement, fostering interaction between interior and exterior environments. The resulting geometry captures the duality of solidity and openness, inviting exploration and engagement."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, num_voids, min_void_size, max_void_size, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Porous fractured monolith'.
    
    The function generates a monolithic solid with strategic voids and fractures, emphasizing the contrast between mass and void,
    while allowing for light and air permeability, as well as dynamic pathways.

    Parameters:
    - base_length (float): Length of the base monolithic form in meters.
    - base_width (float): Width of the base monolithic form in meters.
    - base_height (float): Height of the base monolithic form in meters.
    - num_voids (int): Number of voids to introduce into the monolithic form.
    - min_void_size (float): Minimum size of the voids in meters.
    - max_void_size (float): Maximum size of the voids in meters.
    - seed (int): Seed for randomness to ensure replicability.
    
    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Create the base monolithic form
    base_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(0, base_length),
        rg.Interval(0, base_width),
        rg.Interval(0, base_height)
    )
    base_brep = base_box.ToBrep()

    # Function to create a random void
    def create_random_void():
        void_length = random.uniform(min_void_size, max_void_size)
        void_width = random.uniform(min_void_size, max_void_size)
        void_height = random.uniform(min_void_size, max_void_size)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

        void_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(void_x, void_x + void_length),
            rg.Interval(void_y, void_y + void_width),
            rg.Interval(void_z, void_z + void_height)
        )
        return void_box.ToBrep()

    # Create voids and subtract from the base brep
    voids = [create_random_void() for _ in range(num_voids)]
    breps = [base_brep]

    for void in voids:
        breps = rg.Brep.CreateBooleanDifference(breps, [void], 0.001)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(10, 5, 3, 15, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(8, 4, 6, 10, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(12, 6, 4, 20, 0.2, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(15, 7, 5, 25, 0.4, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(9, 3, 2, 12, 0.1, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
