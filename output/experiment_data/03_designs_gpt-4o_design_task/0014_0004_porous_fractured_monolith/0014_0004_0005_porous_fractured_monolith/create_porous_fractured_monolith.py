# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model based on the metaphor "Porous fractured monolith." It begins by creating a robust, singular mass representing the monolithic form, defined by user-specified dimensions. The function then carves out a series of voids with varying sizes and orientations, reflecting the complexity and dynamism of the metaphor. The resulting model emphasizes the contrast between solid mass and voids, using a blend of opaque and transparent materials to highlight permeability and lightness. This design facilitates natural ventilation and guides movement, promoting interaction and connectivity within the architectural space."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, num_voids, void_min_size, void_max_size):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Porous fractured monolith'. The model is a substantial
    singular mass disrupted by a series of voids and fractures, conveying a balance of permanence and fluidity.

    Args:
    - base_length (float): The length of the base monolithic form in meters.
    - base_width (float): The width of the base monolithic form in meters.
    - base_height (float): The height of the base monolithic form in meters.
    - num_voids (int): Number of voids to carve out from the monolith.
    - void_min_size (float): Minimum size of the voids in meters.
    - void_max_size (float): Maximum size of the voids in meters.

    Returns:
    - List[Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicable randomness

    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []

    # Generate random voids
    for _ in range(num_voids):
        # Random void dimensions
        void_length = random.uniform(void_min_size, void_max_size)
        void_width = random.uniform(void_min_size, void_max_size)
        void_height = random.uniform(void_min_size, void_max_size)

        # Random position within the base volume
        x = random.uniform(0, base_length - void_length)
        y = random.uniform(0, base_width - void_width)
        z = random.uniform(0, base_height - void_height)

        # Create the void as a box
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + void_length), rg.Interval(y, y + void_width), rg.Interval(z, z + void_height))
        void_brep = void_box.ToBrep()

        voids.append(void_brep)

    # Subtract voids from the base form
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
    geometry = create_porous_fractured_monolith(10.0, 5.0, 15.0, 8, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(12.0, 6.0, 20.0, 10, 1.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(8.0, 4.0, 10.0, 5, 0.2, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(15.0, 7.0, 12.0, 6, 0.3, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(9.0, 4.5, 14.0, 7, 0.4, 1.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
