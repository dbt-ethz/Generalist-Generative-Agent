# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model that embodies the metaphor "Porous fractured monolith." It begins by creating a solid box representing the monolithic mass. The function then introduces a specified number of voids, randomly determining their dimensions and positions to reflect the metaphor's complexity. These voids are subtracted from the monolith, resulting in a fractured appearance that highlights the contrast between solidity and openness. The design promotes natural light and air flow, fostering interaction between interior and exterior spaces, while also encouraging exploration through the dynamic pathways created by the voids."""

#! python 3
function_code = """def create_porous_fractured_monolith(width, depth, height, void_count, seed=42):
    \"""
    Create a 'Porous Fractured Monolith' architectural concept model.

    Parameters:
    - width (float): The width of the monolithic form in meters.
    - depth (float): The depth of the monolithic form in meters.
    - height (float): The height of the monolithic form in meters.
    - void_count (int): The number of voids to create within the monolith.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create the initial monolithic mass as a box
    base_point = rg.Point3d(0, 0, 0)
    monolith = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
    monolith_brep = monolith.ToBrep()

    voids = []

    for _ in range(void_count):
        # Randomly generate dimensions and position for each void
        void_width = random.uniform(0.1 * width, 0.3 * width)
        void_depth = random.uniform(0.1 * depth, 0.3 * depth)
        void_height = random.uniform(0.1 * height, 0.7 * height)

        x_pos = random.uniform(0, width - void_width)
        y_pos = random.uniform(0, depth - void_depth)
        z_pos = random.uniform(0, height - void_height)

        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_pos, x_pos + void_width), 
                          rg.Interval(y_pos, y_pos + void_depth), rg.Interval(z_pos, z_pos + void_height))
        void_brep = void_box.ToBrep()
        voids.append(void_brep)

    # Subtract the voids from the monolith to create the fractured effect
    fractured_monolith = monolith_brep
    for void in voids:
        fractured_result = rg.Brep.CreateBooleanDifference([fractured_monolith], [void], 0.01)
        if fractured_result:
            fractured_monolith = fractured_result[0]

    return [fractured_monolith] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(5.0, 3.0, 10.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(7.5, 4.0, 12.0, 10, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(6.0, 2.5, 9.0, 5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(8.0, 6.0, 15.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(4.0, 3.5, 8.0, 6, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
