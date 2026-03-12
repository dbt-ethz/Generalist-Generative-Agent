# Created for 0008_0004_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell_model` generates an architectural concept model inspired by the "branching network shell" metaphor. It utilizes parameters such as base radius, height, branch length, branch count, and shell thickness to create a central core and branching elements that radiate outward. The branches mimic natural forms, enhancing visual complexity and spatial connectivity. A lofted shell structure is created to represent the protective yet permeable outer layer, allowing light and air to filter through. This model embodies the metaphor's themes of exploration, organic growth, and integration with the environment, effectively translating the design task into a tangible form."""

#! python 3
function_code = """def create_branching_network_shell_model(base_radius, height, branch_length, branch_count, shell_thickness):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor. The model consists of vertical 
    and horizontal branching elements radiating from a central core, creating a protective yet permeable shell structure.

    Inputs:
    - base_radius (float): Radius of the central core from which branches emerge.
    - height (float): Total height of the structure.
    - branch_length (float): Average length of the branching elements.
    - branch_count (int): Number of branches emerging from the central core.
    - shell_thickness (float): Thickness of the outer shell layer.

    Outputs:
    - List of 3D geometries (breps and surfaces) representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize randomness with a seed for reproducibility
    random.seed(42)

    # Create the central core cylinder
    core = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, base_radius), height).ToBrep(True, True)

    # Create branching elements
    branches = []
    for i in range(branch_count):
        angle = random.uniform(0, 2 * 3.14159)
        branch_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0.5, 1))
        branch_vector.Unitize()
        branch_vector *= branch_length
        branch_start = rg.Point3d(0, 0, random.uniform(0, height))
        branch_end = branch_start + branch_vector
        branch_line = rg.Line(branch_start, branch_end)
        branch_curve = branch_line.ToNurbsCurve()
        branches.append(branch_curve)

    # Create shell structure using lofted surface
    shell_curves = [rg.Circle(branch.PointAtStart, shell_thickness).ToNurbsCurve() for branch in branches]
    shell_loft = rg.Brep.CreateFromLoft(shell_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

    # Gather all geometry
    geometries = [core] + list(shell_loft)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell_model(5.0, 10.0, 3.0, 12, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell_model(4.0, 15.0, 2.5, 8, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell_model(6.0, 20.0, 4.0, 10, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell_model(3.5, 12.0, 2.0, 15, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell_model(7.0, 18.0, 5.0, 20, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
