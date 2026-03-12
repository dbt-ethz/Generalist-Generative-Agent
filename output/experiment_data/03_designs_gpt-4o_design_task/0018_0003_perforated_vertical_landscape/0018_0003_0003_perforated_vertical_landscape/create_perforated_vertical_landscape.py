# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model based on the "Perforated vertical landscape" metaphor. It constructs a series of vertical fins or ribs with varying depths and spacing, which embody the essence of verticality and permeability. By utilizing parameters for height, width, and fin characteristics, the function creates a rhythmic interplay of solid (fins) and void (spaces) elements that allow light and air to penetrate the structure. This design approach fosters a connection with natural landscapes, resulting in adaptable interior spaces that enhance interactions between the building and its environment."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, fin_count, fin_thickness, void_variability):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    The model consists of vertical fins or ribs with interspersed voids, emphasizing vertical rhythm and
    interaction with light and air. The design suggests a connection to natural landscapes, with varying
    depths and spacing of elements to convey permeability and integration with the environment.
    
    Parameters:
        height (float): The total height of the structure in meters.
        width (float): The total width of the structure in meters.
        depth (float): The total depth of the structure in meters.
        fin_count (int): The number of vertical fins or ribs.
        fin_thickness (float): The thickness of each fin.
        void_variability (float): A parameter controlling the variability of voids between fins.
    
    Returns:
        List[Rhino.Geometry.Brep]: A list of Brep geometries representing the vertical fins and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness
    random.seed(42)

    # List to store resulting geometries
    geometries = []

    # Calculate spacing between fins
    total_spacing = (width - (fin_count * fin_thickness)) / (fin_count - 1)
    
    for i in range(fin_count):
        # Calculate the position of the current fin
        x_position = i * (fin_thickness + total_spacing)
        
        # Create the basic fin geometry
        fin = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position, x_position + fin_thickness), 
                     rg.Interval(0, depth), rg.Interval(0, height))
        geometries.append(fin.ToBrep())

        # Add voids randomly between the fins, controlled by void_variability
        if i < fin_count - 1:
            void_depth = depth * (0.5 + void_variability * (random.random() - 0.5))
            void_height = height * (0.5 + void_variability * (random.random() - 0.5))
            
            void = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position + fin_thickness, x_position + fin_thickness + total_spacing), 
                          rg.Interval(0, void_depth), rg.Interval(0, void_height))
            geometries.append(void.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 2.0, 8, 0.1, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 7.0, 3.0, 10, 0.15, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 2.5, 6, 0.2, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 1.5, 5, 0.05, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(20.0, 10.0, 4.0, 12, 0.2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
