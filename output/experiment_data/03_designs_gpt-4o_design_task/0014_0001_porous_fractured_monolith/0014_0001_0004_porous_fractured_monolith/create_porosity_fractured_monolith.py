# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porosity_fractured_monolith` generates an architectural concept model inspired by the metaphor "Porous fractured monolith." It begins by creating a solid monolithic block defined by specified dimensions. The function then introduces a series of voids through random geometric cuts, embodying the metaphor's themes of fragmentation and permeability. These voids are strategically placed to enhance the interplay of light and shadow, allowing for dynamic spatial relationships that connect interior and exterior spaces. This process results in a model that visually represents the balance between solidity and transparency, fostering exploration and interaction throughout the structure."""

#! python 3
function_code = """def create_porosity_fractured_monolith(base_length=30, base_width=20, base_height=10, void_count=5, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Porous fractured monolith' metaphor. 
    The model consists of a monolithic form with strategic voids and openings, emphasizing the 
    balance between solidity and permeability.

    Parameters:
    - base_length (float): The length of the base monolithic block in meters.
    - base_width (float): The width of the base monolithic block in meters.
    - base_height (float): The height of the base monolithic block in meters.
    - void_count (int): The number of voids to be introduced in the monolithic form.
    - seed (int): Seed for randomness to ensure replicability in the generation of voids.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the solid and void components of the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Box, Plane, Point3d, Vector3d, Brep, Interval

    # Set the random seed for consistent results
    random.seed(seed)

    # Create the base monolithic form
    base_plane = Plane.WorldXY
    base_box = Box(base_plane, Interval(0, base_length), Interval(0, base_width), Interval(0, base_height))
    base_brep = base_box.ToBrep()

    breps = [base_brep]

    # Create voids within the monolithic form
    for _ in range(void_count):
        void_length = random.uniform(base_length * 0.1, base_length * 0.3)
        void_width = random.uniform(base_width * 0.1, base_width * 0.3)
        void_height = random.uniform(base_height * 0.4, base_height * 0.8)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

        void_plane = Plane(Point3d(void_x, void_y, void_z), Vector3d.ZAxis)
        void_box = Box(void_plane, Interval(0, void_length), Interval(0, void_width), Interval(0, void_height))
        void_brep = void_box.ToBrep()

        # Subtract the void from the base brep
        split_breps = Brep.CreateBooleanDifference(breps, [void_brep], Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance)
        if split_breps:
            breps = split_breps

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porosity_fractured_monolith(base_length=40, base_width=25, base_height=15, void_count=8, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porosity_fractured_monolith(base_length=50, base_width=30, base_height=20, void_count=10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porosity_fractured_monolith(base_length=35, base_width=22, base_height=12, void_count=6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porosity_fractured_monolith(base_length=45, base_width=28, base_height=18, void_count=7, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porosity_fractured_monolith(base_length=60, base_width=40, base_height=25, void_count=12, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
