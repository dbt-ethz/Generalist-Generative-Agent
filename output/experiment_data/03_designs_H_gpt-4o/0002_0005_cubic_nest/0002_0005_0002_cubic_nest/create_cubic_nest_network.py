# Created for 0002_0005_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Cubic nest" metaphor by creating a network of interlaced cubic volumes. It employs a 3D grid system where cubes are placed and categorized as solid, perforated, or void, reflecting the design task's focus on modularity and spatial layering. This arrangement fosters a dynamic, protective framework that emphasizes complexity and interconnectedness, aligning with the metaphor's implications. By manipulating cube types and their arrangements, the model achieves a variety of spatial experiences, inviting exploration while maintaining each cube's distinct identity within the cohesive structure."""

#! python 3
function_code = """def create_cubic_nest_network(cube_size, grid_dim, seed=123):
    \"""
    Create an architectural Concept Model based on the 'Cubic nest' metaphor. This function generates
    a network of interlaced cubic volumes, focusing on the rhythmic arrangement and spatial layering 
    to create a dynamic and protective network.

    Parameters:
    - cube_size (float): The edge length of each cube in meters.
    - grid_dim (int): The dimension of the grid (number of cubes along each axis).
    - seed (int, optional): A seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Define base plane for the cube grid
    base_plane = rg.Plane.WorldXY

    # Iterate over a 3D grid to create cubes
    for x in range(grid_dim):
        for y in range(grid_dim):
            for z in range(grid_dim):
                # Determine the placement of the cube
                base_point = rg.Point3d(x * cube_size, y * cube_size, z * cube_size)
                current_plane = rg.Plane(base_point, rg.Vector3d.ZAxis)

                # Randomly decide if the cube is solid, perforated, or void
                cube_type = random.choice(['solid', 'perforated', 'void'])

                if cube_type == 'solid':
                    # Create a solid cube
                    box = rg.Box(current_plane, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
                    geometries.append(box.ToBrep())
                elif cube_type == 'perforated':
                    # Create a perforated cube by applying a series of small voids
                    box = rg.Box(current_plane, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
                    brep_cube = box.ToBrep()

                    # Define perforation parameters
                    perforation_count = random.randint(1, 3)
                    for _ in range(perforation_count):
                        hole_size = cube_size * random.uniform(0.1, 0.3)
                        hole_origin = rg.Point3d(
                            base_point.X + random.uniform(0, cube_size - hole_size),
                            base_point.Y + random.uniform(0, cube_size - hole_size),
                            base_point.Z + random.uniform(0, cube_size - hole_size)
                        )
                        hole_box = rg.Box(rg.Plane(hole_origin, rg.Vector3d.ZAxis), rg.Interval(0, hole_size), rg.Interval(0, hole_size), rg.Interval(0, hole_size))
                        brep_hole = hole_box.ToBrep()
                        bool_result = rg.Brep.CreateBooleanDifference([brep_cube], [brep_hole], 0.01)
                        if bool_result:
                            brep_cube = bool_result[0]

                    geometries.append(brep_cube)
                elif cube_type == 'void':
                    # No cube is added to the model, representing a void
                    continue

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_network(cube_size=2.0, grid_dim=4, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_network(cube_size=1.5, grid_dim=3, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_network(cube_size=3.0, grid_dim=5, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_network(cube_size=2.5, grid_dim=2, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_network(cube_size=4.0, grid_dim=6, seed=654)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
