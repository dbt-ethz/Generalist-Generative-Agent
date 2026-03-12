# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The function `create_porouos_fractured_monolith_model` generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It constructs a solid monolithic block, then introduces irregular fissures that symbolize fragmentation and permeability. These fissures are created with varying depths and widths, adding complexity and a dynamic quality to the structure. The model emphasizes the contrast between solidity and openness, ensuring visual and physical connections between spaces. By manipulating light and airflow through these voids, the design fosters interaction and exploration, aligning with the metaphor's implications of connectivity and organic evolution within the architectural layout."""

#! python 3
function_code = """def create_porouos_fractured_monolith_model(base_length, base_width, base_height, fissure_count, fissure_depth, fissure_width, seed=42):
    \"""
    Creates a 3D architectural concept model based on the metaphor 'Porous fractured monolith'.
    
    The model starts with a solid monolithic block and introduces irregular fissures to create a sense of permeability
    and fragmentation. The fissures provide visual and physical connections through the mass.

    Inputs:
        base_length (float): The length of the base monolithic block in meters.
        base_width (float): The width of the base monolithic block in meters.
        base_height (float): The height of the base monolithic block in meters.
        fissure_count (int): The number of fissures to create in the monolithic block.
        fissure_depth (float): The maximum depth of the fissures in meters.
        fissure_width (float): The maximum width of the fissures in meters.
        seed (int): The seed for random number generation to ensure replicability.

    Outputs:
        A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for random number generation
    random.seed(seed)

    # Create the base monolithic block
    base_origin = rg.Point3d(0, 0, 0)
    base_corners = [
        base_origin,
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_length, 0, base_height),
        rg.Point3d(base_length, base_width, base_height),
        rg.Point3d(0, base_width, base_height)
    ]
    base_box = rg.Brep.CreateFromBox(base_corners)

    # Create fissures (voids) in the monolithic block
    fissures = []
    for _ in range(fissure_count):
        # Randomly generate a starting point, direction, and size for each fissure
        start_x = random.uniform(0, base_length)
        start_y = random.uniform(0, base_width)
        start_z = random.uniform(0, base_height)
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        direction.Unitize()

        # Create a 3D line to represent the fissure
        line = rg.Line(rg.Point3d(start_x, start_y, start_z), direction, fissure_depth)
        # Offset the line to create a fissure width
        plane = rg.Plane(line.From, direction)
        offset_curve = rg.Curve.Offset(line.ToNurbsCurve(), plane, fissure_width / 2, 0.01, rg.CurveOffsetCornerStyle.Sharp)

        # Create a narrow box along the fissure line
        if offset_curve:
            offset_curve = offset_curve[0]  # Take the first offset curve
            fissure_box = rg.Brep.CreateFromSweep(line.ToNurbsCurve(), offset_curve, True, 0.01)
            if fissure_box:
                fissures.append(fissure_box[0])

    # Subtract fissures from the base block
    geom_result = base_box
    for fissure in fissures:
        difference_result = rg.Brep.CreateBooleanDifference([geom_result], [fissure], 0.01)
        if difference_result:
            geom_result = difference_result[0]

    return [geom_result] if geom_result else [base_box]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porouos_fractured_monolith_model(10.0, 5.0, 3.0, 15, 2.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porouos_fractured_monolith_model(8.0, 4.0, 5.0, 10, 1.5, 0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porouos_fractured_monolith_model(12.0, 6.0, 4.0, 20, 3.0, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porouos_fractured_monolith_model(15.0, 7.0, 2.5, 12, 1.0, 0.4, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porouos_fractured_monolith_model(9.0, 5.5, 6.0, 8, 2.5, 0.6, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
