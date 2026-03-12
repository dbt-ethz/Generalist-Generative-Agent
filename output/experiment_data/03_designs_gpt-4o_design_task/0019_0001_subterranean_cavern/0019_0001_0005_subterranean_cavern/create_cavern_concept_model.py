# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The function `create_cavern_concept_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a base circular surface to represent the ground, then defines an undulating ceiling using random heights to mimic organic shapes. The model incorporates interconnected voids, simulating chambers and alcoves through boolean operations, enhancing the exploration aspect. Variations in base radius and height introduce diverse spatial qualities. The result is a conceptual model that embodies the metaphor's essence, featuring intimate and expansive spaces that evoke mystery and refuge, while allowing for dynamic lighting effects through design openings."""

#! python 3
function_code = """def create_cavern_concept_model(base_radius=10, height_variation=3, seed=42):
    \"""
    Generates a conceptual architectural model resembling a subterranean cavern.

    Parameters:
    - base_radius (float): The base radius of the cavern-like structure. Represents the general footprint.
    - height_variation (float): The variation in height throughout the model to simulate organic ceiling changes.
    - seed (int): Seed for random generation to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of BREP geometries representing the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed for consistency
    random.seed(seed)

    # Create a base surface to represent the ground level of the cavern
    base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
    base_surface = rg.Brep.CreatePlanarBreps(base_circle.ToNurbsCurve())[0]

    # Generate a series of points to define the undulating ceiling of the cavern
    ceiling_points = []
    divisions = 10  # Define number of divisions for the circle
    for i in range(divisions):
        angle = (2 * math.pi / divisions) * i
        x = base_radius * math.cos(angle)
        y = base_radius * math.sin(angle)
        z = random.uniform(0, height_variation)
        ceiling_points.append(rg.Point3d(x, y, z))

    # Create a lofted surface to represent the ceiling
    ceiling_curve = rg.Polyline(ceiling_points).ToNurbsCurve()
    ceiling_surface = rg.Brep.CreateFromSurface(rg.RevSurface.Create(ceiling_curve, rg.Line(rg.Point3d(0, 0, 0), rg.Vector3d(0, 0, 1))))

    # Carve out interconnected spaces by boolean operations
    voids = []
    num_voids = random.randint(3, 5)
    for _ in range(num_voids):
        void_center = rg.Point3d(
            random.uniform(-base_radius / 2, base_radius / 2),
            random.uniform(-base_radius / 2, base_radius / 2),
            random.uniform(0, height_variation)
        )
        void_radius = random.uniform(base_radius * 0.2, base_radius * 0.4)
        void_sphere = rg.Sphere(void_center, void_radius)
        voids.append(rg.Brep.CreateFromSphere(void_sphere))

    # Perform boolean difference to carve out spaces
    cavern_structure = rg.Brep.CreateBooleanDifference([ceiling_surface], voids, 0.01)

    # Return the final geometry
    return cavern_structure"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cavern_concept_model(base_radius=15, height_variation=5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cavern_concept_model(base_radius=12, height_variation=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cavern_concept_model(base_radius=20, height_variation=6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cavern_concept_model(base_radius=18, height_variation=2, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cavern_concept_model(base_radius=14, height_variation=3.5, seed=22)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
