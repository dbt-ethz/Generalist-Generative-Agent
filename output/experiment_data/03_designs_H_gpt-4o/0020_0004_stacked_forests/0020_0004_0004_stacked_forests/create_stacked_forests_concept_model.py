# Created for 0020_0004_stacked_forests.json

""" Summary:
The `create_stacked_forests_concept_model` function generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a lattice-like structure with interwoven horizontal and vertical elements, utilizing both rectilinear and curvilinear geometries to symbolize the complexity and interconnectedness of a forest ecosystem. The function implements layers of varying heights, fostering a dynamic silhouette that resembles a forest canopy. The model includes a network of pathways and overlapping spaces, promoting exploration and interaction, thereby embodying the metaphor's essence of organic growth and spatial richness found in natural forest environments."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_width, base_depth, number_layers, layer_height, curve_complexity, randomness_seed=42):
    \"""
    Generate an architectural Concept Model inspired by the 'Stacked forests' metaphor.

    This function creates a lattice-like structure with interwoven horizontal and vertical elements,
    using a combination of rectilinear and curvilinear geometries to symbolize the dense interconnectivity
    of a forest. The model emphasizes a network of pathways and layered spaces, capturing the organic
    growth and complexity of a natural forest ecosystem.

    Parameters:
    - base_width (float): Total width of the structure's base in meters.
    - base_depth (float): Total depth of the structure's base in meters.
    - number_layers (int): Number of vertical layers in the structure.
    - layer_height (float): Height of each layer in meters.
    - curve_complexity (float): Degree of complexity for curvilinear paths (0 to 1).
    - randomness_seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)

    geometries = []

    # Function to create a curvilinear path
    def create_curvilinear_path(layer_z, complexity):
        points = [
            rg.Point3d(random.uniform(0, base_width), random.uniform(0, base_depth), layer_z)
            for _ in range(int(5 + 5 * complexity))
        ]
        curve = rg.Curve.CreateInterpolatedCurve(points, 3)
        return curve

    # Create each layer with mixed rectilinear and curvilinear elements
    for layer_index in range(number_layers):
        layer_z = layer_index * layer_height
        
        # Rectilinear elements
        for _ in range(random.randint(3, 6)):
            x = random.uniform(0, base_width - 2)
            y = random.uniform(0, base_depth - 2)
            rect = rg.Rectangle3d(rg.Plane.WorldXY, rg.Interval(x, x + random.uniform(1, 3)), rg.Interval(y, y + random.uniform(1, 3)))
            extrusion = rg.Extrusion.Create(rect.ToNurbsCurve(), layer_height, True)
            brep_rect = extrusion.ToBrep() if extrusion else None
            if brep_rect:
                geometries.append(brep_rect)
        
        # Curvilinear elements
        for _ in range(random.randint(2, 4)):
            curve = create_curvilinear_path(layer_z + layer_height / 2, curve_complexity)
            pipe = rg.Brep.CreatePipe(curve, [0.1, 0.2], [0.1, 0.1], True, rg.PipeCapMode.Round, True, 0.01, 0.01)
            if pipe:
                geometries.append(pipe[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(10.0, 15.0, 5, 3.0, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(20.0, 25.0, 7, 4.0, 0.5, randomness_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(12.0, 10.0, 4, 2.5, 0.8, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(15.0, 20.0, 6, 2.0, 0.6, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(8.0, 12.0, 3, 2.0, 0.9, randomness_seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
