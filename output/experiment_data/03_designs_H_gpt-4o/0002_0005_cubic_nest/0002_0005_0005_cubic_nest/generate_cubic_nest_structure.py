# Created for 0002_0005_cubic_nest.json

""" Summary:
The provided function, `generate_cubic_nest_structure`, creates an architectural concept model based on the "Cubic nest" metaphor by generating a lattice of interlaced cubic volumes. It employs a 3D grid to arrange cubes with varying configurations, emphasizing rhythmic layering and spatial relationships. Each cube can be solid or contain perforations, enhancing the complexity and depth of the structure. This approach allows for dynamic transitions between sheltered and open spaces, inviting exploration while maintaining the modular identity of each cubic element. The function ultimately produces a cohesive, protective network that embodies the metaphor's essence, encouraging diverse spatial experiences."""

#! python 3
function_code = """def generate_cubic_nest_structure(base_cube_size, grid_size, max_layers, seed=42):
    \"""
    Create an architectural Concept Model that embodies the 'Cubic nest' metaphor. This function generates
    a lattice framework of interlaced cubic volumes, emphasizing a rhythmic arrangement and spatial layering
    to create a dynamic and protective network.

    Parameters:
    - base_cube_size (float): The edge length of each cube in meters.
    - grid_size (int): The number of cubes along one edge of the grid.
    - max_layers (int): The maximum number of overlapping vertical layers for the cubes.
    - seed (int, optional): Random seed for replicable randomness in cube configuration.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Iterate through a 3D grid to create a lattice of cubes
    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(max_layers):
                # Determine whether to create a solid or a void
                if random.random() > 0.2:  # 80% chance to create a solid cube
                    # Define the base point of the cube
                    base_point = rg.Point3d(x * base_cube_size, y * base_cube_size, z * base_cube_size)
                    # Create the cube (as a Brep box)
                    box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), 
                                 rg.Interval(0, base_cube_size), 
                                 rg.Interval(0, base_cube_size), 
                                 rg.Interval(0, base_cube_size))
                    brep = box.ToBrep()

                    # Randomly decide to create perforations or keep solid
                    if random.random() > 0.5:  # 50% chance to create perforations
                        perforations = random.randint(1, 3)
                        for _ in range(perforations):
                            perforation_size = base_cube_size * random.uniform(0.1, 0.3)
                            perforation_origin = rg.Point3d(
                                base_point.X + random.uniform(0, base_cube_size - perforation_size),
                                base_point.Y + random.uniform(0, base_cube_size - perforation_size),
                                base_point.Z + random.uniform(0, base_cube_size - perforation_size)
                            )
                            perforation_box = rg.Box(rg.Plane(perforation_origin, rg.Vector3d.ZAxis),
                                                     rg.Interval(0, perforation_size), 
                                                     rg.Interval(0, perforation_size), 
                                                     rg.Interval(0, perforation_size))
                            perforation_brep = perforation_box.ToBrep()
                            boolean_result = rg.Brep.CreateBooleanDifference([brep], [perforation_brep], 0.01)
                            if boolean_result:
                                brep = boolean_result[0]

                    geometries.append(brep)
                else:
                    # Create a void by not adding the cube to the geometry list
                    continue

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_structure(2.0, 5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_structure(1.5, 4, 2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_structure(3.0, 6, 4, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_structure(1.0, 3, 5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_structure(0.5, 10, 2, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
