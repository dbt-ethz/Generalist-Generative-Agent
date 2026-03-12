# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model by simulating a 'Porous fractured monolith' through a single block of material. It creates a monolithic base defined by specified dimensions and introduces a defined number of voids, which are randomly placed and sized within the block. These voids reflect the metaphor's themes of permeability and fragmentation, enhancing the interplay of light and shadow. By subtracting these voids from the base, the model embodies the duality of mass and void, facilitating dynamic spatial relationships and promoting connectivity between interior and exterior spaces."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length=20, base_width=15, base_height=30, voids_count=5, seed=42):
    \"""
    Creates a conceptual architectural model representing a 'Porous fractured monolith'.
    
    The model consists of a single monolithic block with strategically placed voids
    to reflect permeability and fragmentation. The voids are irregular and dynamic,
    enhancing the interaction of light and shadow and guiding movement throughout the design.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - voids_count (int): The number of voids to create within the monolith.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List of Breps: The 3D geometries of the concept model including the base and voids.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Box, Brep, Vector3d, Point3d, Plane, Interval

    # Set the random seed for consistency
    random.seed(seed)

    # Create the base monolithic block
    base_plane = Plane.WorldXY
    base_box = Box(base_plane, Interval(0, base_length), Interval(0, base_width), Interval(0, base_height))
    base_brep = base_box.ToBrep()

    # Generate voids
    voids = []
    for _ in range(voids_count):
        void_length = random.uniform(3, base_length / 2)
        void_width = random.uniform(2, base_width / 2)
        void_height = random.uniform(5, base_height)
        
        # Random position for the void
        x_pos = random.uniform(0, base_length - void_length)
        y_pos = random.uniform(0, base_width - void_width)
        z_pos = random.uniform(0, base_height - void_height)
        
        void_box = Box(base_plane, Interval(x_pos, x_pos + void_length), Interval(y_pos, y_pos + void_width), Interval(z_pos, z_pos + void_height))
        void_brep = void_box.ToBrep()

        # Subtract the voids from the base block
        result_breps = Brep.CreateBooleanDifference([base_brep], [void_brep], 0.01)
        if result_breps:
            base_brep = result_breps[0]
            voids.append(void_brep)

    # Return the final geometry including the base block and voids
    return [base_brep] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(base_length=25, base_width=20, base_height=35, voids_count=7, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(base_length=30, base_width=10, base_height=40, voids_count=3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(base_length=15, base_width=25, base_height=20, voids_count=4, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(base_length=40, base_width=30, base_height=50, voids_count=6, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(base_length=18, base_width=12, base_height=28, voids_count=8, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
