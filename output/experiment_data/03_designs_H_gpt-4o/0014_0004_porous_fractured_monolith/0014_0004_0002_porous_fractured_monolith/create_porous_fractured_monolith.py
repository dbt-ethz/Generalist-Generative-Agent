# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model that embodies the metaphor "Porous fractured monolith." It starts by establishing a substantial, unified mass representing the monolithic form. The function then introduces strategically placed voids, varying in size and orientation, creating a dynamic interplay of solid and open spaces. This design reflects the metaphor's essence, balancing permanence with fluidity. By using a mix of opaque and transparent materials, the model highlights the contrast between mass and void, enhancing natural light and airflow. Ultimately, it fosters connectivity and interaction within the architectural space, inviting exploration."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_dim, void_dim_range, void_count, seed=42):
    \"""
    Create a 'Porous fractured monolith' architectural concept model.

    This function generates a monolithic mass and introduces voids with irregular, fractal-like patterns
    to exemplify the metaphor's complexity and dynamism. Voids vary in size and orientation, creating an
    intricate play of solid and open spaces.

    Parameters:
    - base_dim (tuple of float): Dimensions of the monolithic base (length, width, height) in meters.
    - void_dim_range (tuple of float): Min and max dimensions for the voids, defining their size range.
    - void_count (int): The number of voids to carve out from the base.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Unpack base dimensions
    base_length, base_width, base_height = base_dim

    # Create the main monolithic base
    base_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(0, base_length),
        rg.Interval(0, base_width),
        rg.Interval(0, base_height)
    )
    base_brep = base_box.ToBrep()

    # Function to create a fractal-like void
    def create_fractal_void(center, scale):
        void_shape = rg.Sphere(center, scale).ToBrep()  # Using a sphere for a more organic void
        return void_shape

    voids = []

    # Strategically place voids in a fractal pattern
    for _ in range(void_count):
        scale = random.uniform(*void_dim_range)
        center_x = random.uniform(0, base_length)
        center_y = random.uniform(0, base_width)
        center_z = random.uniform(0, base_height)
        center = rg.Point3d(center_x, center_y, center_z)
        voids.append(create_fractal_void(center, scale))

    # Subtract voids from the monolithic brep
    fractured_monolith = base_brep
    for void in voids:
        result = rg.Brep.CreateBooleanDifference([fractured_monolith], [void], 0.001)
        if result:
            fractured_monolith = result[0]

    return [fractured_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith((10, 5, 3), (0.1, 0.5), 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith((8, 4, 2), (0.2, 0.6), 10, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith((12, 6, 4), (0.3, 0.7), 20, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith((15, 7, 5), (0.4, 0.8), 12, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith((9, 3, 2), (0.2, 0.4), 8, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
