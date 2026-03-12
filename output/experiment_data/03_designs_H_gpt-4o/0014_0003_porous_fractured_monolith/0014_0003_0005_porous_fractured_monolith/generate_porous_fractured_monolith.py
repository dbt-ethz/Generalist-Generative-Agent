# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The function `generate_porous_fractured_monolith` creates an architectural concept model inspired by the metaphor "Porous fractured monolith." It begins by generating a solid box representing the monolithic form. The function then introduces irregular fissures, varying in shape and size, which disrupt the solid mass, creating a dynamic interplay between solidity and openness. This design fosters visual and physical connections, allowing natural light and airflow to penetrate the structure. The resulting model emphasizes exploration and interaction, with voids acting as transitional spaces that invite engagement, embodying both strength and permeability as described in the metaphor."""

#! python 3
function_code = """def generate_porous_fractured_monolith(length, width, height, num_fissures, fissure_variation, seed=42):
    \"""
    Generates a conceptual architectural model based on the 'Porous fractured monolith' metaphor.

    This function constructs a monolithic form disrupted by a series of irregular fissures, creating a balance
    between solidity and openness. The fissures are varied in shape and size, allowing for visual and physical
    connections within the structure, enhancing exploration and interaction.

    Parameters:
    - length (float): Length of the monolith in meters.
    - width (float): Width of the monolith in meters.
    - height (float): Height of the monolith in meters.
    - num_fissures (int): Number of fissures to introduce.
    - fissure_variation (float): Controls the variation in fissure size and depth.
    - seed (int, optional): Seed for random number generation to ensure replicability.

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    # Create the base monolithic form as a solid box
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    monolith_brep = base_box.ToBrep()

    # Create fissures
    fissures = []
    for _ in range(num_fissures):
        # Randomly generate start and end points for fissure lines
        start_point = rg.Point3d(random.uniform(0, length), random.uniform(0, width), random.uniform(0, height))
        end_point = rg.Point3d(random.uniform(0, length), random.uniform(0, width), random.uniform(0, height))
        # Create a fissure line
        fissure_line = rg.Line(start_point, end_point)
        
        # Create a variation in the size of the fissure
        fissure_depth = random.uniform(fissure_variation * 0.5, fissure_variation)
        fissure_width = random.uniform(fissure_variation * 0.5, fissure_variation)
        
        # Create a narrow box along the fissure line to represent the fissure
        fissure_box = rg.Box(rg.Plane(fissure_line.From, rg.Vector3d.ZAxis),
                             rg.Interval(-fissure_width / 2, fissure_width / 2),
                             rg.Interval(-fissure_depth / 2, fissure_depth / 2),
                             rg.Interval(0, fissure_line.Length))
        fissure_brep = fissure_box.ToBrep()
        
        # Store the fissure geometry
        fissures.append(fissure_brep)

    # Subtract fissures from the monolith
    fractured_monolith = monolith_brep
    for fissure in fissures:
        difference_result = rg.Brep.CreateBooleanDifference([fractured_monolith], [fissure], 0.01)
        if difference_result:
            fractured_monolith = difference_result[0]

    # Return the final geometries: fractured monolith and the fissures
    return [fractured_monolith] + fissures"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_porous_fractured_monolith(10.0, 5.0, 15.0, 8, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_porous_fractured_monolith(12.0, 6.0, 20.0, 10, 3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_porous_fractured_monolith(8.0, 4.0, 12.0, 5, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_porous_fractured_monolith(15.0, 7.0, 25.0, 12, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_porous_fractured_monolith(9.0, 4.5, 14.0, 6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
