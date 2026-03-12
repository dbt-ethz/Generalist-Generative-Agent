# Created for 0002_0003_cubic_nest.json

""" Summary:
The provided function, `generate_cubic_nest_with_ramps`, creates a 3D architectural model inspired by the "Cubic nest" metaphor. It generates a series of interconnected cubic volumes, each representing a distinct module while forming a cohesive structure. The function incorporates randomness in the arrangement and orientation of cubes, enhancing the sense of enclosure and openness. Ramps are added between cubes to facilitate movement, promoting exploration within the nested configuration. By varying cube sizes and ramp widths, it highlights the interplay of solid and void, fostering a dynamic spatial experience that embodies the protective, interconnected qualities of the metaphor."""

#! python 3
function_code = """def generate_cubic_nest_with_ramps(base_size, cube_count, ramp_width, randomness_seed=42):
    \"""
    Generates a 3D architectural concept model based on the 'Cubic nest' metaphor, incorporating ramps for movement between cubes.
    
    Parameters:
        base_size (float): The base size of each cubic module in meters.
        cube_count (int): The number of cubes to generate in the model.
        ramp_width (float): The width of the ramps connecting the cubes.
        randomness_seed (int, optional): Seed for random number generator to ensure replicability. Default is 42.
    
    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D geometry of the model, including cubes and ramps.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize the random seed
    random.seed(randomness_seed)

    # Initialize the list to hold the resulting Breps
    model_breps = []

    # Start position for the first cube
    current_pos = rg.Point3d(0, 0, 0)

    # Create cubes and ramps in a nested pattern
    for i in range(cube_count):
        # Create a cube at the current position
        cube = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(current_pos.X, current_pos.X + base_size),
            rg.Interval(current_pos.Y, current_pos.Y + base_size),
            rg.Interval(current_pos.Z, current_pos.Z + base_size)
        )
        model_breps.append(cube.ToBrep())

        # Determine the direction for the next cube
        direction_choice = random.choice(['x', 'y', 'z'])
        if direction_choice == 'x':
            next_pos = rg.Point3d(current_pos.X + base_size * 1.5, current_pos.Y, current_pos.Z)
            ramp_start = rg.Point3d(current_pos.X + base_size, current_pos.Y + base_size / 2, current_pos.Z + base_size / 2)
            ramp_end = rg.Point3d(next_pos.X, next_pos.Y + base_size / 2, next_pos.Z + base_size / 2)
        elif direction_choice == 'y':
            next_pos = rg.Point3d(current_pos.X, current_pos.Y + base_size * 1.5, current_pos.Z)
            ramp_start = rg.Point3d(current_pos.X + base_size / 2, current_pos.Y + base_size, current_pos.Z + base_size / 2)
            ramp_end = rg.Point3d(next_pos.X + base_size / 2, next_pos.Y, next_pos.Z + base_size / 2)
        else:
            next_pos = rg.Point3d(current_pos.X, current_pos.Y, current_pos.Z + base_size * 1.5)
            ramp_start = rg.Point3d(current_pos.X + base_size / 2, current_pos.Y + base_size / 2, current_pos.Z + base_size)
            ramp_end = rg.Point3d(next_pos.X + base_size / 2, next_pos.Y + base_size / 2, next_pos.Z)

        # Create a ramp connecting this cube to the next
        ramp_curve = rg.Line(ramp_start, ramp_end).ToNurbsCurve()
        ramp = rg.Extrusion.Create(ramp_curve, ramp_width, True)
        if ramp:
            model_breps.append(ramp.ToBrep())

        # Update current position to the next position
        current_pos = next_pos

    return model_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_with_ramps(2.0, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_with_ramps(1.5, 10, 0.3, randomness_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_with_ramps(3.0, 8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_with_ramps(2.5, 6, 0.6, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_with_ramps(4.0, 3, 0.2, randomness_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
