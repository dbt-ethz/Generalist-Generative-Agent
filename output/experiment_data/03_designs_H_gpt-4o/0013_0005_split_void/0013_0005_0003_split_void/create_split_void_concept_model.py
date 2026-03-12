# Created for 0013_0005_split_void.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Split void" metaphor. It creates a building form with a central void that acts as a transformative boundary, dividing the structure into distinct segments. By defining a main volume and a void based on specified dimensions and orientation (vertical or horizontal), the function emphasizes contrast in geometry and materiality. The void facilitates circulation and visual connections, enhancing interactions with light and shadow. Additionally, the function introduces dynamic elements, like translucent covers, to further explore the impact of the void, reinforcing the design's intended duality and tension."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, orientation='vertical', seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Split void' metaphor where a central void divides
    the architectural mass into distinct segments, enhancing visual identity through contrast in form and materiality.

    Args:
        length (float): The overall length of the building in meters.
        width (float): The overall width of the building in meters.
        height (float): The overall height of the building in meters.
        void_width (float): The width of the central void in meters.
        orientation (str): The orientation of the void, either 'vertical' or 'horizontal'.
        seed (int): Seed for random number generation to ensure replicability.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Brep objects representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    geometries = []

    # Define the main volume
    main_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    main_brep = main_box.ToBrep()

    # Define the void based on the orientation
    if orientation == 'vertical':
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(length / 2 - void_width / 2, length / 2 + void_width / 2), rg.Interval(0, width), rg.Interval(0, height))
    else:  # horizontal
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(width / 2 - void_width / 2, width / 2 + void_width / 2), rg.Interval(0, height))
    
    void_brep = void_box.ToBrep()

    # Create the split by subtracting the void from the main volume
    split_results = rg.Brep.CreateBooleanDifference([main_brep], [void_brep], 0.001)

    # Check if the split was successful and add results to geometries
    if split_results:
        geometries.extend(split_results)

    # Further explore the impact of the void by adding dynamic elements
    # Consider adding a translucent cover over the void to emphasize light interaction
    # These additional elements can be conceptualized as different material zones
    if orientation == 'vertical':
        cover_height = random.uniform(height * 0.5, height * 0.75)
        cover_box = rg.Box(rg.Plane.WorldXY, rg.Interval(length / 2 - void_width / 4, length / 2 + void_width / 4),
                           rg.Interval(0, width), rg.Interval(height - cover_height, height))
        cover_brep = cover_box.ToBrep()
        if cover_brep:
            geometries.append(cover_brep)
    else:
        cover_length = random.uniform(length * 0.5, length * 0.75)
        cover_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(width / 2 - void_width / 4, width / 2 + void_width / 4),
                           rg.Interval(height - 1, height))
        cover_brep = cover_box.ToBrep()
        if cover_brep:
            geometries.append(cover_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=30, width=20, height=10, void_width=5, orientation='vertical', seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=25, width=15, height=12, void_width=3, orientation='horizontal', seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=40, width=25, height=15, void_width=6, orientation='vertical', seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=50, width=30, height=20, void_width=8, orientation='horizontal', seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=35, width=22, height=18, void_width=4, orientation='vertical', seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
