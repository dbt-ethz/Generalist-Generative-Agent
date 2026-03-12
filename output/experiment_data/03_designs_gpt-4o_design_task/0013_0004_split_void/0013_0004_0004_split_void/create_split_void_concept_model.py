# Created for 0013_0004_split_void.json

""" Summary:
The provided function generates an architectural concept model based on the "Split void" metaphor by creating a structure that emphasizes the interplay between solid forms and a central void. The model divides the building footprint into two solid sections, separated by a dynamically shaped void. The function incorporates randomness in rotation and translation to create visual tension and movement, enhancing the contrast between solid and void. By adjusting parameters like dimensions and void width, the model explores spatial relationships and light interactions, effectively embodying the metaphor's themes of duality and dynamic spatial experience."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, seed):
    \"""
    Create an architectural Concept Model based on the 'Split void' metaphor.
    
    This function generates a structure divided by a central void, emphasizing the interaction
    between solid and void spaces. The void acts as a dynamic element influencing the building's 
    spatial logic and identity.

    Parameters:
    length (float): The total length of the building footprint.
    width (float): The total width of the building footprint.
    height (float): The height of the building.
    void_width (float): The width of the central void.
    seed (int): Random seed for reproducibility of the design.

    Returns:
    list: A list of Brep geometry objects representing the architectural concept model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Calculate the positions of the void and solids
    half_void_width = void_width / 2
    half_width = width / 2

    # Create the base solid parts
    left_solid = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(-half_width, -half_void_width),
        rg.Interval(0, length),
        rg.Interval(0, height)
    )
    right_solid = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(half_void_width, half_width),
        rg.Interval(0, length),
        rg.Interval(0, height)
    )
    
    # Create the central void
    void_curve = rg.Circle(rg.Plane.WorldXY, half_void_width).ToNurbsCurve()
    void_surface = rg.Extrusion.Create(void_curve, height, True)

    # Apply transformations to create dynamic interaction
    rotation_angle = random.uniform(-15, 15)  # Rotation angle in degrees
    translation_distance = random.uniform(-2, 2)  # Translation distance in meters

    # Rotate and translate the solids to create tension and movement
    rotation_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, height)).ToNurbsCurve()
    left_solid.Transform(rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis.PointAtStart))
    right_solid.Transform(rg.Transform.Rotation(math.radians(-rotation_angle), rotation_axis.PointAtStart))
    left_solid.Transform(rg.Transform.Translation(translation_distance, 0, 0))
    right_solid.Transform(rg.Transform.Translation(-translation_distance, 0, 0))

    # Combine all geometry into a list
    geometry = [left_solid.ToBrep(), right_solid.ToBrep(), void_surface.ToBrep()]

    return geometry"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=20.0, width=10.0, height=15.0, void_width=4.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=25.0, width=12.0, height=18.0, void_width=5.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=30.0, width=15.0, height=20.0, void_width=6.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=22.0, width=14.0, height=10.0, void_width=3.0, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=18.0, width=8.0, height=12.0, void_width=2.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
