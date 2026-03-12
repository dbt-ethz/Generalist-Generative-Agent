# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern, focusing on creating an immersive, labyrinthine experience. It constructs interlocking volumes that represent narrow corridors and expansive chambers through the use of random dimensions, simulating the complexity and mystery of natural caves. The design incorporates both angular, faceted surfaces and organic forms to reflect the rugged and fluid characteristics of cavern spaces. By adding strategic openings, the model enhances the interplay of light and shadow, evoking chiaroscuro effects that deepen the immersive quality, aligned with the metaphor's essence of exploration and surprise."""

#! python 3
function_code = """def generate_subterranean_cavern_model(seed=42, corridor_width=2.0, chamber_size=10.0):
    \"""
    Generates an architectural Concept Model inspired by the metaphor of a subterranean cavern.
    
    The model consists of a series of interlocking volumes that form a maze-like structure,
    combining angular and organic forms. The design emphasizes the complex spatial relationships
    and dynamic interplay of light and shadow found in natural cavern environments.

    Parameters:
    seed (int): Random seed for reproducibility of the design.
    corridor_width (float): Width of the narrow corridors (in meters).
    chamber_size (float): Average size of the larger chambers (in meters).

    Returns:
    List of RhinoCommon.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""

    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    geometries = []

    # Create a series of narrow corridors
    for i in range(5):
        length = random.uniform(5, 15)
        height = random.uniform(3, 5)
        corridor = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, corridor_width),
            rg.Interval(0, length),
            rg.Interval(0, height)
        )
        corridor.Transform(
            rg.Transform.Translation(random.uniform(-5, 5), random.uniform(-5, 5), 0)
        )
        geometries.append(corridor.ToBrep())

    # Create larger, dramatic chambers
    for i in range(3):
        radius = random.uniform(chamber_size / 2, chamber_size)
        sphere = rg.Sphere(
            rg.Point3d(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(0, 10)),
            radius
        )
        brep_sphere = sphere.ToBrep()
        geometries.append(brep_sphere)

    # Create angular, faceted surfaces to contrast with organic forms
    for i in range(4):
        points = [
            rg.Point3d(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(0, 10)) for _ in range(5)
        ]
        mesh = rg.Mesh()
        for pt in points:
            mesh.Vertices.Add(pt)
        mesh.Faces.AddFace(0, 1, 2)
        mesh.Faces.AddFace(0, 2, 3)
        mesh.Faces.AddFace(0, 3, 4)
        mesh.Faces.AddFace(1, 3, 4)  # Fixed index to avoid out of range error
        geometries.append(mesh)

    # Add strategic openings to simulate natural light
    for brep in geometries[:]:  # Create a copy of the list to iterate over
        if isinstance(brep, rg.Brep):
            void = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(-1, 1),
                rg.Interval(-1, 1),
                rg.Interval(1, 3)
            ).ToBrep()
            boolean_difference = rg.Brep.CreateBooleanDifference([brep], [void], 0.001)
            if boolean_difference:  # Check if the operation was successful
                geometries.append(boolean_difference[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_subterranean_cavern_model(seed=123, corridor_width=3.0, chamber_size=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_subterranean_cavern_model(seed=99, corridor_width=1.5, chamber_size=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_subterranean_cavern_model(seed=2023, corridor_width=2.5, chamber_size=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_subterranean_cavern_model(seed=10, corridor_width=2.5, chamber_size=9.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_subterranean_cavern_model(seed=50, corridor_width=4.0, chamber_size=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
