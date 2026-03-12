# Created for 0002_0005_cubic_nest.json

""" Summary:
The function `create_cubic_nest_model` generates an architectural concept model by creating a lattice of interlaced cubic volumes based on the "Cubic nest" metaphor. It uses parameters like base size, cube count, and stacking height to define the model's structure. By employing random translations, the function creates a dynamic arrangement of cubes that embody both solid and void elements, enhancing spatial complexity. The generated geometries reflect various relationships among cubes, allowing for sheltered and open areas that invite exploration. This process results in a cohesive yet intricate network that aligns with the metaphor's emphasis on interconnectedness and shelter."""

#! python 3
function_code = """def create_cubic_nest_model(base_size, cube_count, max_stack_height, seed):
    \"""
    Create an architectural Concept Model that embodies the 'Cubic nest' metaphor by generating a lattice framework
    of interlaced cubic volumes. This model focuses on the rhythmic arrangement and spatial layering of cubes to
    create a dynamic and protective network. The function uses a variety of geometrical operations to distinguish 
    between solid, perforated, and void elements, enhancing the perception of depth and intricacy.

    Parameters:
    - base_size (float): The size of the base cube in meters.
    - cube_count (int): The number of cubes to generate in the model.
    - max_stack_height (int): The maximum number of cubes that can be stacked vertically.
    - seed (int): A seed for the random number generator to ensure reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Define the range for random translations to create complexity in the lattice structure
    translation_range = base_size * 0.5

    for i in range(cube_count):
        # Randomly determine the position of each cube
        x_translation = random.uniform(-translation_range, translation_range)
        y_translation = random.uniform(-translation_range, translation_range)
        z_translation = random.uniform(0, max_stack_height * base_size)

        # Create the base cube
        origin = rg.Point3d(x_translation, y_translation, z_translation)
        cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size))

        # Convert the Box to a Brep
        brep_cube = cube.ToBrep()

        # Randomly decide if the cube should be solid, perforated, or void
        choice = random.choice(['solid', 'perforated', 'void'])

        if choice == 'solid':
            geometries.append(brep_cube)
        elif choice == 'perforated':
            # Create a perforated effect by subtracting smaller cubes
            perforations = int(random.uniform(1, 4))
            for _ in range(perforations):
                perforation_size = base_size * random.uniform(0.1, 0.3)
                perforation_origin = rg.Point3d(
                    x_translation + random.uniform(0, base_size - perforation_size),
                    y_translation + random.uniform(0, base_size - perforation_size),
                    z_translation + random.uniform(0, base_size - perforation_size)
                )
                perforation_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, perforation_size), rg.Interval(0, perforation_size), rg.Interval(0, perforation_size))
                perforation_brep = perforation_box.ToBrep()
                boolean_result = rg.Brep.CreateBooleanDifference([brep_cube], [perforation_brep], 0.01)
                if boolean_result:
                    brep_cube = boolean_result[0]

            geometries.append(brep_cube)
        elif choice == 'void':
            # Create a void by not adding the cube to the geometry list
            continue

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(base_size=1.0, cube_count=10, max_stack_height=5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(base_size=2.0, cube_count=20, max_stack_height=3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(base_size=0.5, cube_count=15, max_stack_height=4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(base_size=1.5, cube_count=8, max_stack_height=6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(base_size=1.2, cube_count=12, max_stack_height=4, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
