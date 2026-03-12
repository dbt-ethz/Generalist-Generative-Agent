# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_assembly` generates an architectural concept model inspired by the 'Distorted puzzle' metaphor. It assembles a series of fragmented, interconnected volumes with varying heights and asymmetric shapes, simulating a dynamic interplay of light and shadow. By randomly defining the position, dimensions, and distortion of each volume, the function creates a visually complex structure that retains a sense of coherence. The model's arrangement allows for diverse spatial experiences, transitioning between openness and enclosure, thereby capturing the metaphor's essence of tension and equilibrium while emphasizing the unpredictability and interconnectedness of the design."""

#! python 3
function_code = """def create_distorted_puzzle_assembly(base_area, height_range, volume_count, seed):
    \"""
    Generates an architectural Concept Model based on the 'Distorted Puzzle' metaphor.

    This function creates a collection of fragmented, interconnected volumes with varying heights and asymmetric shapes.
    The design aims to evoke a sense of dynamic equilibrium and visual complexity, emphasizing the interplay of light
    and shadow through the use of irregular forms and strategic openings.

    Parameters:
    - base_area (tuple of float): The (width, length) of the base area for the concept model in meters.
    - height_range (tuple of float): The minimum and maximum heights of the volumes in meters.
    - volume_count (int): The number of volumes to generate.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    volumes = []

    base_width, base_length = base_area
    min_height, max_height = height_range

    for _ in range(volume_count):
        # Randomly choose position and dimensions for each volume
        x = random.uniform(0, base_width)
        y = random.uniform(0, base_length)
        width = random.uniform(base_width * 0.1, base_width * 0.3)
        length = random.uniform(base_length * 0.1, base_length * 0.3)
        height = random.uniform(min_height, max_height)

        # Create a base rectangle
        base_plane = rg.Plane(rg.Point3d(x, y, 0), rg.Vector3d.ZAxis)
        rect = rg.Rectangle3d(base_plane, width, length)

        # Define a list of control points for a distorted extrusion
        corners = [rect.Corner(i) for i in range(4)]
        distortion = [(random.uniform(-0.1, 0.1) * width, random.uniform(-0.1, 0.1) * length) for _ in range(4)]
        distorted_corners = [
            rg.Point3d(corners[i].X + distortion[i][0], corners[i].Y + distortion[i][1], 0) for i in range(4)
        ]

        # Create a polyline and loft it to form a distorted surface
        polyline = rg.Polyline(distorted_corners + [distorted_corners[0]])
        loft = rg.Brep.CreateFromLoft([polyline.ToNurbsCurve()], base_plane.Origin, base_plane.Origin + rg.Point3d(0, 0, height), rg.LoftType.Normal, False)

        if loft:
            volumes.append(loft[0])

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_assembly((10, 15), (3, 7), 5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_assembly((8, 12), (2, 10), 7, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_assembly((5, 10), (1, 5), 4, 27)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_assembly((20, 25), (4, 8), 6, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_assembly((15, 20), (5, 12), 10, 13)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
