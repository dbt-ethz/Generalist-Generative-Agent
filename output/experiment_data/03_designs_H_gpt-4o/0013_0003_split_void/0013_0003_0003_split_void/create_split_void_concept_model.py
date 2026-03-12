# Created for 0013_0003_split_void.json

""" Summary:
The provided function generates an architectural concept model embodying the "Split void" metaphor by creating a central void that influences spatial organization. It defines the building's base and utilizes a non-linear curve to represent the void, which splits the structure into distinct zones. The void enhances circulation, promotes visual connectivity, and introduces light and shadow dynamics, supporting varied programmatic functions. By offsetting the void curve and lofting it, the model achieves a dramatic, asymmetrical silhouette, reflecting the duality inherent in the design. This process results in a cohesive architectural identity that emphasizes separation and interaction."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, base_height, void_curve_points, seed=None):
    \"""
    Creates an architectural Concept Model exemplifying the 'Split void' metaphor with a non-linear void.

    The model uses a curve-defined void to split the structure, generating complex spatial dynamics and 
    enhancing the architectural composition. The void creates distinct spatial zones and varied circulation paths.

    Parameters:
    - base_length (float): The length of the building base in meters.
    - base_width (float): The width of the building base in meters.
    - base_height (float): The height of the building in meters.
    - void_curve_points (List[Tuple[float, float, float]]): Points defining a curve for the void path.
    - seed (int, optional): A seed for randomization to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    # Create the base solid as a box
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height)).ToBrep()

    # Create a curve for the void path
    void_curve = rg.Curve.CreateInterpolatedCurve([rg.Point3d(x, y, z) for x, y, z in void_curve_points], 3)

    # Offset the curve to create a void volume
    offset_distance = random.uniform(1, 3)  # Random offset within a range for visual interest
    void_curve_offset1 = void_curve.Offset(rg.Plane.WorldXY, offset_distance, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]
    void_curve_offset2 = void_curve.Offset(rg.Plane.WorldXY, -offset_distance, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]

    # Loft between the offset curves to create the void surface
    void_loft = rg.Brep.CreateFromLoft([void_curve_offset1, void_curve_offset2], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

    # Cap the loft to create a closed void Brep
    void_brep = void_loft.CapPlanarHoles(0.01)

    # Split the base geometry with the void
    split_breps = rg.Brep.CreateBooleanDifference([base_box], [void_brep], 0.01)

    return split_breps if split_breps else [base_box]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 5.0, 8.0, [(0, 0, 0), (5, 2, 3), (10, 0, 0)], seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15.0, 10.0, 12.0, [(0, 0, 0), (7, 5, 4), (15, 0, 0)], seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(20.0, 10.0, 15.0, [(0, 0, 0), (10, 7, 5), (20, 0, 0)], seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(12.0, 6.0, 10.0, [(0, 0, 0), (6, 3, 5), (12, 0, 0)], seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(18.0, 9.0, 14.0, [(0, 0, 0), (9, 4, 6), (18, 0, 0)], seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
