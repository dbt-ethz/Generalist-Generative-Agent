# Created for 0001_0003_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating two distinct yet interconnected layers. The function defines the dimensions for both the inner sanctuary and the protective outer shell, emphasizing their spatial relationship. It includes transitional elements like stairs to facilitate movement between layers, reinforcing the duality theme. The inner volume is positioned within the outer volume using a random transformation to simulate nesting. As a result, the model showcases complex interactions between public and private spaces, aligning with the metaphor's implications of refuge and layered spatial hierarchy."""

#! python 3
function_code = """def create_dual_layered_concept_model(inner_dims, outer_dims, transition_height, seed=123):
    \"""
    Constructs a dual-layered architectural Concept Model based on the 'House within a house' metaphor.

    This model features an inner sanctuary encapsulated by an outer protective shell, with vertical transitions
    emphasizing movement and discovery. The design highlights duality, privacy, and spatial interrelations.

    Parameters:
    - inner_dims: Tuple of 3 floats (length, width, height) for the inner sanctuary's dimensions in meters.
    - outer_dims: Tuple of 3 floats (length, width, height) for the outer shell's dimensions in meters.
    - transition_height: Float indicating the height of vertical transitions (e.g., staircases) in meters.
    - seed: Integer for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the conceptual model's geometric entities.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Define the inner sanctuary volume
    inner_length, inner_width, inner_height = inner_dims
    inner_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(0, inner_length),
        rg.Interval(0, inner_width),
        rg.Interval(0, inner_height)
    )
    inner_brep = inner_box.ToBrep()

    # Define the outer protective shell
    outer_length, outer_width, outer_height = outer_dims
    outer_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(0, outer_length),
        rg.Interval(0, outer_width),
        rg.Interval(0, outer_height)
    )
    outer_brep = outer_box.ToBrep()

    # Create a transitional element such as a staircase or ramp
    stair_length = inner_length * 0.4
    stair_width = inner_width * 0.2
    stair_steps = 5
    stair_step_height = transition_height / stair_steps

    stairs = []
    for i in range(stair_steps):
        step_plane = rg.Plane(rg.Point3d(inner_length * 0.1, inner_width * 0.1, i * stair_step_height), rg.Vector3d.ZAxis)
        step_box = rg.Box(
            step_plane,
            rg.Interval(0, stair_length),
            rg.Interval(0, stair_width),
            rg.Interval(0, stair_step_height)
        )
        stairs.append(step_box.ToBrep())

    # Interlock volumes by shifting the inner sanctuary within the outer shell
    interlock_vector = rg.Vector3d(
        random.uniform(-outer_length * 0.1, outer_length * 0.1),
        random.uniform(-outer_width * 0.1, outer_width * 0.1),
        random.uniform(0, outer_height * 0.1)
    )
    interlock_transform = rg.Transform.Translation(interlock_vector)
    inner_brep.Transform(interlock_transform)

    # Collect all geometries
    geometries = [outer_brep, inner_brep] + stairs

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dual_layered_concept_model((5.0, 3.0, 4.0), (8.0, 6.0, 6.0), 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dual_layered_concept_model((10.0, 7.0, 5.0), (15.0, 10.0, 8.0), 3.0, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dual_layered_concept_model((4.0, 4.0, 3.0), (9.0, 9.0, 7.0), 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dual_layered_concept_model((6.0, 4.0, 5.0), (12.0, 8.0, 10.0), 4.0, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dual_layered_concept_model((7.0, 5.0, 6.0), (10.0, 8.0, 9.0), 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
