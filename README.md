A Python utility to make thumbnails of your images, built using [Pillow](//pillow.readthedocs.org/), a fork of PIL (the Python Imaging Library).

### Things to Know
- This program requires Pillow. Install it with `pip install Pillow` or `pip install -r requirements.txt`.
- Default thumbnail size is 150x150 (they're always square). To change the size, modify `THUMB_SIZE` in `thumbnail_one.py`.
- Change the format of your thumbnail's image name by altering the string formatting behind `new_img_name` in `thumbnail_one.py`.
- I only bothered telling this program to support `.tif`, `.tiff`, `.gif`, `.jpeg`, `.jpg`, `.png`, and `.bmp`, but it can theoretically work with [any file format that Pillow supports](//pillow.readthedocs.org/handbook/image-file-formats.html)--if you want to add any additional file formats, just stick them in `IMG_FORMATS` in `thumbnail_all.py`.

### How to Use

**To make a thumb of a single file**: from the command line, run `python thumbnail_one.py path-to-file`.

**To make a thumbs of all the image files in a directory**: from the command line, run `python thumbnail_all.py path-to-directory`. (Only files with extensions listed in `IMG_FORMATS` will be thumb-ified--see "Things to know", above.)
