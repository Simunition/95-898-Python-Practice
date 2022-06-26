"""Program to take a single image or directory of images and
convert the file type as specified by the user"""

import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser(description = 'Given a single image or directory'
                                 +' convert image filetype(s)')

# arguments
parser.add_argument("name", metavar="<filename>|<dir>", type=str,
                    help = "Enter the source image filename or directory")
parser.add_argument("format", metavar="<format>", type=str,
                    help = "New file format to change the file(s) to",
                    choices = ["jpg", "jpeg", "png", "bmp", "tiff"])
parser.add_argument("output_dir", metavar="<output_dir>", type=str, nargs="?",
                    help = "Set output directory", default=(os.getcwd()))

# options
parser.add_argument("-b", "--blur", help = "Blur image", action="store_true")
parser.add_argument("-c", "--color", help = "Color manipulation", action="store_true")

args = parser.parse_args()

# check if file(s) are actually image files, error if not
def filetype_check(check_file):
    """function to check if file matches acceptable filetypes"""
    accepted_types = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]
    extension = os.path.splitext(check_file)[1]
    return extension in accepted_types

def convert_image(in_file, desired_format): #improve to handle custom out locations
    """function to convert image to specified format"""
    name = os.path.splitext(in_file)[0]
    out_file = name + "." + desired_format
    if in_file != out_file:
        try:
            with Image.open(in_file) as image:
                image.save(out_file)
                print(f"{in_file} converted to {out_file}")
        except OSError:
            print(f"cannot convert {in_file}")
    else:
        print(f"{in_file} already a {format}")

# determine if args.filname|dir is file or dir
if os.path.isfile(args.name):
    convert_image(args.name, args.format)
elif os.path.isdir(args.name):
    # Find some way to check if dir has any image files
    if any(filetype_check(file) for file in os.listdir(args.name)):
        for file in os.listdir(args.name):
            f = os.path.join(args.name, file)
            if os.path.isfile(f) and filetype_check(f):
                convert_image(f, args.format)
    else:
        print("No image files in specific directory")
else:
    print("File or directory supplied does not exist")
