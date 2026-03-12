# Created for 0002_0005_cubic_nest.json

""" Summary:
The provided function, `create_cubic_nest_structure`, generates an architectural concept model inspired by the "Cubic nest" metaphor. It constructs a lattice framework of interlaced cubic volumes, emphasizing the rhythmic arrangement and spatial layering of cubes. The function allows for variability in cube materials, distinguishing between solid, perforated, and void elements, enhancing depth and complexity. By iterating over a grid, it stacks and interconnects cubes at varying heights, creating transitional spaces that promote exploration. This approach results in a dynamic, protective network of cubes that embodies the metaphor's themes of shelter, interconnectedness, and modular identity."""

#! python 3
function_code = """def create_cubic_nest_structure(cube_size, grid_dim, layer_height, material_variation, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor. The model features a lattice framework
    of interlaced cubic volumes, emphasizing the dynamic interplay between solid, perforated, and void elements.

    Parameters:
    - cube_size (float): The edge length of each cube in meters.
    - grid_dim (tuple): A tuple (x_count, y_count) defining the number of cubes along the x and y axes.
    - layer_height (float): The height difference between each layer of cubes.
    - material_variation (float): The probability of a cube being perforated or void to introduce material variety.
    - seed (int, optional): Random seed for ensuring replicable randomness in cube material variation.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Iterate through the grid to build the structure
    for x in range(grid_dim[0]):
        for y in range(grid_dim[1]):
            # Alternate layers for visual variation
            z_offset = (x + y) % 2 * layer_height

            # Decide material type for the cube
            material_type = random.random()
            cube_center = rg.Point3d(x * cube_size, y * cube_size, z_offset)

            # Create a base cube
            base_cube = rg.Box(
                rg.Plane(cube_center, rg.Vector3d.ZAxis),
                rg.Interval(-cube_size / 2, cube_size / 2),
                rg.Interval(-cube_size / 2, cube_size / 2),
                rg.Interval(-cube_size / 2, cube_size / 2)
            )

            # Determine cube's material and geometry
            if material_type < material_variation / 3:
                # Solid cube
                geometries.append(base_cube.ToBrep())
            elif material_type < 2 * material_variation / 3:
                # Perforated cube: subtract smaller cubes from the base cube
                perforation_size = cube_size * 0.3
                perforation = rg.Box(
                    rg.Plane(cube_center, rg.Vector3d.ZAxis),
                    rg.Interval(-perforation_size / 2, perforation_size / 2),
                    rg.Interval(-perforation_size / 2, perforation_size / 2),
                    rg.Interval(-perforation_size / 2, perforation_size / 2)
                )
                perforated_brep = rg.Brep.CreateBooleanDifference([base_cube.ToBrep()], [perforation.ToBrep()], 0.01)
                if perforated_brep:
                    geometries.append(perforated_brep[0])
            else:
                # Void cube: represented as an empty space
                continue

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_structure(cube_size=1.0, grid_dim=(5, 5), layer_height=0.5, material_variation=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_structure(cube_size=2.0, grid_dim=(3, 4), layer_height=1.0, material_variation=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_structure(cube_size=0.5, grid_dim=(6, 6), layer_height=0.3, material_variation=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_structure(cube_size=1.5, grid_dim=(4, 3), layer_height=0.7, material_variation=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_structure(cube_size=0.75, grid_dim=(7, 2), layer_height=0.4, material_variation=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
