# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith_v2` generates an architectural concept model based on the metaphor "Porous fractured monolith" by creating a robust monolithic structure and strategically carving cylindrical voids. The function begins by defining the dimensions of the monolith and then randomly generates voids characterized by varying sizes and heights, reflecting the metaphor's complexity and dynamism. The contrast between the solid mass and the carved voids symbolizes both permanence and fluidity, enhancing natural light and ventilation. This design approach encourages interaction and connectivity between spaces, embodying the metaphor's duality of solidity and openness, while promoting exploration within the architectural framework."""

#! python 3
function_code = """def create_porous_fractured_monolith_v2(base_length, base_width, base_height, num_voids, void_radius_range, seed=42):
    \"""
    Create an architectural Concept Model based on the metaphor 'Porous fractured monolith'. 
    This version employs cylindrical voids to enhance the sense of fluidity and movement.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - num_voids (int): The number of cylindrical voids to carve out from the base.
    - void_radius_range (tuple): A tuple (min_radius, max_radius) defining the range for the radii of voids.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for replicability
    random.seed(seed)
    
    # Create the main monolithic block
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_length, 0, base_height),
        rg.Point3d(base_length, base_width, base_height),
        rg.Point3d(0, base_width, base_height)
    ]
    monolith_brep = rg.Brep.CreateFromBox(base_corners)
    
    voids = []
    
    # Create cylindrical voids
    for _ in range(num_voids):
        # Randomly generate cylinder dimensions
        radius = random.uniform(*void_radius_range)
        height = random.uniform(base_height * 0.2, base_height * 0.8)
        
        # Randomly position the cylinder within the base volume
        x = random.uniform(radius, base_length - radius)
        y = random.uniform(radius, base_width - radius)
        z = random.uniform(0, base_height - height)
        
        base_circle = rg.Circle(rg.Point3d(x, y, z), radius)
        axis = rg.Line(base_circle.Center, rg.Point3d(x, y, z + height))
        cylinder = rg.Cylinder(base_circle, axis.Length)
        void_brep = cylinder.ToBrep(True, True)
        voids.append(void_brep)
    
    # Subtract voids from the monolithic brep
    result_brep = monolith_brep
    for void in voids:
        result = rg.Brep.CreateBooleanDifference(result_brep, void, 0.001)
        if result:  # Check if the result is not empty
            result_brep = result[0]
    
    return [result_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith_v2(10.0, 5.0, 3.0, 8, (0.2, 0.5), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith_v2(15.0, 7.0, 4.0, 10, (0.3, 0.6), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith_v2(12.0, 6.0, 5.0, 15, (0.1, 0.4), seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith_v2(8.0, 4.0, 2.5, 5, (0.15, 0.35), seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith_v2(20.0, 10.0, 6.0, 12, (0.25, 0.75), seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
