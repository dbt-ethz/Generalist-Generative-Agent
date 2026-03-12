# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model based on the "Perforated vertical landscape" metaphor by constructing a vertical structure with alternating solid and void elements. It defines layers of varying heights and introduces random voids that create a dynamic silhouette reminiscent of natural landscapes, such as cliffs. This design maximizes light penetration and spatial interaction by using materials that allow air and views to flow through. The result is a model that embodies the essence of permeability and verticality, enhancing the relationship between interior and exterior spaces through rhythmic patterns of solid and void."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=15, depth=10, layers=5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.

    This function generates a structure with a dynamic silhouette by alternating between solid and void elements,
    resembling geological formations with perforations. This model maximizes the interaction between interior and
    exterior spaces, emphasizing light penetration and views.

    Parameters:
    - height (float): Total height of the structure in meters.
    - width (float): Width of the base of the structure in meters.
    - depth (float): Depth of the base of the structure in meters.
    - layers (int): Number of layers in the structure.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    layer_height = height / layers
    geometries = []

    for i in range(layers):
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * layer_height))

        # Create a solid layer
        solid_box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, layer_height))
        solid_brep = solid_box.ToBrep()

        # Create random voids to perforate the solid layer
        num_voids = random.randint(1, 4)
        for _ in range(num_voids):
            void_width = random.uniform(0.2, 0.5) * width
            void_depth = random.uniform(0.2, 0.5) * depth
            void_x = random.uniform(0, width - void_width)
            void_y = random.uniform(0, depth - void_depth)

            void_box = rg.Box(base_plane, rg.Interval(void_x, void_x + void_width), rg.Interval(void_y, void_y + void_depth), rg.Interval(0, layer_height))
            void_brep = void_box.ToBrep()

            # Subtract void from the solid
            result = rg.Brep.CreateBooleanDifference([solid_brep], [void_brep], 0.01)
            if result:
                solid_brep = result[0]

        geometries.append(solid_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=20, depth=15, layers=6, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, width=10, depth=12, layers=4, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=18, depth=14, layers=3, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=45, width=22, depth=16, layers=8, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=50, width=25, depth=20, layers=7, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
