# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates interconnected volumes resembling natural chambers by utilizing randomized parameters such as base radius and height variation, which mimic organic forms found in nature. The low-profile base blends with the landscape, while the varied heights and shapes of the chambers enhance the sense of concealment and discovery. By incorporating flowing lines and undulating surfaces, the model reflects the cavern's mystery and refuge, while the use of materials with different textures reinforces the connection to the earth, simulating an immersive experience."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius=10, height_variation=5, chamber_count=3, seed=42):
    \"""
    Creates a 3D architectural Concept Model inspired by the metaphor of a subterranean cavern.

    Parameters:
    - base_radius (float): The average radius of the base of the cavern-like structure.
    - height_variation (float): The variation in height to create an undulating ceiling and floor.
    - chamber_count (int): The number of main interconnected volumes (chambers) to create.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, NurbsSurface, Brep

    random.seed(seed)

    # List to store the resulting 3D geometries
    geometries = []

    # Define the base point for the model
    base_point = Point3d(0, 0, 0)

    # Create main chambers
    for i in range(chamber_count):
        # Randomize dimensions for organic variation
        radius = base_radius + random.uniform(-2, 2)
        height = height_variation + random.uniform(-2, 2)

        # Create a base circle for the chamber
        base_circle = Rhino.Geometry.Circle(base_point, radius)

        # Define height points for the top and bottom of the chamber
        top_height = random.uniform(height, height + 3)
        bottom_height = random.uniform(-height, -height - 3)

        # Define points to create a surface that represents a chamber
        top_point = Point3d(base_point.X, base_point.Y, top_height)
        bottom_point = Point3d(base_point.X, base_point.Y, bottom_height)

        # Create a lofted surface between top and bottom circles
        top_circle = Rhino.Geometry.Circle(top_point, radius)
        bottom_circle = Rhino.Geometry.Circle(bottom_point, radius)

        # Loft the surfaces
        loft = Rhino.Geometry.Brep.CreateFromLoft(
            [top_circle.ToNurbsCurve(), bottom_circle.ToNurbsCurve()],
            Rhino.Geometry.Point3d.Unset, Rhino.Geometry.Point3d.Unset,
            Rhino.Geometry.LoftType.Normal, False
        )

        if loft:
            geometries.append(loft[0])

        # Move base point for the next chamber
        base_point = Point3d(base_point.X + random.uniform(5, 10), 
                             base_point.Y + random.uniform(5, 10),
                             base_point.Z + random.uniform(-1, 1))

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_radius=12, height_variation=6, chamber_count=5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_radius=15, height_variation=4, chamber_count=4, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_radius=8, height_variation=7, chamber_count=6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_radius=11, height_variation=3, chamber_count=2, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_radius=9, height_variation=8, chamber_count=7, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
