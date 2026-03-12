# Created for 0008_0002_branching_network_shell.json

""" Summary:
The provided function generates an architectural concept model inspired by the "branching network shell" metaphor. It creates a dome-like structure characterized by a protective yet permeable form, resembling the interwoven branches of a tree canopy. The function constructs this model by defining a dome profile and adding branching pathways that diverge and converge, promoting fluidity and interconnectedness among spaces. By varying parameters such as base radius, height, and branch levels, the function produces diverse geometries that reflect the dynamic interplay of enclosed and open areas, while allowing natural light and air to filter through, enhancing the overall spatial experience."""

#! python 3
function_code = """def create_branching_network_shell(base_radius=10, height=8, branch_levels=3, radial_segments=12, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.

    The model generates a dome-like structure that is both protective and permeable. It features branching
    pathways that create a dynamic interplay of enclosed and open spaces, promoting fluidity and growth.

    Inputs:
    - base_radius: The base radius of the dome-like structure (in meters).
    - height: The total height of the dome structure (in meters).
    - branch_levels: The number of levels or tiers of branching elements.
    - radial_segments: The number of segments used to define the dome's profile.
    - seed: The seed for random generation to ensure replicability.

    Outputs:
    - A list of 3D geometries (breps) representing the architectural Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create a list to hold the resulting geometries
    geometries = []

    # Define the dome profile using a series of points
    dome_points = [rg.Point3d(base_radius * math.cos(2 * math.pi * i / radial_segments),
                              base_radius * math.sin(2 * math.pi * i / radial_segments),
                              height) for i in range(radial_segments)]

    # Create the dome surface using Loft
    dome_curve = rg.Curve.CreateInterpolatedCurve(dome_points, 3)
    dome_loft = rg.Brep.CreateFromLoft([dome_curve, rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height)).ToNurbsCurve()],
                                       rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

    # Add the dome to geometries
    if dome_loft:
        geometries.append(dome_loft[0])

    # Create branching pathways
    for level in range(branch_levels):
        level_height = (height / branch_levels) * (level + 1)
        num_branches = random.randint(3, 6)

        for _ in range(num_branches):
            angle = random.uniform(0, 2 * math.pi)
            branch_length = random.uniform(0.3, 0.5) * base_radius
            branch_start = rg.Point3d(base_radius * math.cos(angle), base_radius * math.sin(angle), level_height)
            branch_end = rg.Point3d((base_radius + branch_length) * math.cos(angle),
                                    (base_radius + branch_length) * math.sin(angle),
                                    level_height + random.uniform(-0.5, 0.5) * (height / branch_levels))

            # Create a branching curve
            branch_curve = rg.Curve.CreateInterpolatedCurve([branch_start, branch_end], 3)

            # Create a pipe for the branch
            branch_pipe = rg.Brep.CreatePipe(branch_curve, random.uniform(0.1, 0.2), True, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]

            # Add the branch to geometries
            geometries.append(branch_pipe)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(base_radius=15, height=10, branch_levels=4, radial_segments=16, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(base_radius=12, height=6, branch_levels=5, radial_segments=10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(base_radius=20, height=15, branch_levels=2, radial_segments=8, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(base_radius=18, height=12, branch_levels=3, radial_segments=14, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(base_radius=14, height=9, branch_levels=6, radial_segments=20, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
