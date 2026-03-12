# Created for 0012_0002_twisted_volumes.json

""" Summary:
The function `construct_twisted_volumes` generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates a series of interlocking, spiraling modules by defining base square prisms, which are then twisted at incremental angles and vertically spaced. This twisting evokes fluidity and dynamic spatial interactions, allowing for overlapping spaces that foster unique experiences and views. The varied heights and angles enhance light play across the surfaces, highlighting the transformation and energy of the structure. Ultimately, the model visually captures the metaphor's essence, reflecting movement and innovation in architectural design."""

#! python 3
function_code = """def construct_twisted_volumes(base_size, height, num_modules, twist_step, vertical_gap):
    \"""
    Constructs an architectural Concept Model using the 'Twisted volumes' metaphor.
    Creates a series of interlocking, spiraling quadrilateral prisms that evoke a sense of motion and dynamic spatial interactions.

    Parameters:
    - base_size (float): The side length of the square base of each module in meters.
    - height (float): The height of each module in meters.
    - num_modules (int): The number of modules to be created.
    - twist_step (float): The incremental twist angle (in degrees) applied between consecutive modules.
    - vertical_gap (float): The vertical gap between each module to enhance spatial layering.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize the list to store the resulting Breps
    twisted_volumes = []

    # Base plane for the first module
    base_plane = rg.Plane.WorldXY

    for i in range(num_modules):
        # Define the base square points
        base_points = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_size, 0, 0),
            rg.Point3d(base_size, base_size, 0),
            rg.Point3d(0, base_size, 0)
        ]

        # Create a polyline from the base points
        base_polyline = rg.Polyline(base_points + [base_points[0]])

        # Create a surface from the base polyline
        base_surface = rg.Brep.CreatePlanarBreps(base_polyline.ToNurbsCurve())[0]

        # Extrude the planar surface to create a prismatic module
        extrusion_vector = rg.Vector3d(0, 0, height)
        extrusion = rg.Extrusion.Create(base_polyline.ToNurbsCurve(), height, True)
        module_brep = extrusion.ToBrep()

        # Calculate the twist angle for the current module
        twist_angle_rad = math.radians(twist_step * i)

        # Define the twist transformation
        twist_axis = rg.Line(base_plane.Origin, base_plane.Origin + rg.Vector3d(0, 0, height))
        twist_transform = rg.Transform.Rotation(twist_angle_rad, twist_axis.Direction, twist_axis.From)

        # Apply the twist transformation
        twisted_module = module_brep.Duplicate()
        twisted_module.Transform(twist_transform)

        # Apply a vertical translation to create spacing between modules
        vertical_translation = rg.Transform.Translation(0, 0, i * (height + vertical_gap))
        twisted_module.Transform(vertical_translation)

        # Add the twisted module to the list of Breps
        twisted_volumes.append(twisted_module)

    return twisted_volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = construct_twisted_volumes(2.0, 3.0, 10, 15, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = construct_twisted_volumes(1.5, 4.0, 8, 10, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = construct_twisted_volumes(3.0, 2.5, 12, 20, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = construct_twisted_volumes(2.5, 5.0, 15, 25, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = construct_twisted_volumes(1.0, 2.0, 5, 30, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
