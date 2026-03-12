# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern by creating a series of stacked cylindrical layers that simulate the stratification of a cave. Each layer's radius decreases progressively to evoke the feeling of descending into depth, while a central void represents a cavern's core space. The function incorporates random pathways between layers, enhancing the exploration theme. By adjusting parameters like base radius, layer thickness, and central void ratio, the model emphasizes vertical movement and varied spatial experiences, ultimately capturing the essence of immersion and mystery inherent in subterranean environments."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius=10, height_layers=5, layer_thickness=2, central_void_ratio=0.3):
    \"""
    Create an Architectural Concept Model evoking a 'subterranean cavern' metaphor using stacked layers
    with a central void, representing the stratification and depth of a cavern. The model focuses on vertical
    layering with a central atrium around which spaces spiral.

    Parameters:
    - base_radius: The radius of the lowest layer or base of the model in meters.
    - height_layers: The number of stacked layers representing different strata.
    - layer_thickness: The thickness of each layer in meters.
    - central_void_ratio: Ratio of the central void radius to the base_radius.

    Returns:
    - A list of RhinoCommon Brep objects representing the model's geometry.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability of randomness

    geometries = []

    # Define the central void
    central_void_radius = base_radius * central_void_ratio
    central_void = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, central_void_radius), layer_thickness * height_layers).ToBrep(True, True)

    # Create descending layers
    for i in range(height_layers):
        # Calculate current layer radius
        layer_radius = base_radius - (i * base_radius * 0.1)
        
        # Create the layer
        layer_base = rg.Circle(rg.Plane.WorldXY, layer_radius)
        layer_height = layer_thickness * (i + 1)
        layer = rg.Cylinder(layer_base, layer_thickness).ToBrep(True, True)
        
        # Move layer to appropriate height
        translation = rg.Transform.Translation(0, 0, -layer_height)
        layer.Transform(translation)
        
        # Subtract central void from layer
        layer_difference = rg.Brep.CreateBooleanDifference([layer], [central_void], 0.01)
        if layer_difference:
            layer = layer_difference[0]
        
        # Add to geometries list
        geometries.append(layer)

        # Spiral Pathway
        if i < height_layers - 1:
            angle = random.uniform(0, 2 * 3.1415)
            start_point = rg.Point3d(layer_radius * 0.9, 0, -layer_height)
            rotation = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, rg.Point3d.Origin)
            start_point.Transform(rotation)
            end_point = rg.Point3d(layer_radius * 0.9, 0, -(layer_height + layer_thickness))
            rotation_end = rg.Transform.Rotation(angle + 3.1415 / 2, rg.Vector3d.ZAxis, rg.Point3d.Origin)
            end_point.Transform(rotation_end)
            pathway = rg.LineCurve(start_point, end_point)
            geometries.append(pathway)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_radius=15, height_layers=6, layer_thickness=3, central_void_ratio=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_radius=12, height_layers=4, layer_thickness=2.5, central_void_ratio=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_radius=20, height_layers=8, layer_thickness=1.5, central_void_ratio=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_radius=18, height_layers=7, layer_thickness=2, central_void_ratio=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_radius=9, height_layers=5, layer_thickness=1, central_void_ratio=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
