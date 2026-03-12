# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor. It constructs a vertical structure by layering solid floor slabs interspersed with voids, reflecting the rhythmic interplay between mass and space. The height, width, depth, and number of floors are customizable, allowing for varied configurations. Voids, created randomly within specified ratios, enhance light penetration and spatial interaction, evoking natural formations like cliffs. The model emphasizes transparency and connectivity between interior and exterior environments, aligning with the metaphor's essence of verticality and permeability, ultimately producing a dynamic architectural representation."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=10, floors=5, void_ratio=0.3, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    Parameters:
    - height (float): Total height of the structure in meters.
    - width (float): Width of the base of the structure in meters.
    - depth (float): Depth of the base of the structure in meters.
    - floors (int): Number of floors or layers in the structure.
    - void_ratio (float): Proportion of void volume to total volume, between 0 and 1.
    - seed (int): Seed for random number generator to ensure replicability.
    
    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    floor_height = height / floors
    geometries = []

    # Create layers and introduce voids
    for i in range(floors):
        # Create solid floor slab
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * floor_height))
        slab = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, floor_height * (1 - void_ratio)))
        brep_slab = slab.ToBrep()
        geometries.append(brep_slab)

        # Create voids in the slab
        void_count = random.randint(1, 3)  # Randomly choose the number of voids per floor
        for _ in range(void_count):
            void_width = random.uniform(0.2, 0.5) * width
            void_depth = random.uniform(0.2, 0.5) * depth
            void_x = random.uniform(0, width - void_width)
            void_y = random.uniform(0, depth - void_depth)
            
            void_box = rg.Box(base_plane, rg.Interval(void_x, void_x + void_width), rg.Interval(void_y, void_y + void_depth), rg.Interval(0, floor_height))
            brep_void = void_box.ToBrep()
            
            # Subtract void from the slab
            result = rg.Brep.CreateBooleanDifference([brep_slab], [brep_void], 0.01)
            if result:
                brep_slab = result[0]

        # Add the final slab with voids to the list of geometries
        geometries[-1] = brep_slab

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=15, depth=15, floors=6, void_ratio=0.25, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=50, width=12, depth=12, floors=4, void_ratio=0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=20, depth=5, floors=3, void_ratio=0.2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=45, width=18, depth=8, floors=5, void_ratio=0.35, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=60, width=25, depth=20, floors=7, void_ratio=0.5, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
