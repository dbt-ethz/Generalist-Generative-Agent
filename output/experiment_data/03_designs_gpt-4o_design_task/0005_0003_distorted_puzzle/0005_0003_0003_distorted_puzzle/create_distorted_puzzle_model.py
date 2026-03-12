# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_model`, generates an architectural concept model inspired by the "Distorted puzzle" metaphor. It creates a series of geometric elements that are slightly twisted and rotated, reflecting the metaphor's emphasis on dynamic imbalance and visual complexity. Each element is randomly scaled and positioned, ensuring a playful interplay of sizes and orientations, which enhances the structure's interconnectedness. The function applies transformations to create a network of interdependent rooms and corridors, guiding movement through unexpected pathways. This approach evokes a sense of exploration and transformation, aligning with the metaphor's core qualities of coherence amid distortion."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_scale=10, twist_angle=15, num_elements=5, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    The model consists of a series of geometric elements that are twisted or rotated
    relative to each other, creating a dynamic and visually complex structure. The
    geometries are designed to interlock like a puzzle, with varying scales and orientations.
    
    Parameters:
    - base_scale (float): The base size of the elements in meters.
    - twist_angle (float): The maximum angle in degrees by which elements can be twisted.
    - num_elements (int): The number of geometric elements to create.
    - seed (int): The seed for the random number generator to ensure replicable results.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Breps representing the concept model.
    \"""
    import Rhino
    import random
    import math
    
    random.seed(seed)
    elements = []
    current_position = Rhino.Geometry.Point3d(0, 0, 0)
    
    for i in range(num_elements):
        # Create a base box for the element
        scale_factor = base_scale * random.uniform(0.8, 1.2)
        box = Rhino.Geometry.Box(
            Rhino.Geometry.Plane.WorldXY,
            Rhino.Geometry.Interval(0, scale_factor),
            Rhino.Geometry.Interval(0, scale_factor),
            Rhino.Geometry.Interval(0, scale_factor)
        )
        
        # Apply a random twist
        twist = random.uniform(-twist_angle, twist_angle)
        axis = Rhino.Geometry.Line(current_position, Rhino.Geometry.Point3d(current_position.X, current_position.Y, current_position.Z + scale_factor))
        twisted_brep = box.ToBrep()
        twist_transform = Rhino.Geometry.Transform.Rotation(math.radians(twist), axis.Direction, axis.From)
        twisted_brep.Transform(twist_transform)
        
        # Move the element to a new position
        offset_vector = Rhino.Geometry.Vector3d(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2))
        transform = Rhino.Geometry.Transform.Translation(offset_vector)
        twisted_brep.Transform(transform)
        
        # Add to elements
        elements.append(twisted_brep)
        
        # Update the current position
        current_position = Rhino.Geometry.Point3d.Add(current_position, offset_vector)
    
    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(base_scale=15, twist_angle=30, num_elements=10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_scale=8, twist_angle=45, num_elements=7, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_scale=12, twist_angle=20, num_elements=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_scale=5, twist_angle=10, num_elements=8, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_scale=20, twist_angle=25, num_elements=12, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
