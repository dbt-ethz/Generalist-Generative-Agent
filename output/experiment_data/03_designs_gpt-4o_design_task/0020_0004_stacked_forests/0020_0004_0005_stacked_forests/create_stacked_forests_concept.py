# Created for 0020_0004_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Stacked forests" metaphor, reflecting the complex interconnectivity of a forest ecosystem. It creates a lattice-like structure through interwoven horizontal and vertical elements, emphasizing layered spatial relationships. Each layer's height is defined in the input, allowing for varied vertical growth, while random placements of lines simulate organic forms. By combining rectilinear and curvilinear shapes, the model captures the unpredictable yet harmonious nature of forests. The resulting geometries, represented as 3D Breps, embody the essence of a forest's layered and dynamic silhouette, promoting exploration and interaction."""

#! python 3
function_code = """def create_stacked_forests_concept(height_layers, width, depth, num_verticals, num_horizontals, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Stacked forests' metaphor. The model is a lattice-like structure
    composed of interwoven horizontal and vertical elements, representing the dense interconnectivity of a forest.
    
    Parameters:
    - height_layers: List of floats representing the height of each layer in meters.
    - width: Float, the overall width of the structure in meters.
    - depth: Float, the overall depth of the structure in meters.
    - num_verticals: Integer, number of vertical elements per layer.
    - num_horizontals: Integer, number of horizontal elements per layer.
    - seed: Integer, random seed for reproducibility.
    
    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    geometries = []

    base_rect = rg.Rectangle3d(rg.Plane.WorldXY, width, depth)

    for i, layer_height in enumerate(height_layers):
        # Create a plane for each layer
        plane = rg.Plane(rg.Point3d(0, 0, sum(height_layers[:i])), rg.Vector3d.ZAxis)
        
        # Create vertical elements
        for _ in range(num_verticals):
            x = random.uniform(0, width)
            vertical_line = rg.Line(rg.Point3d(x, 0, plane.OriginZ), rg.Point3d(x, depth, plane.OriginZ + layer_height))
            vertical_brep = rg.Brep.CreateFromBox(vertical_line.BoundingBox)
            geometries.append(vertical_brep)

        # Create horizontal elements
        for _ in range(num_horizontals):
            y = random.uniform(0, depth)
            horizontal_line = rg.Line(rg.Point3d(0, y, plane.OriginZ), rg.Point3d(width, y, plane.OriginZ))
            thickness = random.uniform(0.5, 1.5)  # Random thickness for variation
            offset_curve = horizontal_line.ToNurbsCurve().Offset(rg.Plane.WorldXY, thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)
            if offset_curve:
                extrude_vector = rg.Vector3d(0, 0, layer_height)
                brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(offset_curve[0], extrude_vector))
                if brep:
                    geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept([2.0, 3.0, 1.5], 5.0, 5.0, 10, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept([1.0, 2.5, 3.5, 4.0], 7.0, 4.0, 8, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept([1.2, 2.5, 3.0, 2.0], 6.0, 6.0, 5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept([1.0, 1.5, 2.0, 2.5, 3.0], 10.0, 8.0, 12, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept([3.0, 4.0, 2.0, 5.0], 8.0, 6.0, 6, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
