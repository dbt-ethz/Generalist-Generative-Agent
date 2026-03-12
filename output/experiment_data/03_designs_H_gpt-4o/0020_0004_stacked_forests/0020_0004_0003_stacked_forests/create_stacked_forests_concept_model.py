# Created for 0020_0004_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept_model`, generates an architectural concept model inspired by the "Stacked forests" metaphor. It creates a network of interwoven horizontal and vertical elements that emulate the complexity and interconnectedness of forest ecosystems. The function utilizes parameters like base dimensions, number of layers, and densities to define the structure's scale and density. By combining rectilinear and organic shapes, it captures the forest's dynamic essence. The resulting model features varied heights and depths, symbolizing organic growth and spatial richness, ultimately fostering exploration and interaction within a layered architectural experience."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_dims, num_layers, horizontal_density, vertical_density, organic_variation):
    \"""
    Create an architectural Concept Model based on the 'Stacked forests' metaphor.

    This function generates a network of interwoven vertical and horizontal elements, 
    reflecting the dense interconnectivity of a forest. It combines rectilinear forms with 
    organic variations to create a dynamic structure that captures the essence of a forest ecosystem.

    Parameters:
    - base_dims: tuple of (float, float) representing the base dimensions of the model (width, depth).
    - num_layers: int, number of vertical layers to stack, representing different forest levels.
    - horizontal_density: int, number of horizontal elements per layer, representing pathways.
    - vertical_density: int, number of vertical elements per layer, representing trunks.
    - organic_variation: float, a factor influencing the organic deformation of elements (0 to 1).

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    width, depth = base_dims
    height_per_layer = 3.0  # Standard height for each vertical layer

    geometries = []

    # Create vertical elements
    for i in range(vertical_density):
        x_pos = random.uniform(0, width)
        y_pos = random.uniform(0, depth)
        for layer in range(num_layers):
            base_height = layer * height_per_layer
            line = rg.Line(rg.Point3d(x_pos, y_pos, base_height), rg.Point3d(x_pos, y_pos, base_height + height_per_layer))
            cylinder = rg.Cylinder(rg.Circle(line.From, 0.1), line.Length).ToBrep(True, True)
            if cylinder:
                geometries.append(cylinder)

    # Create horizontal elements with organic variations
    for layer in range(num_layers):
        base_height = layer * height_per_layer
        for _ in range(horizontal_density):
            start_point = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), base_height)
            end_point = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), base_height)

            curve = rg.LineCurve(start_point, end_point)
            midpoint = curve.PointAtNormalizedLength(0.5)
            deviation = random.uniform(-organic_variation, organic_variation)
            midpoint.Z += deviation

            nurbs_curve = rg.NurbsCurve.Create(False, 3, [curve.PointAtStart, midpoint, curve.PointAtEnd])
            
            if nurbs_curve and nurbs_curve.IsValid:
                extrusion = rg.Extrusion.Create(nurbs_curve, height_per_layer * 0.1, True)
                if extrusion:
                    brep = extrusion.ToBrep()
                    if brep:
                        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model((10.0, 10.0), 5, 15, 10, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model((20.0, 15.0), 3, 8, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model((12.0, 8.0), 4, 10, 7, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model((15.0, 10.0), 6, 12, 8, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model((25.0, 20.0), 7, 20, 12, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
