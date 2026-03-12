# Created for 0001_0003_house_within_a_house.json

""" Summary:
The provided function `create_house_within_house_model` generates an architectural concept model based on the "House within a house" metaphor by creating two distinct yet interconnected volumes: an outer layer that serves as a protective shell and an inner layer representing a sanctuary. The function takes dimensions and material properties for both layers, allowing for variations in opacity to enhance the visual transition between public and private spaces. By incorporating random interlocking movements and creating geometries that represent the layers, the function emphasizes the dual nature of the design, facilitating exploration of spatial relationships and experiences inherent in the concept."""

#! python 3
function_code = """def create_house_within_house_model(outer_dimensions, inner_dimensions, outer_material_opacity, inner_material_opacity, interlock_depth, randomness_seed):
    \"""
    Creates a conceptual architectural model based on the 'House within a house' metaphor.
    
    The model consists of a dual-layered form where each layer serves a distinct function and spatial quality, 
    with an outer protective form and an inner sanctuary. The function returns a list of 3D geometries representing 
    these layers, incorporating interlocking volumes and transitions to emphasize the design concept.

    Parameters:
    - outer_dimensions: Tuple of 3 floats (length, width, height) representing the dimensions of the outer volume in meters.
    - inner_dimensions: Tuple of 3 floats (length, width, height) representing the dimensions of the inner volume in meters.
    - outer_material_opacity: Float (0.0 to 1.0) representing the opacity of the outer layer.
    - inner_material_opacity: Float (0.0 to 1.0) representing the opacity of the inner layer.
    - interlock_depth: Float representing the depth of interlocking between the outer and inner volumes.
    - randomness_seed: Integer seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the conceptual model's geometric entities.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)

    def create_box(center, dimensions):
        \"""Helper function to create a box Brep given a center point and dimensions.\"""
        length, width, height = dimensions
        corner1 = rg.Point3d(center.X - length / 2, center.Y - width / 2, center.Z - height / 2)
        corner2 = rg.Point3d(center.X + length / 2, center.Y + width / 2, center.Z + height / 2)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(corner1.X, corner2.X), rg.Interval(corner1.Y, corner2.Y), rg.Interval(corner1.Z, corner2.Z))
        return box.ToBrep()

    # Create base points for outer and inner volumes
    outer_center = rg.Point3d(0, 0, 0)
    inner_center = rg.Point3d(0, 0, 0)
    
    # Create outer and inner volumes
    outer_volume = create_box(outer_center, outer_dimensions)
    inner_volume = create_box(inner_center, inner_dimensions)

    # Interlock the volumes by moving the inner volume slightly within the outer volume
    move_vector = rg.Vector3d(random.uniform(-interlock_depth, interlock_depth),
                              random.uniform(-interlock_depth, interlock_depth),
                              random.uniform(-interlock_depth, interlock_depth))
    translation = rg.Transform.Translation(move_vector)
    inner_volume.Transform(translation)

    # Collect geometries
    geometries = [outer_volume, inner_volume]

    # Optionally, apply materials or visual properties (not represented in basic geometry creation)
    # In a real application, you might associate materials or opacity with these geometries.

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house_model((10, 8, 6), (6, 4, 3), 0.5, 0.8, 1.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house_model((12, 10, 7), (7, 5, 4), 0.6, 0.9, 1.5, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house_model((15, 12, 9), (8, 6, 5), 0.4, 0.7, 2.0, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house_model((20, 15, 10), (10, 8, 5), 0.3, 0.6, 0.5, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house_model((18, 14, 11), (9, 7, 6), 0.7, 0.5, 1.2, 57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
