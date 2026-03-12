# Created for 0012_0001_twisted_volumes.json

""" Summary:
The provided function `create_twisted_volumes` generates an architectural concept model based on the metaphor of "Twisted volumes." By creating a series of twisted geometric forms, the function embodies dynamic and fluid characteristics, reflecting movement and tension. It manipulates spatial relationships by twisting the volumes, which results in innovative circulation paths and enhanced interaction between interior and exterior spaces. The twisting also allows for varied light and shadow effects, as different angles capture and reflect light throughout the day. The function generates multiple variations of these forms, enriching the design exploration process."""

#! python 3
function_code = """def create_twisted_volumes(height=10, width=5, depth=5, twist_angle=30):
    \"""
    Create an architectural Concept Model based on the metaphor 'Twisted volumes'.
    
    This function generates a series of twisted geometric volumes that embody dynamic and fluid forms.
    The twisting of the volumes suggests movement and tension, allowing for innovative spatial relationships
    and interactions between interior and exterior spaces. The design also plays with light and shadow due to
    the angles created by twisting the forms.

    Parameters:
    height (float): The height of the volumes in meters.
    width (float): The width of each volume in meters.
    depth (float): The depth of each volume in meters.
    twist_angle (float): The angle in degrees by which to twist the volumes.

    Returns:
    list: A list of 3D geometries (breps) representing the twisted volumes.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    from math import radians

    random.seed(42)  # Ensure replicability

    breps = []

    # Create base rectangle
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(width, 0, 0),
        rg.Point3d(width, depth, 0),
        rg.Point3d(0, depth, 0),
        rg.Point3d(0, 0, 0)  # Close the polyline by repeating the first point
    ]
    base_curve = rg.Polyline(base_corners)

    # Create the vertical extrusion path
    path = rg.Line(base_corners[0], rg.Point3d(0, 0, height))

    # Create a twisted volume by rotating the top face
    for i in range(3):  # Create three twisted volumes for variety
        angle = radians(twist_angle * (i + 1))
        rotation = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, rg.Point3d(0, 0, height))
        
        top_curve = base_curve.ToNurbsCurve()
        top_curve.Transform(rotation)
        top_curve.Translate(rg.Vector3d(0, 0, height))
        
        loft = rg.Brep.CreateFromLoft([base_curve.ToNurbsCurve(), top_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft and len(loft) > 0:
            breps.append(loft[0])

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes(height=15, width=6, depth=4, twist_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes(height=12, width=7, depth=3, twist_angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes(height=8, width=10, depth=5, twist_angle=90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes(height=20, width=8, depth=6, twist_angle=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes(height=18, width=9, depth=7, twist_angle=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
