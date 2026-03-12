# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Perforated Vertical Landscape" metaphor. It creates a vertical grid or mesh structure, emphasizing both solid and void elements to enhance openness and connectivity. By manipulating parameters such as height, width, depth, and grid density, the function produces various iterations of the model. Each iteration employs randomization to determine whether specific points in the grid will be solid or void, mimicking the natural lattice effect. This approach fosters spatial interaction between interior and exterior environments, encapsulating the essence of the metaphor while allowing light and air to permeate the structure."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=10, grid_density=5):
    \"""
    Create an architectural Concept Model based on the 'Perforated Vertical Landscape' metaphor.
    
    This function generates a vertical grid or mesh structure that integrates verticality with 
    a lattice-like form, where the interplay of solid and void creates a sense of openness and connectivity.

    Parameters:
    - height (float): Total height of the model in meters. Default is 30 meters.
    - width (float): Width of the base of the model in meters. Default is 10 meters.
    - depth (float): Depth of the base of the model in meters. Default is 10 meters.
    - grid_density (int): Number of divisions in the grid along each axis. Default is 5.

    Returns:
    - List of breps: A list of 3D geometries representing the concept model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Ensure replicable randomness
    random.seed(42)

    # Create base points for the grid
    x_divisions = grid_density
    y_divisions = grid_density
    z_divisions = grid_density * 2  # Increase vertical divisions for verticality

    x_step = width / x_divisions
    y_step = depth / y_divisions
    z_step = height / z_divisions

    # Container for breps
    breps = []

    # Create vertical grid structure
    for i in range(x_divisions + 1):
        for j in range(y_divisions + 1):
            for k in range(z_divisions + 1):
                # Randomly decide if this point will create a solid or void
                if random.random() > 0.5:
                    # Create solid cube
                    x = i * x_step
                    y = j * y_step
                    z = k * z_step
                    box_corner = rg.Point3d(x, y, z)
                    box_size = min(x_step, y_step, z_step) * 0.8  # Ensure small gaps between cubes
                    box = rg.Box(rg.Plane(box_corner, rg.Vector3d(1, 0, 0), rg.Vector3d(0, 1, 0)), rg.Interval(0, box_size), rg.Interval(0, box_size), rg.Interval(0, box_size))
                    breps.append(box.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=15, depth=15, grid_density=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, width=12, depth=8, grid_density=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=20, depth=5, grid_density=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=20, width=10, depth=10, grid_density=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=50, width=25, depth=20, grid_density=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
