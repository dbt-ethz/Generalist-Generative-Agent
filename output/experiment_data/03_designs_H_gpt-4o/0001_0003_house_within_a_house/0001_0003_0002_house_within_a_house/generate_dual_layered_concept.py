# Created for 0001_0003_house_within_a_house.json

""" Summary:
The function `generate_dual_layered_concept` creates an architectural concept model based on the "House within a house" metaphor. It generates two distinct layers: an inner sanctuary and an outer protective shell, using specified dimensions. The function utilizes random interlocking geometries to symbolize the interaction between spaces, emphasizing the notion of nesting and layering. Parameters such as `offset_factor` and `transparency_contrast` allow for variation in the model's geometry and visual properties, enhancing the spatial relationship between public and private realms. The output consists of Brep objects that visually represent the dual nature of the design."""

#! python 3
function_code = """def generate_dual_layered_concept(inner_size, outer_size, offset_factor, transparency_contrast, seed_value):
    \"""
    Constructs a dual-layered architectural Concept Model based on the 'House within a house' metaphor.
    
    This model illustrates the idea of an inner sanctuary enclosed by an outer protective shell, using 
    interpenetrating geometries and contrasting spatial qualities.

    Parameters:
    - inner_size (tuple of 3 floats): Dimensions (length, width, height) of the inner space in meters.
    - outer_size (tuple of 3 floats): Dimensions (length, width, height) of the outer shell in meters.
    - offset_factor (float): Factor to control the offset of interlocking geometries.
    - transparency_contrast (float): Factor to simulate material transparency contrast.
    - seed_value (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the concept model's geometry.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed_value)

    # Helper function to create a box Brep
    def create_box(center, dimensions):
        length, width, height = dimensions
        corner1 = rg.Point3d(center.X - length / 2, center.Y - width / 2, center.Z - height / 2)
        corner2 = rg.Point3d(center.X + length / 2, center.Y + width / 2, center.Z + height / 2)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(corner1.X, corner2.X), rg.Interval(corner1.Y, corner2.Y), rg.Interval(corner1.Z, corner2.Z))
        return box.ToBrep()

    # Create the inner sanctuary
    inner_center = rg.Point3d(0, 0, 0)
    inner_brep = create_box(inner_center, inner_size)

    # Create the outer shell
    outer_center = rg.Point3d(0, 0, 0)
    outer_brep = create_box(outer_center, outer_size)

    # Define interlocking geometry (e.g., intersecting corridors)
    interlock_length = outer_size[0] * offset_factor
    interlock_width = outer_size[1] * offset_factor
    interlock_height = outer_size[2] * offset_factor
    interlock_center = rg.Point3d(random.uniform(-interlock_length, interlock_length), random.uniform(-interlock_width, interlock_width), random.uniform(-interlock_height, interlock_height))
    interlock_brep = create_box(interlock_center, (interlock_length, interlock_width, interlock_height))

    # Perform boolean union to integrate interlocking geometries
    outer_with_interlocks = rg.Brep.CreateBooleanUnion([outer_brep, interlock_brep], 0.01)
    if outer_with_interlocks:
        outer_brep = outer_with_interlocks[0]

    # Adjust transparency or other visual properties if necessary (not represented in geometry)
    # This can be simulated by different geometry layers or materials in a real application

    # Return the breps representing the dual-layered concept
    return [inner_brep, outer_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_dual_layered_concept((5.0, 5.0, 3.0), (10.0, 10.0, 6.0), 0.2, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_dual_layered_concept((3.0, 4.0, 2.0), (8.0, 9.0, 5.0), 0.3, 0.7, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_dual_layered_concept((6.0, 6.0, 4.0), (12.0, 12.0, 8.0), 0.25, 0.6, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_dual_layered_concept((4.0, 4.0, 2.5), (9.0, 9.0, 5.5), 0.15, 0.4, 77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_dual_layered_concept((7.0, 8.0, 5.0), (14.0, 16.0, 10.0), 0.1, 0.3, 33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
