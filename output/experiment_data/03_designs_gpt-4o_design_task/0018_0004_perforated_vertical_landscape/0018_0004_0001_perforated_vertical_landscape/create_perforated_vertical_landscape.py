# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The `create_perforated_vertical_landscape` function generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a vertical grid structure that alternates between solid and perforated columns. It uses parameters like height, width, depth, grid density, and perforation size to define the model's dimensions and aesthetics. The function employs randomness to determine which columns are solid and which have perforations, thereby reflecting the metaphors emphasis on light, air, and spatial interaction. The resulting geometry evokes a natural lattice, enhancing the connection between interior and exterior spaces while embodying verticality and openness."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, grid_density, perforation_size):
    \"""
    Creates an architectural Concept Model inspired by the 'Perforated vertical landscape' metaphor.
    
    Parameters:
    - height (float): The total height of the concept model in meters.
    - width (float): The total width of the concept model in meters.
    - depth (float): The total depth of the concept model in meters.
    - grid_density (int): The density of the vertical grid or mesh (number of divisions along the width and depth).
    - perforation_size (float): The size of the perforations in the grid structure.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    # Initialize container for breps
    breps = []

    # Calculate spacing based on grid density
    x_spacing = width / (grid_density + 1)
    z_spacing = depth / (grid_density + 1)

    # Create vertical grid structure
    for i in range(1, grid_density + 1):
        for j in range(1, grid_density + 1):
            # Calculate grid point positions
            x = i * x_spacing
            z = j * z_spacing

            # Create vertical column path
            start = rg.Point3d(x, 0, z)
            end = rg.Point3d(x, height, z)
            column = rg.Line(start, end)

            # Randomly decide if this column should be perforated
            if random.random() > 0.3:  # 70% chance of being a solid column
                # Create a solid column
                plane = rg.Plane(start, rg.Vector3d.ZAxis)
                cylinder = rg.Cylinder(rg.Circle(plane, perforation_size), height)
                breps.append(cylinder.ToBrep(True, True))
            else:
                # Create a perforated column with gaps
                segment_height = height / 10
                for k in range(10):
                    if k % 2 == 0:
                        segment_start = rg.Point3d(x, k * segment_height, z)
                        plane = rg.Plane(segment_start, rg.Vector3d.ZAxis)
                        segment_cylinder = rg.Cylinder(rg.Circle(plane, perforation_size), segment_height)
                        breps.append(segment_cylinder.ToBrep(True, True))

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 5.0, 4, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 8.0, 6.0, 5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 7.0, 4.0, 6, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(8.0, 10.0, 3.0, 3, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(20.0, 12.0, 7.0, 8, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
