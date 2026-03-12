# Created for 0002_0005_cubic_nest.json

""" Summary:
The function `create_cubic_nest_structure` generates an architectural concept model embodying the "Cubic nest" metaphor by creating a three-dimensional lattice of interlaced cubic volumes. It systematically places cubes in a defined grid, varying their material properties (solid, perforated, void) based on specified probabilities. This approach results in a rhythmic arrangement that echoes the metaphor's themes of complexity and interconnectedness. The stacking and interconnection of cubes generate dynamic transitional spaces, enhancing exploration within the structure. The use of different materials adds depth and intricacy, allowing each cube to maintain its identity while contributing to a cohesive, protective architectural framework."""

#! python 3
function_code = """def create_cubic_nest_structure(cube_size, grid_dimensions, height_levels, material_variation, seed=1):
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    breps = []

    # Sum probabilities to ensure they add up to 1
    total_probability = sum(material_variation.values())
    material_probs = {k: v / total_probability for k, v in material_variation.items()}

    # Iterate through a 3D grid to place cubes
    for x in range(grid_dimensions[0]):
        for y in range(grid_dimensions[1]):
            for z in range(height_levels):
                # Determine material type based on probabilities
                rand_val = random.random()
                if rand_val < material_probs['solid']:
                    material_type = 'solid'
                elif rand_val < material_probs['solid'] + material_probs['perforated']:
                    material_type = 'perforated'
                else:
                    material_type = 'void'

                # Base point for the cube
                base_point = rg.Point3d(x * cube_size, y * cube_size, z * cube_size)

                # Create the cube as a Brep
                box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis),
                             rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
                brep_cube = box.ToBrep()

                if material_type == 'solid':
                    breps.append(brep_cube)
                elif material_type == 'perforated':
                    # Create perforation by subtracting smaller volumes
                    perforation_count = random.randint(1, 3)
                    for _ in range(perforation_count):
                        perforation_size = cube_size * random.uniform(0.3, 0.6)
                        perforation_origin = rg.Point3d(
                            base_point.X + random.uniform(0, cube_size - perforation_size),
                            base_point.Y + random.uniform(0, cube_size - perforation_size),
                            base_point.Z + random.uniform(0, cube_size - perforation_size)
                        )
                        perforation_box = rg.Box(rg.Plane(perforation_origin, rg.Vector3d.ZAxis),
                                                 rg.Interval(0, perforation_size), rg.Interval(0, perforation_size),
                                                 rg.Interval(0, perforation_size))
                        perforation_brep = perforation_box.ToBrep()
                        difference_result = rg.Brep.CreateBooleanDifference([brep_cube], [perforation_brep], 0.01)
                        if difference_result:
                            brep_cube = difference_result[0]
                    breps.append(brep_cube)
                # If material_type is 'void', do not add the brep_cube to the breps list

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_structure(cube_size=2, grid_dimensions=(5, 5), height_levels=3, material_variation={'solid': 0.5, 'perforated': 0.3, 'void': 0.2}, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_structure(cube_size=1, grid_dimensions=(4, 4), height_levels=2, material_variation={'solid': 0.7, 'perforated': 0.2, 'void': 0.1}, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_structure(cube_size=3, grid_dimensions=(6, 6), height_levels=4, material_variation={'solid': 0.4, 'perforated': 0.4, 'void': 0.2}, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_structure(cube_size=1.5, grid_dimensions=(3, 3), height_levels=5, material_variation={'solid': 0.6, 'perforated': 0.3, 'void': 0.1}, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_structure(cube_size=2.5, grid_dimensions=(7, 3), height_levels=2, material_variation={'solid': 0.2, 'perforated': 0.5, 'void': 0.3}, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
