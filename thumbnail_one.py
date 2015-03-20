import os.path
from PIL import Image
import sys

THUMB_SIZE = 150 # crop dimension -- img will be cropped into THUMB_SIZExTHUMB_SIZE square.

# get filename from command line arguments
args = sys.argv[:]
script = args.pop(0)
filename = args.pop(0)

def make_thumb(f):
    # open the image
    img = Image.open(f)

    # resize the image so smaller dimension = THUMB_SIZE
    size = img.size

    if size[0] == size[1]:
        newsize = (THUMB_SIZE, THUMB_SIZE)
    elif size[0] < size[1]:
        newsize = (THUMB_SIZE, int(size[1] * float(THUMB_SIZE) / size[0]))
    elif size[0] > size[1]:
        newsize = (int(size[0] * float(THUMB_SIZE) / size[1]), THUMB_SIZE)

    img = img.resize(newsize)

    # crop a THUMB_SIZExTHUMB_SIZE box from center of img
    center = (img.size[0]/2, img.size[1]/2)
    crop_box = (center[0] - THUMB_SIZE/2,
                    center[1] - THUMB_SIZE/2,
                    center[0] + THUMB_SIZE/2,
                    center[1] + THUMB_SIZE/2)
    img = img.crop(crop_box)

    # save img
    img_path = os.path.dirname(f)
    img_name_with_extension = os.path.basename(f)
    img_name = os.path.splitext(img_name_with_extension)[0]
    img_extension = os.path.splitext(img_name_with_extension)[1]
    new_img_name = "THUMB_%s%s" % (img_name, img_extension)
    new_path = os.path.join(img_path, new_img_name)
    img.save(new_path)

if __name__ == '__main__':
    make_thumb(filename)
