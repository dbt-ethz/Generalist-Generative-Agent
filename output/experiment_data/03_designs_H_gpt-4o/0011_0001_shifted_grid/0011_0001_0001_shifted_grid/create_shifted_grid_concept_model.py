# Created for 0011_0001_shifted_grid.json

""" Summary:
The provided function, `create_shifted_grid_concept_model`, generates an architectural concept model based on the 'Shifted Grid' metaphor by manipulating a standard grid pattern. It creates a series of grid elements (surfaces and vertical features) that are randomly shifted and rotated, introducing dynamic spatial arrangements. This process allows for varied circulation paths and distinct zones, enhancing spatial experiences. The model incorporates angled surfaces to interact playfully with light and shadow, fostering adaptability for multiple functions. By varying parameters like grid size and shift limits, the function produces diverse architectural forms that embody the metaphor's essence."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, base_size=10, max_shift=3, max_angle=25):
    \"""
    Creates an architectural Concept Model embodying the 'Shifted Grid' metaphor.

    This function generates a series of intersecting surfaces and shifted volumetric elements
    based on a regular grid pattern. It selectively shifts and rotates elements to create
    dynamic spatial arrangements, promoting varied circulation paths and diverse spatial zones
    that enhance light and shadow interaction.

    Parameters:
    grid_size (int): Number of grid cells along one dimension; creates a square grid.
    base_size (float): Base size of each grid element in meters.
    max_shift (float): Maximum shift distance for grid elements in meters.
    max_angle (float): Maximum rotation angle for grid elements in degrees.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    geometries = []

    for i in range(grid_size):
        for j in range(grid_size):
            # Base point for each grid element
            base_point = rg.Point3d(i * base_size, j * base_size, 0)
            
            # Create a base surface as a plane
            plane = rg.Plane(base_point, rg.Vector3d.ZAxis)
            rectangle = rg.Rectangle3d(plane, base_size, base_size)
            surface = rg.Brep.CreateFromCornerPoints(rectangle.Corner(0), rectangle.Corner(1),
                                                     rectangle.Corner(2), rectangle.Corner(3), 0.01)
            
            # Randomly shift the surface
            shift_x = random.uniform(-max_shift, max_shift)
            shift_y = random.uniform(-max_shift, max_shift)
            shift_transform = rg.Transform.Translation(shift_x, shift_y, 0)
            surface.Transform(shift_transform)

            # Randomly rotate the surface around its center
            center_point = surface.GetBoundingBox(True).Center
            angle_rad = math.radians(random.uniform(-max_angle, max_angle))
            rotation_transform = rg.Transform.Rotation(angle_rad, rg.Vector3d.ZAxis, center_point)
            surface.Transform(rotation_transform)

            # Add the surface to the list of geometries
            geometries.append(surface)

            # Create and add a vertical element (column or wall) to introduce height and shadow play
            height = random.uniform(3, 6)
            column_corners = [
                rg.Point3d(base_point.X, base_point.Y, 0),
                rg.Point3d(base_point.X + 1, base_point.Y, 0),
                rg.Point3d(base_point.X + 1, base_point.Y, height),
                rg.Point3d(base_point.X, base_point.Y, height)
            ]
            column = rg.Brep.CreateFromCornerPoints(column_corners[0], column_corners[1],
                                                    column_corners[2], column_corners[3], 0.01)
            column.Transform(shift_transform)
            column.Transform(rotation_transform)
            geometries.append(column)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=7, base_size=12, max_shift=4, max_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=4, base_size=8, max_shift=2, max_angle=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=6, base_size=15, max_shift=5, max_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=5, base_size=10, max_shift=2, max_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=3, base_size=20, max_shift=1, max_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
