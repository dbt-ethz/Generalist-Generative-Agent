# Created for 0012_0002_twisted_volumes.json

""" Summary:
The function `generate_twisted_volumes_with_voids` creates an architectural concept model inspired by the metaphor of "Twisted volumes." It generates a series of voxel-based structures that twist and interweave, embodying fluidity and motion. By varying the twist angle and incorporating voids, the model emphasizes dynamic spatial interactions and the contrast between solid and empty spaces. This manipulation of volumes fosters unique perspectives and circulation paths, enhancing the interplay of light and shadow. The resulting geometries reflect the transformative quality of the metaphor, capturing its essence while maintaining a coherent visual impact."""

#! python 3
function_code = """def generate_twisted_volumes_with_voids(voxel_size, twist_angle, num_voxels, num_twists):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor.
    This function generates a series of voxel-based twisting volumes, incorporating voids
    to emphasize light and shadow interplay and create dynamic spatial interactions.

    Parameters:
    - voxel_size (float): The side length of each voxel cube.
    - twist_angle (float): The angle in degrees by which the entire structure twists.
    - num_voxels (int): The number of voxels along one edge of the base grid.
    - num_twists (int): The number of full twists in the entire structure.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted voxel volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Calculate the total height of the structure
    height = voxel_size * num_voxels

    # List to store the resulting Breps
    breps = []
    
    # Angle increment for the twist
    angle_increment = math.radians(twist_angle) / (height * num_twists)

    # Create the voxel grid
    for x in range(num_voxels):
        for y in range(num_voxels):
            for z in range(num_voxels):
                # Skip some voxels to create voids
                if (x + y + z) % 2 == 0:
                    continue

                # Calculate the center of the voxel
                center = rg.Point3d(x * voxel_size, y * voxel_size, z * voxel_size)

                # Create a voxel (cube)
                voxel = rg.Box(rg.Plane(center, rg.Vector3d.ZAxis),
                               rg.Interval(-voxel_size / 2, voxel_size / 2),
                               rg.Interval(-voxel_size / 2, voxel_size / 2),
                               rg.Interval(-voxel_size / 2, voxel_size / 2)).ToBrep()

                # Apply the twist transformation
                twist_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height))
                current_angle = angle_increment * center.Z
                twist_transform = rg.Transform.Rotation(current_angle, twist_axis.Direction, twist_axis.From)

                voxel.Transform(twist_transform)

                # Add the twisted voxel to the list
                breps.append(voxel)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_twisted_volumes_with_voids(1.0, 45.0, 10, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_twisted_volumes_with_voids(0.5, 30.0, 8, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_twisted_volumes_with_voids(0.75, 60.0, 12, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_twisted_volumes_with_voids(1.5, 90.0, 6, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_twisted_volumes_with_voids(2.0, 15.0, 5, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
