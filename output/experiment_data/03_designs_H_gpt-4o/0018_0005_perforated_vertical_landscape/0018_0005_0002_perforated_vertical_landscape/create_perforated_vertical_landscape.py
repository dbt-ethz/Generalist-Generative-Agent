# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model that embodies the "Perforated vertical landscape" metaphor by creating a series of vertically tapered columns interspersed with voids. This design mimics a vertical forest, with columns resembling tree trunks and voids acting as natural clearings. The function allows for customization of parameters such as column count, height, and layer configuration, ensuring varied spatial experiences. Utilizing materials that permit light and air flow, the model emphasizes the dynamic interplay between solid and void, promoting movement and interaction, and reinforcing the connection between interior and exterior environments."""

#! python 3
function_code = """def create_perforated_vertical_landscape(column_count=12, height=20.0, base_radius=0.5, top_radius=1.0, void_height=5.0, layers=3, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    The model consists of a series of vertical tapered columns interspersed with voids, creating a layered effect 
    that mirrors a vertical forest. The columns represent tree trunks while the voids function as clearings 
    or pathways, enhancing interaction between interior and exterior spaces.
    
    Parameters:
    column_count (int): The number of columns to generate.
    height (float): The height of each column in meters.
    base_radius (float): The radius of each column's base in meters.
    top_radius (float): The radius of each column's top in meters.
    void_height (float): The height of each void in meters.
    layers (int): Number of vertical layers of columns and voids.
    seed (int): The seed for the random number generator, ensuring replicability.
    
    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for replicable randomness
    random.seed(seed)

    # List to store the generated 3D geometries
    geometries = []

    # Base point for the structure
    base_point = rg.Point3d(0, 0, 0)

    # Calculate the total height of the structure with all layers
    total_height = height * layers + void_height * (layers - 1)

    # Create columns and voids
    for layer in range(layers):
        layer_base_z = layer * (height + void_height)

        for i in range(column_count):
            # Randomly position columns in a circular arrangement
            angle = random.uniform(0, 2 * 3.14159)
            radius = random.uniform(5, 10)
            x_offset = radius * math.cos(angle)
            y_offset = radius * math.sin(angle)

            # Create a tapered column
            bottom_center = rg.Point3d(base_point.X + x_offset, base_point.Y + y_offset, layer_base_z)
            top_center = rg.Point3d(base_point.X + x_offset, base_point.Y + y_offset, layer_base_z + height)
            bottom_circle = rg.Circle(bottom_center, base_radius)
            top_circle = rg.Circle(top_center, top_radius)
            column = rg.Brep.CreateFromLoft([bottom_circle.ToNurbsCurve(), top_circle.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
            
            geometries.append(column)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(column_count=10, height=15.0, base_radius=0.4, top_radius=0.8, void_height=4.0, layers=5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(column_count=8, height=25.0, base_radius=0.6, top_radius=1.2, void_height=6.0, layers=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(column_count=15, height=30.0, base_radius=0.5, top_radius=1.0, void_height=3.0, layers=6, seed=13)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(column_count=12, height=20.0, base_radius=0.5, top_radius=1.0, void_height=5.0, layers=3, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(column_count=20, height=18.0, base_radius=0.3, top_radius=0.7, void_height=4.5, layers=2, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
