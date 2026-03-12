# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It creates a three-dimensional representation by defining multiple suspended elements represented as pipes, which mimic the illusion of floating structures. Each element's starting and ending points are randomly determined within a specified base area, emphasizing the dynamic intersections described in the metaphor. Additionally, semi-transparent meshes are created to enhance the visual complexity and fluidity of the design, while reflective surfaces can be integrated to further depict the interplay of light. The output is a cohesive model that embodies the proposed architectural characteristics."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length, base_width, height, num_elements, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Suspended intersecting assembly' metaphor.
    
    Parameters:
    - base_length (float): The length of the base area in meters.
    - base_width (float): The width of the base area in meters.
    - height (float): The overall height of the model in meters.
    - num_elements (int): The number of intersecting elements to generate.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    elements = []
    
    for _ in range(num_elements):
        # Randomly define the starting and ending points of the element within the base area
        start_x = random.uniform(0, base_length)
        start_y = random.uniform(0, base_width)
        end_x = random.uniform(0, base_length)
        end_y = random.uniform(0, base_width)
        
        # Create a line to represent the suspended element
        start_point = rg.Point3d(start_x, start_y, random.uniform(0, height))
        end_point = rg.Point3d(end_x, end_y, random.uniform(0, height))
        
        line = rg.Line(start_point, end_point)
        
        # Create a pipe around the line to represent the element
        pipe_radius = random.uniform(0.1, 0.3)
        pipe = rg.Brep.CreatePipe(line.ToNurbsCurve(), pipe_radius, True, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]
        
        # Add transparency by creating a mesh with holes
        mesh_faces = []
        for i in range(10):
            for j in range(10):
                if random.random() > 0.5:
                    pt1 = rg.Point3d(start_x + i, start_y + j, random.uniform(0, height))
                    pt2 = rg.Point3d(start_x + i + 1, start_y + j, random.uniform(0, height))
                    pt3 = rg.Point3d(start_x + i + 1, start_y + j + 1, random.uniform(0, height))
                    pt4 = rg.Point3d(start_x + i, start_y + j + 1, random.uniform(0, height))
                    mesh_faces.append((pt1, pt2, pt3, pt4))
        
        mesh = rg.Mesh()
        for face in mesh_faces:
            idx1 = mesh.Vertices.Add(face[0])
            idx2 = mesh.Vertices.Add(face[1])
            idx3 = mesh.Vertices.Add(face[2])
            idx4 = mesh.Vertices.Add(face[3])
            mesh.Faces.AddFace(idx1, idx2, idx3, idx4)
        
        elements.append(pipe)
        elements.append(mesh)
    
    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 5.0, 15.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(8.0, 4.0, 10.0, 15, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(12.0, 6.0, 20.0, 25, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15.0, 7.0, 12.0, 30, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(5.0, 3.0, 8.0, 10, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
