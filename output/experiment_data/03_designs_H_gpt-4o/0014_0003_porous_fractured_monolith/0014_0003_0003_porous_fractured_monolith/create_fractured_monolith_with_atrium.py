# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The function `create_fractured_monolith_with_atrium` generates an architectural concept model based on the metaphor "Porous fractured monolith." It begins by establishing a cohesive monolithic structure, defined by specified dimensions. A central atrium is created as a void, symbolizing openness within the solid form. The function then introduces irregular fissures, varying in size and direction, which evoke movement and complexity. This design emphasizes the contrast between solid mass and voids, facilitating natural light and airflow. The resulting model promotes spatial interaction, discovery, and engagement, effectively embodying the metaphor's themes of strength, permeability, and dynamism."""

#! python 3
function_code = """def create_fractured_monolith_with_atrium(base_length, base_width, base_height, atrium_width, num_fissures, fissure_variability, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Porous fractured monolith' metaphor.

    This function creates a cohesive monolithic form with a central atrium and introduces irregular fissures
    to convey a sense of movement and complexity. The design emphasizes the contrast between the solid monolithic
    mass and the voids, promoting light penetration and spatial interaction.

    Parameters:
    - base_length (float): Length of the monolithic base in meters.
    - base_width (float): Width of the monolithic base in meters.
    - base_height (float): Height of the monolithic base in meters.
    - atrium_width (float): Width of the central atrium in meters.
    - num_fissures (int): Number of fissures to introduce in the monolith.
    - fissure_variability (float): Variability factor for fissure size and orientation.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries representing the monolithic form, atrium, and fissures.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = base_box.ToBrep()

    # Create the central atrium as a void
    atrium_origin = rg.Point3d(base_length / 2 - atrium_width / 2, base_width / 2 - atrium_width / 2, 0)
    atrium_box = rg.Box(rg.Plane.WorldXY, rg.Interval(atrium_origin.X, atrium_origin.X + atrium_width), 
                        rg.Interval(atrium_origin.Y, atrium_origin.Y + atrium_width), rg.Interval(0, base_height))
    atrium_brep = atrium_box.ToBrep()

    # Subtract the atrium from the monolith
    fractured_monolith = rg.Brep.CreateBooleanDifference([monolith_brep], [atrium_brep], 0.01)
    if fractured_monolith:
        monolith_brep = fractured_monolith[0]

    # Generate and subtract fissures
    fissures = []
    for _ in range(num_fissures):
        start_point = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        direction.Unitize()

        fissure_length = random.uniform(base_length * 0.1, base_length * 0.3) * fissure_variability
        end_point = rg.Point3d.Add(start_point, direction * fissure_length)
        
        line = rg.Line(start_point, end_point)
        offset_distance = random.uniform(0.2, 0.5) * fissure_variability
        fissure_box = rg.Box(rg.Plane.WorldXY, 
                             rg.Interval(line.FromX - offset_distance, line.ToX + offset_distance),
                             rg.Interval(line.FromY - offset_distance, line.ToY + offset_distance),
                             rg.Interval(0, base_height))
        fissure_brep = fissure_box.ToBrep()

        fissures.append(fissure_brep)

    for fissure in fissures:
        result = rg.Brep.CreateBooleanDifference([monolith_brep], [fissure], 0.01)
        if result:
            monolith_brep = result[0]

    # Return the final geometries
    return [monolith_brep] + fissures"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith_with_atrium(10.0, 5.0, 8.0, 3.0, 5, 1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith_with_atrium(15.0, 7.0, 10.0, 4.0, 8, 2.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith_with_atrium(12.0, 6.0, 9.0, 3.5, 6, 1.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith_with_atrium(20.0, 10.0, 15.0, 5.0, 10, 2.5, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith_with_atrium(8.0, 4.0, 6.0, 2.0, 3, 1.2, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
