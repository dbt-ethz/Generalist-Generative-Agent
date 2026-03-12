# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model that embodies the metaphor of "Suspended intersecting assembly." It creates a series of lightweight, wireframe elements that appear to float and intersect in space. By randomly generating start and end points for each element within specified dimensions, the function emphasizes fluidity and structural transparency. The use of thin pipes simulates the delicate nature of these components, while varying angles and heights enhances visual interconnectivity and movement. The result is a dynamic model that reflects the metaphor's essence of balance and tension, evoking a sense of suspended geometry."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_size, height, num_elements, seed=42):
    \"""
    Creates an architectural Concept Model that embodies the 'Suspended intersecting assembly' metaphor.

    This function generates a model composed of intersecting wireframe elements that appear to float in space.
    The design emphasizes lightness, fluidity, and structural transparency, with elements intersecting at various angles.

    Parameters:
    - base_size (float): The size of the base area for the model (in meters), assuming a square base.
    - height (float): The maximum height of the model (in meters).
    - num_elements (int): The number of intersecting wireframe elements to create.
    - seed (int, optional): Seed for the random number generator to ensure replicable results.

    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for _ in range(num_elements):
        # Randomly generate the start and end points of a wireframe element
        start_x = random.uniform(0, base_size)
        start_y = random.uniform(0, base_size)
        start_z = random.uniform(0, height)
        
        end_x = random.uniform(0, base_size)
        end_y = random.uniform(0, base_size)
        end_z = random.uniform(0, height)

        start_point = rg.Point3d(start_x, start_y, start_z)
        end_point = rg.Point3d(end_x, end_y, end_z)

        # Create a line element between the two points
        line = rg.Line(start_point, end_point)

        # Generate a pipe around the line to simulate a wireframe element
        pipe_radius = random.uniform(0.01, 0.05)  # Thin wire-like radius
        pipe_brep = rg.Brep.CreatePipe(line.ToNurbsCurve(), pipe_radius, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0]

        geometries.append(pipe_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(5.0, 10.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(3.0, 8.0, 15, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(4.0, 12.0, 25, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(6.0, 15.0, 30, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(2.5, 5.0, 10, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
