# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model embodying the "Perforated vertical landscape" metaphor. It constructs vertical fins that symbolize the building's form, emphasizing verticality and permeability. By defining parameters such as base dimensions, fin thickness, and perforation size, the function creates a series of interconnected vertical elements. Each fin features random circular perforations, allowing light and air to penetrate, thus enhancing interaction with the environment. The result is a dynamic and adaptable structure that reflects natural rhythms and textures, fostering a seamless connection between interior spaces and the surrounding landscape while capturing the essence of the metaphor."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_width, base_depth, height, fin_thickness, fin_spacing, perforation_size):
    \"""
    Creates a conceptual architectural model based on the 'Perforated vertical landscape' metaphor.

    Parameters:
    - base_width (float): The width of the building base in meters.
    - base_depth (float): The depth of the building base in meters.
    - height (float): The height of the structure in meters.
    - fin_thickness (float): The thickness of each vertical fin in meters.
    - fin_spacing (float): The spacing between each vertical fin in meters.
    - perforation_size (float): The diameter of the circular perforations in the fins in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the building structure.
    \"""
    import Rhino
    from Rhino.Geometry import Brep, Point3d, Vector3d, Plane, Box, Interval, Circle, Surface
    import random

    # Set randomness seed for replicability
    random.seed(42)

    # List to store the resulting Brep geometries
    geometries = []

    # Define the number of fins based on the base width and fin spacing
    num_fins = int(base_width / (fin_thickness + fin_spacing))

    for i in range(num_fins):
        # Calculate the position of each fin
        x_position = i * (fin_thickness + fin_spacing)

        # Create a vertical fin as a box from the base to the defined height
        fin_base = Box(Plane(Point3d(x_position, 0, 0), Vector3d.ZAxis), Interval(0, fin_thickness), Interval(0, base_depth), Interval(0, height))
        fin_brep = fin_base.ToBrep()

        # Create perforations as circular holes
        num_perforations = random.randint(3, 7)  # Random number of perforations per fin
        for _ in range(num_perforations):
            # Random position for each perforation within the fin
            perforation_height = random.uniform(perforation_size, height - perforation_size)
            perforation_center = Point3d(x_position + fin_thickness / 2, random.uniform(perforation_size, base_depth - perforation_size), perforation_height)
            perforation_circle = Circle(Plane(perforation_center, Vector3d.ZAxis), perforation_size / 2)
            perforation_surface = Surface.CreateExtrusion(perforation_circle.ToNurbsCurve(), Vector3d(0, 0, height))
            perforation_brep = perforation_surface.ToBrep()

            # Subtract the perforation from the fin
            result = Brep.CreateBooleanDifference(fin_brep, perforation_brep, 0.01)
            if result:
                fin_brep = result[0]

        # Add the perforated fin to the list of geometries
        geometries.append(fin_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 15.0, 0.2, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 20.0, 0.25, 0.4, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 10.0, 0.15, 0.3, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(15.0, 7.0, 12.0, 0.3, 0.6, 0.35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(14.0, 8.0, 18.0, 0.2, 0.7, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
