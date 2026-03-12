# Created for 0020_0005_stacked_forests.json

""" Summary:
The function `create_stacked_forests_volume` generates an architectural concept model inspired by the metaphor of 'Stacked forests.' It creates a series of cascading terraces or ledges, each representing different ecological layers, utilizing parameters like base dimensions, total height, and organic variation. The design emphasizes vertical integration, allowing light to filter through and casting dynamic shadows. By manipulating the size and shape of each layer, the function captures the natural stratification of a forest, reflecting its hierarchy and depth. The resulting 3D geometries embody a stepped silhouette reminiscent of a forest hillside, fostering a rich, immersive spatial experience."""

#! python 3
function_code = """def create_stacked_forests_volume(base_length, base_width, total_height, num_layers, organic_factor):
    \"""
    Creates an architectural Concept Model based on the 'Stacked forests' metaphor.
    
    This model generates a series of cascading terraces or ledges, each representing a unique ecological layer.
    The design focuses on vertical integration and the interplay of light and shadow, with a mix of linear 
    and organic shapes to capture the natural stratification of a forest.

    Parameters:
    - base_length (float): The total length of the model's base in meters.
    - base_width (float): The total width of the model's base in meters.
    - total_height (float): The total height of the model in meters.
    - num_layers (int): The number of layers to create, each representing an ecological layer.
    - organic_factor (float): A factor to introduce organic variation in the shapes (0 for none, higher for more).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness for reproducibility
    random.seed(42)
    
    # Initialize the list to store Brep geometries
    geometries = []

    # Calculate the height of each layer
    layer_height = total_height / num_layers
    
    # Base plane for the model
    base_plane = rg.Plane.WorldXY

    for i in range(num_layers):
        # Calculate dimensions for the current layer
        current_length = base_length * (1 - i / num_layers * 0.2)
        current_width = base_width * (1 - i / num_layers * 0.2)
        
        # Create a random organic shape by perturbing the corner points
        rectangle = rg.Rectangle3d(base_plane, current_length, current_width)
        corners = [rectangle.Corner(j) for j in range(4)]
        for j, corner in enumerate(corners):
            offset_x = random.uniform(-organic_factor, organic_factor)
            offset_y = random.uniform(-organic_factor, organic_factor)
            corners[j] = rg.Point3d(corner.X + offset_x, corner.Y + offset_y, corner.Z)

        # Create a surface from the perturbed rectangle
        polyline = rg.Polyline(corners + [corners[0]])
        loft_curve = rg.PolylineCurve(polyline)
        loft_surface = rg.Brep.CreateFromLoft([loft_curve], base_plane.Origin, base_plane.Origin, rg.LoftType.Normal, False)

        if loft_surface and len(loft_surface) > 0:
            loft_surface = loft_surface[0]
            # Translate the surface to the correct height
            translation = rg.Transform.Translation(0, 0, i * layer_height)
            loft_surface.Transform(translation)
            geometries.append(loft_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_volume(10.0, 5.0, 15.0, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_volume(12.0, 6.0, 20.0, 4, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_volume(8.0, 4.0, 10.0, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_volume(15.0, 7.0, 25.0, 3, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_volume(9.0, 4.5, 12.0, 7, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
