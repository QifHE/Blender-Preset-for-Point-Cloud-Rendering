# Blender Preset for Point Cloud Batch Rendering

 A simple and convenient Blender EEVEE preset for the customable and automated rendering of point clouds suitable for academic papers.

![cover](image/README/cover.jpg)

### Previously

My previous repo [QifHE/3D-Point-Cloud-Rendering-with-Mitsuba (github.com)](https://github.com/QifHE/3D-Point-Cloud-Rendering-with-Mitsuba) provides a method to batch render point clouds by [Mitsuba](https://github.com/mitsuba-renderer/mitsuba2), however, it is inconvenient to adjust the point cloud objects, since the parameters can only be set in the XML configuration file, and it cannot output images with a transparent background. Therefore, this repo aims to develop an alternative method based on the very popular Blender, so people can directly view the shading results in the software and modify the parameters in real time according to their needs.

### How To Use

**Click** the below for the **Tutorial Video** if you don't want to read.

[![Tutorial Video](image/README/1680618245812.png)](tutorial_blenderpointcloud.mp4)

Only limited file formats can be imported into Blender, so please convert your point cloud files into `.ply` extension at first, you can use `convert_to_ply.py` provided by this repo. The guide to this script is at the bottom of this readme.

This is a Blender 3.x preset so you can either open the `PointCloudRenderPreset.blend` file directly then replace the mesh object named  `Airplane` inside and do whatever you want, or append the following in the `PointCloudRenderPreset.blend` file into your Blender project.

- `Material/points`
- `Material/shadowcatcher`
- `NodeTree/instances`
- `Collection/Lighting`

Firstly, you go to the `Geometry Nodes` tab on the top. Select your point cloud object in the view, then go to the NodeTree editor in the below, and assign the object with the `instances` nodetree. This transforms your vertices into ball mesh instances. In the `Transform` node, you can adjust your object to proper position and scale. In `Ico Sphere` node, you can change the radius of balls. Note that the material in the `Set Material` node should be assigned to `points`.

![1680602275766](image/README/1680602275766.png)

Then go to the `Shading` tab on the top, and select your object and assign it with the preset's `points` material. On the top right corner, switch your current view to `Viewport Shading`, then you can see the shading result. You can change the color in the `ColorRamp` node, and if your `.ply` file has stored color in the vertices' `Col` attribute, you can reconnect `ColorAttribute` node with the `Hue Saturation Value` node.

![1680602377758](image/README/1680602377758.png)

![1680602510521](image/README/1680602510521.png)

If you used the appending method, remeber to add a plane on the ground, and assign it with the preset's `shadowcatcher` material. It shows some white shadow by the transparent background in order to reduce the intensity of the black shadow, and it will look fine by a white background, especially in the acdemic papers.

![1680602574127](image/README/1680602574127.png)

Finally, go back to `Layout` and toggle the camera view on the right to see that if the camera position is set properly. Then go to the  `Render Properties `, make sure that the render engine is `Eevee`. Increase the sampling amount of Render if you like. Enable `Ambient Occlusion, Bloom, Screen Space Reflections `. In the `film `tab, enable `Transparent`. In the  `Shadows` tab, increase the `cube size `to `4096px` and enable `Soft Shadows`. After that, go to the `Output Properties`, change the `resolution` as you like, and make sure the output is in `PNG` format.

![1680602669445](image/README/1680602669445.png)

![1680602760177](image/README/1680602760177.png)

![1680602817009](image/README/1680602817009.png)

After all the steps above, go to the `Render` tab and `Render Image`. Then you are done!

![1680602836811](image/README/1680602836811.png)

### Automation for Batch Rendering

Go to the `Scripting` tab. If the `batch_render.py` is not there, copy the code from `batch_render.py` of this repo into the script editor. Modify the `ply_dir` and `output_folder` varaibles to your `.ply` input and `.png` output directories. Now, assume that all your `.ply` point clouds have similar initial location and scale. You import one of your `.ply` file, delete the default `Airplane` then adjust the  `Transform `and `Radius` in `Geometry Nodes`, color in `Shading`, and camera position in `Layout` as mentioned above. Then delete the imported object, go back to `Scripting` and run the script by the run botton. If you want to monitor the progress, open `Toggle System Console` in the `Window` dropdown on the top. Then you are done!

![1680612738029](image/README/1680612738029.png)

![1680612689620](image/README/1680612689620.png)

![1680612759595](image/README/1680612759595.png)

![1680612789457](image/README/1680612789457.png)

![1680613088783](image/README/1680613088783.png)

![1680613525904](image/README/1680613525904.png)

### PLY Conversion and Custom Coloring

Modify the input and output pathes in  `convert_to_ply.py` file, then run the script. It supports conversion from ` .npy, .pcd, .ply, h5, .txt, .xyz, .pts`. This script also provides an example function to write the color attribute into  `.ply `files. The default `defind_color()`function randomly writes Red, Green, Blue, and Yellow into the `.ply `file. You can switch from the `Preset Color `node to `Color From Input Data `node in the `points `material's `Shading` nodetree to see the attribute color.

![1680860543065](image/README/1680860543065.png)

### Acknowledgement

- [TombstoneTumbleweedArt/import-ply-as-verts: New Blender 3.0* / 3.1 PLY importer v2.0 for point clouds and nonstandard models. (github.com)](https://github.com/TombstoneTumbleweedArt/import-ply-as-verts) Thank them for the method to convert `.ply` vertices into point instances.
- [Blender Shadow Catcher - Enable Shadow Catcher in both EEVEE &amp; Cycles - YouTube](https://www.youtube.com/watch?v=xFi_88TIQgc) Thank them for the method to create a workaround for the shadow catcher in the EEVEE engine.
- [PoinTr/io.py at 1dc2cfcb90ecbda64880c28e0a4f94dd41d879c8 · yuxumin/PoinTr (github.com)](https://github.com/yuxumin/PoinTr/blob/1dc2cfcb90ecbda64880c28e0a4f94dd41d879c8/datasets/io.py)
