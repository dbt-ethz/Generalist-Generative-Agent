# Created for 0016_0004_curved_partitions.json

""" Summary:
The function `create_curved_partition_concept_model` generates an architectural concept model that embodies the metaphor of "curved partitions." It creates a series of interwoven curved surfaces that symbolize fluidity and organic movement by utilizing elliptical arcs, which are extruded vertically to form partitions. These partitions are designed to promote smooth transitions and connections between spaces, reflecting a sense of natural progression. By varying parameters such as the number of partitions, space radius, and height, the model achieves diverse configurations that enhance light and shadow interplay, ultimately creating an inviting and serene environment that encourages exploration and engagement."""

#! python 3
function_code = """def create_curved_partition_concept_model(num_partitions=5, space_radius=10, height=3, seed=42):
    \"""
    Creates a conceptual architectural model based on the metaphor of 'curved partitions'.
    
    This function generates a series of interwoven curved partitions that suggest a dynamic flow and 
    harmonious spatial organization. The partitions are designed to reflect natural progression and 
    elegance through gentle curves, facilitating smooth transitions and creating an inviting environment.
    
    Inputs:
        num_partitions (int): The number of curved partitions to generate.
        space_radius (float): The approximate radius of the space the partitions occupy.
        height (float): The height of each partition.
        seed (int): A seed for randomness to ensure replicable results.
    
    Outputs:
        list: A list of RhinoCommon Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    random.seed(seed)
    
    partitions = []
    center_point = rg.Point3d(0, 0, 0)
    
    for i in range(num_partitions):
        # Randomly determine the start and end angles for the curve
        start_angle = random.uniform(0, 2 * 3.14159)
        end_angle = start_angle + random.uniform(1, 2) * 3.14159 / num_partitions
        
        # Create an elliptical arc to represent the curved partition
        major_radius = space_radius * random.uniform(0.6, 1.0)
        minor_radius = major_radius * random.uniform(0.3, 0.7)
        
        # Define the ellipse plane and the elliptical arc
        ellipse_plane = rg.Plane(center_point, rg.Vector3d.ZAxis)
        ellipse = rg.Ellipse(ellipse_plane, major_radius, minor_radius)
        arc = ellipse.ToNurbsCurve().Trim(start_angle, end_angle)
        
        # Create a surface by extruding the arc vertically
        extrusion_vector = rg.Vector3d(0, 0, height)
        partition_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(arc, extrusion_vector))
        
        partitions.append(partition_surface)
    
    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partition_concept_model(num_partitions=7, space_radius=15, height=4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_concept_model(num_partitions=3, space_radius=8, height=2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_concept_model(num_partitions=6, space_radius=12, height=5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_concept_model(num_partitions=4, space_radius=20, height=6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_concept_model(num_partitions=8, space_radius=18, height=7, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
