# Created for 0008_0002_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model inspired by the "branching network shell" metaphor. It constructs a dome-like structure, representing the organic form of a tree canopy, with a specified radius and height. The function creates multiple interlaced pathways, reflecting the interconnectedness and fluidity of space. Each pathway diverges from the dome, maintaining a balance between open and enclosed areas, while allowing natural elements like light to permeate through. The output comprises 3D geometries that embody the protective yet permeable nature of the shell, promoting harmony with the surrounding environment."""

#! python 3
function_code = """def create_branching_network_shell(radius=10, branch_count=8, height=5, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.
    
    The model generates a dome-like structure with interlaced pathways, balancing enclosed and open areas to 
    reflect a protective yet permeable nature. It emphasizes interconnected spaces, promoting fluidity and growth.

    Inputs:
    - radius: The radius of the dome-like structure (in meters).
    - branch_count: The number of branching pathways that intersect the dome.
    - height: The maximum height of the dome-like structure (in meters).
    - seed: The seed for random generation to ensure replicability.

    Outputs:
    - A list of 3D geometries (breps) representing the architectural Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the main dome-like shell
    sphere = rg.Sphere(rg.Point3d(0, 0, height / 2), radius)
    dome = rg.Brep.CreateFromSphere(sphere)
    
    # Create a list to hold the resulting geometries
    geometries = [dome]

    # Create branching pathways
    for i in range(branch_count):
        angle = (2 * math.pi / branch_count) * i
        pathway_height = random.uniform(0.3 * height, 0.8 * height)
        base_point = rg.Point3d(radius * math.cos(angle), radius * math.sin(angle), 0)
        top_point = rg.Point3d(0, 0, pathway_height)

        # Create a curved pathway
        pathway_curve = rg.Curve.CreateInterpolatedCurve([base_point, top_point], 3)
        pathway = rg.Brep.CreateFromSweep(pathway_curve, rg.Circle(base_point, 0.2 * radius).ToNurbsCurve(), True, 0.1)[0]

        # Add the pathway to the geometries list
        geometries.append(pathway)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(radius=15, branch_count=10, height=7, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(radius=12, branch_count=6, height=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(radius=8, branch_count=12, height=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(radius=20, branch_count=5, height=10, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(radius=18, branch_count=9, height=9, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
