# Created for 0001_0004_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating concentric layers around an inner core. It defines the core as a simple sphere and constructs additional layers as hollow spheres, representing protection and nesting. The parameters for core radius, layer thickness, and the number of layers allow for variations in spatial hierarchy. Each layer enhances the interplay of exposure and seclusion, with the outer layers acting as a protective envelope. This approach emphasizes the experiential journey through the model, reflecting the metaphor's focus on privacy and layered spatial relationships."""

#! python 3
function_code = """def create_house_within_a_house_model(core_radius=5.0, layer_thickness=2.0, num_layers=3):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.
    This function uses concentric or interwoven layers to evoke a sense of nesting and protection.
    
    Parameters:
    - core_radius (float): Radius of the inner sanctuary or core space in meters.
    - layer_thickness (float): Thickness of each protective layer surrounding the core in meters.
    - num_layers (int): Number of concentric layers surrounding the core.
    
    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    
    # List to store the resulting geometries
    geometries = []
    
    # Create the inner core, a sphere for simplicity
    core = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d(0, 0, 0), core_radius))
    geometries.append(core)
    
    # Create concentric layers around the core
    for i in range(1, num_layers + 1):
        outer_radius = core_radius + i * layer_thickness
        outer_sphere = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d(0, 0, 0), outer_radius))
        
        # Create the layer as a shell by subtracting the previous layer
        if i == 1:
            inner_sphere = core
        else:
            inner_radius = core_radius + (i - 1) * layer_thickness
            inner_sphere = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d(0, 0, 0), inner_radius))
        
        layer = rg.Brep.CreateBooleanDifference([outer_sphere], [inner_sphere], 0.01)
        if layer:
            geometries.append(layer[0])
    
    # Returning the list of geometries
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_a_house_model(core_radius=10.0, layer_thickness=3.0, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_a_house_model(core_radius=7.0, layer_thickness=1.5, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_a_house_model(core_radius=6.0, layer_thickness=2.5, num_layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_a_house_model(core_radius=8.0, layer_thickness=2.0, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_a_house_model(core_radius=12.0, layer_thickness=4.0, num_layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
