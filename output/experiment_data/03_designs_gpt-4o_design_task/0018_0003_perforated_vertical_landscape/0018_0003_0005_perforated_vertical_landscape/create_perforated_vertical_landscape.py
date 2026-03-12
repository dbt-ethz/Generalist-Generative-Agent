# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating vertical fins with voids that allow light and air to pass through. It accepts parameters for the structures dimensions, number of fins, and void ratio. For each fin, the function calculates its position, dimensions, and randomly generates voids, which are then subtracted to create perforations. This results in a series of fins that embody verticality and permeability, aligning with the metaphor's essence, while enabling flexible interior spaces that adapt to varying light conditions and enhance the connection to the environment."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=5, fin_count=15, void_ratio=0.3):
    \"""
    Creates an architectural Concept Model based on the 'Perforated vertical landscape' metaphor. 
    The model consists of vertical fins with interspersed voids to allow light and air to penetrate the structure.

    Args:
    - height (float): Total height of the structure in meters.
    - width (float): Width of the structure in meters.
    - depth (float): Depth of the fins in meters.
    - fin_count (int): Number of vertical fins.
    - void_ratio (float): Ratio of voids to total fin area, between 0 and 1.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the fins with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensures replicable randomness

    # Calculate spacing between fins
    spacing = width / fin_count

    # Create list to store Brep geometries
    breps = []

    for i in range(fin_count):
        # Calculate fin position
        x_position = i * spacing

        # Create base surface for each fin using a PlaneSurface
        plane = rg.Plane(rg.Point3d(x_position, 0, 0), rg.Vector3d.ZAxis)
        fin_surface = rg.PlaneSurface(plane, rg.Interval(0, depth), rg.Interval(0, height))

        # Create Brep from surface to calculate area
        brep_fin = rg.Brep.CreateFromSurface(fin_surface)
        fin_area = brep_fin.GetArea()

        # Determine number of voids per fin
        voids_count = int(fin_area * void_ratio / (depth * height))

        # Generate voids
        voids = []
        for _ in range(voids_count):
            void_height = random.uniform(0.05 * height, 0.2 * height)
            void_y = random.uniform(0, height - void_height)
            void = rg.Rectangle3d(rg.Plane.WorldXY, rg.Interval(x_position, x_position + depth), rg.Interval(void_y, void_y + void_height))
            voids.append(void.ToNurbsCurve())

        # Subtract voids from the fin surface
        for void in voids:
            void_brep = rg.Brep.CreatePlanarBreps([void])[0]
            brep_fin = rg.Brep.CreateBooleanDifference([brep_fin], [void_brep], 0.01)[0]

        breps.append(brep_fin)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=15, depth=6, fin_count=20, void_ratio=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=35, width=12, depth=4, fin_count=10, void_ratio=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=25, width=8, depth=3, fin_count=12, void_ratio=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=32, width=14, depth=5, fin_count=18, void_ratio=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=28, width=16, depth=7, fin_count=22, void_ratio=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
