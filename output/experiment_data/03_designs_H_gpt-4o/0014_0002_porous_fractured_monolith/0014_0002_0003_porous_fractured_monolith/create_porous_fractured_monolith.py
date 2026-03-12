# Created for 0014_0002_porous_fractured_monolith.json

""" Summary:
The provided function `create_porous_fractured_monolith` generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It starts by creating a solid base form, simulating a unified mass. The function introduces a series of voids cylindrical and conical shapes randomly positioned and sized to emphasize the fractured quality of the design. These voids penetrate deeply into the monolith, allowing for light penetration and airflow, which fosters interaction between spaces. The resulting geometries reflect a strong, cohesive mass interspersed with dynamic voids, capturing the metaphor's essence of complexity and connectivity in spatial design."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length=30, base_width=20, base_height=10, num_voids=5, seed=42):
    \"""
    Creates a conceptual architectural model of a 'Porous fractured monolith'.
    
    This function generates a monolithic form and introduces a series of deeply penetrating voids,
    using cylindrical and conical shapes to create varied spatial experiences. The voids are aligned
    to promote vertical and horizontal connectivity, emphasizing light penetration and airflow.
    
    Parameters:
        base_length (float): Length of the base monolith in meters.
        base_width (float): Width of the base monolith in meters.
        base_height (float): Height of the base monolith in meters.
        num_voids (int): Number of voids to create within the monolith.
        seed (int): Seed for randomness to ensure replicability.
    
    Returns:
        List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the monolithic form with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()
    
    voids = []
    
    # Generate voids using cylindrical and conical shapes
    for _ in range(num_voids):
        # Randomly determine the size and position of the cylindrical voids
        void_radius = random.uniform(0.1, 0.3) * min(base_length, base_width)
        void_height = base_height * random.uniform(0.5, 1.0)
        
        center_x = random.uniform(void_radius, base_length - void_radius)
        center_y = random.uniform(void_radius, base_width - void_radius)
        center_z = random.uniform(0, base_height - void_height)
        
        # Create a cylindrical void
        cylinder = rg.Cylinder(rg.Circle(rg.Plane(rg.Point3d(center_x, center_y, center_z), rg.Vector3d.ZAxis), void_radius), void_height)
        voids.append(cylinder.ToBrep(True, True))
        
        # Create a conical void
        cone_radius = void_radius * random.uniform(0.5, 1.0)
        cone_height = base_height * random.uniform(0.3, 0.7)
        cone_center_z = random.uniform(0, base_height - cone_height)
        cone = rg.Cone(rg.Plane(rg.Point3d(center_x, center_y, cone_center_z), rg.Vector3d.ZAxis), cone_height, cone_radius)
        voids.append(cone.ToBrep(True))
    
    # Subtract the voids from the base form
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
    geometry = create_porous_fractured_monolith(base_length=40, base_width=25, base_height=15, num_voids=10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(base_length=50, base_width=30, base_height=20, num_voids=7, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(base_length=35, base_width=22, base_height=12, num_voids=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(base_length=45, base_width=35, base_height=18, num_voids=8, seed=72)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(base_length=60, base_width=40, base_height=25, num_voids=12, seed=88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
