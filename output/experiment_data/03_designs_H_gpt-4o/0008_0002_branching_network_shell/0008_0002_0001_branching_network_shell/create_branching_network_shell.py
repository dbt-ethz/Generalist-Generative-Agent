# Created for 0008_0002_branching_network_shell.json

""" Summary:
The provided function `create_branching_network_shell` generates an architectural concept model inspired by the "branching network shell" metaphor. It creates a dome-like structure resembling a tree canopy, utilizing a half-sphere as its base. The function employs randomized branching pathways, reflecting organic growth and interconnectedness, by generating arcs that mimic natural forms. By adjusting parameters like radius and branch density, the model achieves a balance between enclosed and open spaces, emphasizing permeability and interaction with light and air. Ultimately, this code embodies the metaphor's essence, promoting fluidity and harmony with the surrounding environment."""

#! python 3
function_code = """def create_branching_network_shell(radius=10, height=5, branch_density=0.2, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.

    The model generates a woven dome-like structure, emphasizing organic growth and spatial fluidity 
    through a network of interlaced pathways. It balances enclosed and open areas to reflect a 
    protective yet permeable nature, promoting interconnectedness and integration with the environment.

    Inputs:
    - radius: The radius of the dome-like structure (in meters).
    - height: The maximum height of the dome-like structure (in meters).
    - branch_density: A factor influencing the density and complexity of branching pathways.
    - seed: The seed for random generation to ensure replicability.

    Outputs:
    - A list of 3D geometries (breps) representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the main dome-like structure using a half sphere
    sphere = rg.Sphere(rg.Point3d(0, 0, 0), radius)
    hemisphere = rg.Brep.CreateFromSphere(sphere)
    hemisphere = [b for b in hemisphere.Faces if b.OrientationIsReversed is False][0].ToBrep()

    # Create a list to hold the resulting geometries
    geometries = [hemisphere]

    # Calculate the number of branches based on density
    num_branches = int(branch_density * radius * 10)

    # Create branching pathways
    for _ in range(num_branches):
        start_angle = random.uniform(0, 2 * math.pi)
        end_angle = start_angle + random.uniform(math.pi / 6, math.pi / 3)  # limit the angle to create arcs
        start_height = random.uniform(0, height / 2)
        end_height = random.uniform(height / 2, height)

        start_point = rg.Point3d(
            radius * math.cos(start_angle),
            radius * math.sin(start_angle),
            start_height
        )
        end_point = rg.Point3d(
            (radius - 1) * math.cos(end_angle),
            (radius - 1) * math.sin(end_angle),
            end_height
        )

        # Create an arc for the pathway
        arc_curve = rg.ArcCurve(rg.Arc(start_point, rg.Point3d(0, 0, height), end_point))
        branch = rg.Brep.CreatePipe(arc_curve, 0.1, True, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]

        # Add the branch to the geometries list
        geometries.append(branch)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(radius=15, height=10, branch_density=0.3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(radius=12, height=6, branch_density=0.25, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(radius=20, height=8, branch_density=0.15, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(radius=18, height=7, branch_density=0.4, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(radius=25, height=12, branch_density=0.5, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
