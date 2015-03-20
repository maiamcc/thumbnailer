import os
import sys
from thumbnail_one import make_thumb

args = sys.argv[:]
script = args.pop(0)
directory = args.pop(0)

IMG_FORMATS = [".tif", ".tiff", ".gif", ".jpeg", ".jpg", ".png", ".bmp"]

def thumb_all(dir):
    if not os.path.isdir(dir):
        raise os.error("Given filepath isn't a directory, try again!")

    all_files = [os.path.join(root, file)[2:] for root, dirs, files in os.walk(dir) \
        for file in files]
    # filter out those already thumb-ified, and non-images
    all_files = filter(lambda filename: "thumb" not in filename.lower() and \
        any([filename.endswith(ext) for ext in IMG_FORMATS]), all_files)
    # TODO: ignore any files for which file_thumb.ext exists?

    for f in all_files:
        make_thumb(f)

if __name__ == '__main__':
    thumb_all(directory)