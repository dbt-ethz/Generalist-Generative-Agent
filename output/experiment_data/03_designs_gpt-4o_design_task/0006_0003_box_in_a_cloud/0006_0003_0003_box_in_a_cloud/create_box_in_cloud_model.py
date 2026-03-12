# Created for 0006_0003_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_model`, generates an architectural concept model encapsulating the "Box in a Cloud" metaphor. It constructs a solid, geometric core ("box") using defined dimensions and robust materials, reflecting stability and permanence. Surrounding this core, the function creates a fluid, amorphous outer layer ("cloud") composed of semi-transparent surfaces that evoke lightness and ethereality. By manipulating parameters such as cloud radius and density, the model explores the dynamic interplay between the solid box and the fluid cloud, emphasizing contrasts in opacity and translucency. This results in a visually compelling dialogue between the two forms."""

#! python 3
function_code = """def create_box_in_cloud_model(box_length=10, box_width=10, box_height=15, cloud_radius=20, cloud_density=10):
    \"""
    Creates an architectural Concept Model embodying the 'Box in a Cloud' metaphor.
    
    This function generates a geometric form where a solid, angular core ('box') is surrounded by a more fluid,
    dynamic outer form ('cloud'). The box is represented by a Brep, while the cloud consists of a collection
    of semi-transparent surfaces that create a nebulous envelope around the core.

    Parameters:
        box_length (float): The length of the box in meters.
        box_width (float): The width of the box in meters.
        box_height (float): The height of the box in meters.
        cloud_radius (float): The radius of the cloud-like envelope.
        cloud_density (int): The number of surfaces to generate for the cloud.

    Returns:
        list: A list of RhinoCommon Breps and Surfaces representing the 3D geometries of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    
    # Set a seed for randomness
    random.seed(42)
    
    # Create the box (core structure)
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_length, 0, 0),
        rg.Point3d(box_length, box_width, 0),
        rg.Point3d(0, box_width, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_length, 0, box_height),
        rg.Point3d(box_length, box_width, box_height),
        rg.Point3d(0, box_width, box_height)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)
    
    # Create the cloud (amorphous envelope)
    cloud_surfaces = []
    for _ in range(cloud_density):
        # Generate random points around the box to form the cloud
        angle = random.uniform(0, 2 * 3.14159)
        distance = random.uniform(0.8 * cloud_radius, cloud_radius)
        height = random.uniform(0, box_height)
        
        x_offset = distance * random.uniform(-1, 1)
        y_offset = distance * random.uniform(-1, 1)
        z_offset = random.uniform(-0.5, 0.5) * cloud_radius
        
        cloud_point = rg.Point3d(
            box_length / 2 + x_offset,
            box_width / 2 + y_offset,
            height + z_offset
        )
        
        # Create a surface from the box top face to the cloud point
        box_top_center = rg.Point3d(box_length / 2, box_width / 2, box_height)
        line_to_cloud = rg.Line(box_top_center, cloud_point)
        cloud_surface = rg.Surface.CreateExtrusion(rg.Curve.CreateControlPointCurve([box_top_center, cloud_point], 1), rg.Vector3d(0, 0, 1))
        cloud_surfaces.append(cloud_surface)
    
    return [box_brep] + cloud_surfaces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model(box_length=12, box_width=8, box_height=10, cloud_radius=25, cloud_density=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model(box_length=5, box_width=5, box_height=5, cloud_radius=30, cloud_density=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model(box_length=15, box_width=10, box_height=20, cloud_radius=35, cloud_density=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model(box_length=14, box_width=6, box_height=8, cloud_radius=22, cloud_density=18)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model(box_length=10, box_width=12, box_height=18, cloud_radius=15, cloud_density=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
