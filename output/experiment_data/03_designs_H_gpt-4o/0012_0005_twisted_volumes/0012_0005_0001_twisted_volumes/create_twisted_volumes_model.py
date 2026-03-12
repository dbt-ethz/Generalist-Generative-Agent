# Created for 0012_0005_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model inspired by the metaphor "Twisted volumes." It constructs a series of interwoven and distorted rectangular prisms, each twisted around its axis, embodying fluidity and tension. By varying the number of twists, base dimensions, and twist angles, the function creates dynamic silhouettes that evoke movement and transformation. The resulting model features layered spatial experiences and innovative circulation paths, enhancing interactions between interior and exterior spaces. Additionally, the twisted forms facilitate intricate light and shadow play, reflecting the metaphor's emphasis on dynamic perception and visual connection."""

#! python 3
function_code = """def create_twisted_volumes_model(num_twists=3, base_width=5, base_depth=5, total_height=15, twist_increment=45):
    \"""
    Creates a Concept Model of 'Twisted Volumes' by generating a series of interwoven and contorted prisms.

    The function uses a series of rectangular prisms which are twisted around their central axis to embody
    fluidity and tension. This approach creates a dynamic and expressive silhouette, with innovative spatial
    experiences and circulation paths.

    Parameters:
    - num_twists (int): The number of complete twists for the entire structure.
    - base_width (float): The width of the base of the prism (in meters).
    - base_depth (float): The depth of the base of the prism (in meters).
    - total_height (float): The total height of the structure (in meters).
    - twist_increment (float): The degree of twist applied per segment (in degrees).

    Returns:
    - List of Rhino.Geometry.Brep: A list of Breps representing the twisted geometric forms.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []

    # Calculate height per segment
    num_segments = num_twists * 4  # four segments per twist
    segment_height = total_height / num_segments

    for i in range(num_segments):
        # Calculate the twist angle for the current segment
        current_twist = math.radians(twist_increment * i)

        # Create a rectangle at the base
        base_plane = rg.Plane.WorldXY
        base_rect = rg.Rectangle3d(base_plane, base_width, base_depth)

        # Create a rectangle at the top with the same dimensions
        top_plane = rg.Plane(base_plane)
        top_plane.Translate(rg.Vector3d(0, 0, segment_height))
        top_rect = rg.Rectangle3d(top_plane, base_width, base_depth)

        # Twist the top rectangle
        top_rect.Transform(rg.Transform.Rotation(current_twist, rg.Vector3d.ZAxis, top_plane.Origin))

        # Create a ruled surface between the base and top rectangle
        ruled_surface = rg.Brep.CreateFromLoft(
            [base_rect.ToNurbsCurve(), top_rect.ToNurbsCurve()],
            rg.Point3d.Unset,
            rg.Point3d.Unset,
            rg.LoftType.Straight,
            False
        )

        if ruled_surface:
            breps.append(ruled_surface[0])

        # Update the base rectangle to be the top rectangle for next iteration
        base_rect = top_rect

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(num_twists=5, base_width=4, base_depth=4, total_height=20, twist_increment=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(num_twists=2, base_width=6, base_depth=3, total_height=10, twist_increment=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(num_twists=4, base_width=3, base_depth=7, total_height=12, twist_increment=90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(num_twists=6, base_width=5, base_depth=2, total_height=18, twist_increment=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(num_twists=3, base_width=7, base_depth=5, total_height=25, twist_increment=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
