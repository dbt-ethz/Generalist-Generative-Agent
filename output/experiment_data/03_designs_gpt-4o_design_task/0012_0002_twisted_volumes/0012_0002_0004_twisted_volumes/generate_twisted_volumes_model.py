# Created for 0012_0002_twisted_volumes.json

""" Summary:
The provided function, `generate_twisted_volumes_model`, creates an architectural concept model inspired by the metaphor "Twisted volumes." It constructs a series of interlocking cylindrical forms that twist around a vertical axis, reflecting fluidity and motion. Each cylindrical layer is slightly rotated and vertically offset to enhance the dynamic interplay of angles and curves, fostering unique spatial experiences. The function allows for customization of parameters like base radius, height, twist angle, and the number of layers, which together influence the model's visual complexity and interaction with light. The result is a striking representation of movement and transformation in architectural design."""

#! python 3
function_code = """def generate_twisted_volumes_model(base_radius=5, height=20, twist_angle=45, num_layers=5):
    \"""
    Generates an architectural Concept Model based on the 'Twisted volumes' metaphor. The model consists of interlocking
    twisting cylindrical forms that create a dynamic and fluid architectural form.

    Parameters:
    base_radius (float): The radius of the base of each cylindrical module.
    height (float): The height of each cylindrical module.
    twist_angle (float): The angle by which each module is twisted relative to the one below it, in degrees.
    num_layers (int): The number of interlocking cylindrical layers to generate.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Helper function to create a twisted cylinder
    def create_twisted_cylinder(base_radius, height, twist_angle, z_offset):
        # Define base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        base_curve = base_circle.ToNurbsCurve()

        # Define top circle with twist
        angle_rad = math.radians(twist_angle)
        twisted_plane = rg.Plane.WorldXY
        twisted_plane.Rotate(angle_rad, rg.Vector3d.ZAxis)
        top_circle = rg.Circle(twisted_plane, base_radius)
        top_circle.Translate(rg.Vector3d(0, 0, height))
        top_curve = top_circle.ToNurbsCurve()

        # Loft between base and top circles
        loft = rg.Brep.CreateFromLoft([base_curve, top_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        twisted_cylinder = loft[0] if loft else None
        
        # Move the cylinder to the correct z offset
        if twisted_cylinder:
            translation = rg.Transform.Translation(rg.Vector3d(0, 0, z_offset))
            twisted_cylinder.Transform(translation)

        return twisted_cylinder

    # Generate twisted volumes
    volumes = []
    for i in range(num_layers):
        z_offset = i * (height * 0.8)  # overlap layers slightly
        cylinder = create_twisted_cylinder(base_radius, height, twist_angle * i, z_offset)
        if cylinder:
            volumes.append(cylinder)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_twisted_volumes_model(base_radius=6, height=15, twist_angle=30, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_twisted_volumes_model(base_radius=7, height=25, twist_angle=60, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_twisted_volumes_model(base_radius=5, height=10, twist_angle=90, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_twisted_volumes_model(base_radius=8, height=18, twist_angle=15, num_layers=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_twisted_volumes_model(base_radius=4, height=22, twist_angle=75, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
