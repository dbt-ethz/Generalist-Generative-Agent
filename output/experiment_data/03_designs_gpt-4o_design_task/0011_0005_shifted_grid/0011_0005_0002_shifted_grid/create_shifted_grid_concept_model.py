# Created for 0011_0005_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the 'Shifted Grid' metaphor by creating a 3D grid of cubic volumes. It starts with a defined grid and applies random shifts and rotations to each volume, simulating a dynamic reconfiguration that embodies movement and fluidity. The function incorporates parameters for grid size, count, and transformation limits, resulting in staggered and skewed volumes that enhance spatial experiences and innovative circulation paths. The interaction of light and shadow is emphasized through the irregular arrangement of volumes, promoting adaptability and inviting exploration within the architectural design."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_grid_size=3, grid_count=4, max_shift=1.5, max_rotation=15):
    \"""
    Create a Concept Model based on the 'Shifted Grid' metaphor.
    
    This function generates a 3D architectural model by starting with a grid 
    of cubic volumes, then applying random shifts and rotations to create a 
    sense of fluidity and movement. The resulting model embodies dynamic 
    reconfiguration, diverse spatial experiences, and unique circulation paths 
    while playing with light and shadow through staggered volumes.
    
    Inputs:
    - base_grid_size: The size of each grid cell in meters (default is 3).
    - grid_count: The number of cells along each axis of the grid (default is 4).
    - max_shift: The maximum distance to shift each volume in meters (default is 1.5).
    - max_rotation: The maximum rotation angle in degrees to apply to each volume 
      (default is 15).
      
    Outputs:
    - A list of RhinoCommon Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(42)  # Ensuring replicable randomness
    
    volumes = []
    
    for i in range(grid_count):
        for j in range(grid_count):
            # Define the center of the current grid cell
            x = i * base_grid_size
            y = j * base_grid_size
            z = 0
            
            # Create a base cube
            base_cube = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(x, x + base_grid_size),
                rg.Interval(y, y + base_grid_size),
                rg.Interval(z, base_grid_size)
            )
            
            # Randomly shift the cube within the maximum shift limits
            shift_x = random.uniform(-max_shift, max_shift)
            shift_y = random.uniform(-max_shift, max_shift)
            shift_z = random.uniform(-max_shift, max_shift)
            
            # Create a transformation matrix for the shift
            move_transform = rg.Transform.Translation(shift_x, shift_y, shift_z)
            
            # Randomly rotate the cube around its center
            angle_rad = math.radians(random.uniform(-max_rotation, max_rotation))
            rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
            rotation_center = base_cube.Center
            rotate_transform = rg.Transform.Rotation(angle_rad, rotation_axis, rotation_center)
            
            # Apply transformations
            transformed_cube = base_cube.ToBrep()
            transformed_cube.Transform(move_transform)
            transformed_cube.Transform(rotate_transform)
            
            # Add the transformed cube to the list of volumes
            volumes.append(transformed_cube)
    
    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(base_grid_size=4, grid_count=5, max_shift=2.0, max_rotation=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(base_grid_size=2, grid_count=3, max_shift=1.0, max_rotation=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(base_grid_size=5, grid_count=6, max_shift=1.0, max_rotation=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(base_grid_size=3, grid_count=4, max_shift=2.0, max_rotation=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(base_grid_size=6, grid_count=3, max_shift=1.0, max_rotation=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
