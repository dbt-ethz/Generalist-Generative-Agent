# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The provided function, `create_porous_fractured_monolith_v2`, generates an architectural concept model based on the metaphor "Porous fractured monolith." It begins by creating a solid monolithic form defined by specified dimensions. The function then introduces irregular fissures that represent the fragmented aspect, enhancing the contrast between mass and void. The fissures are generated randomly, varying in shape and direction, which evokes movement and complexity. This design approach allows for dynamic spatial interactions and natural light penetration, ultimately reflecting the metaphor's essence of solidity and openness, while promoting exploration and connectivity within the architectural space."""

#! python 3
function_code = """def create_porous_fractured_monolith_v2(base_length, base_width, base_height, num_fissures, fissure_variability, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Porous fractured monolith' metaphor.

    This model starts with a monolithic block and introduces a series of irregular fissures
    that represent the fractured aspect, enhancing the interplay between solidity and voids.
    The fissure variability controls the randomness of the fissure patterns, influencing 
    the movement and complexity of the form.

    Parameters:
    - base_length (float): The length of the base monolithic form in meters.
    - base_width (float): The width of the base monolithic form in meters.
    - base_height (float): The height of the base monolithic form in meters.
    - num_fissures (int): The number of fissures to introduce.
    - fissure_variability (float): Controls the randomness and scale of fissures.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries including the main mass and the voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = base_box.ToBrep()

    # Function to create a fissure pattern
    def create_fissure_pattern():
        start_pt = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        end_pt = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        direction.Unitize()
        axis = rg.Line(start_pt, end_pt)
        plane = rg.Plane(start_pt, direction)
        scale_factor = random.uniform(0.5, 1.5) * fissure_variability
        width = random.uniform(0.1, scale_factor)
        
        # Use the plane and line to create a fissure
        offset_curve = rg.Curve.Offset(axis.ToNurbsCurve(), plane, width, 0.01, rg.CurveOffsetCornerStyle.Sharp)
        if offset_curve:
            offset_curve = offset_curve[0]
            fissure_brep = rg.Brep.CreateFromSweep(axis.ToNurbsCurve(), offset_curve, True, 0.01)
            if fissure_brep:
                return fissure_brep[0]
        return None

    # List to hold the fissures
    fissures = []

    # Generate fissures
    for _ in range(num_fissures):
        fissure = create_fissure_pattern()
        if fissure:
            fissures.append(fissure)

    # Subtract fissures from the monolith to create voids
    fractured_monolith = monolith_brep
    for fissure in fissures:
        difference_result = rg.Brep.CreateBooleanDifference([fractured_monolith], [fissure], 0.01)
        if difference_result:
            fractured_monolith = difference_result[0]

    # Return the fractured monolith with voids
    return [fractured_monolith] + fissures"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith_v2(10.0, 5.0, 3.0, 15, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith_v2(12.0, 6.0, 4.0, 20, 1.2, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith_v2(8.0, 4.0, 2.0, 10, 0.5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith_v2(15.0, 7.0, 5.0, 25, 1.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith_v2(9.0, 4.5, 3.5, 12, 0.6, seed=78)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
