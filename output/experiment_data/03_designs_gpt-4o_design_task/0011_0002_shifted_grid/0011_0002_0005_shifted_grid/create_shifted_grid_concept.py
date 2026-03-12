# Created for 0011_0002_shifted_grid.json

""" Summary:
The provided function, `create_shifted_grid_concept`, generates an architectural concept model based on the "Shifted Grid" metaphor by creating a series of staggered and misaligned volumes. It begins with a standard grid framework and introduces random shifts in the grid lines to produce irregular alignments. This results in a complex spatial arrangement that fosters movement and exploration within the structure. The function also incorporates varying extrusion heights to enhance the dynamism of the model, allowing for playful interactions with light and shadow. Ultimately, this approach captures the essence of fluidity and adaptability, aligning with the metaphor's implications."""

#! python 3
function_code = """def create_shifted_grid_concept(x_size, y_size, z_height, grid_size, shift_amount, layers, seed=42):
    \"""
    Create an architectural Concept Model based on the "Shifted Grid" metaphor.

    The function generates a series of staggered and misaligned volumes based on a regular grid,
    introducing shifts to create complex spatial relationships and interesting light and shadow effects.

    Parameters:
    - x_size (float): The total width of the model in the x-direction (meters).
    - y_size (float): The total depth of the model in the y-direction (meters).
    - z_height (float): The height of the model from base to top (meters).
    - grid_size (float): The size of each grid cell in meters.
    - shift_amount (float): The maximum amount by which grid lines can be shifted.
    - layers (int): The number of vertical layers to stack.
    - seed (int, optional): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Calculate the number of grid cells in x and y directions
    x_cells = int(x_size // grid_size)
    y_cells = int(y_size // grid_size)

    # Iterate over each layer
    for layer in range(layers):
        z_offset = layer * (z_height / layers)

        # Create shifted grid for each layer
        for i in range(x_cells):
            for j in range(y_cells):
                # Introduce randomness in shifting the grid
                x_shift = random.uniform(-shift_amount, shift_amount)
                y_shift = random.uniform(-shift_amount, shift_amount)

                # Define corner points of each cell with shifts
                pt1 = rg.Point3d(i * grid_size + x_shift, j * grid_size + y_shift, z_offset)
                pt2 = rg.Point3d((i + 1) * grid_size + x_shift, j * grid_size + y_shift, z_offset)
                pt3 = rg.Point3d((i + 1) * grid_size + x_shift, (j + 1) * grid_size + y_shift, z_offset)
                pt4 = rg.Point3d(i * grid_size + x_shift, (j + 1) * grid_size + y_shift, z_offset)

                # Create vertical extrusion height
                extrusion_height = random.uniform(0.5 * (z_height / layers), 1.5 * (z_height / layers))

                # Create base surface
                base_surface = rg.Brep.CreateFromCornerPoints(pt1, pt2, pt3, pt4, 0.01)
                
                # Extrude the base surface upwards to create a volume
                if base_surface:
                    boundary_curve = base_surface.DuplicateNakedEdgeCurves(True, False)
                    extrusion_vector = rg.Vector3d(0, 0, extrusion_height)
                    extrusion = rg.Extrusion.Create(boundary_curve[0], extrusion_vector.Z, True)
                    if extrusion:
                        geometries.append(extrusion.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept(10.0, 10.0, 5.0, 1.0, 0.5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept(15.0, 20.0, 10.0, 2.0, 1.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept(12.0, 15.0, 8.0, 1.5, 0.75, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept(8.0, 12.0, 6.0, 1.0, 0.3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept(20.0, 15.0, 12.0, 2.5, 2.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
