# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model that embodies the "Perforated vertical landscape" metaphor by creating a series of vertical layers composed of cylindrical columns and spherical voids. Each layer mimics a vertical forest, where columns represent tree trunks and voids serve as natural clearings. The design incorporates parameters such as layer height, column radius, and void spacing to achieve a harmonious balance between solid and void, promoting light and air passage. This structuring fosters movement and interaction, reflecting the metaphors essence of integrating interior and exterior environments, while encouraging exploration of the organic forms within the model."""

#! python 3
function_code = """def create_perforated_vertical_landscape(num_layers=5, layer_height=3.0, column_radius=0.4, void_radius=1.2, layer_spacing=1.5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.

    This model features a series of vertical layers, each composed of columns and interspersed voids,
    mimicking a vertical forest with tree trunks and natural clearings. The design allows light and air
    to pass through, fostering a connection between interior and exterior spaces.

    Parameters:
    - num_layers (int): The number of vertical layers to create.
    - layer_height (float): The height of each layer in meters.
    - column_radius (float): The radius of each column in meters.
    - void_radius (float): The radius of each void in meters.
    - layer_spacing (float): The vertical spacing between layers in meters.
    - seed (int): The seed for randomness to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for randomness
    random.seed(seed)

    # List to store the generated 3D geometries
    geometries = []

    for layer in range(num_layers):
        # Calculate the Z position of the current layer
        z_position = layer * (layer_height + layer_spacing)
        
        # Alternating columns and voids in each layer
        for i in range(6):  # Assume 6 positions per layer in a circular arrangement
            angle = i * (2 * math.pi / 6)
            x = 2 * void_radius * math.cos(angle)
            y = 2 * void_radius * math.sin(angle)

            # Create columns
            column_center = rg.Point3d(x, y, z_position)
            column = rg.Cylinder(rg.Circle(column_center, column_radius), layer_height).ToBrep(True, True)
            geometries.append(column)

            # Create voids as spheres at the same height
            if i % 2 == 0:  # Only create voids at alternate positions for variety
                void_center = rg.Point3d(x, y, z_position + layer_height / 2)
                void = rg.Sphere(void_center, void_radius).ToBrep()
                geometries.append(void)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(num_layers=7, layer_height=4.0, column_radius=0.5, void_radius=1.5, layer_spacing=2.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(num_layers=6, layer_height=2.5, column_radius=0.3, void_radius=1.0, layer_spacing=1.0, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(num_layers=4, layer_height=5.0, column_radius=0.6, void_radius=1.0, layer_spacing=1.2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(num_layers=8, layer_height=3.5, column_radius=0.45, void_radius=1.3, layer_spacing=1.8, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(num_layers=5, layer_height=3.5, column_radius=0.4, void_radius=1.0, layer_spacing=1.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
