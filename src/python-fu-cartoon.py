#!/usr/bin/python2.7

from gimpfu import *

def cartoon_file(n_propagation, filepath, filename, output_directory):
    img = pdb.gimp_file_load(filepath, filepath)
    dodgeLayer = img.layers[0].copy()
    dodgeLayer.mode = DODGE_MODE
    img.add_layer(dodgeLayer, 0)
    pdb.gimp_invert(dodgeLayer)
    for n in range(n_propagation):
        pdb.plug_in_vpropagate(img, dodgeLayer, 1, 1, 1, 15, 0, 255)
    layer=pdb.gimp_layer_new(img, img.width, img.height , RGB_IMAGE, "base", n_propagation * 10, LAYER_MODE_LCH_CHROMA)
    pdb.gimp_context_set_foreground((229,21,175))
    img.add_layer(layer,0)
    pdb.gimp_drawable_edit_bucket_fill(layer, 0, 0, 0)
    img.flatten()
    pdb.gimp_file_save(img, img.layers[0], output_directory + "/" + filename, output_directory + "/" + filename)
    pdb.gimp_image_delete(img)

register(
    "python-fu-cartoon",
    "Applies a color propagate filter on an image to create a cartoonish look",
    "Pass the filepath, filename and output directory",
    "Carlos Castillo",
    "Carlos Castillo",
    "2020",
    "RGB*",
    "",
    [
        (PF_INT, "n_propagation", "GlobPattern", "*.*"),
        (PF_STRING, "filepath", "GlobPattern", "*.*"),
        (PF_STRING, "filename", "GlobPattern", "*.*"),
        (PF_STRING, "output_directory", "GlobPattern", "*.*")
    ],
    [],
    cartoon_file)

main()
