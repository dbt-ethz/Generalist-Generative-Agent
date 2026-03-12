# Created for 0016_0005_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model by creating a series of undulating, curved partitions that embody the metaphor of "curved partitions." It utilizes parameters like base radius, height, and the number of partitions to define the model's dimensions. Each partition is formed by defining a path with organic curves that suggest fluidity and movement, reflecting natural elements. By extruding these curves into 3D shapes, the model achieves interconnected spaces that facilitate smooth transitions. Additionally, manipulating light and shadow through design enhances the atmosphere, inviting exploration and interaction within a tranquil environment, in line with the metaphor's essence."""

#! python 3
function_code = """def create_curved_partitions_model(base_radius=10.0, height=5.0, num_partitions=5, seed=42):
    \"""
    Generates an architectural Concept Model embodying the metaphor of 'curved partitions'.
    The model is characterized by fluid, wave-like contours that create interconnected spaces
    with a natural flow. The partitions are designed to suggest movement and exploration, with
    an interplay of light and shadow.

    Parameters:
    - base_radius (float): The radius of the base curve from which partitions emanate, in meters.
    - height (float): The height of the partitions, in meters.
    - num_partitions (int): The number of curved partitions to generate.
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Create a list to hold the resulting Brep geometries
    breps = []

    # Base circle for partition generation
    base_circle = rg.Circle(rg.Point3d(0, 0, 0), base_radius)
    
    # Generate partitions with organic curves
    for i in range(num_partitions):
        # Determine partition angle and offset
        angle = random.uniform(0, 2 * 3.14159)
        offset = random.uniform(-base_radius / 2, base_radius / 2)
        
        # Create a curve that defines the partition's path
        start_point = base_circle.PointAt(angle)
        end_point = rg.Point3d(start_point.X, start_point.Y, height)
        mid_point = rg.Point3d((start_point.X + end_point.X) / 2 + offset, 
                               (start_point.Y + end_point.Y) / 2 + offset / 2, 
                               height / 2)
        
        # Create a NurbsCurve for the partition
        curve = rg.NurbsCurve.Create(False, 3, [start_point, mid_point, end_point])
        
        # Check if curve creation was successful
        if curve:
            # Extrude the curve to form a partition
            extrusion = rg.Extrusion.Create(curve, height, True)
            partition = extrusion.ToBrep()
            
            # Add the partition to the list of Breps
            if partition:
                breps.append(partition)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(base_radius=15.0, height=7.0, num_partitions=8, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(base_radius=12.0, height=6.0, num_partitions=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(base_radius=20.0, height=10.0, num_partitions=6, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(base_radius=8.0, height=4.0, num_partitions=10, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(base_radius=14.0, height=5.5, num_partitions=7, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
