# Created for 0013_0003_split_void.json

""" Summary:
The `create_split_void_concept_model` function generates an architectural concept model based on the "Split void" metaphor by creating a central void that divides the building's mass. This void is defined by a non-linear path, enhancing spatial dynamics and influencing circulation. The function constructs a base mass and extrudes the void to create a cutting surface, resulting in distinct zones that allow for varied interactions with light and shadow. The model emphasizes the contrast and duality inherent in the design, fostering opportunities for visual connections and layered perspectives, while maintaining a cohesive architectural identity."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, base_height, void_path, void_width, seed=42):
    \"""
    Creates a conceptual architectural model that embodies the 'Split void' metaphor.

    The model features a central void that divides the building form, providing spatial organization
    and opportunities for varied interactions with light and shadow. The void is shaped along a
    non-linear path to enrich spatial dynamics and influence the building's composition and user circulation.

    Parameters:
    - base_length (float): The length of the base form in meters.
    - base_width (float): The width of the base form in meters.
    - base_height (float): The height of the building form in meters.
    - void_path (list of tuples): A list of (x, y) coordinates defining the path of the void.
    - void_width (float): The width of the void in meters.
    - seed (int): A seed for randomization to ensure replicability. Defaults to 42.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep geometries representing the architectural model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Create the base solid mass
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height)).ToBrep()

    # Define the path of the void
    void_polyline_points = [rg.Point3d(pt[0], pt[1], 0) for pt in void_path]
    void_polyline = rg.Polyline(void_polyline_points)
    void_curve = void_polyline.ToNurbsCurve()

    # Extrude the void path to create a cutting surface
    void_curve_extrusion = rg.Extrusion.Create(void_curve, base_height, True)
    void_sweep = rg.SweepOneRail()
    void_sweep.AngleToleranceRadians = math.radians(1.0)
    void_sweep.SweepTolerance = 0.01

    # Create a cross-section for the void
    cross_section = rg.Rectangle3d(rg.Plane.WorldXY, void_width, base_height * 1.5).ToNurbsCurve()
    void_brep = void_sweep.PerformSweep(void_curve, cross_section)[0]

    # Split the base geometry with the void
    split_brep = rg.Brep.CreateBooleanDifference([base_box], [void_brep], 0.01)

    return split_brep if split_brep is not None else []"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10, 5, 15, [(0, 0), (5, 5), (10, 0)], 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(12, 8, 20, [(0, 0), (6, 4), (12, 0)], 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(15, 10, 25, [(0, 0), (7.5, 10), (15, 0)], 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(8, 4, 12, [(0, 0), (4, 2), (8, 0)], 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(20, 10, 30, [(0, 0), (10, 15), (20, 0)], 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
