# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The function `create_cantilevered_concept_model` generates an architectural concept model by interpreting the metaphor of "Cantilevering corners." It constructs a central mass and attaches multiple cantilevered segments, each extending outward at varying heights and orientations. This design emphasizes the tension between stability and motion, creating a striking silhouette. The function incorporates voids beneath the cantilevers to enhance the feeling of suspension, while the varied scales and materials differentiate the solid core from the lighter extensions. Additionally, the model's interplay with light and shadows invites exploration and interaction with the surrounding environment, embodying the metaphor's dynamic nature."""

#! python 3
function_code = """def create_cantilevered_concept_model(base_size, cantilever_lengths, cantilever_heights, cantilever_orientations):
    \"""
    Creates a conceptual architectural model based on the metaphor of 'Cantilevering corners'.
    
    The function generates a central mass with various segments extending dramatically, each cantilevered 
    at different heights and orientations. It emphasizes the contrast between the substantial, stable core 
    and the lighter, projecting sections by using different scales and materiality. The model incorporates 
    voids beneath the cantilevered portions to accentuate the sense of suspension and tension.

    Parameters:
    - base_size: Tuple of three floats (width, depth, height) representing the dimensions of the central mass.
    - cantilever_lengths: List of floats representing the lengths of each cantilever.
    - cantilever_heights: List of floats representing the heights at which each cantilever is placed.
    - cantilever_orientations: List of tuples, each containing three floats (x, y, z) for the orientation vector of each cantilever.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for reproducibility
    random.seed(42)

    # Create the central mass
    base_width, base_depth, base_height = base_size
    base = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, base_height))
    geometries = [base.ToBrep()]

    # Generate cantilevered sections
    for i, length in enumerate(cantilever_lengths):
        height = cantilever_heights[i]
        orientation = cantilever_orientations[i]
        
        # Create a cantilevered box
        cantilever_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, length),
            rg.Interval(-base_depth / 4, base_depth / 4),
            rg.Interval(0, base_height / 4)
        )
        
        # Move the cantilever to the appropriate height and orientation
        translation = rg.Vector3d(orientation[0], orientation[1], height)
        cantilever_box.Transform(rg.Transform.Translation(translation))
        
        # Add the cantilever to the list of geometries
        geometries.append(cantilever_box.ToBrep())

    # Create voids beneath the cantilevered portions
    for cantilever in geometries[1:]:
        bounding_box = cantilever.GetBoundingBox(False)
        void_height = bounding_box.Max.Z - bounding_box.Min.Z
        void_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(bounding_box.Min.X, bounding_box.Max.X),
            rg.Interval(bounding_box.Min.Y, bounding_box.Max.Y),
            rg.Interval(bounding_box.Min.Z - void_height, bounding_box.Min.Z)
        )
        geometries.append(void_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model((10.0, 5.0, 8.0), [4.0, 6.0, 3.0], [2.0, 4.0, 1.0], [(1, 0, 2), (0, 1, 3), (1, 1, 1)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model((12.0, 6.0, 10.0), [5.0, 7.0], [3.0, 5.0], [(1, 2, 3), (0, 0, 4)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model((15.0, 7.0, 9.0), [5.5, 8.0, 4.0, 6.5], [3.5, 5.5, 2.0, 4.0], [(1, 0, 1), (0, 1, 2), (1, 1, 0), (0, 0, 3)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model((8.0, 4.0, 6.0), [3.0, 5.0, 2.5], [1.5, 3.0, 2.0], [(1, 1, 1), (0, 2, 2), (1, 0, 0)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model((9.0, 4.5, 7.0), [3.5, 4.5, 5.0], [2.0, 3.0, 4.0], [(1, 1, 0), (0, 1, 2), (1, 0, 3)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
