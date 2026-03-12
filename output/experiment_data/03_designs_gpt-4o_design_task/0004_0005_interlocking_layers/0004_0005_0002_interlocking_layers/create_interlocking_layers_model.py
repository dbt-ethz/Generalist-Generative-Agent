# Created for 0004_0005_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the "Interlocking Layers" metaphor by creating multiple overlapping planes or volumes that embody the metaphor's dynamic nature. It takes parameters such as the number of layers, base size, height variation, and overlap factor, allowing for a varied and intricate composition. Each layer is positioned with random offsets to enhance the overlap and complexity, while varying heights contribute to a multifaceted silhouette. The resulting geometries reflect the interplay between openness and seclusion, showcasing a structural complexity that aligns with the metaphor's emphasis on interconnected yet distinct spatial experiences."""

#! python 3
function_code = """def create_interlocking_layers_model(layer_count=5, base_size=10.0, height_variation=3.0, overlap_factor=0.3):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor. This model consists of multiple
    intersecting and overlapping planes or volumes to reflect the metaphor's dynamic and multifaceted form.

    Parameters:
    - layer_count (int): The number of interlocking layers to create.
    - base_size (float): The base size of each layer in meters.
    - height_variation (float): The variation in height between layers in meters.
    - overlap_factor (float): The degree to which layers overlap each other, expressed as a fraction of the base size.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the layers.
    \"""
    import Rhino
    import random
    import System

    # Ensure repeatability by setting a random seed
    random.seed(42)

    # Create a list to hold the generated Brep geometries
    breps = []

    # Loop through the number of layers to create
    for i in range(layer_count):
        # Calculate random offsets for each layer
        x_offset = random.uniform(-overlap_factor * base_size, overlap_factor * base_size)
        y_offset = random.uniform(-overlap_factor * base_size, overlap_factor * base_size)
        z_offset = i * height_variation
        
        # Create a base plane for the layer
        base_plane = Rhino.Geometry.Plane(Rhino.Geometry.Point3d(x_offset, y_offset, z_offset), Rhino.Geometry.Vector3d.ZAxis)
        
        # Define the corners of the rectangle for this layer
        corner1 = base_plane.PointAt(-base_size / 2, -base_size / 2)
        corner2 = base_plane.PointAt(base_size / 2, -base_size / 2)
        corner3 = base_plane.PointAt(base_size / 2, base_size / 2)
        corner4 = base_plane.PointAt(-base_size / 2, base_size / 2)
        
        # Create the rectangular profile for this layer
        rectangle_corners = [corner1, corner2, corner3, corner4, corner1]
        polyline = Rhino.Geometry.Polyline(rectangle_corners)
        rectangle = polyline.ToNurbsCurve()
        
        # Extrude the rectangle to form a 3D volume
        extrusion_vector = Rhino.Geometry.Vector3d(0, 0, random.uniform(1, height_variation))
        extrusion = Rhino.Geometry.Extrusion.Create(rectangle, extrusion_vector.Z, True)
        brep = extrusion.ToBrep()
        
        # Add the Brep to the list
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(layer_count=7, base_size=15.0, height_variation=4.0, overlap_factor=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(layer_count=10, base_size=12.0, height_variation=2.5, overlap_factor=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(layer_count=6, base_size=20.0, height_variation=5.0, overlap_factor=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(layer_count=8, base_size=18.0, height_variation=6.0, overlap_factor=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(layer_count=5, base_size=25.0, height_variation=3.5, overlap_factor=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
