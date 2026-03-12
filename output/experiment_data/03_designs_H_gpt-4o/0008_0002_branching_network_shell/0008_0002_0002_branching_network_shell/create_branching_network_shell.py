# Created for 0008_0002_branching_network_shell.json

""" Summary:
The provided function `create_branching_network_shell` generates an architectural concept model inspired by the "branching network shell" metaphor. It creates a dome-like structure resembling a tree canopy, using parameters like radius, height, and branch density to define its form. The function constructs a protective shell made of layered, interwoven pathways that balance enclosed and open spaces, allowing for light and air interaction. Each layer of branches, generated randomly, enhances the model's organic aesthetic and spatial complexity, reflecting the interconnectedness and fluidity of a natural ecosystem while harmonizing with the surrounding environment."""

#! python 3
function_code = """def create_branching_network_shell(radius=10, height=5, branch_layers=3, branch_density=10, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'branching network shell' metaphor.

    The model generates a dome-like structure with interwoven, layered branches that create both enclosed and open areas.
    The design reflects a protective yet permeable shell, promoting a sense of fluidity and growth.

    Inputs:
    - radius: The radius of the dome-like structure (in meters).
    - height: The maximum height of the structure (in meters).
    - branch_layers: The number of vertical layers of branches.
    - branch_density: The number of branches per layer.
    - seed: The seed for random generation to ensure replicability.

    Outputs:
    - A list of 3D geometries (breps) representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the main dome-like shell as a half-sphere
    sphere = rg.Sphere(rg.Point3d(0, 0, height / 2), radius)
    dome = rg.Brep.CreateFromSphere(sphere)

    # Create a list to hold the resulting geometries
    geometries = [dome]

    # Create layered branching pathways
    for layer in range(branch_layers):
        # Adjust the current height of the layer
        layer_height = (height / branch_layers) * layer + (height / (2 * branch_layers))
        
        for i in range(branch_density):
            angle = (2 * math.pi / branch_density) * i + random.uniform(-0.1, 0.1)
            branch_length = random.uniform(0.5 * radius, radius)
            branch_thickness = random.uniform(0.1, 0.3)

            base_point = rg.Point3d(radius * math.cos(angle), radius * math.sin(angle), layer_height)
            mid_point = rg.Point3d((radius - branch_length / 2) * math.cos(angle), 
                                   (radius - branch_length / 2) * math.sin(angle), 
                                   layer_height + branch_length / 4)
            top_point = rg.Point3d((radius - branch_length) * math.cos(angle), 
                                   (radius - branch_length) * math.sin(angle), 
                                   layer_height + branch_length / 2)

            # Create a curved pathway
            pathway_curve = rg.Curve.CreateInterpolatedCurve([base_point, mid_point, top_point], 3)
            pathway = rg.Brep.CreatePipe(pathway_curve, branch_thickness, True, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]

            # Add the pathway to the geometries list
            geometries.append(pathway)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(radius=15, height=10, branch_layers=4, branch_density=12, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(radius=20, height=7, branch_layers=5, branch_density=8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(radius=12, height=6, branch_layers=2, branch_density=15, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(radius=25, height=15, branch_layers=6, branch_density=10, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(radius=18, height=8, branch_layers=3, branch_density=14, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
