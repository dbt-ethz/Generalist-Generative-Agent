# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model that embodies the "Perforated vertical landscape" metaphor by constructing vertical columns and interspersed voids. Each column, represented as a cylinder, symbolizes tree trunks, while the voids, represented as spheres, facilitate light and air flow, enhancing the interaction between interior and exterior spaces. The parameters allow for customization of column height, radius, and void dimensions, resulting in a dynamic and organic composition. This model visually reflects the metaphor's essence through its rhythmic interplay of solid and void, promoting exploration and engagement with natural elements."""

#! python 3
function_code = """def create_perforated_vertical_landscape(column_height=10.0, column_radius=0.5, void_radius=1.5, num_columns=10):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    The model consists of a series of vertical columns interspersed with voids, creating a layered 
    effect that mimics a vertical forest. The columns represent tree trunks while the voids serve as 
    pathways allowing light and air to flow through, promoting interaction between interior and exterior spaces.

    Parameters:
    column_height (float): The height of each vertical column in meters.
    column_radius (float): The radius of each vertical column in meters.
    void_radius (float): The radius of each void in meters.
    num_columns (int): The number of columns to generate.

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for replicable randomness
    random.seed(42)

    # List to store the generated 3D geometries
    geometries = []

    # Base point for the structure
    base_point = rg.Point3d(0, 0, 0)

    # Create columns and voids
    for i in range(num_columns):
        # Randomly position columns in a grid-like layout
        x_offset = random.uniform(-5, 5)
        y_offset = random.uniform(-5, 5)
        
        # Create a column
        column_center = rg.Point3d(base_point.X + x_offset, base_point.Y + y_offset, base_point.Z)
        column = rg.Cylinder(rg.Circle(column_center, column_radius), column_height).ToBrep(True, True)
        
        # Create a void around the column
        void_center = rg.Point3d(column_center.X, column_center.Y, column_center.Z + column_height / 2)
        void = rg.Sphere(void_center, void_radius).ToBrep()

        # Add the column and void to the geometries list
        geometries.append(column)
        geometries.append(void)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(column_height=12.0, column_radius=0.6, void_radius=1.8, num_columns=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(column_height=8.0, column_radius=0.4, void_radius=1.2, num_columns=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(column_height=9.0, column_radius=0.7, void_radius=1.0, num_columns=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(column_height=15.0, column_radius=0.8, void_radius=2.0, num_columns=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(column_height=11.0, column_radius=0.5, void_radius=1.3, num_columns=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
