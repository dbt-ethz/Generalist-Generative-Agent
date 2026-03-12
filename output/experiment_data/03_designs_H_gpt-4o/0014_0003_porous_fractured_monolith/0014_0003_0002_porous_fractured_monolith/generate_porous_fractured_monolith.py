# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Porous fractured monolith" by creating a cohesive monolithic structure that is intentionally interrupted by irregular fissures. These fissures introduce complexity and permeability, reflecting the metaphor's themes of solidity and openness. Through specified parameters, the function constructs a solid base and adds varying fissures, which serve as conduits for light and airflow, enhancing spatial interaction. The model visually represents the dynamic interplay between the robust mass and the fragmented voids, encouraging exploration and engagement within the architectural space, thereby fulfilling the design task's requirements."""

#! python 3
function_code = """def generate_porous_fractured_monolith(base_length, base_width, base_height, num_fissures, fissure_variation, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Porous fractured monolith' metaphor.

    This function generates a cohesive monolithic base with irregular fissures to introduce
    permeability and complexity. The fissures are designed to create visual and physical connections,
    allowing light and air to penetrate the monolith, enhancing exploration and interaction.

    Parameters:
    - base_length (float): Length of the monolithic base in meters.
    - base_width (float): Width of the monolithic base in meters.
    - base_height (float): Height of the monolithic base in meters.
    - num_fissures (int): Number of fissures to create.
    - fissure_variation (float): Variation range for fissure size and orientation.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the monolithic form and its voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize random seed
    random.seed(seed)

    # Create the base monolith
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = base_box.ToBrep()

    fissures = []
    for _ in range(num_fissures):
        # Randomly select start and end points for fissure
        start_x = random.uniform(0, base_length)
        start_y = random.uniform(0, base_width)
        start_z = random.uniform(0, base_height)
        
        end_x = start_x + random.uniform(-fissure_variation, fissure_variation)
        end_y = start_y + random.uniform(-fissure_variation, fissure_variation)
        end_z = start_z + random.uniform(-fissure_variation, fissure_variation)

        # Create fissure line and its extrusion
        fissure_line = rg.Line(rg.Point3d(start_x, start_y, start_z), rg.Point3d(end_x, end_y, end_z))
        fissure_dir = rg.Vector3d(end_x - start_x, end_y - start_y, end_z - start_z)
        fissure_dir.Unitize()
        
        # Create a perpendicular plane to use as a cutting surface
        perpendicular_dir = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        perpendicular_dir = rg.Vector3d.CrossProduct(fissure_dir, perpendicular_dir)
        fissure_plane = rg.Plane(fissure_line.PointAt(0.5), perpendicular_dir)
        
        # Create a surface for the fissure
        fissure_surface = rg.Surface.CreateExtrusion(fissure_line.ToNurbsCurve(), perpendicular_dir)
        fissure_brep = fissure_surface.ToBrep()

        fissures.append(fissure_brep)
    
    # Subtract fissures from the monolith
    fractured_monolith = monolith_brep
    for fissure in fissures:
        result = rg.Brep.CreateBooleanDifference([fractured_monolith], [fissure], 0.01)
        if result:
            fractured_monolith = result[0]

    return [fractured_monolith] + fissures"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_porous_fractured_monolith(5.0, 3.0, 2.0, 10, 0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_porous_fractured_monolith(4.0, 2.5, 3.0, 15, 0.7, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_porous_fractured_monolith(6.0, 4.0, 3.5, 20, 1.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_porous_fractured_monolith(7.0, 5.0, 4.0, 12, 0.3, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_porous_fractured_monolith(8.0, 6.0, 5.0, 25, 0.8, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
