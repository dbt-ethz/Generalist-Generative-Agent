# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model by first establishing a solid, monolithic base defined by specified dimensions. It then introduces a series of strategically located voids and fractures, simulating the metaphor of a "Porous fractured monolith." Each void varies in size and orientation, enhancing the model's complexity and dynamism, while the fractured surfaces promote lightness and permeability. The boolean difference operation subtracts these voids from the base, resulting in a structure that visually and spatially embodies the interplay of solidity and openness, inviting exploration and interaction within the architectural space."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, num_voids, fracture_depth, seed=42):
    \"""
    Create an architectural Concept Model based on the metaphor 'Porous fractured monolith'.
    
    This function generates a monolithic form and introduces strategic voids and fractures.
    It emphasizes the interplay of mass and void, creating a dynamic architectural space.

    Parameters:
    - base_length (float): Length of the monolithic base in meters.
    - base_width (float): Width of the monolithic base in meters.
    - base_height (float): Height of the monolithic base in meters.
    - num_voids (int): Number of voids to create within the monolith.
    - fracture_depth (float): Depth of the fractures to be introduced.
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

    # Function to create a random void with a fracture
    def create_random_void_with_fracture():
        void_length = random.uniform(0.1 * base_length, 0.3 * base_length)
        void_width = random.uniform(0.1 * base_width, 0.3 * base_width)
        void_height = random.uniform(0.1 * base_height, 0.7 * base_height)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

        void_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(void_x, void_x + void_length),
            rg.Interval(void_y, void_y + void_width),
            rg.Interval(void_z, void_z + void_height)
        )
        
        # Create a fracture plane
        fracture_plane = rg.Plane(rg.Point3d(void_x, void_y, void_z), rg.Vector3d(1, 0, 0))
        fracture_surface = rg.PlaneSurface(fracture_plane, rg.Interval(0, void_length), rg.Interval(0, void_height))
        
        # Split the void with the fracture surface
        split_breps = void_box.ToBrep().Split([fracture_surface.ToBrep()], 0.001)
        if split_breps and len(split_breps) > 0:
            return split_breps[0]  # Return the largest part after split for simplicity

        return void_box.ToBrep()

    # Generate voids with fractures and subtract from the base brep
    voids = [create_random_void_with_fracture() for _ in range(num_voids)]
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
    geometry = create_porous_fractured_monolith(5.0, 3.0, 4.0, 10, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(6.0, 2.5, 3.5, 8, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(4.0, 4.0, 5.0, 12, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(7.0, 3.5, 6.0, 15, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(8.0, 2.0, 5.0, 9, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
