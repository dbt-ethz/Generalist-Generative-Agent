# Created for 0013_0003_split_void.json

""" Summary:
The provided function `create_split_void_concept_model` generates an architectural concept model based on the "Split void" metaphor. It creates a base form defined by specified dimensions, then introduces a central void that acts as an organizing element, cutting through the structure at a designated angle. This void enhances spatial dynamics by creating distinct zones and pathways, encouraging movement while allowing light and visual connections to permeate the design. The resulting model reflects the duality and contrast inherent in the metaphor, showcasing how the void influences both the buildings composition and user interaction through its tectonic expression."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, base_height, void_angle, seed=None):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor. The model features a central
    void that acts as an organizing element, creating distinct spatial zones and encouraging movement
    through varied pathways. The void is introduced at an angle to enrich spatial dynamics and impacts the
    building's composition, circulation, and tectonic expression.

    Parameters:
    - base_length (float): The length of the base building form.
    - base_width (float): The width of the base building form.
    - base_height (float): The height of the base building form.
    - void_angle (float): The angle (in degrees) at which the central void cuts through the base form.
    - seed (int, optional): A seed for randomization to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D brep geometries representing the architectural concept model.
    \"""
    import Rhino
    import random
    import math

    if seed is not None:
        random.seed(seed)

    # Define base form
    base_box = Rhino.Geometry.Box(
        Rhino.Geometry.Plane.WorldXY,
        Rhino.Geometry.Interval(0, base_length),
        Rhino.Geometry.Interval(0, base_width),
        Rhino.Geometry.Interval(0, base_height)
    )
    base_brep = base_box.ToBrep()

    # Define the void
    void_plane_origin = Rhino.Geometry.Point3d(base_length / 2, base_width / 2, 0)
    void_plane_normal = Rhino.Geometry.Vector3d(
        math.sin(math.radians(void_angle)), 
        math.cos(math.radians(void_angle)), 
        0
    )
    void_plane = Rhino.Geometry.Plane(void_plane_origin, void_plane_normal)

    # Define void cut
    void_cut = Rhino.Geometry.PlaneSurface(
        void_plane,
        Rhino.Geometry.Interval(-base_width * 2, base_width * 2),
        Rhino.Geometry.Interval(-base_height, base_height * 2)
    ).ToBrep()

    # Split the base form with the void cut
    split_result = Rhino.Geometry.Brep.Split(base_brep, [void_cut], 0.01)

    if len(split_result) < 2:
        raise ValueError("Splitting the base form did not produce the expected number of parts.")

    # Ensure the void is a true void by removing the part that intersects
    void_brep = split_result[0] if split_result[0].GetVolume() < split_result[1].GetVolume() else split_result[1]

    # Collect remaining parts as solid geometries
    solid_breps = [b for b in split_result if b != void_brep]

    return solid_breps

# Example usage:
# breps = create_split_void_concept_model(30, 20, 15, 45, seed=42)"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(40, 25, 10, 30, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(50, 30, 20, 60, seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(35, 15, 25, 75, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(45, 35, 15, 15, seed=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(60, 40, 30, 90, seed=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
