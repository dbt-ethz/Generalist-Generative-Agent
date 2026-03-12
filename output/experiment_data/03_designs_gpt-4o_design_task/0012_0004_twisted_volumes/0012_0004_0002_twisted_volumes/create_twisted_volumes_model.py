# Created for 0012_0004_twisted_volumes.json

""" Summary:
The `create_twisted_volumes_model` function generates an architectural concept model by embodying the 'Twisted volumes' metaphor. It constructs a series of overlapping and rotating volumes based on specified dimensions, number of volumes, and twist angles. Each volume is created as a block, which is then twisted to convey dynamic balance and fluidity. The function incorporates transparency through selective cutouts, enhancing the interplay of light and shadow. By varying parameters, the model explores unexpected spatial relationships and encourages interaction between interior and exterior spaces, ultimately reflecting the transformative energy described in the metaphor."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length, base_width, height, num_volumes, twist_angle, transparency_ratio):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor. This function generates a series of overlapping
    and twisting volumes that embody dynamic balance and interaction of light and shadow.

    Parameters:
    - base_length (float): The base length of each volume in meters.
    - base_width (float): The base width of each volume in meters.
    - height (float): The height of each volume in meters.
    - num_volumes (int): The number of volumes to generate in the model.
    - twist_angle (float): The maximum angle in degrees to twist each volume.
    - transparency_ratio (float): The ratio of transparent surfaces to total surfaces (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted volumes of the Concept Model.
    \"""
    import Rhino
    import System
    from Rhino.Geometry import Point3d, Box, Plane, Brep, Vector3d, Transform
    from random import seed, uniform

    # Set the seed for randomness
    seed(42)

    # List to store the resulting Breps
    breps = []

    # Calculate the step for transparency
    transparency_step = max(int(num_volumes * transparency_ratio), 1)

    for i in range(num_volumes):
        # Base plane for each volume
        base_plane = Plane(Point3d(0, 0, i * height * 0.5), Vector3d.ZAxis)

        # Create a base box for the volume
        box = Box(base_plane, Rhino.Geometry.Interval(0, base_length), Rhino.Geometry.Interval(0, base_width), Rhino.Geometry.Interval(0, height))

        # Transform the box into a Brep
        brep = box.ToBrep()

        # Apply a twist transformation
        twist_transform = Transform.Rotation(System.Math.PI * uniform(0, twist_angle) / 180.0, base_plane.Normal, base_plane.Origin)
        brep.Transform(twist_transform)

        # Add or subtract transparency
        if i % transparency_step == 0:
            # Create a cutout (void) by scaling down the brep
            scale_transform = Transform.Scale(base_plane, 0.8, 0.8, 0.8)
            brep.Transform(scale_transform)

        # Append the twisted and possibly transparent brep to the list
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(5.0, 3.0, 10.0, 8, 45, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(4.0, 2.5, 12.0, 10, 60, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(6.0, 4.0, 15.0, 6, 30, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(7.0, 5.0, 20.0, 12, 90, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(3.5, 2.0, 8.0, 5, 75, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
