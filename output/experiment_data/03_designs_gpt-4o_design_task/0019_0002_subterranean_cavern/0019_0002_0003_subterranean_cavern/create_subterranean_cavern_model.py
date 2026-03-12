# Created for 0019_0002_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model based on the metaphor of a subterranean cavern by creating layered structures that evoke the idea of depth and verticality. It takes parameters such as the base radius, total height, number of layers, and layer thickness. The model features a central void or atrium represented as a cylinder, around which various circular layers are extruded to create a tiered effect. Random variations in layer radius simulate the natural stratification of a cavern, while vertical spacing enhances the sense of descent and exploration, embodying the immersive qualities of the metaphor."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, height, num_layers, layer_thickness, seed=None):
    \"""
    Creates a 3D architectural Concept Model based on the metaphor of a subterranean cavern. The model features layered
    platforms descending into a central void, evoking the stratified nature of a cave with a focus on vertical transitions
    and spatial depth.

    Inputs:
    - base_radius (float): The radius of the base of the central void or atrium.
    - height (float): The total height of the cavern model from top to bottom.
    - num_layers (int): The number of horizontal layers or tiers in the model.
    - layer_thickness (float): The thickness of each layer, defining the height gap between levels.
    - seed (int, optional): Seed for randomness to ensure replicability if randomness is used.

    Outputs:
    - List of 3D geometries (breps): The resulting architectural Concept Model geometries.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    # Calculate the vertical step between each layer
    vertical_step = height / num_layers

    # Create a list to store all geometries
    geometries = []

    # Define the central void (atrium) as a cylinder
    central_void = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, base_radius), height).ToBrep(True, True)
    geometries.append(central_void)

    # Generate layers around the central void
    for i in range(num_layers):
        # Calculate the Z position of the current layer
        z_position = i * vertical_step

        # Create a circular layer around the central void
        outer_radius = base_radius + random.uniform(0.5, 1.5) * base_radius / num_layers
        layer_circle = rg.Circle(rg.Plane.WorldXY, outer_radius)
        layer_curve = layer_circle.ToNurbsCurve()

        # Extrude the curve to create a 3D layer
        layer_extrusion = rg.Extrusion.Create(layer_curve, layer_thickness, True).ToBrep()

        # Move the extrusion to the correct Z position
        translation = rg.Transform.Translation(0, 0, z_position)
        layer_extrusion.Transform(translation)

        # Add the layer to the list of geometries
        geometries.append(layer_extrusion)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(5.0, 20.0, 4, 2.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(3.5, 15.0, 6, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(4.0, 25.0, 5, 3.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(6.0, 30.0, 7, 2.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(7.5, 18.0, 3, 2.0, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
