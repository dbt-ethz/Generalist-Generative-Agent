# Created for 0013_0005_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model based on the 'Split void' metaphor by creating a central void that divides the building form into distinct segments. It accepts parameters for building dimensions and void orientation, generating a 3D geometric representation. The main volume is defined as a box, and a void is created either vertically or horizontally, resulting in a split of the main volume into separate parts. This division allows for contrasting materials and spatial arrangements, reflecting the metaphor's themes of duality, interaction, and dynamic circulation, enhancing the overall architectural identity."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, orientation='vertical', seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor where a central void divides the building form.

    Args:
        length (float): The total length of the building form in meters.
        width (float): The total width of the building form in meters.
        height (float): The height of the building form in meters.
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

    # Define the main volume of the building
    main_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

    # Create the void
    if orientation == 'vertical':
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(length / 2 - void_width / 2, length / 2 + void_width / 2),
                          rg.Interval(0, width), rg.Interval(0, height))
    else:  # horizontal
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length),
                          rg.Interval(width / 2 - void_width / 2, width / 2 + void_width / 2), rg.Interval(0, height))

    # Split the main volume with the void
    void_brep = void_box.ToBrep()
    main_brep = main_volume.ToBrep()
    split_breps = main_brep.Split(void_brep, 0.001)

    # Add the split parts to the geometries list
    if split_breps:
        geometries.extend(split_breps)

    # Optionally, emphasize contrast by altering materiality (not represented in geometry, but conceptually considered)
    # Different textures or materials can be imagined for each segment

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(30, 20, 10, 5, orientation='vertical', seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(40, 25, 15, 8, orientation='horizontal', seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(50, 30, 20, 10, orientation='vertical', seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(35, 15, 12, 6, orientation='horizontal', seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(45, 22, 18, 7, orientation='vertical', seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
