# Created for 0001_0004_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model embodying the "House within a house" metaphor by creating a series of concentric cylindrical layers. Each layer represents a distinct spatial realm, transitioning from a protective outer envelope to a secluded inner sanctuary. The function uses parameters like inner and outer radii, height, and segment count to define the model's dimensions and smoothness. It incorporates light wells to enhance visual connectivity between layers, promoting natural light penetration. This approach effectively illustrates the metaphor's themes of nesting, protection, and the experiential journey through varying levels of intimacy in space."""

#! python 3
function_code = """def create_concept_model(inner_radius, outer_radius, height, segment_count):
    \"""
    Creates an architectural concept model based on the 'House within a house' metaphor.
    
    This function generates a composition of concentric cylindrical layers, representing nested spaces
    to evoke a sense of protection and privacy. Each layer is differentiated by its size, simulating the 
    transition from outer public spaces to a secluded inner sanctuary. The design includes light wells 
    to enhance the visual and light interplay between layers.
    
    Inputs:
        inner_radius: float - The radius of the innermost cylindrical space (sanctuary).
        outer_radius: float - The radius of the outermost cylindrical envelope.
        height: float - The height of the cylinders, defining the vertical extent of the model.
        segment_count: int - The number of segments used to create the cylindrical layers, influencing the 
                             smoothness of the geometry.
                             
    Outputs:
        List of RhinoCommon Brep objects - The generated 3D geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensures replicability

    # Create the inner sanctuary cylinder
    sanctuary_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, inner_radius), height).ToBrep(True, True)

    # Create the outer protective envelope cylinder
    envelope_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, outer_radius), height).ToBrep(True, True)

    # Create intermediate layers with varying radii to simulate nested spaces
    layers = []
    step = (outer_radius - inner_radius) / segment_count
    for i in range(1, segment_count):
        radius = inner_radius + i * step
        layer_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, radius), height).ToBrep(True, True)
        layers.append(layer_cylinder)

    # Create light wells by subtracting smaller cylinders from the layers
    light_wells = []
    for i, layer in enumerate(layers):
        well_radius = random.uniform(inner_radius / 4, inner_radius / 2)
        well_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, well_radius), height).ToBrep(False, False)
        light_well = rg.Brep.CreateBooleanDifference([layer], [well_cylinder], 0.01)
        if light_well:
            light_wells.extend(light_well)

    # Combine all layers into a single list
    all_layers = [sanctuary_cylinder, envelope_cylinder] + layers + light_wells

    return all_layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(5.0, 15.0, 10.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(3.0, 12.0, 8.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(4.0, 20.0, 15.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(6.0, 18.0, 12.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(2.5, 9.0, 7.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
