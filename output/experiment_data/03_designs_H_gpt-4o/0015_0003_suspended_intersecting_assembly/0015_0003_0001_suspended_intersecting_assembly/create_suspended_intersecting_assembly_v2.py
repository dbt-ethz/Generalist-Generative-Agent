# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly_v2` generates an architectural concept model inspired by the metaphor "Suspended intersecting assembly." It creates a series of modular components, each consisting of circular and linear elements that appear to float and intersect dynamically. By utilizing random positioning, the function ensures variability while maintaining a cohesive arrangement that emphasizes lightness, transparency, and interconnectivity. The generated components are combined into Brep geometries, visually representing the metaphor's key traits, such as balance and fluidity. These elements collectively form a network of spatial relationships, enhancing movement and engagement within the architectural model."""

#! python 3
function_code = """def create_suspended_intersecting_assembly_v2(num_modules=5, module_radius=1.5, module_height=6.0, seed=42):
    \"""
    Creates an architectural Concept Model that embodies the 'Suspended intersecting assembly' metaphor.

    This version focuses on creating modules that consist of intersecting circular and linear components forming 
    a floating assembly. The modules are strategically arranged to emphasize transparency, lightness, and dynamic spatial 
    connections.

    Inputs:
    - num_modules: The number of modules to generate in the model.
    - module_radius: The radius of the circular components within each module.
    - module_height: The height at which each module is suspended.
    - seed: A seed for random number generation to ensure replicability.

    Outputs:
    - A list of Brep geometries representing the suspended modules.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Initialize a list to hold the generated Breps
    brep_list = []

    # Define the base plane for the model
    base_plane = rg.Plane.WorldXY

    # Generate modules with intersecting components
    for _ in range(num_modules):
        # Randomly determine the center of the module within a defined range
        x_center = random.uniform(-10, 10)
        y_center = random.uniform(-10, 10)
        z_center = random.uniform(module_height - 2, module_height + 2)

        # Create a point for the center of the module
        center_point = rg.Point3d(x_center, y_center, z_center)

        # Create circular base component
        circle = rg.Circle(base_plane, center_point, module_radius)
        
        # Convert the circle to a NurbsCurve
        circle_curve = circle.ToNurbsCurve()

        # Create a pipe around the circle to represent the circular component
        circle_brep = rg.Brep.CreatePipe(circle_curve, 0.1, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0]
        
        # Create linear connecting component
        start_point = rg.Point3d(x_center - module_radius, y_center, z_center)
        end_point = rg.Point3d(x_center + module_radius, y_center, z_center)
        line_curve = rg.LineCurve(start_point, end_point)

        # Create a pipe around the line to represent the connecting rod
        line_brep = rg.Brep.CreatePipe(line_curve, 0.1, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0]

        # Combine components into a module
        module = rg.Brep.CreateBooleanUnion([circle_brep, line_brep], 0.01)

        # Add the module to the list of Breps
        brep_list.extend(module)

    # Return the list of Breps representing the model
    return brep_list"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly_v2(num_modules=8, module_radius=2.0, module_height=5.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly_v2(num_modules=10, module_radius=1.0, module_height=7.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly_v2(num_modules=6, module_radius=1.2, module_height=4.5, seed=57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly_v2(num_modules=12, module_radius=1.8, module_height=6.5, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly_v2(num_modules=7, module_radius=1.0, module_height=8.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
