# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model reflecting the metaphor 'Porous fractured monolith' by creating a substantial base form with voids that symbolize complexity and movement. It starts by defining a monolithic mass using specified dimensions, then introduces randomly sized and positioned voids to reflect the metaphor's dynamic nature. These voids enhance spatial interaction and flow, representing both enclosure and openness. The process of Boolean subtraction integrates the voids into the solid mass, producing a model that embodies the key traits of solidity, lightness, and connectivity, inviting exploration and engagement within the design."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length=30, base_width=20, base_height=15, void_count=5, seed=42):
    \"""
    Creates a 'Porous fractured monolith' architectural concept model.
    
    The model consists of a substantial monolithic mass with integrated voids and fractures
    that convey dynamic complexity and movement. The voids serve as connectors between different
    zones, enhancing spatial flow and interaction.

    Parameters:
    - base_length: Length of the monolithic base form in meters.
    - base_width: Width of the monolithic base form in meters.
    - base_height: Height of the monolithic base form in meters.
    - void_count: Number of voids to introduce into the monolith.
    - seed: Random seed for reproducible results.

    Returns:
    - A list of RhinoCommon Brep objects representing the solid and void components of the model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set random seed
    random.seed(seed)

    # Create the monolithic base
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    # Create voids
    voids = []
    for _ in range(void_count):
        # Randomly position and size the voids within the base dimensions
        void_length = random.uniform(2, base_length / 2)
        void_width = random.uniform(2, base_width / 2)
        void_height = random.uniform(2, base_height / 2)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), 
                          rg.Interval(void_y, void_y + void_width), 
                          rg.Interval(void_z, void_z + void_height))
        void_brep = void_box.ToBrep()
        voids.append(void_brep)

    # Subtract voids from the base monolith
    result_brep = base_brep
    for void in voids:
        boolean_difference = rg.Brep.CreateBooleanDifference([result_brep], [void], 0.01)
        if boolean_difference:
            result_brep = boolean_difference[0]

    # Return the final geometry
    return [result_brep] + voids

# Example usage in Grasshopper: 
# breps = create_porous_fractured_monolith()"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(base_length=40, base_width=30, base_height=25, void_count=10, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(base_length=50, base_width=40, base_height=20, void_count=8, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(base_length=35, base_width=25, base_height=18, void_count=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(base_length=45, base_width=35, base_height=22, void_count=7, seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(base_length=60, base_width=50, base_height=30, void_count=12, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
