# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The provided function, `create_fractured_monolith_with_slits`, generates an architectural concept model based on the metaphor "Porous fractured monolith." It begins by creating a substantial monolithic block, representing solidity. The function then introduces a series of randomly generated voids (slits) within this mass, reflecting the metaphor's dynamic and complex nature. These voids vary in size and orientation, illustrating permeability, lightness, and connectivity between spaces. By employing different slit counts and dimensions, the model captures the intended balance between enclosure and openness, inviting exploration and interaction within the architectural space."""

#! python 3
function_code = """def create_fractured_monolith_with_slits(base_length=25, base_width=15, base_height=10, slit_count=7, slit_thickness=0.5, seed=24):
    \"""
    Creates an architectural Concept Model based on the 'Porous fractured monolith' metaphor.
    
    The model features a substantial monolithic mass intersected by narrow slits that form a network of voids,
    illustrating the dynamic complexity and permeability of the metaphor.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - slit_count (int): Number of slits to create within the monolith.
    - slit_thickness (float): Thickness of each slit in meters.
    - seed (int): Random seed for reproducibility.

    Returns:
    - List of Rhino.Geometry objects (breps) representing the monolith with integrated slits.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)  # Ensuring replicability

    # Define the main monolithic block
    monolith = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = monolith.ToBrep()

    # Generate slits
    slits = []
    for _ in range(slit_count):
        slit_length = random.uniform(base_length * 0.3, base_length)
        slit_height = random.uniform(base_height * 0.3, base_height)
        
        slit_x = random.uniform(0, base_length - slit_length)
        slit_y = random.uniform(0, base_width - slit_thickness)
        slit_z = random.uniform(0, base_height - slit_height)

        slit_box = rg.Box(rg.Plane.WorldXY, rg.Interval(slit_x, slit_x + slit_length), rg.Interval(slit_y, slit_y + slit_thickness), rg.Interval(slit_z, slit_z + slit_height))
        slits.append(slit_box.ToBrep())

    # Boolean difference to carve slits out of the monolith
    result_brep = monolith_brep
    for slit in slits:
        result = rg.Brep.CreateBooleanDifference(result_brep, slit, 0.01)
        if result:
            result_brep = result[0]

    # Return the final geometry with slits
    return [result_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith_with_slits(base_length=30, base_width=20, base_height=15, slit_count=10, slit_thickness=0.4, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith_with_slits(base_length=40, base_width=25, base_height=20, slit_count=5, slit_thickness=0.6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith_with_slits(base_length=50, base_width=30, base_height=25, slit_count=12, slit_thickness=0.3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith_with_slits(base_length=35, base_width=22, base_height=18, slit_count=8, slit_thickness=0.7, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith_with_slits(base_length=28, base_width=18, base_height=12, slit_count=6, slit_thickness=0.8, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
