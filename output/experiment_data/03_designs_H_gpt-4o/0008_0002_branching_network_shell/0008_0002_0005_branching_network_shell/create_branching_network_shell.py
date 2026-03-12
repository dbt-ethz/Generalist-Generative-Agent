# Created for 0008_0002_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model inspired by the "branching network shell" metaphor. It constructs a dome-like structure with interwoven pathways, reflecting the metaphor's organic and interconnected nature. By defining parameters such as radius, height, and branch thickness, the function creates a protective yet permeable shell that allows light and air to filter through. The branching pathways are designed to balance open and enclosed spaces, promoting fluidity and growth. The resulting geometries, which form a dynamic silhouette, emphasize a harmonious integration with the surrounding environment, mimicking natural ecosystems."""

#! python 3
function_code = """def create_branching_network_shell(radius=15, height=8, num_branches=12, branch_thickness=0.5, seed=99):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.

    This function constructs a dome-like structure with interwoven branching pathways that balance enclosed and open areas.
    The design reflects the protective yet permeable nature of the shell, emphasizing interconnected spaces that promote fluidity and growth.

    Parameters:
    - radius (float): The radius of the dome-like structure (in meters).
    - height (float): The maximum height of the dome-like structure (in meters).
    - num_branches (int): The number of branching pathways that intersect the dome.
    - branch_thickness (float): The thickness of the branching pathways (in meters).
    - seed (int): The seed for random generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the architectural Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the main dome-like shell
    circle = rg.Circle(rg.Point3d(0, 0, 0), radius)
    line = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height))
    hemisphere = rg.Brep.CreateFromRevSurface(
        rg.RevSurface.Create(circle.ToNurbsCurve(), line),
        True, True
    ).CapPlanarHoles(0.1)
    
    # Create a list to hold the resulting geometries
    geometries = [hemisphere]

    # Create branching pathways
    for i in range(num_branches):
        angle = (2 * math.pi / num_branches) * i
        start_height = random.uniform(0.2 * height, 0.8 * height)
        end_height = random.uniform(0.2 * height, 0.8 * height)
        start_point = rg.Point3d(radius * math.cos(angle), radius * math.sin(angle), start_height)
        end_point = rg.Point3d(radius * 0.5 * math.cos(angle + math.pi / 6), radius * 0.5 * math.sin(angle + math.pi / 6), end_height)
        
        # Create a curved pathway
        pathway_curve = rg.Curve.CreateInterpolatedCurve([start_point, end_point], 3)
        
        # Create a pipe around the pathway
        pathway = rg.Brep.CreatePipe(pathway_curve, branch_thickness, True, rg.PipeCapMode.Round, True, 0.1, 0.1)[0]
        
        # Add the pathway to the geometries list
        geometries.append(pathway)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(radius=20, height=10, num_branches=15, branch_thickness=0.6, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(radius=25, height=12, num_branches=10, branch_thickness=0.4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(radius=18, height=9, num_branches=14, branch_thickness=0.7, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(radius=30, height=15, num_branches=20, branch_thickness=0.3, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(radius=22, height=11, num_branches=18, branch_thickness=0.8, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
