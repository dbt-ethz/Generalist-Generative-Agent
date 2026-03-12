# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevered_concept_model`, generates an architectural concept model based on the metaphor of "Cantilevering corners." It creates a central core structure with extensions projecting outward at various angles and lengths, embodying the tension and balance inherent in cantilevered design. The function employs randomization to decide whether each extension is solid or void, enhancing the dynamic interplay between stability and instability. By manipulating dimensions and orientations, the model visually represents the metaphor's implications, showcasing unexpected voids and volumes while exploring how light and shadow interact across these cantilevered elements, thus fulfilling the design task effectively."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_size, extension_lengths, extension_angles, seed=42):
    \"""
    Creates an architectural Concept Model emphasizing the dynamic tension of cantilevered elements.
    
    The model consists of a central core from which extensions project outward in varying directions and lengths,
    creating a sense of balance and instability. The design focuses on the interplay between solid and void.

    Parameters:
    - core_size: tuple of floats (width, depth, height) representing the dimensions of the core in meters.
    - extension_lengths: list of floats representing the lengths of the cantilevered extensions in meters.
    - extension_angles: list of floats representing the angles (in degrees) at which each extension projects from the core.
    - seed: int, optional, seed for random number generator to ensure replicability (default is 42).

    Returns:
    - list of Rhino.Geometry.Brep objects representing the solid and void geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)

    # Create the central core
    core_width, core_depth, core_height = core_size
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    breps = [core.ToBrep()]

    # Function to create a cantilevered extension
    def create_extension(base_box, length, angle):
        # Randomly determine whether the extension will be a solid or void
        is_solid = random.choice([True, False])
        
        # Calculate the direction vector for the extension
        angle_rad = math.radians(angle)
        direction = rg.Vector3d(math.cos(angle_rad), math.sin(angle_rad), random.uniform(-0.3, 0.3))
        
        # Create the extension box
        extension_box = rg.Box(rg.Plane(base_box.Center, rg.Vector3d.ZAxis),
                               rg.Interval(0, length), rg.Interval(-core_depth / 4, core_depth / 4),
                               rg.Interval(-core_height / 4, core_height / 4))
        
        # Transform the extension box to its cantilevered position
        move_vector = direction * length
        transform = rg.Transform.Translation(move_vector)
        extension_box.Transform(transform)
        
        # Return the appropriate geometry based on whether it's solid or void
        if is_solid:
            return extension_box.ToBrep()
        else:
            corners = [extension_box.GetCorners()[i] for i in [0, 1, 4]]
            return rg.Brep.CreateFromCornerPoints(*corners, 0.01)
    
    # Create extensions at different angles and lengths
    for length, angle in zip(extension_lengths, extension_angles):
        extension = create_extension(core, length, angle)
        if extension:
            breps.append(extension)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model((2.0, 1.0, 3.0), [1.5, 2.0, 2.5], [30, 60, 90])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model((1.5, 1.5, 2.0), [2.0, 1.0, 1.5], [45, 135, 225])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model((3.0, 2.0, 4.0), [2.5, 3.0, 1.5], [15, 75, 120])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model((1.0, 2.0, 1.0), [1.0, 1.2, 1.4], [0, 90, 180])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model((2.5, 2.0, 3.5), [2.0, 1.8, 2.2], [10, 50, 100])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
