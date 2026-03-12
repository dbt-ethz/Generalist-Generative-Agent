# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model based on the metaphor "Porous fractured monolith" by creating a large, unified mass and introducing voids and fractures that reflect the metaphor's complexity. It starts with a robust box representing the monolith, then carves out varying voids to enhance lightness and permeability. Randomly placed fractures are added, emphasizing the structural tension and non-linearity. The resulting model illustrates the dynamic interplay between solidity and openness, promoting exploration and interaction while facilitating natural light and ventilation, thus embodying the duality and connectivity inherent in the metaphor."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, void_count, fracture_count, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Porous fractured monolith'.
    
    This function generates a large monolithic mass and introduces voids and fractures to emphasize 
    the duality of solidity and openness. The fractures further enhance the sense of permeability 
    and complexity in the structure.

    Parameters:
    - base_length (float): Length of the monolithic base in meters.
    - base_width (float): Width of the monolithic base in meters.
    - base_height (float): Height of the monolithic base in meters.
    - void_count (int): Number of voids to introduce within the monolith.
    - fracture_count (int): Number of fractures to add to the form.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create the initial monolithic mass as a box
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_length, 0, base_height),
        rg.Point3d(base_length, base_width, base_height),
        rg.Point3d(0, base_width, base_height)
    ]
    monolith_brep = rg.Brep.CreateFromBox(base_corners)

    voids = []
    fractures = []

    # Create voids by subtracting smaller boxes from the monolith
    for _ in range(void_count):
        void_length = random.uniform(base_length * 0.1, base_length * 0.3)
        void_width = random.uniform(base_width * 0.1, base_width * 0.3)
        void_height = random.uniform(base_height * 0.1, base_height * 0.3)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

        void_corners = [
            rg.Point3d(void_x, void_y, void_z),
            rg.Point3d(void_x + void_length, void_y, void_z),
            rg.Point3d(void_x + void_length, void_y + void_width, void_z),
            rg.Point3d(void_x, void_y + void_width, void_z),
            rg.Point3d(void_x, void_y, void_z + void_height),
            rg.Point3d(void_x + void_length, void_y, void_z + void_height),
            rg.Point3d(void_x + void_length, void_y + void_width, void_z + void_height),
            rg.Point3d(void_x, void_y + void_width, void_z + void_height)
        ]
        void_brep = rg.Brep.CreateFromBox(void_corners)
        voids.append(void_brep)

    # Create fractures as thin slices through the monolith
    for _ in range(fracture_count):
        fracture_plane = rg.Plane(
            rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height)),
            rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1]))
        )
        fracture_brep = rg.Brep.CreateFromSurface(
            rg.Surface.CreateExtrusion(
                rg.Line(fracture_plane.Origin, fracture_plane.Origin + fracture_plane.Normal * max(base_length, base_width, base_height)).ToNurbsCurve(),
                rg.Vector3d.ZAxis * 0.1
            )
        )
        fractures.append(fracture_brep)

    # Subtract the voids and fractures from the monolithic brep
    all_subtractions = voids + fractures
    fractured_monolith = monolith_brep
    for subtraction in all_subtractions:
        result = rg.Brep.CreateBooleanDifference(fractured_monolith, subtraction, 0.001)
        if result:
            fractured_monolith = result[0]

    return [fractured_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(10.0, 5.0, 8.0, 3, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(15.0, 10.0, 12.0, 4, 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(7.5, 3.5, 9.0, 2, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(20.0, 15.0, 10.0, 5, 7, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(12.0, 6.0, 9.0, 6, 8, seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
