# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a vertical structure composed of alternating solid and void elements. It takes parameters like height, number of layers, and dimensions for solids and voids. The function calculates the dimensions of each layer and uses random variations to enhance the voids, simulating natural erosion. This approach creates a dynamic silhouette reminiscent of geological formations, allowing light and air to penetrate through the structure. The resulting geometries illustrate the interplay between interior and exterior spaces, embodying the metaphor's essence of permeability and verticality."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, num_layers=5, solid_width=2, void_width=1):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    Parameters:
    height (float): Total height of the vertical structure in meters.
    num_layers (int): Number of alternating solid and void layers.
    solid_width (float): Width of the solid elements in meters.
    void_width (float): Width of the void elements in meters.

    Returns:
    list: A list of Brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a random seed for reproducibility
    random.seed(42)

    # Initialize a list to store geometries
    geometries = []

    # Calculate the total width of the structure
    total_width = (solid_width + void_width) * num_layers

    # Calculate the height of each layer
    layer_height = height / num_layers

    # Create alternating solid and void layers
    for i in range(num_layers):
        # Determine the x position of the current layer
        x_position = i * (solid_width + void_width)

        # Create a solid layer
        solid = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(x_position, x_position + solid_width),
            rg.Interval(0, total_width),
            rg.Interval(0, layer_height)
        )
        geometries.append(solid.ToBrep())

        # Create a void layer with random height variation
        void_height_variation = random.uniform(-layer_height * 0.2, layer_height * 0.2)
        void = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(x_position + solid_width, x_position + solid_width + void_width),
            rg.Interval(0, total_width),
            rg.Interval(0, layer_height + void_height_variation)
        )
        geometries.append(void.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, num_layers=6, solid_width=3, void_width=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, num_layers=4, solid_width=1.5, void_width=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=50, num_layers=8, solid_width=4, void_width=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=35, num_layers=5, solid_width=2.5, void_width=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, num_layers=7, solid_width=3.5, void_width=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
