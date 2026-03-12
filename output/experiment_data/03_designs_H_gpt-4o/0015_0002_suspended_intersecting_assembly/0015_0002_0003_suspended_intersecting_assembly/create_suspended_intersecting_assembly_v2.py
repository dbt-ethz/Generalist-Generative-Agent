# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly_v2` generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." By employing a layered structure, it creates various horizontal layers of floating elements, represented as boxes, arranged within a defined base area. The elements are interlinked by tensile cables, which enhance the illusion of suspension and interconnectivity. The model incorporates randomness in element placement and size, echoing the dynamic interplay highlighted in the metaphor. This approach emphasizes lightness and spatial complexity, aligning with the architectural vision of overlapping volumes and the delicate balance suggested by the metaphor."""

#! python 3
function_code = """def create_suspended_intersecting_assembly_v2(base_area=100, height=10, num_layers=5, num_elements_per_layer=8, element_thickness=0.2, cable_radius=0.05, seed=101):
    \"""
    Generates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly'.
    This version uses a layered approach to create intersecting, floating elements connected by tensile cables.

    Parameters:
    - base_area (float): The area of the base in square meters.
    - height (float): The total height of the assembly in meters.
    - num_layers (int): Number of horizontal layers of intersecting elements.
    - num_elements_per_layer (int): Number of elements per layer.
    - element_thickness (float): Thickness of the intersecting elements.
    - cable_radius (float): Radius of the tensile cables.
    - seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    breps = []

    # Calculate base dimensions
    base_length = math.sqrt(base_area)
    base_width = base_length

    # Define the vertical spacing between layers
    layer_spacing = height / num_layers

    # Create intersecting elements for each layer
    for layer in range(num_layers):
        z = layer * layer_spacing
        for _ in range(num_elements_per_layer):
            # Random position and size within the base area
            x = random.uniform(0, base_length)
            y = random.uniform(0, base_width)
            length = random.uniform(base_length * 0.1, base_length * 0.3)
            width = random.uniform(base_width * 0.1, base_width * 0.3)

            # Create a box element
            box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + length), rg.Interval(y, y + width), rg.Interval(z, z + element_thickness))
            breps.append(box.ToBrep())

    # Create tensile cables connecting random elements
    for _ in range(num_layers * num_elements_per_layer // 2):
        start_idx = random.randint(0, len(breps) - 1)
        end_idx = random.randint(0, len(breps) - 1)
        if start_idx != end_idx:
            start_brep = breps[start_idx]
            end_brep = breps[end_idx]
            start_point = start_brep.GetBoundingBox(True).Center
            end_point = end_brep.GetBoundingBox(True).Center

            # Create a cable as a cylinder
            cable_line = rg.Line(start_point, end_point)
            cable = rg.Cylinder(rg.Circle(rg.Plane(start_point, cable_line.Direction), cable_radius), cable_line.Length).ToBrep(True, True)
            breps.append(cable)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly_v2(base_area=150, height=20, num_layers=6, num_elements_per_layer=10, element_thickness=0.25, cable_radius=0.05, seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly_v2(base_area=200, height=15, num_layers=4, num_elements_per_layer=12, element_thickness=0.3, cable_radius=0.07, seed=303)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly_v2(base_area=120, height=25, num_layers=8, num_elements_per_layer=15, element_thickness=0.15, cable_radius=0.04, seed=404)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly_v2(base_area=180, height=30, num_layers=7, num_elements_per_layer=5, element_thickness=0.1, cable_radius=0.06, seed=505)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly_v2(base_area=250, height=18, num_layers=5, num_elements_per_layer=7, element_thickness=0.2, cable_radius=0.03, seed=606)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
