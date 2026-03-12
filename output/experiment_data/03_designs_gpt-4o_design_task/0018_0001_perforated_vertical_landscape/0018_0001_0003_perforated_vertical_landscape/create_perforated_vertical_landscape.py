# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model that embodies the metaphor of a "Perforated vertical landscape." By creating a vertical structure with multiple layers, it alternates solid blocks with voids to simulate a dynamic interplay of light and shadow, akin to natural formations like cliffs or mountains. The random placement of voids allows for transparency and permeability, enhancing spatial interactions between interior and exterior spaces. The resulting geometries reflect the metaphor's essence, showcasing a balance of mass and void while inviting natural light and views into the design, thus fulfilling the design task effectively."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=10, num_layers=5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    This function generates a vertical form with alternating solid and void elements, designed to
    mimic a natural cliff face or mountain with perforations that enhance light and spatial interaction.
    
    Parameters:
    - height (float): Total height of the structure in meters.
    - width (float): Total width of the structure in meters.
    - depth (float): Total depth of the structure in meters.
    - num_layers (int): Number of horizontal layers in the structure.
    - seed (int): Random seed for replicable void pattern generation.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Calculate the height of each layer
    layer_height = height / num_layers
    
    # Initialize an empty list to store the breps
    breps = []
    
    # Generate the layers
    for i in range(num_layers):
        # Calculate the base height of the current layer
        base_height = i * layer_height
        
        # Create a solid block for this layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = base_height
        block = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, layer_height)).ToBrep()
        
        # Create voids within the block
        num_voids = random.randint(1, 3)
        for _ in range(num_voids):
            void_width = random.uniform(1, width / 2)
            void_depth = random.uniform(1, depth / 2)
            void_height = random.uniform(layer_height / 2, layer_height)
            void_x = random.uniform(0, width - void_width)
            void_y = random.uniform(0, depth - void_depth)
            void_z = base_height + random.uniform(0, layer_height - void_height)
            
            void_plane = rg.Plane.WorldXY
            void_plane.OriginX = void_x
            void_plane.OriginY = void_y
            void_plane.OriginZ = void_z
            
            void_box = rg.Box(void_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height)).ToBrep()
            boolean_result = rg.Brep.CreateBooleanDifference([block], [void_box], 0.01)
            if boolean_result:
                block = boolean_result[0]
        
        # Add the modified block to the list
        breps.append(block)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=50, width=15, depth=15, num_layers=7, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=40, width=20, depth=5, num_layers=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=12, depth=8, num_layers=6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=60, width=25, depth=20, num_layers=8, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, width=18, depth=12, num_layers=5, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
