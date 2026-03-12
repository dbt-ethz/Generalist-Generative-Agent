# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model that embodies the "Perforated vertical landscape" metaphor by creating a vertical grid structure. It utilizes randomization to determine the presence of solid cubes or voids within a defined three-dimensional grid, allowing light and air to permeate through the structure. The parameters, including grid spacing and void probability, control the density and arrangement of these elements, promoting a dynamic interplay between solid and void. The resulting model visually represents openness, connectivity, and a rhythmic pattern reminiscent of a natural lattice, fulfilling the design task effectively."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=10, grid_spacing=2, void_probability=0.3, seed=42):
    \"""
    Creates an architectural Concept Model that represents the 'Perforated vertical landscape' metaphor.
    
    This function generates a vertical grid or mesh structure with an interplay of solid and void, 
    promoting light and air flow through the structure. The model highlights the interlacing of solid 
    and void to evoke a natural lattice pattern.

    Parameters:
    - height (float): The total height of the structure in meters.
    - width (float): The width of the structure in meters.
    - depth (float): The depth of the structure in meters.
    - grid_spacing (float): The spacing between grid elements in meters.
    - void_probability (float): The probability (0 to 1) of creating a void instead of a solid at each grid point.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    breps = []

    # Create the vertical grid structure
    num_x = int(width / grid_spacing)
    num_y = int(height / grid_spacing)
    num_z = int(depth / grid_spacing)

    # Iterate over the grid and randomly generate voids or solids
    for x in range(num_x):
        for y in range(num_y):
            for z in range(num_z):
                # Determine if this grid cell should be a void or a solid
                if random.random() > void_probability:
                    # Create a solid cube
                    box = rg.Box(
                        rg.Plane.WorldXY,
                        rg.Interval(x * grid_spacing, (x + 1) * grid_spacing),
                        rg.Interval(z * grid_spacing, (z + 1) * grid_spacing),
                        rg.Interval(y * grid_spacing, (y + 1) * grid_spacing)
                    )
                    breps.append(box.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=15, depth=5, grid_spacing=3, void_probability=0.2, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, width=20, depth=15, grid_spacing=1, void_probability=0.4, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=12, depth=8, grid_spacing=2.5, void_probability=0.5, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=50, width=10, depth=10, grid_spacing=4, void_probability=0.1, seed=999)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, width=18, depth=12, grid_spacing=3.5, void_probability=0.25, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
