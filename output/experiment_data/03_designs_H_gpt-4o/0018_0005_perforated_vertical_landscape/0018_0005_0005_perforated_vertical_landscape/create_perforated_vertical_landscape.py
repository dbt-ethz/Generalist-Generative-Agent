# Created for 0018_0005_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model that embodies the 'Perforated vertical landscape' metaphor by creating a series of tapered vertical columns that resemble tree trunks, interspersed with voids representing natural pathways. By utilizing parameters such as column dimensions, heights, and void probabilities, the function creates a dynamic arrangement that allows light and air to permeate through the structure. The random positioning of columns in a circular layout enhances the organic feel of a vertical forest, promoting interaction between interior and exterior spaces while emphasizing the metaphor's essence through a rhythmic interplay of solid and void forms."""

#! python 3
function_code = """def create_perforated_vertical_landscape(columns_base_radius=1.0, columns_top_radius=0.5, height=10.0, column_count=15, void_probability=0.3, seed=42):
    \"""
    Generates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.

    This function creates a series of tapered vertical columns interspersed with voids, resembling a vertical
    forest. The columns taper from a larger base to a smaller top, symbolizing tree trunks, while the voids
    serve as natural pathways allowing light and air penetration, promoting interaction between interior and
    exterior environments.

    Parameters:
    - columns_base_radius (float): The radius of the columns at the base in meters.
    - columns_top_radius (float): The radius of the columns at the top in meters.
    - height (float): The height of the columns in meters.
    - column_count (int): The number of columns to generate.
    - void_probability (float): The probability that a column will be a void.
    - seed (int): The seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the columns and voids.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    geometries = []

    for i in range(column_count):
        # Randomly position columns in a circular layout
        angle = (2 * math.pi / column_count) * i
        x = 10 * math.sin(angle)
        y = 10 * math.cos(angle)
        position = rg.Point3d(x, y, 0)

        # Decide if this column is a solid or a void
        if random.random() > void_probability:
            # Create a tapered column (solid)
            bottom_circle = rg.Circle(position, columns_base_radius)
            top_circle = rg.Circle(rg.Point3d(x, y, height), columns_top_radius)
            loft = rg.Brep.CreateFromLoft([bottom_circle.ToNurbsCurve(), top_circle.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft:
                geometries.append(loft[0])
        else:
            # Create a void as a tapered cylinder
            void_bottom_circle = rg.Circle(position, columns_base_radius * 1.5)
            void_top_circle = rg.Circle(rg.Point3d(x, y, height), columns_top_radius * 1.5)
            void_loft = rg.Brep.CreateFromLoft([void_bottom_circle.ToNurbsCurve(), void_top_circle.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if void_loft:
                geometries.append(void_loft[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(columns_base_radius=2.0, columns_top_radius=1.0, height=15.0, column_count=20, void_probability=0.4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(columns_base_radius=1.5, columns_top_radius=0.75, height=12.0, column_count=10, void_probability=0.2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(columns_base_radius=1.0, columns_top_radius=0.3, height=8.0, column_count=12, void_probability=0.5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(columns_base_radius=1.2, columns_top_radius=0.6, height=9.0, column_count=25, void_probability=0.1, seed=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(columns_base_radius=1.8, columns_top_radius=0.9, height=11.0, column_count=18, void_probability=0.35, seed=57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
