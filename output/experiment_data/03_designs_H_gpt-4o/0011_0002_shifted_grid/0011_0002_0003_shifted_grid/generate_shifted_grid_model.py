# Created for 0011_0002_shifted_grid.json

""" Summary:
The function `generate_shifted_grid_model` creates an architectural concept model inspired by the 'Shifted Grid' metaphor. It begins with a regular grid, applying systematic shifts to introduce irregularity and movement. By adjusting the grid lines and layering volumes with varied heights, the model embodies fluidity and dynamic spatial relationships. Each generated box represents a unique volume, contributing to an overall complex silhouette. The approach highlights light and shadow interactions, fostering a playful atmosphere and encouraging exploration. This adaptability in design allows for diverse uses and enhances occupant experience within the architectural space."""

#! python 3
function_code = """def generate_shifted_grid_model(grid_size, grid_spacing, shift_ratio, height_variation, num_layers, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    This function constructs a model by initially establishing a regular grid and subsequently 
    introducing systematic shifts and offsets to create interconnected and non-traditional volumes 
    and spaces. The design emphasizes movement, fluidity, and the dynamic interplay of light and shadow.

    Parameters:
    - grid_size (int): The number of cells along one side of the square grid.
    - grid_spacing (float): The distance between grid lines in meters.
    - shift_ratio (float): The ratio of grid_spacing used as the maximum shift for grid lines.
    - height_variation (float): The variability in height for each layer in meters.
    - num_layers (int): The number of vertical layers to stack.
    - seed (int, optional): Seed for random number generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Iterate over each layer to create shifted grids
    for layer in range(num_layers):
        z_height = layer * height_variation
        
        for i in range(grid_size):
            for j in range(grid_size):
                # Calculate base position with shifts
                x_shift = random.uniform(-shift_ratio, shift_ratio) * grid_spacing
                y_shift = random.uniform(-shift_ratio, shift_ratio) * grid_spacing
                base_point = rg.Point3d(i * grid_spacing + x_shift, j * grid_spacing + y_shift, z_height)

                # Create a box with varied height
                layer_height = height_variation + random.uniform(-0.5, 0.5) * height_variation
                box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis),
                             rg.Interval(0, grid_spacing),
                             rg.Interval(0, grid_spacing),
                             rg.Interval(0, layer_height))
                
                # Convert the box to Brep and add to geometries
                brep_box = box.ToBrep()
                geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_shifted_grid_model(10, 2.0, 0.3, 1.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_shifted_grid_model(8, 1.5, 0.2, 2.0, 4, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_shifted_grid_model(12, 3.0, 0.4, 1.0, 6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_shifted_grid_model(15, 2.5, 0.5, 1.2, 3, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_shifted_grid_model(6, 1.0, 0.1, 2.5, 7, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
