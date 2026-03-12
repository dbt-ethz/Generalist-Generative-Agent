# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model inspired by the metaphor "Suspended intersecting assembly." It creates a dynamic arrangement of intersecting cables and translucent membrane surfaces, embodying a sense of lightness and fluidity. By utilizing random points and directions, the function simulates the floating elements, enhancing the spatial relationships and interconnectivity implied by the metaphor. The resulting geometries represent the delicate balance and play with gravity, while the inclusion of multiple configurations allows for diverse interpretations of movement and transparency, aligning with the design task's emphasis on engaging pathways and visual connections."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_cables=7, num_membranes=4, cable_length=10.0, membrane_radius=2.0, seed=24):
    \"""
    Creates an architectural Concept Model based on the 'Suspended intersecting assembly' metaphor.

    This function generates a series of intersecting cables and circular membrane surfaces that suggest
    movement and fluidity. The cables represent tensioned wires, while the membranes are lightweight
    translucent surfaces arranged to create a complex web of connections, enhancing the sense of 
    suspension and interconnectivity.

    Parameters:
    - num_cables (int): The number of intersecting cables to create.
    - num_membranes (int): The number of circular membrane surfaces to create.
    - cable_length (float): The length of each cable in meters.
    - membrane_radius (float): The radius of each circular membrane surface in meters.
    - seed (int): The seed for random number generation to ensure replicable results.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Breps representing the created cables and membrane surfaces.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Function to generate a random point within a specified range
    def random_point(range_x, range_y, range_z):
        return rg.Point3d(
            random.uniform(*range_x),
            random.uniform(*range_y),
            random.uniform(*range_z)
        )

    # Generate cables
    cables = []
    range_x = (0, 10)
    range_y = (0, 10)
    range_z = (0, 10)
    
    for _ in range(num_cables):
        start_pt = random_point(range_x, range_y, range_z)
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        direction.Unitize()
        end_pt = start_pt + direction * cable_length
        line_curve = rg.LineCurve(start_pt, end_pt)
        cables.append(line_curve)  # Directly append the LineCurve

    # Generate membranes
    membranes = []
    for _ in range(num_membranes):
        center_pt = random_point(range_x, range_y, range_z)
        normal = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        normal.Unitize()
        circle = rg.Circle(rg.Plane(center_pt, normal), membrane_radius)
        membrane_surface = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]
        membranes.append(membrane_surface)

    # Combine all geometries into a single list
    geometries = cables + membranes

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_cables=5, num_membranes=3, cable_length=15.0, membrane_radius=3.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_cables=10, num_membranes=6, cable_length=12.0, membrane_radius=2.5, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_cables=8, num_membranes=5, cable_length=20.0, membrane_radius=4.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_cables=12, num_membranes=8, cable_length=18.0, membrane_radius=2.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_cables=6, num_membranes=7, cable_length=14.0, membrane_radius=2.2, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
