# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function, `create_concept_model_curved_partitions`, generates an architectural concept model that embodies the metaphor of "curved partitions." By utilizing parameters such as base radius, height, number of partitions, and curvature, the function creates a series of interlocking, flowing forms characterized by smooth curves. These elements suggest movement and continuity, reflecting the design task's emphasis on dynamic spatial organization. The model's partitions are designed to delineate spaces without rigid separations, promoting fluid interactions. By incorporating varying curvature and randomness, the generated model enhances the play of light and shadow, fostering an elegant and exploratory environment."""

#! python 3
function_code = """def create_concept_model_curved_partitions(base_radius=10, height=5, num_partitions=5, curvature=0.3):
    \"""
    Create an architectural concept model based on the metaphor of 'curved partitions'.

    This function generates a series of interlocking, flowing forms that suggest movement and continuity.
    The partitions are defined by curves, creating dynamic and fluid spatial organization.

    Parameters:
    - base_radius (float): The base radius of the circular boundary within which partitions are generated.
    - height (float): The height of the partitions.
    - num_partitions (int): The number of curved partitions to create.
    - curvature (float): The degree of curvature for the partitions; higher values create more pronounced curves.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # List to store the resulting breps
    breps = []

    # Generate curved partitions
    for i in range(num_partitions):
        angle_offset = random.uniform(0, 2 * math.pi)
        radius = base_radius + random.uniform(-curvature, curvature)
        circle = rg.Circle(rg.Plane.WorldXY, radius)
        partition_curve = circle.ToNurbsCurve()

        # Create the partition surface by extruding the curve
        partition_surface = rg.Surface.CreateExtrusion(partition_curve, rg.Vector3d(0, 0, height))

        # Convert the surface to a brep
        partition_brep = partition_surface.ToBrep()
        
        if partition_brep:
            breps.append(partition_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_curved_partitions(base_radius=15, height=7, num_partitions=8, curvature=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_curved_partitions(base_radius=12, height=6, num_partitions=6, curvature=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_curved_partitions(base_radius=20, height=10, num_partitions=10, curvature=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_curved_partitions(base_radius=18, height=8, num_partitions=7, curvature=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_curved_partitions(base_radius=25, height=12, num_partitions=9, curvature=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
