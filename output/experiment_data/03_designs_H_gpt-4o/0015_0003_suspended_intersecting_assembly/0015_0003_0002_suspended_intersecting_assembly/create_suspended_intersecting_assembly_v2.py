# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model that embodies the metaphor of "Suspended intersecting assembly." It creates a series of curved panels that appear to float and intersect dynamically within a defined space. By utilizing randomized center points and orientations, the function ensures the panels are arranged in a visually engaging network, emphasizing lightness and fluidity. The model's geometry highlights complex spatial relationships and connections, while the varying panel sizes and arrangements allow for adaptability. Overall, it captures the essence of transparency and movement, reflecting the metaphor's key traits of balance and dynamic interaction."""

#! python 3
function_code = """def create_suspended_intersecting_assembly_v2(num_panels=8, panel_radius=3, seed=42):
    \"""
    Creates an architectural Concept Model encapsulating the 'Suspended intersecting assembly' metaphor.
    
    This model consists of a series of suspended, intersecting panels that create a network of dynamic spatial relationships.
    The panels are designed to appear as floating, flexible elements that enhance lightness and fluidity within the space.
    
    Inputs:
    - num_panels: The number of panels to generate in the model.
    - panel_radius: The radius of each panel's curvature, representing its size.
    - seed: A seed for random number generation to ensure replicability.
    
    Outputs:
    - A list of Brep geometries representing the suspended panels.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for replicability
    random.seed(seed)

    # Initialize a list to hold the generated Breps
    brep_list = []

    # Define the base plane for the model
    base_plane = rg.Plane.WorldXY

    # Generate panels with random parameters
    for _ in range(num_panels):
        # Randomly determine the center of the panel within a defined range
        x_center = random.uniform(-10, 10)
        y_center = random.uniform(-10, 10)
        z_center = random.uniform(5, 15)

        # Create a point for the center of the panel
        center_point = rg.Point3d(x_center, y_center, z_center)

        # Define the panel's normal vector for its orientation
        normal_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        normal_vector.Unitize()

        # Create a plane for the panel
        panel_plane = rg.Plane(center_point, normal_vector)

        # Create a circular panel using the given radius
        circle = rg.Circle(panel_plane, panel_radius)

        # Create a surface from the circle
        panel_surface = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]

        # Add the panel to the list of Breps
        brep_list.append(panel_surface)

    # Return the list of Breps representing the model
    return brep_list"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly_v2(num_panels=10, panel_radius=4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly_v2(num_panels=5, panel_radius=2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly_v2(num_panels=12, panel_radius=3.5, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly_v2(num_panels=6, panel_radius=5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly_v2(num_panels=15, panel_radius=6, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
