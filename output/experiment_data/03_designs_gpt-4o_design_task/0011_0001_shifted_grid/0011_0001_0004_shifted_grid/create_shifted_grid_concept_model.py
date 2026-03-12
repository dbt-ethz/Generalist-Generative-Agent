# Created for 0011_0001_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the "Shifted Grid" metaphor by creating a dynamic 3D representation of a grid structure. It begins with a regular grid, then selectively shifts and rotates grid elements to introduce movement and fluidity. By manipulating geometry through random shifts and rotations, the model embodies diverse circulation paths and distinct spatial zones. The design encourages interaction with light and shadow by employing angled surfaces, resulting in varied projections. This adaptable model fosters exploration and discovery, aligning with the metaphors emphasis on innovative spatial experiences and flexibility."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=10, shift_amount=2, rotation_angle=15):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    The function generates a model starting with a regular grid pattern and selectively shifts
    and rotates certain elements to create a dynamic and fluid form. The resulting geometry includes
    intersecting planes and rotated volumes that embody varied circulation paths and distinct spatial zones. 
    The design experiments with light and shadow by introducing angled surfaces and projections.

    Parameters:
    grid_size (int): The size of the grid (number of units in each direction).
    shift_amount (float): The amount by which certain elements in the grid are shifted (in meters).
    rotation_angle (float): The angle by which certain volumes are rotated (in degrees).

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Add this line to resolve the error
    
    random.seed(42)  # Ensure replicable randomness
    
    geometries = []
    base_plane = rg.Plane.WorldXY
    
    # Create a regular grid of base points
    for i in range(grid_size):
        for j in range(grid_size):
            # Determine if this element should be shifted and rotated
            shift_x = random.choice([-shift_amount, 0, shift_amount])
            shift_y = random.choice([-shift_amount, 0, shift_amount])
            rotation = random.choice([-rotation_angle, 0, rotation_angle])
            
            # Create a base box at each grid point
            center = rg.Point3d(i, j, 0)
            box_size = rg.Interval(-0.5, 0.5)
            box = rg.Brep.CreateFromBox(rg.Box(base_plane, box_size, box_size, box_size))
            
            # Apply shift and rotation to the box
            translation = rg.Transform.Translation(shift_x, shift_y, 0)
            box.Transform(translation)
            
            if rotation != 0:
                rotation_point = rg.Point3d(i + shift_x, j + shift_y, 0)
                rotation_axis = base_plane.Normal
                rotation_transform = rg.Transform.Rotation(math.radians(rotation), rotation_axis, rotation_point)
                box.Transform(rotation_transform)
            
            geometries.append(box)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=15, shift_amount=3, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=1, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=12, shift_amount=2.5, rotation_angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=4, rotation_angle=90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=20, shift_amount=1.5, rotation_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
