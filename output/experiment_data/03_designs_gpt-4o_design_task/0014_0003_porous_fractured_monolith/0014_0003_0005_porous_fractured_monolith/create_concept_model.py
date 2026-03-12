# Created for 0014_0003_porous_fractured_monolith.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Porous fractured monolith." It starts by creating a solid monolithic form, represented as a box, and then introduces irregular fissures that disrupt this mass, replicating the metaphor's essence. These fissures vary in shape and orientation, embodying complexity and movement, while their depth and width can be adjusted for intensity. The model integrates both solid and translucent materials, enhancing the contrast between mass and void, which facilitates natural light and airflow. Ultimately, the design fosters exploration and interaction within the spaces, aligning with the metaphor's implications."""

#! python 3
function_code = """def create_concept_model(base_size, num_fissures, fissure_intensity, void_materiality_factor):
    \"""
    Generate a 3D architectural Concept Model based on the metaphor 'Porous fractured monolith'.
    
    This function creates a cohesive monolithic form with irregular fissures and openings to convey
    a sense of movement and complexity. The model emphasizes the contrast between solid and translucent
    elements, illustrating a balance between strength and openness. The fissures influence the flow of
    spaces and light, encouraging exploration within the model.

    Parameters:
    - base_size: float, the size of the base monolithic form (in meters).
    - num_fissures: int, the number of fissures to introduce into the monolithic form.
    - fissure_intensity: float, controls the depth and width of the fissures.
    - void_materiality_factor: float, between 0 and 1, determines the proportion of translucent to solid elements.

    Returns:
    - List of RhinoCommon geometry objects (Breps) representing the concept model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(42)

    # Create the base monolith as a box
    base_monolith = rg.Brep.CreateFromBox(rg.BoundingBox(rg.Point3d(0, 0, 0), rg.Point3d(base_size, base_size, base_size)))

    # Generate fissures
    fissures = []
    for _ in range(num_fissures):
        # Randomly position and orient the fissure planes
        start_point = rg.Point3d(random.uniform(0, base_size), random.uniform(0, base_size), random.uniform(0, base_size))
        end_point = rg.Point3d(random.uniform(0, base_size), random.uniform(0, base_size), random.uniform(0, base_size))
        fissure_line = rg.Line(start_point, end_point)
        
        # Create a plane from the fissure line
        fissure_plane = rg.Plane(fissure_line.From, rg.Vector3d.ZAxis)
        fissure_width = random.uniform(0.1, fissure_intensity)
        
        # Generate a fissure volume
        fissure = rg.Brep.CreateFromBox(rg.BoundingBox(fissure_plane.PointAt(-fissure_width, -fissure_width), fissure_plane.PointAt(fissure_width, fissure_width)))
        fissures.append(fissure)

    # Subtract fissures from the base monolith
    fractured_monolith = base_monolith
    for fissure in fissures:
        difference_result = rg.Brep.CreateBooleanDifference([fractured_monolith], [fissure], 0.01)
        if difference_result:
            fractured_monolith = difference_result[0]

    # Determine void materiality
    voids = []
    for fissure in fissures:
        if random.random() < void_materiality_factor:
            voids.append(fissure)

    # Combine solids and voids
    concept_model = [fractured_monolith] + voids

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10.0, 5, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(15.0, 10, 0.8, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(8.0, 3, 0.6, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(12.0, 7, 0.4, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(20.0, 12, 0.7, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
