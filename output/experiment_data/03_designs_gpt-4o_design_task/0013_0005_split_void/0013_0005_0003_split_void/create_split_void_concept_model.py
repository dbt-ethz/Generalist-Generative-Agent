# Created for 0013_0005_split_void.json

""" Summary:
The provided function, `create_split_void_concept_model`, generates an architectural concept model by embodying the 'Split void' metaphor. It creates a building volume defined by specified dimensions and introduces a central void that divides this volume into two distinct segments. The orientation of the void either vertical or horizontal determines how the architectural mass is interrupted, creating contrast in form and materiality. This split enhances circulation and visual connections, fostering dynamic spatial experiences. The function outputs a list of 3D geometries that visually represent the duality and tension inherent in the design, demonstrating interaction with light and shadow."""

#! python 3
function_code = """def create_split_void_concept_model(width, depth, height, void_width, split_orientation='vertical'):
    \"""
    Create an architectural Concept Model that embodies the 'Split void' metaphor, featuring a central void that divides the structure into two distinct segments.
    
    Parameters:
    - width (float): The total width of the building in meters.
    - depth (float): The total depth of the building in meters.
    - height (float): The height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - split_orientation (str): The orientation of the split ('vertical' or 'horizontal').
    
    Returns:
    - List of RhinoCommon.Geometry.Brep: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Create the main building volume
    building_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height)).ToBrep()

    # Determine the orientation of the split void
    if split_orientation == 'vertical':
        # Create the vertical void
        void_x = (width - void_width) / 2
        void_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_width), rg.Interval(0, depth), rg.Interval(0, height)).ToBrep()
    else:
        # Create the horizontal void
        void_y = (depth - void_width) / 2
        void_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(void_y, void_y + void_width), rg.Interval(0, height)).ToBrep()

    # Split the building volume with the void volume
    split_parts = rg.Brep.CreateBooleanDifference([building_volume], [void_volume], 0.01)

    # Check if split was successful and return the results
    if split_parts:
        return split_parts
    else:
        return [building_volume]  # Return the original volume if split fails"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 20.0, 15.0, 2.0, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15.0, 30.0, 10.0, 3.0, 'horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(12.0, 18.0, 10.0, 4.0, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(8.0, 25.0, 12.0, 1.5, 'horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(14.0, 22.0, 18.0, 5.0, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
