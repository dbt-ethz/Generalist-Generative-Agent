# Created for 0001_0003_house_within_a_house.json

""" Summary:
The provided function, `create_conceptual_house_within_house`, generates an architectural concept model based on the "House within a house" metaphor by creating a dual-layered structure. It takes dimensions for inner and outer volumes, constructing a protective outer shell that encapsulates an intimate inner sanctuary. The function includes a transition element like a ramp to emphasize movement between spaces, fostering dynamic spatial relationships. By utilizing Boolean operations, it ensures a cohesive design that visually and physically connects layers, embodying the metaphor's duality of public and private realms while allowing for varied spatial experiences and discovery within the nested layers."""

#! python 3
function_code = """def create_conceptual_house_within_house(inner_dims, outer_dims, transition_height, randomness_seed=42):
    \"""
    Constructs an architectural Concept Model based on the 'House within a house' metaphor.

    This function creates a dual-layered structure with distinct interconnected volumes, embodying the concept of an inner sanctuary enclosed by an outer protective form. The model includes transitions to emphasize movement and discovery between layers.

    Parameters:
    - inner_dims: Tuple of 3 floats (length, width, height) for the inner volume dimensions in meters.
    - outer_dims: Tuple of 3 floats (length, width, height) for the outer volume dimensions in meters.
    - transition_height: Float indicating the height of the transition element (e.g., ramp or staircase).
    - randomness_seed: Integer seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)

    def create_box(center, dimensions):
        \"""Helper function to create a box Brep given a center point and dimensions.\"""
        length, width, height = dimensions
        corner1 = rg.Point3d(center.X - length / 2, center.Y - width / 2, center.Z)
        corner2 = rg.Point3d(center.X + length / 2, center.Y + width / 2, center.Z + height)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(corner1.X, corner2.X), rg.Interval(corner1.Y, corner2.Y), rg.Interval(corner1.Z, corner2.Z))
        return box.ToBrep()

    # Create inner sanctuary volume
    inner_center = rg.Point3d(0, 0, 0)
    inner_brep = create_box(inner_center, inner_dims)

    # Create outer protective volume
    outer_center = rg.Point3d(0, 0, 0)
    outer_brep = create_box(outer_center, outer_dims)

    # Subtract inner from outer to create a hollow protective form
    hollow_outer_brep = rg.Brep.CreateBooleanDifference([outer_brep], [inner_brep], 0.01)
    if not hollow_outer_brep or len(hollow_outer_brep) == 0:
        hollow_outer_brep = [outer_brep]  # Fallback in case of failed boolean operation

    # Create a transition element (e.g., ramp)
    ramp_length = random.uniform(inner_dims[0] * 0.3, inner_dims[0] * 0.5)
    ramp_width = inner_dims[1] * 0.2
    ramp_height = transition_height

    ramp_base_center = rg.Point3d(inner_dims[0] / 2 - ramp_length / 2, -inner_dims[1] / 2 + ramp_width / 2, 0)
    ramp_box = rg.Box(rg.Plane.WorldXY, rg.Interval(ramp_base_center.X - ramp_length / 2, ramp_base_center.X + ramp_length / 2),
                      rg.Interval(ramp_base_center.Y - ramp_width / 2, ramp_base_center.Y + ramp_width / 2),
                      rg.Interval(0, ramp_height))
    ramp_brep = ramp_box.ToBrep()

    # Collect geometries
    geometries = list(hollow_outer_brep) + [inner_brep, ramp_brep]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_conceptual_house_within_house((5.0, 3.0, 3.0), (7.0, 5.0, 5.0), 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_conceptual_house_within_house((4.0, 2.0, 2.5), (6.0, 4.0, 4.5), 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_conceptual_house_within_house((6.0, 4.0, 3.5), (8.0, 6.0, 6.0), 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_conceptual_house_within_house((3.5, 2.5, 2.0), (5.5, 4.5, 4.0), 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_conceptual_house_within_house((10.0, 8.0, 6.0), (12.0, 10.0, 8.0), 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
