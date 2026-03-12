# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `generate_porosity_fractured_monolith` creates an architectural concept model embodying the 'Porous fractured monolith' metaphor. It starts by defining a solid block that represents the monolithic form. The function then introduces a specified number of irregular voids, simulating the porous and fractured characteristics of the design. These voids enhance the interplay of light and shadow, creating dynamic spatial relationships that facilitate movement and interaction. By adjusting void sizes and locations, the model embodies the duality of solidity and permeability, promoting connectivity between interior and exterior spaces while reflecting the metaphors essence of complexity and engagement."""

#! python 3
function_code = """def generate_porosity_fractured_monolith(base_size, voids_count, seed):
    \"""
    Generates an architectural Concept Model representing the 'Porous fractured monolith' metaphor.

    The model is composed of a solid monolithic block with irregular voids introduced to emphasize
    the interplay between solidity and permeability. This approach creates dynamic spatial relationships
    and guides light and shadow interaction.

    Parameters:
    - base_size (tuple of floats): Dimensions of the monolithic base (length, width, height) in meters.
    - voids_count (int): Number of voids to be introduced within the monolith.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the solid and void components of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    length, width, height = base_size

    # Create the base monolithic block
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    base_brep = base_box.ToBrep()

    voids = []

    # Create voids
    for _ in range(voids_count):
        # Random dimensions for irregular voids
        void_radius = random.uniform(min(length, width, height) * 0.1, min(length, width, height) * 0.3)
        void_center_x = random.uniform(void_radius, length - void_radius)
        void_center_y = random.uniform(void_radius, width - void_radius)
        void_center_z = random.uniform(void_radius, height - void_radius)

        # Create a spherical void
        void_sphere = rg.Sphere(rg.Point3d(void_center_x, void_center_y, void_center_z), void_radius)
        void_brep = rg.Brep.CreateFromSphere(void_sphere)

        voids.append(void_brep)
    
    # Subtract voids from the base block
    fractured_monolith = base_brep
    for void in voids:
        boolean_difference = rg.Brep.CreateBooleanDifference([fractured_monolith], [void], 0.001)
        if boolean_difference:  # Check if the operation succeeded
            fractured_monolith = boolean_difference[0]

    return [fractured_monolith] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_porosity_fractured_monolith((10.0, 5.0, 3.0), 15, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_porosity_fractured_monolith((8.0, 4.0, 2.5), 10, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_porosity_fractured_monolith((12.0, 6.0, 4.0), 20, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_porosity_fractured_monolith((15.0, 10.0, 5.0), 25, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_porosity_fractured_monolith((9.0, 4.5, 3.5), 18, 33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
