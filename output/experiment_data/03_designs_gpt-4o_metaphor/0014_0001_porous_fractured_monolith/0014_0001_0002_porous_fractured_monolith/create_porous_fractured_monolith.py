# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It creates a solid monolithic form defined by specified dimensions, then introduces voids to represent permeability and lightness. The voids are positioned randomly within the structure, enhancing the design's interaction with light and air. Additionally, the function incorporates fractures, adding complexity and movement to the monolith. The resulting model embodies the duality of solidity and fragmentation, fostering dynamic spatial relationships while inviting connectivity and engagement within the architectural space."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, void_count, void_size):
    \"""
    Creates a Concept Model based on the 'Porous Fractured Monolith' metaphor. The model combines a monolithic form with
    voids that introduce lightness and permeability, along with fractures that add complexity and tension.

    Parameters:
    - base_length (float): The length of the base monolith form in meters.
    - base_width (float): The width of the base monolith form in meters.
    - base_height (float): The height of the base monolith form in meters.
    - void_count (int): The number of voids to create within the monolith.
    - void_size (float): The approximate size of each void in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the solid and void components of the Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = base_box.ToBrep()

    # Generate voids randomly within the monolith
    voids = []
    for _ in range(void_count):
        # Randomly position and size each void
        void_center = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        void_radius = random.uniform(void_size * 0.5, void_size)
        void_sphere = rg.Sphere(void_center, void_radius)
        void_brep = void_sphere.ToBrep()
        voids.append(void_brep)

    # Subtract voids from the monolith to create the porous effect
    porous_monolith = rg.Brep.CreateBooleanDifference([monolith_brep], voids, 0.01)

    # Creating fractures in the monolith
    fractures = []
    for _ in range(int(void_count / 2)):  # Use half the number of voids to create fractures
        fracture_start = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        fracture_end = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        fracture_line = rg.Line(fracture_start, fracture_end)
        fracture_crv = fracture_line.ToNurbsCurve()
        fracture_surface = rg.Surface.CreateExtrusion(fracture_crv, rg.Vector3d(0, 0, base_height))
        fractures.append(fracture_surface.ToBrep())

    # Subtract fractures from the porous monolith to add the fractured effect
    fractured_monolith = rg.Brep.CreateBooleanDifference(porous_monolith, fractures, 0.01)

    # Return the final list of 3D geometries
    return fractured_monolith if fractured_monolith else [monolith_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(5.0, 3.0, 2.0, 10, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(4.0, 2.5, 3.0, 8, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(6.0, 4.0, 5.0, 15, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(7.0, 5.0, 4.0, 20, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(8.0, 6.0, 3.5, 12, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
