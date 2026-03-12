# Created for 0012_0002_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volume_structure`, generates an architectural concept model inspired by the metaphor "Twisted volumes." It creates a series of interlocking, twisted modules by defining parameters such as height, base diameter, and twist angle. Each module is represented as a lofted surface between a base and a top circle, with the latter rotated to introduce dynamic shapes. This process results in a visually complex structure that embodies fluidity and movement, while promoting unique spatial interactions. The twisting nature of the volumes enhances light and shadow play, thereby capturing the transformative essence of the metaphor."""

#! python 3
function_code = """def create_twisted_volume_structure(num_modules=6, module_height=5, base_diameter=8, max_twist=90):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor, focusing on the
    interplay of dynamic forms and spatial interactions. The model consists of a series of interlocking
    twisted volumes with varying degrees of twist, emphasizing transformation and movement.

    Parameters:
    - num_modules (int): The number of twisted modules to be generated.
    - module_height (float): The height of each module.
    - base_diameter (float): The diameter of each module at its base.
    - max_twist (float): The maximum twist angle in degrees applied to each module.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # List to hold the resulting Breps
    twisted_volumes = []

    # Calculate twist increment for each module
    twist_increment = max_twist / num_modules

    # Generate each module with increasing twist
    for i in range(num_modules):
        # Calculate the parameters for the current module
        current_twist = twist_increment * (i + 1)
        base_radius = base_diameter / 2

        # Create a base circle for the module
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)

        # Define the top circle with a rotation applied
        top_plane = rg.Plane.WorldXY
        top_plane.Translate(rg.Vector3d(0, 0, module_height))
        top_plane.Rotate(math.radians(current_twist), rg.Vector3d.ZAxis)
        top_circle = rg.Circle(top_plane, base_radius)

        # Create a lofted brep between the base and top circles
        loft_curves = [base_circle.ToNurbsCurve(), top_circle.ToNurbsCurve()]
        loft_brep = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft_brep:
            twisted_volumes.append(loft_brep[0])

    return twisted_volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volume_structure(num_modules=8, module_height=6, base_diameter=10, max_twist=120)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volume_structure(num_modules=5, module_height=4, base_diameter=6, max_twist=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volume_structure(num_modules=10, module_height=7, base_diameter=12, max_twist=150)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volume_structure(num_modules=7, module_height=3, base_diameter=9, max_twist=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volume_structure(num_modules=9, module_height=8, base_diameter=11, max_twist=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
