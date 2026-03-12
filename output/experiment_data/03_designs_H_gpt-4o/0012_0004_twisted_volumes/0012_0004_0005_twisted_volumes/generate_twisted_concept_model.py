# Created for 0012_0004_twisted_volumes.json

""" Summary:
The provided function, `generate_twisted_concept_model`, visually interprets the metaphor "Twisted volumes" by creating a series of layered and intersecting geometric volumes. Each volume is defined by its base dimensions, height, and a maximum twist angle, which introduces rotation and distortion. The function employs randomization to vary the twist and position of each volume, enhancing the dynamic and fluid nature of the design. Transparency cutouts are applied to emphasize light interaction, allowing for intricate light and shadow patterns, ultimately embodying the metaphors implications of movement, tension, and innovative spatial relationships. This results in a coherent architectural concept model."""

#! python 3
function_code = """def generate_twisted_concept_model(base_length, base_width, height, num_volumes, max_twist, transparency_factor):
    \"""
    Generates an architectural Concept Model embodying the 'Twisted volumes' metaphor.
    This function creates a series of layered and intersecting volumes, each with a unique twist,
    emphasizing dynamic balance and the play of light and shadow.

    Parameters:
    - base_length (float): The base length of each volume in meters.
    - base_width (float): The base width of each volume in meters.
    - height (float): The height of each volume in meters.
    - num_volumes (int): The number of volumes to generate.
    - max_twist (float): The maximum twist angle in degrees for the volumes.
    - transparency_factor (float): Ratio indicating transparency cutout extent (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted volumes.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    from System import Random
    import math

    # Seed for reproducibility
    random_gen = Random(42)

    # List to store the resulting Breps
    twisted_volumes = []

    # Generate each volume
    for i in range(num_volumes):
        # Define the base rectangle
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)

        # Define the extrusion vector
        extrusion_vector = rg.Vector3d(0, 0, height)

        # Calculate a random twist angle
        twist_angle = random_gen.NextDouble() * 2 * max_twist - max_twist
        twist_plane = rg.Plane(base_rect.Center, rg.Vector3d(0, 0, 1))
        twisted_rect = rg.Rectangle3d(twist_plane, base_length, base_width)
        twisted_rect.Transform(rg.Transform.Rotation(math.radians(twist_angle), rg.Vector3d(0, 0, 1), twisted_rect.Center))
        
        # Create a lofted surface between the base and twisted rectangle
        loft = rg.Brep.CreateFromLoft([base_rect.ToNurbsCurve(), twisted_rect.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        
        if loft:
            brep = loft[0]

            # Implement transparency cutouts
            if random_gen.NextDouble() < transparency_factor:
                cutout_scale = 0.7  # Define a scale for cutout
                cutout_transform = rg.Transform.Scale(base_rect.Plane, cutout_scale, cutout_scale, 1)
                cutout_rect = rg.Rectangle3d(base_rect.Plane, base_length * cutout_scale, base_width * cutout_scale)
                cutout_surface = rg.Brep.CreatePlanarBreps([cutout_rect.ToNurbsCurve()])[0]
                cutout_surface.Transform(cutout_transform)

                # Perform boolean difference to create a cutout
                boolean_diff = rg.Brep.CreateBooleanDifference(brep, cutout_surface, 0.01)
                if boolean_diff:
                    brep = boolean_diff[0]

            # Append the final twisted brep to the list
            twisted_volumes.append(brep)

        # Move the starting plane for the next volume
        base_rect.Transform(rg.Transform.Translation(random_gen.NextDouble() * 2 - 1, random_gen.NextDouble() * 2 - 1, height * 0.2))

    return twisted_volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_twisted_concept_model(5.0, 3.0, 10.0, 10, 45.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_twisted_concept_model(4.0, 2.5, 8.0, 15, 30.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_twisted_concept_model(6.0, 4.0, 12.0, 20, 60.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_twisted_concept_model(3.5, 2.0, 7.0, 12, 50.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_twisted_concept_model(7.0, 5.0, 15.0, 8, 90.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
