# Created for 0001_0002_house_within_a_house.json

""" Summary:
The provided function `create_house_within_house_concept_model` generates an architectural concept model based on the "House within a house" metaphor by creating interlocking geometric forms that represent nested spaces. It defines an outer shell with lofted surfaces and rounded edges, symbolizing protection, while the inner sanctuary incorporates curvature, reflecting intimacy and retreat. The function also introduces transitional voids to enhance spatial relationships, allowing light and visual connections between layers. By varying dimensions and curvature, it explores the metaphor's essence, culminating in a model that visually communicates a layered hierarchy, transitioning from public openness to private sanctity."""

#! python 3
function_code = """def create_house_within_house_concept_model(outer_dims, inner_dims, height, curvature_factor=0.2):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.
    This model explores the idea of nesting and protection through interlocking curved and angular forms,
    emphasizing the transition from an outer protective shell to an inner sanctuary.

    Parameters:
    - outer_dims (tuple of floats): The dimensions (length, width) of the outer shell in meters.
    - inner_dims (tuple of floats): The dimensions (length, width) of the inner sanctuary in meters.
    - height (float): The height of the entire structure in meters.
    - curvature_factor (float): The factor to determine the curvature applied to the inner sanctuary, default is 0.2.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    # Define base outer shell as a lofted surface with curved edges
    outer_length, outer_width = outer_dims
    inner_length, inner_width = inner_dims
    
    # Define base curves for outer shell
    outer_curve_1 = rg.ArcCurve(rg.Arc(rg.Point3d(0, 0, 0), outer_length * 0.5, math.pi))
    outer_curve_2 = rg.ArcCurve(rg.Arc(rg.Point3d(0, 0, height), outer_length * 0.5, math.pi))
    
    outer_shell = rg.Brep.CreateFromLoft([outer_curve_1, outer_curve_2], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

    # Define inner sanctuary with curvature
    inner_points = [
        rg.Point3d(inner_length * 0.5, inner_width * 0.5, 0),
        rg.Point3d(-inner_length * 0.5, inner_width * 0.5, 0),
        rg.Point3d(-inner_length * 0.5, -inner_width * 0.5, 0),
        rg.Point3d(inner_length * 0.5, -inner_width * 0.5, 0)
    ]

    inner_curves = []
    for pt in inner_points:
        offset = pt * curvature_factor
        inner_curves.append(rg.LineCurve(pt, pt + offset))

    # Loft inner sanctuary
    inner_sanctuary = rg.Brep.CreateFromLoft(inner_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)[0]
    
    # Create a series of transitional voids
    voids = []
    void_height = height * 0.3
    for i in range(3):
        void_radius = (inner_length / 4) * (1 - i * 0.2)
        void_center = rg.Point3d(0, 0, void_height * (i + 1))
        void_sphere = rg.Sphere(void_center, void_radius)
        voids.append(void_sphere.ToBrep())

    # Return the list of 3D geometries: outer shell, inner sanctuary, and voids
    return [outer_shell, inner_sanctuary] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house_concept_model((10, 8), (6, 4), 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house_concept_model((15, 10), (7, 5), 6, curvature_factor=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house_concept_model((12, 9), (5, 3), 4, curvature_factor=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house_concept_model((20, 15), (10, 7), 8, curvature_factor=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house_concept_model((18, 12), (9, 6), 7, curvature_factor=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
