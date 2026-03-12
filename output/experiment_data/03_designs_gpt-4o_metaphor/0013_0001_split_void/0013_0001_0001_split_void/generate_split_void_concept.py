# Created for 0013_0001_split_void.json

""" Summary:
The function `generate_split_void_concept` creates an architectural concept model based on the metaphor "Split void." By defining parameters for height, width, depth, and a split ratio, it generates a central void that is divided into two distinct volumes, reflecting the metaphor's emphasis on separation and contrast. The function utilizes Rhino.Geometry to create geometric representations, including walls that enclose the volumes, enhancing the idea of duality and dynamic tension. This architectural model promotes varied interactions with light and space, aligning with the metaphor's essence of openness and movement while retaining a strong formal identity."""

#! python 3
function_code = """def generate_split_void_concept(height=10.0, width=20.0, depth=15.0, split_ratio=0.5):
    \"""
    Generates a conceptual architectural model based on the 'Split void' metaphor.
    
    Parameters:
    height (float): The height of the central void in meters.
    width (float): The total width of the structure in meters.
    depth (float): The depth of the structure in meters.
    split_ratio (float): The ratio at which the void is split, ranging from 0 to 1.
    
    Returns:
    list: A list of RhinoCommon Brep objects representing the architectural concept.
    \"""
    import Rhino.Geometry as rg
    
    # Create a central void as a box
    central_void = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
    
    # Calculate the split line based on the split_ratio
    split_line_x = width * split_ratio
    
    # Create two separate volumes by splitting the central void
    left_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, split_line_x), rg.Interval(0, depth), rg.Interval(0, height))
    right_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(split_line_x, width), rg.Interval(0, depth), rg.Interval(0, height))
    
    # Create walls to enclose the volumes
    left_wall = rg.Box(rg.Plane.WorldYZ, rg.Interval(-0.5, 0.5), rg.Interval(0, depth), rg.Interval(0, height))
    right_wall = rg.Box(rg.Plane.WorldYZ, rg.Interval(-0.5, 0.5), rg.Interval(0, depth), rg.Interval(0, height))
    
    # Move walls to their respective positions
    left_wall.Transform(rg.Transform.Translation(split_line_x, 0, 0))
    right_wall.Transform(rg.Transform.Translation(width - 0.5, 0, 0))
    
    # Return the conceptual model as a list of Breps
    return [central_void.ToBrep(), left_volume.ToBrep(), right_volume.ToBrep(), left_wall.ToBrep(), right_wall.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_split_void_concept(height=12.0, width=25.0, depth=10.0, split_ratio=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_split_void_concept(height=15.0, width=30.0, depth=20.0, split_ratio=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_split_void_concept(height=8.0, width=18.0, depth=12.0, split_ratio=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_split_void_concept(height=14.0, width=22.0, depth=16.0, split_ratio=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_split_void_concept(height=10.0, width=20.0, depth=15.0, split_ratio=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
