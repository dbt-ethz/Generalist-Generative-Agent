# Created for 0012_0002_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volumes_spiral`, generates an architectural concept model that embodies the metaphor of "Twisted volumes" by constructing a series of interlocking, spiraling modules. Each module is created using a base and top circle, with the top circle twisted at a specified angle to evoke fluidity and dynamic movement. The function manipulates the height, radius, and twist angle to create varying shapes, facilitating unique spatial relationships and interactions. This design emphasizes light and shadow play through its layered geometry, reflecting the transformative nature of the metaphor while maintaining a coherent, complex visual impact."""

#! python 3
function_code = """def create_twisted_volumes_spiral(base_radius=3, module_height=4, spiral_height=20, twist_angle=30, num_spirals=3):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor by arranging modules in a spiral 
    configuration. This design approach emphasizes fluidity, dynamic spatial relationships, and the interplay of light 
    and shadow.

    Parameters:
    - base_radius (float): The base radius of each cylindrical module.
    - module_height (float): The height of each module.
    - spiral_height (float): The total height of the spiral.
    - twist_angle (float): The angle by which each module is twisted along the spiral, in degrees.
    - num_spirals (int): The number of spirals to generate.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the twisted spiral volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # List to store the resulting Breps
    spiral_volumes = []

    # Calculate the number of modules per spiral
    modules_per_spiral = int(spiral_height / module_height)

    # Create each spiral of twisted modules
    for spiral_index in range(num_spirals):
        for i in range(modules_per_spiral):
            # Create base circle for the module
            base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
            base_curve = base_circle.ToNurbsCurve()

            # Define the top circle with a twist
            angle_rad = math.radians(twist_angle * i)
            twisted_plane = rg.Plane.WorldXY
            twisted_plane.Rotate(angle_rad, rg.Vector3d.ZAxis)
            top_circle = rg.Circle(twisted_plane, base_radius)
            top_circle.Translate(rg.Vector3d(0, 0, module_height))
            top_curve = top_circle.ToNurbsCurve()

            # Loft between base and top circles
            loft = rg.Brep.CreateFromLoft([base_curve, top_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            twisted_module = loft[0] if loft else None

            # Move the module to the correct height and offset for spiraling
            if twisted_module:
                spiral_offset = 2 * math.pi * base_radius * (spiral_index + i / modules_per_spiral)
                translation = rg.Transform.Translation(rg.Vector3d(math.cos(spiral_offset) * base_radius,
                                                                   math.sin(spiral_offset) * base_radius,
                                                                   i * module_height))
                twisted_module.Transform(translation)
                spiral_volumes.append(twisted_module)

    return spiral_volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_spiral(base_radius=5, module_height=3, spiral_height=15, twist_angle=45, num_spirals=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_spiral(base_radius=2, module_height=5, spiral_height=25, twist_angle=60, num_spirals=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_spiral(base_radius=4, module_height=6, spiral_height=30, twist_angle=15, num_spirals=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_spiral(base_radius=6, module_height=2, spiral_height=10, twist_angle=90, num_spirals=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_spiral(base_radius=3, module_height=4, spiral_height=18, twist_angle=75, num_spirals=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
