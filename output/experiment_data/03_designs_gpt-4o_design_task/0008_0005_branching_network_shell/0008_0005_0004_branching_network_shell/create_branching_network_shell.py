# Created for 0008_0005_branching_network_shell.json

""" Summary:
The provided function generates an architectural concept model based on the "branching network shell" metaphor by creating a 3D structure that embodies organic, fractal-like forms. It utilizes parameters such as base radius, height, branch layers, and density to define the model's intricacy and rhythm. The function constructs a base, adds branching elements that mimic natural networks, and incorporates a semi-transparent shell that encapsulates the design while allowing light and air to permeate. This approach fosters a dynamic relationship with the environment, emphasizing interconnectedness and adaptability, thereby translating the metaphor into a tangible architectural form."""

#! python 3
function_code = """def create_branching_network_shell(base_radius, height, branch_layers, branch_density, transparency_factor):
    \"""
    Generates an architectural Concept Model using the 'branching network shell' metaphor.
    
    Parameters:
    - base_radius (float): The radius of the base of the structure in meters.
    - height (float): The total height of the structure in meters.
    - branch_layers (int): The number of layers of branching elements.
    - branch_density (int): The number of branches per layer.
    - transparency_factor (float): A value between 0 and 1 representing the degree of transparency of the shell.
    
    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)
    
    geometries = []
    
    # Create base
    base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
    base_brep = rg.Brep.CreatePlanarBreps([base_circle.ToNurbsCurve()])[0]
    geometries.append(base_brep)
    
    # Create branches
    for layer in range(branch_layers):
        layer_height = (height / branch_layers) * (layer + 1)
        for branch in range(branch_density):
            angle = (branch / branch_density) * 2 * math.pi
            start_point = rg.Point3d(base_radius * math.cos(angle), base_radius * math.sin(angle), layer_height)
            end_point = rg.Point3d((base_radius / 2) * math.cos(angle + random.uniform(-0.1, 0.1)), 
                                   (base_radius / 2) * math.sin(angle + random.uniform(-0.1, 0.1)), 
                                   layer_height + (height / branch_layers) * random.uniform(0.5, 1.5))
            
            line = rg.Line(start_point, end_point)
            cylinder = rg.Cylinder(rg.Circle(line.PointAt(0.5), base_radius * 0.05), line.Length)
            brep_cylinder = cylinder.ToBrep(True, True)
            geometries.append(brep_cylinder)
    
    # Create shell
    shell_radius = base_radius + 0.5
    shell = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d(0, 0, height / 2), shell_radius * (1 + transparency_factor)))
    geometries.append(shell)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_branching_network_shell(base_radius=5, height=10, branch_layers=4, branch_density=6, transparency_factor=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_branching_network_shell(base_radius=3, height=8, branch_layers=5, branch_density=8, transparency_factor=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_branching_network_shell(base_radius=4, height=12, branch_layers=3, branch_density=10, transparency_factor=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_branching_network_shell(base_radius=6, height=15, branch_layers=2, branch_density=5, transparency_factor=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_branching_network_shell(base_radius=7, height=20, branch_layers=6, branch_density=4, transparency_factor=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
