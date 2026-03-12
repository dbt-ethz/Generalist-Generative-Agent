# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model that embodies the "Perforated vertical landscape" metaphor by constructing a vertical structure with alternating solid and void elements. It utilizes parameters such as height, number of layers, and void ratio to create a rhythmic interplay of light and shadow, reminiscent of natural formations. Each layer consists of solid masses interspersed with voids, which are randomly distributed, allowing light and air to penetrate. This design approach enhances transparency and spatial interactions, effectively translating the metaphor into a dynamic architectural form."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, num_layers=5, void_ratio=0.4, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    The model is a vertical structure that alternates between solid and void elements, creating a rhythm of light and shadow.
    This approach emphasizes transparency and permeability, resembling natural cliff faces or geological formations, with 
    openings that mimic erosion or pathways. The structure is designed to maximize the penetration of light and views.

    Parameters:
    - height: The total height of the model in meters.
    - num_layers: Number of layers in the vertical structure.
    - void_ratio: The proportion of each layer that is void (0 to 1).
    - seed: Random seed for reproducibility of the void distribution.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    # Dimensions and proportions
    layer_height = height / num_layers
    layer_width = 10  # Assume a constant width for simplicity
    layer_depth = 10  # Assume a constant depth for simplicity

    geometries = []

    for i in range(num_layers):
        # Determine solid and void portions for this layer
        solid_height = layer_height * (1 - void_ratio)
        void_height = layer_height * void_ratio

        # Create solid part of the layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = i * layer_height
        solid_box = rg.Box(base_plane, rg.Interval(0, layer_width), rg.Interval(0, layer_depth), rg.Interval(0, solid_height))
        geometries.append(solid_box.ToBrep())

        # Create voids in this layer
        num_voids = random.randint(1, 3)  # Random number of voids per layer
        for _ in range(num_voids):
            void_width = random.uniform(1.0, layer_width * 0.5)
            void_depth = random.uniform(1.0, layer_depth * 0.5)
            void_x = random.uniform(0, layer_width - void_width)
            void_y = random.uniform(0, layer_depth - void_depth)
            void_z = random.uniform(solid_height, layer_height - void_height)

            void_base = rg.Plane.WorldXY
            void_base.Origin = rg.Point3d(void_x, void_y, i * layer_height + void_z)
            void_box = rg.Box(void_base, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height))
            void_brep = void_box.ToBrep()

            # Subtract void from solid
            solid_brep = geometries[-1]
            result = rg.Brep.CreateBooleanDifference([solid_brep], [void_brep], 0.001)
            if result:
                geometries[-1] = result[0]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, num_layers=6, void_ratio=0.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, num_layers=4, void_ratio=0.3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, num_layers=7, void_ratio=0.2, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=50, num_layers=8, void_ratio=0.6, seed=11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, num_layers=5, void_ratio=0.4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
