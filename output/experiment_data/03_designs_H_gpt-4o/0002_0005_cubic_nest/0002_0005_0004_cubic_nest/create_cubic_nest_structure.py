# Created for 0002_0005_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Cubic nest" metaphor by creating a lattice framework of interlaced cubic volumes. It calculates the position of cubes in a 3D grid and assigns material types (solid, perforated, void) based on defined probabilities, enhancing the complexity and depth of the structure. Each cube is modular, contributing to a cohesive whole while forming dynamic spatial relationships through stacking and interconnections. This approach fosters exploration and engagement within the design, embodying the metaphor's themes of interconnectedness and shelter through varied spatial experiences."""

#! python 3
function_code = """def create_cubic_nest_structure(cube_size, grid_dimension, z_layers, material_variation, seed=24):
    \"""
    Generates an architectural Concept Model based on the 'Cubic nest' metaphor. This function creates a framework
    of interconnected cubic volumes, utilizing both solid and void elements to form a dynamic spatial composition.

    Parameters:
    - cube_size (float): The size of each individual cube in meters.
    - grid_dimension (int): The number of cubes along one edge of the grid in the XY plane.
    - z_layers (int): The number of vertical layers of cubes.
    - material_variation (dict): A dictionary defining material types ('solid', 'perforated', 'void') and their probabilities.
    - seed (int, optional): Random seed for replicable randomness in cube material assignment.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the cubic structure.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    breps = []

    # Calculate the total number of cubes
    total_cubes = grid_dimension * grid_dimension * z_layers

    for index in range(total_cubes):
        x = (index % grid_dimension) * cube_size
        y = ((index // grid_dimension) % grid_dimension) * cube_size
        z = (index // (grid_dimension * grid_dimension)) * cube_size

        # Determine the material type based on given probabilities
        material_type = random.choices(
            list(material_variation.keys()), 
            list(material_variation.values()), 
            k=1
        )[0]

        base_point = rg.Point3d(x, y, z)
        cube = rg.Box(
            rg.Plane(base_point, rg.Vector3d.ZAxis),
            rg.Interval(0, cube_size),
            rg.Interval(0, cube_size),
            rg.Interval(0, cube_size)
        )

        if material_type == 'solid':
            breps.append(cube.ToBrep())
        elif material_type == 'perforated':
            # Create perforations by subtracting smaller cubes
            perforation_size = cube_size * 0.4
            perforation_box = rg.Box(
                rg.Plane(base_point, rg.Vector3d.ZAxis),
                rg.Interval(cube_size * 0.3, cube_size * 0.7),
                rg.Interval(cube_size * 0.3, cube_size * 0.7),
                rg.Interval(cube_size * 0.3, cube_size * 0.7)
            )
            perforated_brep = rg.Brep.CreateBooleanDifference([cube.ToBrep()], [perforation_box.ToBrep()], 0.01)
            if perforated_brep:
                breps.extend(perforated_brep)
        # If type is 'void', intentionally leave space empty

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_structure(2.0, 5, 3, {'solid': 0.6, 'perforated': 0.3, 'void': 0.1})
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_structure(1.5, 4, 2, {'solid': 0.5, 'perforated': 0.4, 'void': 0.1})
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_structure(3.0, 6, 4, {'solid': 0.7, 'perforated': 0.2, 'void': 0.1})
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_structure(1.0, 3, 5, {'solid': 0.4, 'perforated': 0.4, 'void': 0.2})
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_structure(2.5, 7, 2, {'solid': 0.5, 'perforated': 0.4, 'void': 0.1})
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
