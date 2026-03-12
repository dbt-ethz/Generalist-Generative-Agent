# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "curved partitions." It creates a series of interlocking, flowing 3D forms using parameters like base radius, height, and curvature strength. The model's organic shapes are defined by NURBS curves, which are lofted to create surfaces that suggest movement and continuity. By incorporating transparency and perforations, the design enhances light interplay, aligning with the metaphor's emphasis on dynamic spatial relationships. Ultimately, the function produces a model that embodies fluidity, calmness, and exploration, allowing for harmonious transitions between public and private spaces."""

#! python 3
function_code = """def generate_curved_partition_model(base_radius, partition_height, num_partitions, curvature_strength, transparency_factor, seed=42):
    \"""
    Create an architectural Concept Model inspired by the metaphor of 'curved partitions'.

    This function generates a series of interlocking, flowing 3D forms that suggest movement and continuity.
    It uses curved partitions to define spaces that flow into one another, allowing for dynamic interaction
    of public and private spaces. The design emphasizes the interplay of light and shadow through the
    incorporation of transparency.

    Parameters:
    - base_radius: float, the base radius around which the partitions are organized.
    - partition_height: float, the height of each partition.
    - num_partitions: int, the number of partitions to generate.
    - curvature_strength: float, controls the degree of curvature and organic flow.
    - transparency_factor: float, controls the level of transparency, influencing light interaction.
    - seed: int, optional, seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    breps = []

    for i in range(num_partitions):
        # Define the base curve with random perturbations for organic shape
        angle = i * (2 * math.pi / num_partitions)
        perturbation = random.uniform(-curvature_strength, curvature_strength)
        control_points = [
            rg.Point3d(base_radius * math.cos(angle + perturbation), 
                       base_radius * math.sin(angle + perturbation), 0),
            rg.Point3d(base_radius * math.cos(angle + math.pi / num_partitions + perturbation), 
                       base_radius * math.sin(angle + math.pi / num_partitions + perturbation), 
                       partition_height / 2),
            rg.Point3d(base_radius * math.cos(angle + 2 * math.pi / num_partitions + perturbation), 
                       base_radius * math.sin(angle + 2 * math.pi / num_partitions + perturbation), 
                       partition_height)
        ]

        # Create a NURBS curve from control points
        curve = rg.NurbsCurve.Create(False, 3, control_points)

        # Create surface by lofting with a slight twist for dynamic flow
        loft = rg.Brep.CreateFromLoft([curve, curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Tight, False)
        if loft:
            loft_brep = loft[0]
            # Apply transparency by creating perforations
            if transparency_factor > 0:
                perforation_count = int(transparency_factor * 10)
                for _ in range(perforation_count):
                    perforation_center = rg.Point3d(
                        random.uniform(control_points[0].X, control_points[2].X),
                        random.uniform(control_points[0].Y, control_points[2].Y),
                        random.uniform(0, partition_height)
                    )
                    perforation_radius = random.uniform(0.1, 0.3) * transparency_factor
                    sphere = rg.Sphere(perforation_center, perforation_radius)
                    sphere_brep = sphere.ToBrep()
                    diff_result = rg.Brep.CreateBooleanDifference([loft_brep], [sphere_brep], 0.001)
                    if diff_result:
                        loft_brep = diff_result[0]

            breps.append(loft_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_curved_partition_model(5.0, 3.0, 10, 1.5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_curved_partition_model(7.0, 4.0, 12, 2.0, 0.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_curved_partition_model(6.0, 2.5, 15, 1.0, 0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_curved_partition_model(4.5, 3.5, 8, 1.2, 0.6, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_curved_partition_model(8.0, 5.0, 14, 2.5, 0.9, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
