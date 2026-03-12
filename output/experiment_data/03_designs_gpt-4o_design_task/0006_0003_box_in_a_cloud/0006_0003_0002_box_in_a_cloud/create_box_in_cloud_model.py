# Created for 0006_0003_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model` generates an architectural concept model by integrating the metaphor of a "Box in a Cloud." It constructs a solid, geometric "box" using specified dimensions and robust materials, symbolizing stability. Surrounding this core is a dynamic "cloud" composed of randomly distributed points, representing lightness and fluidity. The parameters allow for customization of the box size and cloud characteristics, such as density and radius. This interplay of solid and diffuse elements visually embodies the metaphor, creating a spatial narrative that juxtaposes permanence with ethereality, encouraging exploration of contrasting spatial experiences."""

#! python 3
function_code = """def create_box_in_cloud_model(box_dimensions, cloud_radius, cloud_density, seed=42):
    \"""
    Create an architectural Concept Model embodying the 'Box in a Cloud' metaphor.

    Parameters:
    box_dimensions (tuple): A tuple (length, width, height) representing the dimensions of the central box.
    cloud_radius (float): The radius of the spherical cloud surrounding the box.
    cloud_density (int): The number of points or elements representing the cloud.
    seed (int, optional): The seed for random number generation to ensure replicable results. Default is 42.

    Returns:
    list: A list of RhinoCommon geometry objects (breps representing the box and points representing the cloud).

    This function generates a central geometric box form and surrounds it with a dynamic, diffuse cloud of points.
    The box is constructed as a BRep, and the cloud is represented by a collection of points, which can be further
    processed to create a mesh or surface for visualization.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the central box as a BRep
    box_length, box_width, box_height = box_dimensions
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

    # Create the cloud of points
    cloud_points = []
    for _ in range(cloud_density):
        x = random.uniform(-cloud_radius, cloud_radius)
        y = random.uniform(-cloud_radius, cloud_radius)
        z = random.uniform(-cloud_radius, cloud_radius)
        # Ensure the cloud surrounds the box
        if (x**2 + y**2 + z**2) <= cloud_radius**2:
            cloud_points.append(rg.Point3d(x + box_length/2, y + box_width/2, z + box_height/2))

    # Return the box and the cloud point collection as a list
    return [box_brep, cloud_points]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model((2, 3, 4), 5.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model((1, 1, 1), 3.0, 50, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model((5, 5, 5), 10.0, 200, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model((4, 2, 3), 6.0, 150, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model((3, 4, 5), 8.0, 75, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
