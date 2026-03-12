# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The function `create_fractured_monolith_with_cavities` generates an architectural concept model based on the metaphor "Porous fractured monolith." It begins with a solid monolithic shape, then introduces irregular voids (spherical cavities) to embody the porous quality, ensuring varied sizes and positions to enhance complexity and movement. Following this, the function simulates fractures using random planes, emphasizing the contrast between solidity and openness. The process results in a 3D model that visually represents the dynamic relationship between the mass and the voids, promoting natural light flow and encouraging exploration of spatial connections within the design."""

#! python 3
function_code = """def create_fractured_monolith_with_cavities(base_length, base_width, base_height, cavity_count, max_cavity_radius, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'Porous fractured monolith' metaphor.

    This function starts with a solid monolithic mass, introduces spherical cavities to emphasize the porous nature,
    and applies irregular fractures to create a sense of dynamic complexity and movement.

    Parameters:
    - base_length (float): The length of the monolith base in meters.
    - base_width (float): The width of the monolith base in meters.
    - base_height (float): The height of the monolith base in meters.
    - cavity_count (int): The number of cavities to introduce.
    - max_cavity_radius (float): The maximum radius of each cavity.
    - seed (int, optional): Seed for random number generation to ensure replicable results.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries including the main mass and the voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed
    random.seed(seed)

    # Create the base monolithic mass
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = base_box.ToBrep()

    # Function to create random spherical cavities
    def create_spherical_cavity():
        center_x = random.uniform(0, base_length)
        center_y = random.uniform(0, base_width)
        center_z = random.uniform(0, base_height)
        radius = random.uniform(0.1, max_cavity_radius)
        sphere = rg.Sphere(rg.Point3d(center_x, center_y, center_z), radius)
        return sphere.ToBrep()

    # Generate cavities
    cavities = [create_spherical_cavity() for _ in range(cavity_count)]

    # Subtract cavities from the monolith
    fractured_monolith = monolith_brep
    for cavity in cavities:
        difference_result = rg.Brep.CreateBooleanDifference([fractured_monolith], [cavity], 0.01)
        if difference_result and len(difference_result) > 0:
            fractured_monolith = difference_result[0]

    # Adding fractures by using simple planes
    fractures = []
    for _ in range(cavity_count // 2):
        start_point = rg.Point3d(
            random.uniform(0, base_length),
            random.uniform(0, base_width),
            random.uniform(0, base_height)
        )
        end_point = rg.Point3d(
            random.uniform(0, base_length),
            random.uniform(0, base_width),
            random.uniform(0, base_height)
        )
        line = rg.Line(start_point, end_point)
        fracture_plane = rg.Plane(line.PointAt(0.5), rg.Vector3d.ZAxis)
        planar_breps = rg.Brep.CreatePlanarBreps([rg.Curve.ProjectToPlane(line.ToNurbsCurve(), fracture_plane)])
        if planar_breps and len(planar_breps) > 0:
            fractures.append(planar_breps[0])

    # Apply fractures to the monolith
    for fracture in fractures:
        difference_result = rg.Brep.CreateBooleanDifference([fractured_monolith], [fracture], 0.01)
        if difference_result and len(difference_result) > 0:
            fractured_monolith = difference_result[0]

    return [fractured_monolith] + cavities"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith_with_cavities(10.0, 5.0, 15.0, 8, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith_with_cavities(20.0, 10.0, 25.0, 12, 3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith_with_cavities(15.0, 7.5, 10.0, 5, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith_with_cavities(12.0, 6.0, 18.0, 10, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith_with_cavities(25.0, 12.0, 30.0, 15, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
