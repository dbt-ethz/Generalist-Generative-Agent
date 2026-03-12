import os

import Grasshopper
import Rhino
import System
from Rhino.FileIO import FileObj, FileObjWriteOptions, FileWriteOptions


class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, mesh: Grasshopper.DataTree[Rhino.Geometry.Mesh]):

        # set the write options
        write_options = FileWriteOptions()
        write_options.WriteSelectedObjectsOnly = True
        write_options.SuppressDialogBoxes = True
        # https://developer.rhino3d.com/api/rhinocommon/rhino.fileio.fileobjwriteoptions
        obj_options = FileObjWriteOptions(write_options)
        obj_options.CullUnnecessaryVertexesInNgons = True
        obj_options.EolType = FileObjWriteOptions.AsciiEol.Crlf
        obj_options.ExportAsTriangles = False
        # obj_options.ExportGroupNameLayerNames = FileObjWriteOptions.ObjGroupNames.NoGroups
        obj_options.ExportMaterialDefinitions = False
        obj_options.ExportNormals = False
        # obj_options.ExportObjectNames = FileObjWriteOptions.ObjObjectNames.NoObjects
        obj_options.ExportOpenMeshes = True
        obj_options.ExportTcs = True
        obj_options.ExportVcs = True
        obj_options.UseSimpleDialog = False
        obj_options.IncludeUnweldedEdgesInNgons = False
        obj_options.MapZtoY = True
        obj_options.MeshType = FileObjWriteOptions.VertexWelding.Normal
        obj_options.ObjectType = FileObjWriteOptions.GeometryType.Mesh
        obj_options.SignificantDigits = 16
        obj_options.WrapLongLines = False

        # get current gresshopper definition path
        file_name = ghenv.Component.OnPingDocument().FilePath
        # print(file_name)
        # get the directory of the file
        dir_name = os.path.dirname(file_name)
        # Create a list to store the file paths of generated obj files
        obj_file_paths = []

        # Loop through each path in the DataTree
        for i, path in enumerate(mesh.Paths):
            # Get the mesh at the current path
            mesh_list = mesh.Branch(path)

            # If the branch contains meshes, proceed with export
            if mesh_list:
                # Create the file name with the index padded to 2 digits
                padded_index = str(i).zfill(2)
                file_name = f"mesh_{padded_index}.obj"
                full_path = os.path.join(dir_name, file_name)

                # Write the mesh to the file
                FileObj.Write(full_path, meshes=list(mesh_list), options=obj_options)

                # Add the file path to the list
                obj_file_paths.append(full_path)

        # Output the list of generated file paths
        return obj_file_paths
