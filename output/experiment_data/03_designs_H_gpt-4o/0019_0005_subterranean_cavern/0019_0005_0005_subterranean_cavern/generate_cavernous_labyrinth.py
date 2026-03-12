# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The function `generate_cavernous_labyrinth` creates an architectural concept model inspired by the metaphor of a subterranean cavern. It generates a series of interlocking geometric volumes, alternating between angular and organic forms to reflect the rugged and fluid characteristics of natural caves. By incorporating varying heights, widths, and strategic openings, the model simulates the interplay of light and shadow, enhancing the immersive experience. The design features narrow corridors leading to expansive chambers, embodying the exploration and surprise intrinsic to caverns. This approach results in a complex, maze-like structure that evokes a sense of mystery and refuge."""

#! python 3
function_code = """def generate_cavernous_labyrinth(base_size, height_range, corridor_width, chamber_radius, num_elements, seed=1):
    \"""
    Generates an architectural Concept Model inspired by the metaphor of a subterranean cavern.

    This function constructs a complex, maze-like structure using interlocking volumes inspired by
    natural cave formations. It integrates angular forms with organic curves and strategically placed
    voids to simulate the interplay of light and shadow, enhancing exploration and surprise.

    Parameters:
    - base_size (float): The base area dimension for the overall model footprint in meters.
    - height_range (tuple): A tuple defining min and max height variation for the volumes in meters.
    - corridor_width (float): The width of the corridors connecting spaces in meters.
    - chamber_radius (float): The average radius of the larger chambers in meters.
    - num_elements (int): The number of geometric elements to create.
    - seed (int): Random seed for reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create interlocking volumes with varying forms
    for _ in range(num_elements):
        # Determine if the current form is angular or organic
        is_angular = random.choice([True, False])

        # Random dimensions and position
        length = random.uniform(base_size * 0.1, base_size * 0.3)
        width = random.uniform(base_size * 0.1, base_size * 0.3)
        height = random.uniform(*height_range)
        x_offset = random.uniform(0, base_size - length)
        y_offset = random.uniform(0, base_size - width)

        if is_angular:
            # Create a faceted, angular volume
            box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(x_offset, x_offset + length),
                rg.Interval(y_offset, y_offset + width),
                rg.Interval(0, height)
            )
            geometries.append(box.ToBrep())
        else:
            # Create a smooth, organic chamber
            center = rg.Point3d(x_offset + length / 2, y_offset + width / 2, height / 2)
            sphere = rg.Sphere(center, chamber_radius)
            geometries.append(sphere.ToBrep())

    # Add corridors to connect volumes
    for i in range(num_elements - 1):
        corridor_length = random.uniform(corridor_width * 2, corridor_width * 4)
        x_offset = random.uniform(0, base_size - corridor_length)
        y_offset = random.uniform(0, base_size - corridor_width)
        corridor_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(x_offset, x_offset + corridor_length),
            rg.Interval(y_offset, y_offset + corridor_width),
            rg.Interval(0, random.uniform(*height_range) * 0.5)
        )
        geometries.append(corridor_box.ToBrep())

    # Apply strategic openings to enhance light and shadow effects
    for geom in geometries[:]:
        if isinstance(geom, rg.Brep):
            gap_size = random.uniform(0.5, 1.5)
            opening = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(-gap_size / 2, gap_size / 2),
                rg.Interval(-gap_size / 2, gap_size / 2),
                rg.Interval(0, gap_size)
            ).ToBrep()

            boolean_difference = rg.Brep.CreateBooleanDifference([geom], [opening], 0.001)
            if boolean_difference:
                geometries.append(boolean_difference[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cavernous_labyrinth(50.0, (10.0, 20.0), 3.0, 5.0, 10, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cavernous_labyrinth(30.0, (5.0, 15.0), 2.5, 4.0, 15, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cavernous_labyrinth(40.0, (8.0, 18.0), 2.0, 6.0, 12, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cavernous_labyrinth(60.0, (12.0, 22.0), 4.0, 7.0, 8, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cavernous_labyrinth(45.0, (5.0, 25.0), 3.5, 4.5, 20, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
