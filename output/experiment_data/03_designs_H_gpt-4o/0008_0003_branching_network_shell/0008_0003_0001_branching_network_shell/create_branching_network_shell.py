# Created for 0008_0003_branching_network_shell.json

""" Summary:
The function `create_branching_network_shell` generates an architectural concept model inspired by the "branching network shell" metaphor. It creates a layered structure with a central core that expands outward through a lattice framework of pathways and nodes, reflecting organic growth and interconnectedness. Each layer increases in complexity, facilitating varied interactions and activities within a protective yet permeable shell. The model emphasizes adaptability, allowing natural light to filter through, casting dynamic shadows and fostering a seamless integration with the environment. Ultimately, it embodies the metaphor's essence of connectivity and fluidity in architectural design."""

#! python 3
function_code = """def create_branching_network_shell(core_radius=5.0, layer_count=3, layer_height=4.0, shell_thickness=0.3):
    \"""
    Creates an architectural Concept Model embodying the 'branching network shell' metaphor.
    
    This function generates a layered structure with a branching network of pathways and nodes,
    forming a porous and adaptable shell-like enclosure. The design illustrates organic growth
    and interconnectedness, allowing for dynamic light and shadow interplay and promoting
    integration with the environment.

    Parameters:
    - core_radius (float): The radius of the central core of the structure.
    - layer_count (int): The number of vertical layers in the structure.
    - layer_height (float): The height of each layer.
    - shell_thickness (float): The thickness of the shell structure.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import math

    geometries = []

    # Create the central core as a cylinder
    core = rg.Cylinder(rg.Circle(rg.Point3d(0, 0, 0), core_radius), layer_count * layer_height).ToBrep(True, True)
    geometries.append(core)

    # Generate layered structure with branching network
    for layer in range(layer_count):
        layer_base_z = layer * layer_height
        nodes = []

        # Create nodes around the core at this layer
        node_count = 6 + layer  # Increase node count with each layer
        angle_step = 360.0 / node_count
        for i in range(node_count):
            angle = math.radians(i * angle_step)
            x = core_radius * math.cos(angle)
            y = core_radius * math.sin(angle)
            z = layer_base_z
            node = rg.Point3d(x, y, z)
            nodes.append(node)

        # Create the branching network connecting nodes in this layer
        for i in range(node_count):
            start_node = nodes[i]
            end_node = nodes[(i + 1) % node_count]
            branch_curve = rg.LineCurve(start_node, end_node)
            branch_pipe = rg.Brep.CreatePipe(branch_curve, shell_thickness, True, rg.PipeCapMode.Round, True, 0.01, 0.01)
            if branch_pipe:
                geometries.extend(branch_pipe)

        # Connect nodes to the next layer
        if layer < layer_count - 1:
            next_layer_z = (layer + 1) * layer_height
            for node in nodes:
                end_node = rg.Point3d(node.X, node.Y, next_layer_z)
                branch_curve = rg.LineCurve(node, end_node)
                branch_pipe = rg.Brep.CreatePipe(branch_curve, shell_thickness, True, rg.PipeCapMode.Round, True, 0.01, 0.01)
                if branch_pipe:
                    geometries.extend(branch_pipe)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(core_radius=6.0, layer_count=4, layer_height=5.0, shell_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(core_radius=7.0, layer_count=5, layer_height=3.0, shell_thickness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(core_radius=5.5, layer_count=6, layer_height=4.5, shell_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(core_radius=8.0, layer_count=2, layer_height=6.0, shell_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(core_radius=4.0, layer_count=3, layer_height=3.5, shell_thickness=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
