# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." It constructs a series of dynamic, angular surfaces arranged symmetrically around a central axis, emulating the metaphors emphasis on movement and depth. By incorporating variations in fold height and layering, the model achieves a complex spatial organization, reflecting intricate relationships between forms. The use of mirrored surfaces enhances the visual impact, creating a doubling effect that emphasizes symmetry. Ultimately, the function balances complexity and coherence, inviting exploration of the model's layered geometries while adhering to the design task's requirements."""

#! python 3
function_code = """def create_dynamic_mirrored_folded_planes_model(length=20.0, width=5.0, height=4.0, fold_variation=1.0, layers=3):
    \"""
    Generate an architectural Concept Model embodying the 'Mirrored folded planes' metaphor.

    This function constructs a series of dynamic, folded surfaces arranged symmetrically around a central axis.
    The design demonstrates movement and depth, enhanced through the interplay of shadows and reflections.
    Fold variations, layered planes, and symmetry contribute to a complex yet coherent spatial organization.

    Parameters:
    - length (float): The length of the model (in meters).
    - width (float): The width of each folded plane (in meters).
    - height (float): The height of each folded plane (in meters).
    - fold_variation (float): The variation in fold height to create dynamic forms (in meters).
    - layers (int): The number of layered planes on each side of the central axis.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    geometries = []
    central_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(length, 0, 0))

    for layer in range(layers):
        base_y = (layer * width) - (layers * width / 2)
        
        # Create dynamic folded planes
        for i in range(2):
            base_x = (i * length / 2)
            p1 = rg.Point3d(base_x, base_y, 0)
            p2 = rg.Point3d(base_x + length / 2, base_y, 0)
            fold_height = height + random.uniform(-fold_variation, fold_variation)
            p3 = rg.Point3d((base_x + base_x + length / 2) / 2, base_y + width, fold_height)
            
            # Create the folded surface
            folded_surface = rg.Brep.CreateFromCornerPoints(p1, p2, p3, p1, 0.001)
            if folded_surface:
                geometries.append(folded_surface)
    
    # Mirror the geometries across the central axis
    mirror_plane = rg.Plane(rg.Point3d(length / 2, 0, 0), rg.Vector3d(0, 1, 0))
    mirrored_geometries = [geo.DuplicateBrep() for geo in geometries]
    
    for geo in mirrored_geometries:
        geo.Transform(rg.Transform.Mirror(mirror_plane))
        geometries.append(geo)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_mirrored_folded_planes_model(length=30.0, width=6.0, height=5.0, fold_variation=2.0, layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_mirrored_folded_planes_model(length=25.0, width=4.0, height=3.0, fold_variation=1.5, layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_mirrored_folded_planes_model(length=15.0, width=7.0, height=6.0, fold_variation=3.0, layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_mirrored_folded_planes_model(length=40.0, width=8.0, height=7.0, fold_variation=1.0, layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_mirrored_folded_planes_model(length=22.0, width=5.5, height=4.5, fold_variation=1.2, layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
