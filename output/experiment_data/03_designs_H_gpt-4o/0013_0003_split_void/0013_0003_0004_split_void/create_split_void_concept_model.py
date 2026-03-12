# Created for 0013_0003_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model based on the "Split void" metaphor by creating a central twisted void that influences spatial organization within the structure. It takes parameters such as dimensions and void characteristics to define the building's form. The base geometry is a rectangular prism, which is then intersected with a lofted, twisted void. This void acts as a dynamic separator, allowing for diverse spatial zones and enhancing light and movement throughout the design. The resulting geometries reflect the metaphor's emphasis on contrast, duality, and interaction, crucial for achieving the architectural identity."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, void_twist_angle):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor,
    featuring a central twisted void that introduces dynamic spatial separation
    and interaction.

    Parameters:
    - length (float): The length of the base form in meters.
    - width (float): The width of the base form in meters.
    - height (float): The height of the building form in meters.
    - void_width (float): The width of the void in meters.
    - void_twist_angle (float): The angle of twist for the void in degrees, adding a non-linear element.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep geometries representing the architectural model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Base geometry: a simple rectangular prism
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height)).ToBrep()

    # Create a twisted void
    void_profile_start = rg.Rectangle3d(rg.Plane.WorldXY, rg.Interval(-void_width / 2, void_width / 2), rg.Interval(-width / 2, width / 2))
    void_profile_end = rg.Rectangle3d(rg.Plane.WorldXY, rg.Interval(-void_width / 2, void_width / 2), rg.Interval(-width / 2, width / 2))
    void_profile_end.Transform(rg.Transform.Rotation(math.radians(void_twist_angle), rg.Vector3d.ZAxis, rg.Point3d.Origin))

    # Loft the two profiles to create a twisted void brep
    void_loft = rg.Brep.CreateFromLoft([void_profile_start.ToNurbsCurve(), void_profile_end.ToNurbsCurve()],
                                       rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
    void_brep = void_loft[0] if void_loft else None

    if void_brep is not None:
        # Cap the void to make it a solid
        void_brep = rg.Brep.CreateSolid([void_brep], 0.01)

    # Split the base geometry with the void
    split_brep = rg.Brep.CreateBooleanDifference([base_box], [void_brep], 0.01) if void_brep else None

    return split_brep if split_brep is not None else []"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 5.0, 3.0, 1.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15.0, 8.0, 4.0, 2.0, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(12.0, 6.0, 5.0, 1.5, 60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(20.0, 10.0, 7.0, 2.5, 90.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(8.0, 4.0, 3.5, 1.2, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
