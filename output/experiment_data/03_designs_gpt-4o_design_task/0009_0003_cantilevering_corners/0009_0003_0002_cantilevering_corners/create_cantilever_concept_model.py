# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The function `create_cantilever_concept_model` generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a central mass from which multiple cantilevered sections extend. Each cantilever is positioned at various heights and orientations to emphasize the dynamic interplay between stability and motion. The model contrasts the substantial base with lighter, projecting sections, enhancing the sense of suspension and tension. By incorporating voids and varying material thicknesses, the design invites exploration and interaction, while the shadows and light interplay further enhance the visual impact of the structure, embodying the metaphor's essence."""

#! python 3
function_code = """def create_cantilever_concept_model(base_length=10.0, base_width=10.0, base_height=5.0, 
                                    cantilever_length=5.0, cantilever_height=3.0, 
                                    base_material_thickness=0.3, cantilever_material_thickness=0.2, 
                                    num_cantilevers=4):
    \"""
    Creates an architectural Concept Model embodying the metaphor of 'Cantilevering corners'.
    
    This function generates a central mass with cantilevered extensions at various orientations
    and heights, emphasizing the interplay between stability and motion. The resulting geometry
    includes both solid and void elements to accentuate tension and balance.
    
    Parameters:
    - base_length (float): The length of the central base.
    - base_width (float): The width of the central base.
    - base_height (float): The height of the central base.
    - cantilever_length (float): The length of each cantilevered section.
    - cantilever_height (float): The height of each cantilevered section.
    - base_material_thickness (float): Thickness of the material for the central base.
    - cantilever_material_thickness (float): Thickness of the material for the cantilevers.
    - num_cantilevers (int): Number of cantilevered sections to create.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Seed for reproducibility
    random.seed(42)

    # Central base
    base = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height)).ToBrep()

    # Prepare list to store all geometries
    geometries = [base]

    # Function to create a cantilever
    def create_cantilever(base_corner, length, height, thickness, rotation_angle):
        plane = rg.Plane(base_corner, rg.Vector3d.ZAxis)
        cantilever_box = rg.Box(plane, rg.Interval(0, length), rg.Interval(-thickness, thickness), rg.Interval(0, height))
        cantilever = cantilever_box.ToBrep()
        axis = rg.Line(base_corner, rg.Point3d(base_corner.X, base_corner.Y, base_corner.Z + 1)).ToNurbsCurve()
        transform = rg.Transform.Rotation(rotation_angle, axis.PointAtEnd - axis.PointAtStart, base_corner)
        cantilever.Transform(transform)
        return cantilever

    # Add cantilevered sections
    for i in range(num_cantilevers):
        # Select a corner of the base randomly
        corner_index = random.randint(0, 3)
        if corner_index == 0:
            base_corner = rg.Point3d(0, 0, base_height)
        elif corner_index == 1:
            base_corner = rg.Point3d(base_length, 0, base_height)
        elif corner_index == 2:
            base_corner = rg.Point3d(base_length, base_width, base_height)
        else:
            base_corner = rg.Point3d(0, base_width, base_height)

        # Random orientation for cantilevers
        rotation_angle = random.uniform(0, 2 * 3.14159)  # Random rotation between 0 and 360 degrees

        # Creating the cantilever
        cantilever = create_cantilever(base_corner, cantilever_length, cantilever_height, cantilever_material_thickness, rotation_angle)
        geometries.append(cantilever)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilever_concept_model(base_length=15.0, base_width=10.0, cantilever_length=6.0, num_cantilevers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilever_concept_model(base_height=8.0, cantilever_height=4.0, base_material_thickness=0.5, cantilever_material_thickness=0.3, num_cantilevers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilever_concept_model(base_length=12.0, base_width=12.0, base_height=6.0, cantilever_length=4.0, cantilever_height=2.0, num_cantilevers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilever_concept_model(base_length=20.0, base_width=15.0, cantilever_length=7.0, cantilever_height=5.0, num_cantilevers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilever_concept_model(base_length=10.0, base_width=8.0, base_height=4.0, cantilever_length=5.0, cantilever_height=3.0, num_cantilevers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
