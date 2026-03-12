# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The provided function, `create_fractured_monolith_with_curved_voids`, generates an architectural concept model embodying the metaphor of a "Porous fractured monolith." It creates a solid block representing the monolithic form and introduces strategically placed, irregular curved voids within it to reflect the porous quality. This approach enhances the balance between solid and void, fostering dynamic interactions with light and shadow. The randomness in void placement contributes to a fractured appearance, promoting connectivity and exploration through the structure. By manipulating dimensions and void count, the model captures the essence of solidity, fragmentation, and spatial fluidity inherent in the metaphor."""

#! python 3
function_code = """def create_fractured_monolith_with_curved_voids(base_length, base_width, base_height, num_voids, seed):
    \"""
    Creates an architectural Concept Model embodying the 'Porous fractured monolith' metaphor with curved voids.

    This function generates a monolithic block with strategically placed curved voids to represent the porous, 
    fractured quality while maintaining a balance between solid and void. The voids are irregular and dynamic, 
    enhancing the interaction of light, shadow, and spatial relationships.

    Parameters:
    - base_length (float): The length of the monolithic block in meters.
    - base_width (float): The width of the monolithic block in meters.
    - base_height (float): The height of the monolithic block in meters.
    - num_voids (int): The number of voids to cut into the block.
    - seed (int): The seed for the random number generator to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the main solid and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed
    random.seed(seed)

    # Create the base monolithic block
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    # Create curved voids within the monolithic form
    voids = []
    for _ in range(num_voids):
        # Define a random arc to act as a void
        start_point = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        mid_point = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))
        end_point = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height))

        arc_curve = rg.ArcCurve(rg.Arc(start_point, mid_point, end_point))

        # Create a sweep surface along the arc
        sweep_profile = rg.Circle(rg.Plane(start_point, rg.Vector3d.ZAxis), random.uniform(0.5, 1.5))
        sweep_profile_curve = sweep_profile.ToNurbsCurve()  # Convert circle to curve
        sweep_surface = rg.Brep.CreateFromSweep(arc_curve, sweep_profile_curve, True, 0.01)
        
        if sweep_surface:
            void_brep = sweep_surface[0]
            voids.append(void_brep)

            # Subtract the voids from the base block
            result_breps = rg.Brep.CreateBooleanDifference([base_brep], [void_brep], 0.01)
            if result_breps:
                base_brep = result_breps[0]

    return [base_brep] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith_with_curved_voids(10.0, 5.0, 3.0, 6, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith_with_curved_voids(15.0, 8.0, 4.5, 10, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith_with_curved_voids(12.0, 6.0, 5.0, 8, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith_with_curved_voids(20.0, 10.0, 6.0, 5, 23)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith_with_curved_voids(8.0, 4.0, 2.0, 12, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
