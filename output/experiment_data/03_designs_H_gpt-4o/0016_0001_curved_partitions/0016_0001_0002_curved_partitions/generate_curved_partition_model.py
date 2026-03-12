# Created for 0016_0001_curved_partitions.json

""" Summary:
The function `generate_curved_partition_model` creates an architectural concept model inspired by the metaphor of "curved partitions." It generates a series of interlocking, flowing forms that embody organic shapes, emphasizing movement and continuity. By defining control points for NURBS curves, the function ensures that the partitions have smooth, natural curves instead of rigid angles. The model's design allows for seamless transitions between spaces, enhancing light and shadow dynamics. This approach cultivates a calming environment, fostering exploration and interaction, ultimately resulting in a harmonious architectural space that reflects the metaphor's intent."""

#! python 3
function_code = """def generate_curved_partition_model(base_radius=10, height=6, partition_count=4, partition_width=1, seed=24):
    \"""
    Generates an architectural Concept Model based on the metaphor of 'curved partitions'.

    This function creates flowing, interlocking forms that suggest movement and continuity.
    It uses curved partitions to define spaces that transition smoothly, enhancing light
    and shadow interplay while maintaining a sense of openness.

    Parameters:
    - base_radius (float): The radius of the base circle from which partitions will originate.
    - height (float): The height of the partitions.
    - partition_count (int): The number of curved partitions to create.
    - partition_width (float): The width of each partition.
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    breps = []
    angle_increment = 2 * math.pi / partition_count

    for i in range(partition_count):
        # Calculate the base angle for each partition
        angle = i * angle_increment

        # Create control points for a NURBS curve with organic variations
        start_point = rg.Point3d(base_radius * math.cos(angle), 
                                 base_radius * math.sin(angle), 
                                 0)
        control_point1 = rg.Point3d((base_radius - partition_width) * math.cos(angle + angle_increment / 3), 
                                    (base_radius - partition_width) * math.sin(angle + angle_increment / 3), 
                                    height / 3 + random.uniform(-1, 1))
        control_point2 = rg.Point3d((base_radius + partition_width) * math.cos(angle + 2 * angle_increment / 3), 
                                    (base_radius + partition_width) * math.sin(angle + 2 * angle_increment / 3), 
                                    2 * height / 3 + random.uniform(-1, 1))
        end_point = rg.Point3d(base_radius * math.cos(angle + angle_increment), 
                               base_radius * math.sin(angle + angle_increment), 
                               height)

        # Create a NURBS curve
        nurbs_curve = rg.NurbsCurve.Create(False, 3, [start_point, control_point1, control_point2, end_point])

        # Create a surface by lofting the curve with a slight twist
        loft_curves = [nurbs_curve, nurbs_curve.DuplicateCurve()]
        loft_curves[1].Rotate(math.pi / 20, rg.Vector3d.ZAxis, rg.Point3d.Origin)

        loft_brep = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft_brep:
            breps.append(loft_brep[0])

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_curved_partition_model(base_radius=15, height=8, partition_count=6, partition_width=1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_curved_partition_model(base_radius=12, height=5, partition_count=5, partition_width=2, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_curved_partition_model(base_radius=20, height=10, partition_count=3, partition_width=2.5, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_curved_partition_model(base_radius=18, height=7, partition_count=8, partition_width=1, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_curved_partition_model(base_radius=14, height=9, partition_count=7, partition_width=1.2, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
