# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a "subterranean cavern" by creating a low-profile exterior and a complex interior. It utilizes irregular shapes and flowing forms to reflect natural cave geometry while ensuring a balance between intimacy and openness. The function defines parameters for the model's dimensions and the number of interconnected chambers, which are generated randomly to mimic the organic irregularity of caves. By incorporating varied textures and utilizing transformations, it simulates a journey of discovery, reinforcing the themes of concealment and revelation inherent in the metaphor."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_length=40, base_width=30, max_height=15, chamber_count=4, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the metaphor of a 'subterranean cavern'.

    This function creates a low-profile exterior that blends into the landscape and a complex interior
    with interconnected volumes that unfold sequentially. The design uses irregular shapes and flowing
    forms to mimic natural cave geometry, balancing intimacy and openness.

    Parameters:
    - base_length (float): The total length of the model's base in meters.
    - base_width (float): The total width of the model's base in meters.
    - max_height (float): The maximum height of the interior spaces in meters.
    - chamber_count (int): The number of interconnected volumes or chambers to create.
    - seed (int): A seed for the random number generator for reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create the low-profile exterior base
    exterior_base = rg.Brep.CreateFromBox(rg.BoundingBox(rg.Point3d(0, 0, 0), rg.Point3d(base_length, base_width, max_height * 0.15)))

    # Initialize a list to hold the chamber geometries
    chambers = []

    # Chamber dimensions and positions
    for i in range(chamber_count):
        chamber_length = random.uniform(base_length * 0.15, base_length * 0.3)
        chamber_width = random.uniform(base_width * 0.15, base_width * 0.3)
        chamber_height = random.uniform(max_height * 0.3, max_height * 0.7)

        x_position = random.uniform(0, base_length - chamber_length)
        y_position = random.uniform(0, base_width - chamber_width)
        z_position = random.uniform(exterior_base.GetBoundingBox(True).Max.Z, max_height - chamber_height)

        # Create an irregular, organic chamber using a series of lofted curves
        profile1 = rg.Circle(rg.Plane.WorldXY, chamber_width * 0.5).ToNurbsCurve()
        profile2 = rg.Circle(rg.Plane(rg.Point3d(0, 0, chamber_height), rg.Vector3d.ZAxis), chamber_length * 0.5).ToNurbsCurve()
        loft = rg.Brep.CreateFromLoft([profile1, profile2], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

        if loft:
            chamber_brep = loft[0].DuplicateBrep()
            translation = rg.Transform.Translation(x_position, y_position, z_position)
            chamber_brep.Transform(translation)
            chambers.append(chamber_brep)

    # Create boolean union of chambers to form interconnected volumes
    if chambers:
        interior_union = rg.Brep.CreateBooleanUnion(chambers, 0.01)
    else:
        interior_union = []

    # Subtract interior from exterior base to create the concept model
    if interior_union:
        model = rg.Brep.CreateBooleanDifference(exterior_base, interior_union[0], 0.01)
    else:
        model = [exterior_base]

    return model if model else [exterior_base]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_length=50, base_width=40, max_height=20, chamber_count=5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_length=60, base_width=50, max_height=25, chamber_count=6, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_length=45, base_width=35, max_height=18, chamber_count=3, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_length=55, base_width=45, max_height=22, chamber_count=7, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_length=30, base_width=25, max_height=10, chamber_count=2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
