# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a vertical structure featuring alternating solid and void elements. It uses parameters such as height, width, depth, and void ratio to define the model's dimensions and the extent of perforation. By layering solid volumes with randomly placed voids, the structure mimics a natural landscape, enhancing light penetration and spatial interaction. This dynamic silhouette fosters a relationship between interior and exterior spaces, aligning with the metaphor's essence of permeability and verticality while providing a visually engaging architectural form."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=10, layers=5, void_ratio=0.4, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    This function generates a vertical structure with alternating solid and void elements, designed to
    evoke a natural landscape with perforations that enhance light and spatial interaction.
    
    Parameters:
    - height (float): Total height of the structure in meters.
    - width (float): Total width of the structure in meters.
    - depth (float): Total depth of the structure in meters.
    - layers (int): Number of vertical layers in the structure.
    - void_ratio (float): Ratio of void space to solid space in each layer (0 to 1).
    - seed (int): Random seed for replicable void pattern generation.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for reproducibility
    random.seed(seed)

    # Compute dimensions
    layer_height = height / layers
    solid_height = layer_height * (1 - void_ratio)
    void_height = layer_height * void_ratio

    geometries = []

    for i in range(layers):
        base_z = i * layer_height

        # Create the solid part of the layer
        slab = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, width),
            rg.Interval(0, depth),
            rg.Interval(base_z, base_z + solid_height)
        ).ToBrep()
        geometries.append(slab)

        # Introduce voids to create perforation
        void_count = random.randint(1, 3)  # Number of voids in each layer
        for _ in range(void_count):
            void_width = random.uniform(0.2, 0.5) * width
            void_depth = random.uniform(0.2, 0.5) * depth
            void_x = random.uniform(0, width - void_width)
            void_y = random.uniform(0, depth - void_depth)
            void_z = base_z + random.uniform(0, solid_height)

            void_box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(void_x, void_x + void_width),
                rg.Interval(void_y, void_y + void_depth),
                rg.Interval(void_z, void_z + void_height)
            ).ToBrep()

            # Subtract void from the slab
            result = rg.Brep.CreateBooleanDifference([slab], [void_box], 0.01)
            if result:
                slab = result[0]

        # Add the modified slab with voids to the list of geometries
        geometries[-1] = slab

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=15, depth=12, layers=6, void_ratio=0.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, width=8, depth=10, layers=4, void_ratio=0.3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=20, depth=15, layers=3, void_ratio=0.2, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=50, width=18, depth=10, layers=8, void_ratio=0.6, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, width=25, depth=20, layers=7, void_ratio=0.4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
