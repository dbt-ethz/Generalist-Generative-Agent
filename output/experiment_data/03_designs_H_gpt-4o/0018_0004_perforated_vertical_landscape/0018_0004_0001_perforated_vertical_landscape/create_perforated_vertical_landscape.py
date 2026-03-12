# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor by creating a lattice-like structure that emphasizes verticality and openness. It uses parameters such as height, width, depth, and grid density to define the model's dimensions and the arrangement of solid and void elements. By incorporating randomness in element placement, the model embodies a dynamic interplay between light and air, allowing for permeability and connectivity. The resulting geometry reflects a natural lattice form, facilitating spatial interaction between interior and exterior spaces, thereby capturing the essence of the metaphor in a tangible structure."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, grid_density, seed=42):
    \"""
    Creates an architectural Concept Model inspired by the 'Perforated vertical landscape' metaphor.

    This function generates a lattice-like structure with a focus on verticality, using a combination of solid and void
    elements to promote openness and connectivity. The model emphasizes the interlacing of these elements to allow light
    and air to flow through, enhancing spatial interaction.

    Parameters:
    - height (float): The total height of the concept model in meters.
    - width (float): The total width of the concept model in meters.
    - depth (float): The total depth of the concept model in meters.
    - grid_density (int): The density of the vertical grid or mesh (number of divisions along the width and depth).
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)  # Ensure replicability

    breps = []

    # Calculate spacing based on grid density
    x_spacing = width / (grid_density + 1)
    y_spacing = depth / (grid_density + 1)
    z_spacing = height / grid_density

    # Create a lattice structure with varying density
    for i in range(grid_density + 1):
        for j in range(grid_density + 1):
            z = i * z_spacing
            for k in range(grid_density + 1):
                x = k * x_spacing
                y = j * y_spacing

                # Create either a vertical or horizontal element based on randomness and position
                if random.random() > 0.5:
                    # Create a vertical column
                    start = rg.Point3d(x, y, 0)
                    end = rg.Point3d(x, y, height)
                    line = rg.Line(start, end)
                else:
                    # Create a horizontal beam
                    start = rg.Point3d(x, 0, z)
                    end = rg.Point3d(x, depth, z)
                    line = rg.Line(start, end)

                # Decide on creating a solid or void element
                if random.random() > 0.3:
                    # Create a solid element
                    plane = rg.Plane(start, rg.Vector3d.ZAxis)
                    cylinder = rg.Cylinder(rg.Circle(plane, x_spacing * 0.1), line.Length)
                    breps.append(cylinder.ToBrep(True, True))

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=10.0, width=5.0, depth=3.0, grid_density=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=15.0, width=8.0, depth=4.0, grid_density=10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=12.0, width=6.0, depth=2.5, grid_density=8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=20.0, width=10.0, depth=5.0, grid_density=6, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=8.0, width=4.0, depth=2.0, grid_density=4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
