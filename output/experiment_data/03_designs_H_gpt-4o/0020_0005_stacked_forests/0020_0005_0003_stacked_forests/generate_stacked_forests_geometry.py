# Created for 0020_0005_stacked_forests.json

""" Summary:
The function `generate_stacked_forests_geometry` creates a 3D architectural concept model inspired by the "Stacked forests" metaphor, which emphasizes vertical stratification and organic forms. It generates a series of cascading terraces, each representing distinct ecological layers, by varying dimensions and applying randomness to mimic natural irregularities. The function calculates the height and dimensions for each layer, ensuring vertical connectivity and light penetration throughout the structure. The resulting geometries reflect the interplay of open and enclosed spaces, creating a dynamic silhouette that evokes a forest hillside, thus fulfilling the design task of embodying the metaphor's principles."""

#! python 3
function_code = """def generate_stacked_forests_geometry(base_length, base_width, total_height, num_layers, randomness_seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'Stacked forests' metaphor.
    
    This function creates a cascading series of terraces or ledges, each representing a unique ecological layer.
    The design intertwines vertical spaces to facilitate light penetration and shadow play. A mix of linear and
    organic shapes reflects the natural stratification and growth patterns of a forest.

    Parameters:
    - base_length (float): The initial length of the structure in meters.
    - base_width (float): The initial width of the structure in meters.
    - total_height (float): The total height of the entire structure in meters.
    - num_layers (int): The number of cascading layers or terraces.
    - randomness_seed (int): Seed for random operations to ensure result replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for replicable randomness
    random.seed(randomness_seed)

    geometries = []
    layer_height = total_height / num_layers
    current_height = 0

    for i in range(num_layers):
        # Calculate the base dimensions for this layer with organic variation
        length_variation = random.uniform(-0.2, 0.2) * base_length
        width_variation = random.uniform(-0.2, 0.2) * base_width
        current_length = base_length * (1 - i * 0.1) + length_variation
        current_width = base_width * (1 - i * 0.1) + width_variation
        
        # Create a base rectangle for this layer
        base_plane = rg.Plane(rg.Point3d(0, 0, current_height), rg.Vector3d.ZAxis)
        rectangle = rg.Rectangle3d(base_plane, current_length, current_width)
        
        # Offset the corners to add organic, forest-like irregularity
        corners = [rectangle.Corner(j) for j in range(4)]
        for j, corner in enumerate(corners):
            offset_x = random.uniform(-0.5, 0.5)
            offset_y = random.uniform(-0.5, 0.5)
            corners[j] = rg.Point3d(corner.X + offset_x, corner.Y + offset_y, corner.Z)
        
        # Create a lofted surface from the perturbed rectangle
        loft_curve = rg.PolylineCurve(corners + [corners[0]])
        loft_surface = rg.Brep.CreateFromLoft([loft_curve], base_plane.Origin, base_plane.Origin, rg.LoftType.Normal, False)
        
        if loft_surface and len(loft_surface) > 0:
            loft_surface = loft_surface[0]
            geometries.append(loft_surface)

        # Update height for the next layer
        current_height += layer_height

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_stacked_forests_geometry(10.0, 5.0, 15.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_stacked_forests_geometry(12.0, 6.0, 20.0, 5, randomness_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_stacked_forests_geometry(8.0, 4.0, 10.0, 3, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_stacked_forests_geometry(15.0, 7.0, 25.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_stacked_forests_geometry(14.0, 8.0, 18.0, 5, randomness_seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
