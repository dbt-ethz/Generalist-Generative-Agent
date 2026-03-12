# Created for 0013_0004_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model embodying the "Split void" metaphor. It takes parameters such as building dimensions and void characteristics, creating a central void that divides the structure into distinct zones. The void's shape, either curvilinear or faceted, influences the building's spatial organization and visual identity. By manipulating the void's dimensions and type, the model emphasizes the dynamic relationship between solid and void, enhancing light and shadow interactions. The resulting geometries visually express the metaphor's essence, reflecting tension, duality, and varied spatial experiences within the architectural design."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, void_type='faceted', seed=0):
    \"""
    Create an architectural Concept Model based on the 'Split void' metaphor.

    This function generates a concept model with a central void that splits the building into distinct zones,
    emphasizing the interaction between solid and void spaces. The void influences the building's spatial logic 
    and identity, offering dynamic light and shadow play.

    Parameters:
    length (float): The total length of the building footprint.
    width (float): The total width of the building footprint.
    height (float): The height of the building.
    void_width (float): The width of the central void.
    void_type (str): The type of void shape, either 'curvilinear' or 'faceted'.
    seed (int): Random seed for reproducibility.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Define the bounding box for the building
    building_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, length), rg.Interval(0, height))

    # Create the void shape based on the specified type
    if void_type == 'curvilinear':
        void_curve = rg.ArcCurve(rg.Arc(
            rg.Point3d(width / 2, length / 2, 0),
            rg.Point3d(width / 2, length / 2 + random.uniform(-length / 4, length / 4), height / 2),
            rg.Point3d(width / 2, length, height)
        ))
    else:
        void_curve = rg.PolylineCurve([
            rg.Point3d(width / 2 - void_width / 2, 0, 0),
            rg.Point3d(width / 2, length / 2, height / 2),
            rg.Point3d(width / 2 + void_width / 2, length, height)
        ])

    # Create a surface from the void curve
    lofts = rg.Brep.CreateFromLoft([void_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
    if not lofts or len(lofts) == 0:
        return [building_box.ToBrep()]

    void_surface = lofts[0]

    # Split the building with the void surface
    split_breps = building_box.ToBrep().Split(void_surface, 0.01)

    # Return the resulting split geometry
    if split_breps and len(split_breps) > 1:
        return split_breps
    else:
        return [building_box.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(30, 20, 10, 5, void_type='curvilinear', seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(40, 25, 15, 10, void_type='faceted', seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(50, 30, 20, 8, void_type='curvilinear', seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(35, 22, 12, 6, void_type='faceted', seed=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(45, 35, 18, 7, void_type='curvilinear', seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
