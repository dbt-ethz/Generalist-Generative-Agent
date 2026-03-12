# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_fractured_monolith_with_cylindrical_voids` generates an architectural concept model that embodies the metaphor of a "Porous fractured monolith." It creates a solid block representing the monolithic form and introduces randomly placed cylindrical voids to convey permeability and fragmentation. By strategically positioning these voids, the function enhances the interplay of light and shadow, fostering dynamic spatial relationships. The voids promote connectivity between interior and exterior spaces, embodying the metaphor's duality of solidity and openness. This results in a visually engaging structure that encourages exploration and interaction, aligning with the design task's objectives."""

#! python 3
function_code = """def create_fractured_monolith_with_cylindrical_voids(base_length, base_width, base_height, void_radius, num_voids, seed):
    \"""
    Creates an architectural Concept Model embodying the 'Porous fractured monolith' metaphor.
    
    This function generates a monolithic block with cylindrical voids that penetrate the structure, enhancing light, shadow, and spatial dynamics.

    Parameters:
    - base_length (float): The length of the monolithic block in meters.
    - base_width (float): The width of the monolithic block in meters.
    - base_height (float): The height of the monolithic block in meters.
    - void_radius (float): The radius of the cylindrical voids.
    - num_voids (int): The number of cylindrical voids to create.
    - seed (int): The seed for the random number generator to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the main solid and voids.
    \"""
    import Rhino.Geometry as rg
    import random
    import Rhino

    # Set the random seed
    random.seed(seed)

    # Create the base monolithic block
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []

    # Create cylindrical voids
    for _ in range(num_voids):
        # Randomly define the start and end points of the cylinder
        start_x = random.uniform(0, base_length)
        start_y = random.uniform(0, base_width)
        start_z = random.uniform(0, base_height)

        end_x = random.uniform(0, base_length)
        end_y = random.uniform(0, base_width)
        end_z = random.uniform(0, base_height)

        start_point = rg.Point3d(start_x, start_y, start_z)
        end_point = rg.Point3d(end_x, end_y, end_z)
        direction = end_point - start_point
        direction.Unitize()

        # Create the cylinder
        cylinder = rg.Cylinder(rg.Circle(rg.Plane(start_point, direction), void_radius), (end_point - start_point).Length)
        cylinder_brep = cylinder.ToBrep(True, True)

        # Subtract the cylindrical void from the base block
        if cylinder_brep:
            difference = rg.Brep.CreateBooleanDifference([base_brep], [cylinder_brep], Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance)
            if difference:
                base_brep = difference[0]
            voids.append(cylinder_brep)

    return [base_brep] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith_with_cylindrical_voids(5.0, 3.0, 4.0, 0.5, 10, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith_with_cylindrical_voids(8.0, 6.0, 5.0, 0.3, 15, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith_with_cylindrical_voids(10.0, 7.0, 3.0, 0.4, 8, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith_with_cylindrical_voids(4.0, 2.5, 6.0, 0.6, 12, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith_with_cylindrical_voids(6.0, 4.0, 5.0, 0.2, 20, 77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
