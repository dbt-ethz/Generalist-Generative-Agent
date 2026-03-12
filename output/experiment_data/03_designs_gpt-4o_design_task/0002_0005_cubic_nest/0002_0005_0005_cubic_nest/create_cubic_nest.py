# Created for 0002_0005_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model by creating a lattice of interlaced cubic volumes inspired by the "Cubic nest" metaphor. By iterating through a defined lattice size, the function creates cubes that can either be solid or void based on a specified probability. Each cube is layered, with slight offsets for depth, contributing to a dynamic and protective network. This approach evokes complexity through the interplay of solid and void spaces, aligning with the metaphor's emphasis on interconnectedness and modularity. The result is a variety of spatial experiences within a cohesive, multifaceted structure."""

#! python 3
function_code = """def create_cubic_nest(lattice_size=3, cube_edge=2.0, max_layers=3, void_probability=0.3, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor. The model consists of a lattice
    framework of interlaced cubic volumes, emphasizing spatial layering and rhythm within a protective network.
    
    Parameters:
    - lattice_size: int, Number of cubes along one edge of the lattice.
    - cube_edge: float, Edge length of each cubic volume in meters.
    - max_layers: int, Maximum number of overlapping layers for the cubes.
    - void_probability: float, Probability that a cube is a void rather than a solid.
    - seed: int, Random seed for generating replicable randomness.
    
    Returns:
    - List of RhinoCommon.Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Iterate over the lattice to create cubes
    for x in range(lattice_size):
        for y in range(lattice_size):
            for z in range(lattice_size):
                # Determine if this cube should be a void or solid
                if random.random() > void_probability:
                    # Create a cube as a Brep
                    base_point = rg.Point3d(x * cube_edge, y * cube_edge, z * cube_edge)
                    cube = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, cube_edge), rg.Interval(0, cube_edge), rg.Interval(0, cube_edge)).ToBrep()
                    
                    # Determine the number of layers for this cube
                    layers = random.randint(1, max_layers)
                    
                    # Create layered cubes (nested)
                    for layer in range(layers):
                        offset = cube_edge * 0.2 * layer  # Slight offset for each layer
                        transformation = rg.Transform.Translation(offset, offset, offset)
                        layered_cube = cube.Duplicate()
                        layered_cube.Transform(transformation)
                        geometries.append(layered_cube)
                else:
                    # Create a void (empty space)
                    continue

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest(lattice_size=4, cube_edge=1.5, max_layers=2, void_probability=0.2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest(lattice_size=5, cube_edge=3.0, max_layers=4, void_probability=0.1, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest(lattice_size=6, cube_edge=2.5, max_layers=3, void_probability=0.4, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest(lattice_size=3, cube_edge=2.0, max_layers=5, void_probability=0.5, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest(lattice_size=2, cube_edge=1.0, max_layers=1, void_probability=0.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
