# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The provided function `create_perforated_vertical_landscape` generates an architectural concept model based on the metaphor of a "Perforated Vertical Landscape." It constructs a multi-layered structure, incorporating verticality and perforations that allow light, air, and views to flow through. Each layer of the model is defined by its dimensions and contains voids, which are randomly placed openings that create a dynamic interplay between solid and empty spaces. This rhythmic design evokes a natural landscape in a vertical form, resulting in a visually engaging and spatially interactive architectural model that aligns with the metaphor's essence."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_width, base_depth, height, num_layers, void_percentage):
    \"""
    Creates a conceptual architectural model described by the metaphor 'Perforated Vertical Landscape'.
    
    This function generates a structure with verticality and porous elements, allowing light, air, and views 
    to penetrate through its form. The design features a rhythmic interplay between solid and void to create 
    dynamic visual and spatial experiences, resembling a vertical landscape.

    Parameters:
    - base_width (float): The width of the base of the structure in meters.
    - base_depth (float): The depth of the base of the structure in meters.
    - height (float): The total height of the structure in meters.
    - num_layers (int): The number of vertical layers of perforations.
    - void_percentage (float): The percentage of void space in each layer (0 to 1).

    Returns:
    - List of Breps: The 3D geometries representing the conceptual structure.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed the random generator for replicability
    random.seed(42)

    # Calculate the height of each layer
    layer_height = height / num_layers

    # Initialize a list to store the resulting Breps
    breps = []

    for i in range(num_layers):
        # Define the bounding box of the current layer
        layer_base_z = i * layer_height
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(layer_base_z, layer_base_z + layer_height))
        
        # Convert the box into a Brep
        brep = box.ToBrep()
        
        # Determine the number of voids based on void percentage
        num_voids = int(void_percentage * 10)  # Arbitrary scaling for demonstration

        # Create voids within the layer
        for _ in range(num_voids):
            void_width = random.uniform(0.1 * base_width, 0.3 * base_width)
            void_depth = random.uniform(0.1 * base_depth, 0.3 * base_depth)
            void_height = random.uniform(0.5 * layer_height, 0.9 * layer_height)

            void_x = random.uniform(0, base_width - void_width)
            void_y = random.uniform(0, base_depth - void_depth)

            void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_width), rg.Interval(void_y, void_y + void_depth), rg.Interval(layer_base_z, layer_base_z + void_height))
            void_brep = void_box.ToBrep()

            # Subtract the void from the current Brep
            boolean_result = rg.Brep.CreateBooleanDifference([brep], [void_brep], 0.001)
            if boolean_result:
                brep = boolean_result[0]

        # Add the resulting Brep to the list
        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 20.0, 4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 6.0, 30.0, 5, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 8.0, 15.0, 3, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(20.0, 10.0, 25.0, 6, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 18.0, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
