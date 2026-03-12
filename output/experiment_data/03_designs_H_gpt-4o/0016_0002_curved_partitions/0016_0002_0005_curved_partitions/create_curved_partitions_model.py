# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "curved partitions" by creating a series of layered, sweeping curves that mimic natural landscapes. It employs parameters such as the number of layers, base dimensions, and curve intensity to craft a dynamic structure that emphasizes fluidity and spatial transitions. Each layer consists of interpolated curves that are lofted to form 3D geometries, allowing for varying degrees of openness and enclosure. This approach enhances light interplay and shadow patterns, inviting exploration and interaction, while maintaining an elegant aesthetic reflective of the metaphor's essence."""

#! python 3
function_code = """def create_curved_partitions_model(num_layers=6, base_length=15.0, base_width=10.0, curve_intensity=2.0, seed=42):
    \"""
    Create an architectural Concept Model inspired by the 'curved partitions' metaphor, using RhinoCommon.

    This function generates a landscape-like structure with layered, sweeping curves that represent the concept of curved partitions. 
    The design emphasizes fluidity, dynamic spatial transitions, and the interplay of light and shadow.

    Parameters:
    - num_layers (int): Number of curved layers to create.
    - base_length (float): Length of the base of each layer in meters.
    - base_width (float): Width of the base of each layer in meters.
    - curve_intensity (float): Determines the extent of the curve undulations.
    - seed (int): Random seed for replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    geometries = []

    for layer in range(num_layers):
        z_offset = layer * (base_width / num_layers)
        control_points = []

        for i in range(6):
            x = i * (base_length / 5)
            y = random.uniform(-curve_intensity, curve_intensity) + (layer * (curve_intensity / num_layers))
            control_points.append(rg.Point3d(x, y, z_offset))
        
        curve = rg.Curve.CreateInterpolatedCurve(control_points, 3)
        offset_curve = curve.Offset(rg.Plane.WorldXY, base_width, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]
        
        loft_curves = [curve, offset_curve]
        brep = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(num_layers=8, base_length=20.0, base_width=12.0, curve_intensity=3.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(num_layers=5, base_length=10.0, base_width=8.0, curve_intensity=1.5, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(num_layers=10, base_length=25.0, base_width=15.0, curve_intensity=4.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(num_layers=7, base_length=18.0, base_width=14.0, curve_intensity=2.5, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(num_layers=9, base_length=22.0, base_width=11.0, curve_intensity=2.8, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
