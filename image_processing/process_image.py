"""Program to take a single image or directory of images and
convert the file type as specified by the user"""

import argparse
import os

parser = argparse.ArgumentParser(description = 'Given a single image or directory'
                                 +' convert image filetype(s)')

# arguments
parser.add_argument("name", metavar="<filename>|<dir>", type=str,
                    help = "Enter the source image filename or directory")
parser.add_argument("format", metavar="<format>", type=str,
                    help = "New file format to change the file(s) to",
                    choices = ["jpg", "jpeg", "png", "bmp", "tiff"])

# options
parser.add_argument("-o", "--output", help = "Set output directory", default=(os.getcwd()))
parser.add_argument("-b", "--blur", help = "Blur image", action="store_true")
parser.add_argument("-c", "--color", help = "Color manipulation", action="store_true")

args = parser.parse_args()
print(os.path.join(os.getcwd, args.name))

# check if file(s) are actually image files, error if not
def filetype_check(check_file):
    """function to check if file matches acceptable filetypes"""
    accepted_types = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]
    name, extension = os.path.splitext(check_file)
    return extension in accepted_types

# determine if args.filname|dir is file or dir
if os.path.isfile(os.path.join(os.getcwd(), args.name)):
    # item is file
    print("file")
elif os.path.isdir(args.name):
    print("dir")
    for file in os.listdir(args.name):
        f = os.path.join(args.name, file)
        if os.path.isfile(f):
            print(filetype_check(f))
else:
    print("File or directory supplied does not exist")

# if directory doesn't contain any image files print error
# in directory with images, convert images, ignore rest
# if submitted image is already in specified format, inform user
