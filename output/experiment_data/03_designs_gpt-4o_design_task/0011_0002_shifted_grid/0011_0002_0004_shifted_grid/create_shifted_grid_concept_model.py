# Created for 0011_0002_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model by starting with a defined grid size and introducing random shifts to create an irregular layout. This approach embodies the "Shifted Grid" metaphor, emphasizing dynamic spatial relationships and movement. The function iterates through layers, producing boxes at grid points with offsets that result in varied volumes and spatial connections. The resulting geometry captures fluidity and unpredictability, allowing for exploration of light and shadow interactions. This model encourages adaptability in design, reflecting the metaphor's essence while fostering unique spatial experiences for occupants."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size, shift_amount, num_layers, layer_height, seed=42):
    \"""
    Create a conceptual architectural model based on the 'Shifted Grid' metaphor.
    
    This function generates a model starting with a regular grid and introduces deliberate
    shifts and offsets to create interconnected volumes and spaces. The resulting geometry
    emphasizes movement, fluidity, and interaction of light and shadow.
    
    Parameters:
    - grid_size (tuple): The size of the regular grid (x_count, y_count).
    - shift_amount (float): The maximum offset to shift the grid lines.
    - num_layers (int): The number of stacked layers of the grid.
    - layer_height (float): The height of each layer.
    - seed (int): Seed for random number generation to ensure replicable results.
    
    Returns:
    - list: A list of 3D geometries (Brep) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    x_count, y_count = grid_size
    geometries = []
    
    for layer in range(num_layers):
        # Calculate z-height for the current layer
        z_height = layer * layer_height
        
        for i in range(x_count):
            for j in range(y_count):
                # Calculate base position
                x_base = i * 1.0  # Assuming 1 meter spacing in grid
                y_base = j * 1.0
                
                # Introduce random shifts
                x_shift = random.uniform(-shift_amount, shift_amount)
                y_shift = random.uniform(-shift_amount, shift_amount)
                
                # Create a shifted box at this grid point
                base_point = rg.Point3d(x_base + x_shift, y_base + y_shift, z_height)
                x_interval = rg.Interval(0, 1)
                y_interval = rg.Interval(0, 1)
                z_interval = rg.Interval(0, layer_height)
                
                # Create a Box with intervals
                box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), x_interval, y_interval, z_interval)
                brep_box = box.ToBrep()
                
                geometries.append(brep_box)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model((5, 5), 0.5, 3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model((10, 10), 1.0, 4, 3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model((3, 3), 0.2, 2, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model((7, 7), 0.3, 5, 2.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model((4, 6), 0.4, 3, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
