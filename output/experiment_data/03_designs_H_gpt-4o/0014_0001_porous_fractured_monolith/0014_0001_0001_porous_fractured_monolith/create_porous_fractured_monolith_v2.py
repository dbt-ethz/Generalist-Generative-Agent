# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith_v2` generates an architectural concept model that embodies the metaphor of a "Porous fractured monolith." It constructs a monolithic block defined by specified dimensions, then introduces irregular voids through strategically placed, rotated planes. This design approach creates a balance between solidity and transparency, allowing for dynamic interactions of light and shadow. The resulting model showcases a fragmented silhouette, promoting fluid connections between interior and exterior spaces. The voids facilitate movement and engagement, reflecting the metaphor's emphasis on connectivity and the interplay of mass and void, ultimately resulting in an exploratory spatial experience."""

#! python 3
function_code = """def create_porous_fractured_monolith_v2(base_length, base_width, base_height, num_voids, seed):
    \"""
    Creates an architectural Concept Model embodying the 'Porous fractured monolith' metaphor.

    This function constructs a monolithic block with irregular, strategically placed voids, 
    representing permeability and fragmentation. The voids are cut using rotated planes, 
    enhancing the dynamic interaction of light and shadow.

    Parameters:
    - base_length (float): The length of the monolithic block in meters.
    - base_width (float): The width of the monolithic block in meters.
    - base_height (float): The height of the monolithic block in meters.
    - num_voids (int): The number of voids to create within the block.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the monolithic form with voids.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for consistent results
    random.seed(seed)

    # Create the base monolithic block
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []

    # Create voids by slicing the block with rotated planes
    for _ in range(num_voids):
        # Randomly define the rotation axis and angle
        axis_point = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        axis_dir = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        axis_dir.Unitize()

        angle = random.uniform(math.pi / 6, math.pi / 3)  # Angle between 30 and 60 degrees

        # Create a rotated plane for slicing
        slicing_plane = rg.Plane(axis_point, axis_dir)
        slicing_plane.Rotate(angle, slicing_plane.Normal)

        # Create an infinite surface from the plane for slicing
        slicing_surface = rg.PlaneSurface(slicing_plane, rg.Interval(-1e9, 1e9), rg.Interval(-1e9, 1e9))

        # Split the base brep using the slicing surface
        split_breps = base_brep.Split(slicing_surface.ToBrep(), 0.01)
        if split_breps:
            # Randomly keep one of the resulting breps as the void
            void_brep = random.choice(split_breps)
            voids.append(void_brep)

            # Update the base brep to the other part
            base_brep = next(brep for brep in split_breps if brep is not void_brep)

    return [base_brep] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith_v2(10.0, 5.0, 3.0, 4, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith_v2(15.0, 7.5, 4.0, 6, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith_v2(12.0, 6.0, 2.5, 5, 27)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith_v2(8.0, 4.0, 2.0, 3, 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith_v2(20.0, 10.0, 5.0, 8, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
