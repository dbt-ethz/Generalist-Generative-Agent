# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model based on the "Perforated Vertical Landscape" metaphor. It creates a vertical grid structure by defining a 3D grid of points within specified dimensions (height, width, depth) and a designated grid density. Randomly removing points simulates the interplay of solid and void, embodying the metaphor's essence of openness and connectivity. The resulting geometries resemble a lattice, enhancing light and air permeability, while fostering interaction between interior and exterior spaces. This approach captures the dynamic visual experience and spatial relationships suggested by the metaphor, reimagining natural landscapes in a vertical form."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height: float, width: float, depth: float, grid_density: int):
    \"""
    Creates a Concept Model of a 'Perforated Vertical Landscape' using a vertical grid or mesh structure.
    
    Parameters:
    - height (float): The total height of the structure in meters.
    - width (float): The total width of the structure in meters.
    - depth (float): The total depth of the structure in meters.
    - grid_density (int): The number of grid cells along the width and depth to control the perforation density.
    
    Returns:
    - List of RhinoCommon Brep: A list of 3D geometries representing the architectural concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Vector3d, Line, Brep, Mesh
    from Rhino.Geometry import Surface, MeshFace, Plane, Box, Interval
    
    random.seed(0)  # Ensures replicable randomness
    
    breps = []
    
    # Create a base grid of points
    x_interval = width / grid_density
    y_interval = depth / grid_density
    z_interval = height / (grid_density // 2)
    
    for i in range(grid_density + 1):
        for j in range(grid_density + 1):
            for k in range(grid_density // 2 + 1):
                # Randomly decide to remove some points to create voids
                if random.random() > 0.3:  # 70% chance to keep the point
                    x = i * x_interval
                    y = j * y_interval
                    z = k * z_interval

                    # Create a small box at each grid point to represent the grid element
                    base_point = Point3d(x, y, z)
                    box_plane = Plane(base_point, Vector3d.ZAxis)
                    box_size_x = x_interval * 0.8  # Slightly smaller than the grid to create gaps
                    box_size_y = y_interval * 0.8
                    box_size_z = z_interval * 0.8
                    
                    # Create intervals for the box size
                    x_size_interval = Interval(0, box_size_x)
                    y_size_interval = Interval(0, box_size_y)
                    z_size_interval = Interval(0, box_size_z)
                    
                    box = Box(box_plane, x_size_interval, y_size_interval, z_size_interval)
                    
                    # Convert the box to Brep and collect
                    brep = box.ToBrep()
                    if brep:
                        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 3.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 8.0, 4.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 2.5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(20.0, 10.0, 5.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 2.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
