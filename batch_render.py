import bpy
import os

# set the path for directory containing ply files
ply_dir = 'D:\Media\\blender models\Point Cloud Project\Input PLY'.replace("\\","/")

# set the path to the output folder for rendered images
output_folder = 'D:\Media\\blender models\Point Cloud Project\Output PNG'.replace("\\","/")

# get a list of all .ply files in the directory
ply_files = [f for f in os.listdir(ply_dir) if f.endswith('.ply')]

print("Found " + str(len(ply_files)) + " PLY files.")
i = 1

# loop through each ply file
for ply_file in ply_files:
    print("Rendering " + str(i) + "/" + str(len(ply_files)) + "\n")
    # import the ply file as a mesh object
    bpy.ops.import_mesh.ply(filepath=os.path.join(ply_dir, ply_file))
    obj = bpy.context.active_object
    
    # set the corresponding geometry nodetree and material
    obj.active_material = bpy.data.materials['points']
    obj.modifiers.new(name='Geometry Nodes', type='NODES')
    obj.modifiers["Geometry Nodes"].node_group = bpy.data.node_groups['Instances']
    
    # set the output path for the rendered image
    output_path = os.path.join(output_folder, f"{ply_file[:-4]}.png")
    
    # render the image
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)
    
    # delete the imported object
    bpy.data.objects.remove(obj, do_unlink=True)
    
    i += 1

print("Finished!")
    

