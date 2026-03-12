# Created for 0012_0001_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model reflecting the metaphor "Twisted volumes" by creating a series of interlocking geometric forms that embody dynamic twisting and distortion. Each volume is defined by its base dimensions and a specified twist angle, allowing for exploration of varied spatial relationships and innovative circulation paths. The twisting action enhances light and shadow interplay on the surfaces, showcasing movement and energy. By manipulating parameters such as base dimensions and twist angles, the function outputs a diverse range of geometries, illustrating the metaphor's essence in architectural form and spatial interaction."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length, base_width, base_height, twist_angle, num_volumes):
    \"""
    Creates an architectural Concept Model inspired by the metaphor 'Twisted volumes'.
    
    The function generates a series of abstract, interlocking geometric forms that are rotated 
    and distorted, embodying the dynamic and fluid nature of twisting volumes. The design 
    explores spatial relationships, circulation paths, and the interplay of light and shadow.

    Parameters:
    - base_length (float): The length of the base of each volume in meters.
    - base_width (float): The width of the base of each volume in meters.
    - base_height (float): The height of each volume in meters.
    - twist_angle (float): The maximum angle of twist applied to each volume in degrees.
    - num_volumes (int): The number of twisted volumes to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted volumes.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Vector3d, Box, Plane, Transform, Line, Brep
    from scriptcontext import doc

    # Set a random seed for reproducibility
    random.seed(42)

    breps = []
    for i in range(num_volumes):
        # Define the base plane for each volume
        base_plane = Plane(Point3d(0, 0, i * base_height), Vector3d.ZAxis)
        
        # Create a box as the base volume
        base_box = Box(base_plane, Rhino.Geometry.Interval(0, base_length), Rhino.Geometry.Interval(0, base_width), Rhino.Geometry.Interval(0, base_height))
        
        # Convert the box to a Brep
        brep = base_box.ToBrep()
        
        # Define the axis of twist
        twist_axis = Line(base_plane.Origin, base_plane.Origin + Vector3d(0, 0, base_height))
        
        # Apply a twist deformation
        # Correct the method to generate a twisted brep
        edge_curves = brep.DuplicateEdgeCurves()
        
        # Correct the call to CreateFromLoft by passing the correct type
        twist_deformation = Brep.CreateFromLoft(edge_curves, twist_axis.From, twist_axis.To, Rhino.Geometry.LoftType.Straight, False)
        
        if twist_deformation:
            # Random twist angle
            angle_rad = Rhino.RhinoMath.ToRadians(random.uniform(0, twist_angle))
            
            # Apply rotation along the axis
            twist_deformation[0].Rotate(angle_rad, twist_axis.Direction, twist_axis.From)
            breps.append(twist_deformation[0])
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(5.0, 3.0, 10.0, 45.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(4.0, 2.5, 8.0, 30.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(6.0, 4.0, 12.0, 60.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(3.0, 2.0, 5.0, 90.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(7.0, 5.0, 15.0, 75.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
