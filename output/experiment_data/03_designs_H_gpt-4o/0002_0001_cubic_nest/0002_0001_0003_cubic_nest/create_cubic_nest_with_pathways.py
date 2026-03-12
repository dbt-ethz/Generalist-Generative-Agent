# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic nest" metaphor by creating interlocking and overlapping cubic volumes. Each cube is scaled randomly to enhance diversity, simulating the metaphor's layered and protective qualities. The function emphasizes the spatial interplay of solid and void by introducing pathways between cubes, encouraging exploration. By adjusting the cubes' positions with random translations, the function maintains distinct identities for each volume while ensuring cohesive integration. The varying scales and orientations reflect the interconnectedness inherent in the metaphor, resulting in a complex, dynamic structure that evokes shelter and discovery."""

#! python 3
function_code = """def create_cubic_nest_with_pathways(base_cube_size, num_cubes, pathway_width, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Cubic nest' metaphor with defined pathways.

    This function generates a series of interlocking and overlapping cubic volumes, emphasizing
    spatial interplay of solid and void, and introduces pathways to enhance exploration. Each cube
    maintains its identity while contributing to the protective and layered qualities of the structure.

    Parameters:
    - base_cube_size: float, the size of the base cube in meters.
    - num_cubes: int, the number of cubes to generate.
    - pathway_width: float, the width of the pathways between cubes.
    - seed: int, seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the cubic nest model with pathways.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    breps = []
    pathway_vector = rg.Vector3d(pathway_width, pathway_width, 0)

    for i in range(num_cubes):
        # Randomly choose a scale for each cube
        scale_factor = random.uniform(0.5, 1.5)
        cube_size = base_cube_size * scale_factor

        # Create a base cube
        base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))

        # Define a random positioning to simulate pathways
        offset_x = pathway_vector.X * (i % 2) # Alternate positioning for pathway
        offset_y = pathway_vector.Y * ((i + 1) % 2)
        offset_z = random.uniform(-cube_size / 2, cube_size / 2)

        # Move the cube
        translation = rg.Transform.Translation(offset_x, offset_y, offset_z)
        base_cube.Transform(translation)

        # Convert the box to a Brep and add to the list
        brep_cube = base_cube.ToBrep()
        breps.append(brep_cube)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_with_pathways(base_cube_size=2.0, num_cubes=5, pathway_width=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_with_pathways(base_cube_size=1.5, num_cubes=10, pathway_width=0.3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_with_pathways(base_cube_size=3.0, num_cubes=8, pathway_width=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_with_pathways(base_cube_size=2.5, num_cubes=6, pathway_width=0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_with_pathways(base_cube_size=4.0, num_cubes=12, pathway_width=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
