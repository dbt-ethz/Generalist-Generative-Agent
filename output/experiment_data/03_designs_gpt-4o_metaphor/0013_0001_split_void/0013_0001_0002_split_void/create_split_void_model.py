# Created for 0013_0001_split_void.json

""" Summary:
The `create_split_void_model` function generates an architectural concept model based on the metaphor "Split void," which emphasizes a clear division within a central open space. By defining the model's dimensions and a split ratio, the function creates two distinct geometrical zones, enhancing interactions with light and shadow. It constructs a base surface and introduces a split surface to visually represent the division. This approach fosters a sense of openness and movement while maintaining a cohesive architectural identity, allowing for dynamic spatial experiences that align with the metaphor's key traits of contrast and duality."""

#! python 3
function_code = """def create_split_void_model(length, width, height, split_ratio=0.5):
    \"""
    Creates a conceptual architectural model based on the 'Split void' metaphor,
    characterized by a division within a central open space, leading to dynamic 
    interactions with light and shadow and creating distinct zones or pathways.

    Parameters:
    - length (float): The overall length of the model in meters.
    - width (float): The overall width of the model in meters.
    - height (float): The overall height of the model in meters.
    - split_ratio (float): The ratio at which the central space is split. 
                           Default is 0.5 (equal division).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the split void model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Ensure repeatability in randomness
    random.seed(42)

    # Calculate split position
    split_position = length * split_ratio

    # Create base surface representing the overall boundary
    base_surface = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height)))

    # Create the split void by subtracting two distinct zones
    void1 = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, rg.Interval(0, split_position), rg.Interval(0, width), rg.Interval(0, height)))
    void2 = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, rg.Interval(split_position, length), rg.Interval(0, width), rg.Interval(0, height)))

    # Create the split line or surface to emphasize the division
    split_plane = rg.Plane(rg.Point3d(split_position, 0, 0), rg.Vector3d(1, 0, 0))
    split_surface = rg.Brep.CreateFromSurface(rg.PlaneSurface(split_plane, rg.Interval(0, width), rg.Interval(0, height)))

    # Return all distinct volumes and split surface for visualization
    return [void1, void2, split_surface]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_model(10.0, 5.0, 3.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_model(15.0, 7.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_model(12.0, 6.0, 5.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_model(8.0, 4.0, 2.5, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_model(20.0, 10.0, 6.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
