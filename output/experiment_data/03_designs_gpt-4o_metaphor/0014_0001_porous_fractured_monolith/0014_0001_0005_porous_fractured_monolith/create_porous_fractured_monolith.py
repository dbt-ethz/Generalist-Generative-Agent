# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model based on the metaphor "Porous fractured monolith." It creates a solid monolithic structure defined by user-specified dimensions, while incorporating voids and fractures that embody the metaphor's duality of solidity and permeability. The function utilizes parameters for void density and fracture intensity to control the number and size of the openings and disruptions, promoting dynamic interactions between interior and exterior spaces. The resulting 3D geometries reflect complexity and engagement, aligning with the metaphor's emphasis on connectivity and visual tension within a unified structure."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, height, void_density=0.2, fracture_intensity=0.3, seed=42):
    \"""
    Creates a conceptual architectural model representing a 'Porous fractured monolith'.

    The model is a solid monolithic form with strategic voids and fractures to suggest permeability and fragmentation.
    The solid mass balances unity and disruption, allowing for dynamic spatial interaction.

    Parameters:
    - base_length (float): The length of the base of the monolith in meters.
    - base_width (float): The width of the base of the monolith in meters.
    - height (float): The height of the monolith in meters.
    - void_density (float): A value between 0 and 1 indicating the proportion of voids within the monolith.
    - fracture_intensity (float): A value between 0 and 1 indicating the intensity of the fractures.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino
    import random
    import Rhino.Geometry as rg

    # Set the seed for randomness
    random.seed(seed)

    # Create the base solid monolith
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, height))
    monolith_brep = base_box.ToBrep()

    # Calculate number of voids based on density
    num_voids = int(void_density * 10)  # Arbitrary scaling for demonstration

    # Create voids (cylindrical for simplicity) and subtract from monolith
    voids = []
    for _ in range(num_voids):
        void_radius = random.uniform(0.5, 1.5)  # Random radius between 0.5 and 1.5 meters
        void_height = height + random.uniform(1, 2)  # Ensure voids penetrate through the monolith
        void_center = rg.Point3d(random.uniform(0, base_length),
                                 random.uniform(0, base_width),
                                 random.uniform(0, height))
        void_cylinder = rg.Cylinder(rg.Circle(rg.Plane(void_center, rg.Vector3d.ZAxis), void_radius), void_height)
        voids.append(void_cylinder.ToBrep(True, True))

    # Subtract voids from monolith
    porous_monolith_result = rg.Brep.CreateBooleanDifference([monolith_brep], voids, 0.01)
    porous_monolith = porous_monolith_result[0] if porous_monolith_result else monolith_brep

    # Simulate fractures by creating slits or cuts
    fractures = []
    num_fractures = int(fracture_intensity * 5)  # Arbitrary scaling for demonstration
    for _ in range(num_fractures):
        fracture_start = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), 0)
        fracture_end = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), height)
        fracture_line = rg.Line(fracture_start, fracture_end)
        fracture_curve = fracture_line.ToNurbsCurve()
        fracture_surface = rg.Surface.CreateExtrusion(fracture_curve, rg.Vector3d(0, 0, height))
        fractures.append(fracture_surface.ToBrep())

    # Subtract fractures from the porous monolith
    fractured_monolith_result = rg.Brep.CreateBooleanDifference([porous_monolith], fractures, 0.01)
    fractured_monolith = fractured_monolith_result[0] if fractured_monolith_result else porous_monolith

    return [fractured_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(5.0, 3.0, 10.0, void_density=0.25, fracture_intensity=0.4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(7.0, 4.0, 12.0, void_density=0.15, fracture_intensity=0.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(6.0, 2.5, 8.0, void_density=0.3, fracture_intensity=0.2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(10.0, 5.0, 15.0, void_density=0.1, fracture_intensity=0.6, seed=57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(8.0, 3.5, 9.0, void_density=0.4, fracture_intensity=0.1, seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
