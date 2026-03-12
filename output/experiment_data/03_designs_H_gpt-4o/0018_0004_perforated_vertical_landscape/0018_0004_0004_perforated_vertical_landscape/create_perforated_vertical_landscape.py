# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a vertical grid structure composed of cylindrical columns. Parameters such as height, width, depth, column radius, and grid density define the model's dimensions and complexity. The function incorporates randomness to determine which segments of the columns are solid or void, reflecting the interplay of solid and empty spaces. This design approach ensures that light and air flow through the structure, enhancing spatial interaction between interior and exterior environments, while the overall form evokes a natural lattice-like appearance, aligning with the metaphor's essence."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, column_radius, grid_density):
    \"""
    Creates an architectural Concept Model inspired by the 'Perforated vertical landscape' metaphor.
    
    This function constructs a vertical grid-like structure with cylindrical columns, where the
    interplay of solid and void allows for light and air to permeate, highlighting verticality 
    and openness. The density and arrangement of columns create a pattern evocative of a natural lattice.
    
    Parameters:
    - height (float): The total height of the model in meters.
    - width (float): The total width of the model in meters.
    - depth (float): The total depth of the model in meters.
    - column_radius (float): The radius of the cylindrical columns.
    - grid_density (int): The number of columns along the width and depth.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(42)  # Ensure replicability

    breps = []

    # Calculate spacing based on grid density
    x_spacing = width / (grid_density + 1)
    z_spacing = depth / (grid_density + 1)
    y_spacing = height / 10  # Divide height into segments to create a layered effect

    # Create vertical grid structure with cylindrical columns
    for i in range(1, grid_density + 1):
        for j in range(1, grid_density + 1):
            # Calculate grid point positions
            x = i * x_spacing
            z = j * z_spacing

            # Create a series of stacked cylinders to represent columns
            for k in range(10):
                # Randomly decide if this segment should be solid or void
                if random.random() > 0.4:  # 60% chance of being a solid segment
                    # Calculate segment start and end points
                    y_start = k * y_spacing
                    y_end = (k + 1) * y_spacing

                    # Create the base circle for the cylinder
                    base_center = rg.Point3d(x, y_start, z)
                    base_circle = rg.Circle(rg.Plane(base_center, rg.Vector3d.YAxis), column_radius)

                    # Create the cylinder
                    cylinder = rg.Cylinder(base_circle, y_spacing)
                    breps.append(cylinder.ToBrep(True, True))

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 5.0, 0.2, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 10.0, 8.0, 0.3, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 7.0, 6.0, 0.25, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 4.0, 0.15, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(20.0, 12.0, 10.0, 0.4, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
