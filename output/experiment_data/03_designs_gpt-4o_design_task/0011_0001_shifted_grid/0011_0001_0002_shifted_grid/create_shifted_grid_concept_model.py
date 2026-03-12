# Created for 0011_0001_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the 'Shifted Grid' metaphor by creating a 3D representation of a grid pattern that incorporates deviations from traditional orthogonal layouts. It begins with a regular grid and selectively shifts and rotates volumes, resulting in intersecting planes that suggest movement and dynamism. The model emphasizes varied circulation paths and distinct spatial zones, encouraging exploration and interaction with light and shadow through angled projections. The adaptability of spaces is also highlighted, allowing for diverse functionalities and experiences, thereby embodying the metaphor's essence of fluidity and innovation in design."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=10, shift_amount=2, height=5, angle=15):
    \"""
    Creates an architectural Concept Model embodying the 'Shifted Grid' metaphor.
    
    This function generates a series of intersecting planes and rotated volumes based on a regular grid pattern, 
    which are then selectively shifted and rotated to create dynamic and adaptable spatial arrangements. 
    The result is a collection of 3D geometries suggesting varied circulation paths and spatial zones.

    Parameters:
    - grid_size (int): The number of cells in the grid along one dimension. The grid is square.
    - shift_amount (float): The amount by which the elements in the grid are shifted, in meters.
    - height (float): The height of the volumes created, in meters.
    - angle (float): The angle in degrees by which the volumes are rotated to create dynamic intersections.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    import math
    
    random.seed(42)  # Ensures replicability

    model = []
    grid_spacing = 10  # Base spacing between grid lines in meters

    # Create the base grid of points
    points = []
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * grid_spacing
            y = j * grid_spacing
            points.append(Rhino.Geometry.Point3d(x, y, 0))

    # Create volumes on the grid, shifting and rotating some of them
    for pt in points:
        # Randomly decide whether to shift and rotate this volume
        if random.random() > 0.5:
            shift_vector = Rhino.Geometry.Vector3d(
                random.choice([-shift_amount, shift_amount]),
                random.choice([-shift_amount, shift_amount]),
                0
            )
            pt.Transform(Rhino.Geometry.Transform.Translation(shift_vector))
        
        # Create a basic volume (e.g., a box)
        base_origin = pt
        base_box = Rhino.Geometry.Box(
            Rhino.Geometry.Plane(base_origin, Rhino.Geometry.Vector3d.ZAxis),
            Rhino.Geometry.Interval(-grid_spacing / 2, grid_spacing / 2),
            Rhino.Geometry.Interval(-grid_spacing / 2, grid_spacing / 2),
            Rhino.Geometry.Interval(0, height)
        )
        
        # Rotate the box if necessary
        if random.random() > 0.5:
            rotation_axis = Rhino.Geometry.Vector3d(0, 0, 1)
            rotation_center = base_origin + Rhino.Geometry.Vector3d(0, 0, height / 2)
            rotation_angle = math.radians(random.choice([-angle, angle]))
            xform = Rhino.Geometry.Transform.Rotation(rotation_angle, rotation_axis, rotation_center)
            base_box.Transform(xform)
        
        # Convert the box to a Brep and add to the model
        model.append(base_box.ToBrep())

    return model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=12, shift_amount=3, height=6, angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=1.5, height=4, angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=1, height=10, angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=15, shift_amount=4, height=8, angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=2.5, height=3, angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
