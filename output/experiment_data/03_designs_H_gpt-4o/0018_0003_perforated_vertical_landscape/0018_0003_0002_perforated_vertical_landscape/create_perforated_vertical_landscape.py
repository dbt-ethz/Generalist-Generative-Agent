# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model embodying the "Perforated vertical landscape" metaphor. It creates vertical fins with specified heights, widths, and perforation patterns to enhance light and air interaction. By defining the number and spacing of fins, along with their perforated sections, the model reflects the metaphor's emphasis on verticality and dynamic spatial experiences. The resulting geometries evoke a natural formation, with voids that suggest pathways and connections to the environment, aligning with the design task of integrating solid and void for a responsive architectural experience."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, fin_count, fin_thickness, fin_spacing, perforation_pattern):
    \"""
    Generates an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.

    This function creates a series of vertical fins with a specific perforation pattern, emphasizing the interplay of 
    light and air with the structure and creating a visually dynamic experience.

    Parameters:
    - height (float): The total height of the model in meters.
    - width (float): The overall width of the model in meters.
    - depth (float): The overall depth of the model in meters.
    - fin_count (int): The number of vertical fins or ribs to generate.
    - fin_thickness (float): The thickness of each vertical fin in meters.
    - fin_spacing (float): The spacing between each vertical fin in meters.
    - perforation_pattern (list of tuple): A list of tuples where each tuple contains the start and end height of 
      perforations for each fin.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the fins with perforations.
    \"""
    import Rhino.Geometry as rg

    geometries = []

    # Calculate the total width occupied by fins and spacing
    total_fin_width = fin_thickness + fin_spacing

    for i in range(fin_count):
        # Calculate the position of the current fin
        x_position = i * total_fin_width

        if x_position + fin_thickness > width:
            break  # Stop if the fins exceed the specified width

        # Create full height fin
        fin_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position, x_position + fin_thickness),
                         rg.Interval(0, depth), rg.Interval(0, height))

        # Convert box to Brep
        fin_brep = fin_box.ToBrep()

        # Create perforations based on the provided pattern
        for start_height, end_height in perforation_pattern:
            perforation_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position, x_position + fin_thickness),
                                     rg.Interval(0, depth), rg.Interval(start_height, end_height))
            perforation_brep = perforation_box.ToBrep()

            # Subtract the perforation from the fin
            fin_brep = rg.Brep.CreateBooleanDifference([fin_brep], [perforation_brep], 0.01)[0]

        geometries.append(fin_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(5.0, 10.0, 2.0, 6, 0.1, 0.2, [(1, 2), (3, 4)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(8.0, 12.0, 3.0, 8, 0.15, 0.25, [(2, 3), (4, 5), (6, 7)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(6.0, 15.0, 1.5, 5, 0.2, 0.3, [(0.5, 1.5), (2, 3)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(7.0, 14.0, 2.5, 10, 0.12, 0.15, [(1, 3), (4, 5), (6, 7)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(4.0, 8.0, 1.0, 4, 0.2, 0.4, [(0, 1), (2, 3)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
