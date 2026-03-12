# Created for 0013_0002_split_void.json

""" Summary:
The provided function generates an architectural concept model based on the "Split void" metaphor by creating a building form that features a central void, effectively dividing the structure into two distinct yet interconnected halves. It utilizes parameters such as base dimensions, maximum height, and void depth to define the geometry. The function creates two separate sections with varying roof heights, emphasizing the duality and dynamic spatial relationships inherent in the metaphor. The void serves as both a separator and a connector, allowing for natural light to filter through, enhancing movement and interaction while maintaining a cohesive architectural identity."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, max_height, void_depth, roof_slope=0.2, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor, where a central void
    vertically divides the building, creating separate yet connected spaces with varying roof heights.

    Parameters:
    - base_length (float): The total length of the building in meters.
    - base_width (float): The total width of the building in meters.
    - max_height (float): The maximum height of the building in meters.
    - void_depth (float): The depth of the central void in meters.
    - roof_slope (float): The slope ratio for the roofs on either side of the void.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    random.seed(seed)

    # Calculate dimensions for the two halves
    half_length = base_length / 2
    half_width = base_width / 2 - void_depth / 2

    # Create the base box for the first half with a sloped roof
    first_half_base = rg.Rectangle3d(rg.Plane.WorldXY, half_width, half_length)
    first_half_slope_height = max_height * random.uniform(1 - roof_slope, 1)
    first_half_brep = rg.Brep.CreateFromBox((
        first_half_base.Corner(0), first_half_base.Corner(1),
        rg.Point3d(first_half_base.Corner(1).X, first_half_base.Corner(1).Y, first_half_slope_height),
        rg.Point3d(first_half_base.Corner(0).X, first_half_base.Corner(0).Y, first_half_slope_height),
        rg.Point3d(first_half_base.Corner(0).X, first_half_base.Corner(0).Y, 0),
        rg.Point3d(first_half_base.Corner(1).X, first_half_base.Corner(1).Y, 0)
    ))

    # Create the base box for the second half with a sloped roof
    second_half_base = rg.Rectangle3d(rg.Plane.WorldXY, half_width, half_length)
    second_half_base.Transform(rg.Transform.Translation(base_width - half_width, 0, 0))
    second_half_slope_height = max_height * random.uniform(1 - roof_slope, 1)
    second_half_brep = rg.Brep.CreateFromBox((
        second_half_base.Corner(0), second_half_base.Corner(1),
        rg.Point3d(second_half_base.Corner(1).X, second_half_base.Corner(1).Y, second_half_slope_height),
        rg.Point3d(second_half_base.Corner(0).X, second_half_base.Corner(0).Y, second_half_slope_height),
        rg.Point3d(second_half_base.Corner(0).X, second_half_base.Corner(0).Y, 0),
        rg.Point3d(second_half_base.Corner(1).X, second_half_base.Corner(1).Y, 0)
    ))

    # Create the void as a vertical brep
    void_base = rg.Rectangle3d(rg.Plane.WorldXY, void_depth, base_length)
    void_base.Transform(rg.Transform.Translation(half_width, 0, 0))
    void_brep = rg.Brep.CreateFromBox((
        void_base.Corner(0), void_base.Corner(1),
        rg.Point3d(void_base.Corner(1).X, void_base.Corner(1).Y, max_height),
        rg.Point3d(void_base.Corner(0).X, void_base.Corner(0).Y, max_height),
        rg.Point3d(void_base.Corner(0).X, void_base.Corner(0).Y, 0),
        rg.Point3d(void_base.Corner(1).X, void_base.Corner(1).Y, 0)
    ))

    # Return the list of Breps representing the concept model
    return [first_half_brep, second_half_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(20, 10, 15, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(30, 15, 20, 3, roof_slope=0.3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(25, 12, 18, 4, roof_slope=0.25, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(40, 20, 25, 5, roof_slope=0.15, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(35, 18, 22, 6, roof_slope=0.1, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
