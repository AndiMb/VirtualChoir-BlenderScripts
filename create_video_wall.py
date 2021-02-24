import bpy
import glob
import math
import random

######################
#
#   Input
#
######################

# Number of Frames in each Video
numFramesPerVideo = 5025

# all Paths with video files
files = []
files.extend(glob.glob("D:\\VirtualChoirBlender\\Einzelvideos\\*.mp4"))

#########################
#
#   Video Wall Generation
#
#########################

# minimal number of videos per axis (x,y) to add all videos
numVideosPerAxis = int(math.sqrt(len(files))-0.01)+1
# total number of videos
totalVideoNumber = numVideosPerAxis * numVideosPerAxis

# video file names in random order
rFiles = random.sample(files, min(len(files), totalVideoNumber))
if (len(files) < totalVideoNumber):
    rFiles.extend(random.sample(files, totalVideoNumber - len(files)))

# add videos to scene
iX = 0
iZ = 1
for file in rFiles:
    filename = file[file.rindex('\\')+1:]
    path = file[0:file.rindex('\\')+1]
    print(filename)
    
    iX += 1
    if (iX > numVideosPerAxis):
        iX = 1
        iZ += 1
    
    bpy.ops.import_image.to_plane(files=[{"name":filename, "name":filename}], directory=path, shader='SHADELESS', relative=False)
	bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.transform.translate(value=(iX*1.77778-0.88889, 0.0, iZ-0.5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.data.materials[filename[:-4]].node_tree.nodes["Image Texture"].image_user.frame_duration = numFramesPerVideo

# add camera to scene
distanceFromWall = 50.0 / 36.0 * numVideosPerAxis * 1.777777777
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(numVideosPerAxis*1.777777777/2.0, -distanceFromWall, numVideosPerAxis/2.0), rotation=(1.5708, 0.0, 0.0), scale=(1, 1, 1))
