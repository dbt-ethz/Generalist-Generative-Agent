# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model embodying the metaphor of a "Porous fractured monolith." It starts by creating a solid monolithic form defined by specified dimensions. The function then introduces a series of voids, simulating fractures, which vary in size and orientation to reflect the metaphor's complexity. By subtracting these voids from the monolith, the design achieves a balance between solidity and openness, enhancing natural light and airflow. This dynamic interplay invites exploration and interaction within the space, embodying the metaphor's duality of permanence and fluidity, fostering connectivity in architectural environments."""

#! python 3
function_code = """def create_porous_fractured_monolith(length, width, height, void_count, seed=42):
    \"""
    Constructs an architectural Concept Model inspired by the metaphor 'Porous fractured monolith'.
    
    This function creates a robust monolithic structure and introduces voids and fractures strategically,
    reflecting complexity and dynamism by varying void orientation and size. The interplay between mass and void 
    highlights solidity and openness, promoting light diffusion and air flow.

    Parameters:
    - length (float): The length of the monolithic form in meters.
    - width (float): The width of the monolithic form in meters.
    - height (float): The height of the monolithic form in meters.
    - void_count (int): Number of voids to carve within the monolith.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create the main monolithic base
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(length, 0, 0),
        rg.Point3d(length, width, 0),
        rg.Point3d(0, width, 0),
        rg.Point3d(0, 0, height),
        rg.Point3d(length, 0, height),
        rg.Point3d(length, width, height),
        rg.Point3d(0, width, height)
    ]
    monolith_brep = rg.Brep.CreateFromBox(base_corners)

    voids = []

    # Create voids as fractures using planes and subtract them
    for _ in range(void_count):
        # Randomly generate a plane to cut through the monolithic mass
        origin_x = random.uniform(0, length)
        origin_y = random.uniform(0, width)
        origin_z = random.uniform(0, height)

        normal_x = random.uniform(-1, 1)
        normal_y = random.uniform(-1, 1)
        normal_z = random.uniform(-1, 1)

        plane = rg.Plane(rg.Point3d(origin_x, origin_y, origin_z), rg.Vector3d(normal_x, normal_y, normal_z))

        # Create a large box to intersect with the monolith for the void
        large_box = rg.Brep.CreateFromBox([
            rg.Point3d(-length, -width, -height),
            rg.Point3d(2 * length, -width, -height),
            rg.Point3d(2 * length, 2 * width, -height),
            rg.Point3d(-length, 2 * width, -height),
            rg.Point3d(-length, -width, 2 * height),
            rg.Point3d(2 * length, -width, 2 * height),
            rg.Point3d(2 * length, 2 * width, 2 * height),
            rg.Point3d(-length, 2 * width, 2 * height)
        ])

        # Cut the large box with the plane to form a void
        if plane.IsValid:
            bounding_box = rg.BoundingBox(rg.Point3d(-length, -width, -height), rg.Point3d(2 * length, 2 * width, 2 * height))
            void_brep = large_box.Trim(plane, 0.001)
            if void_brep:
                voids.extend(void_brep)

    # Subtract voids from the monolith
    fractured_monolith = monolith_brep
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
    geometry = create_porous_fractured_monolith(10.0, 5.0, 3.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(15.0, 7.0, 4.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(12.0, 6.0, 5.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(8.0, 4.0, 2.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(20.0, 10.0, 6.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
