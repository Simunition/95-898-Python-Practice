"""Program to take a single image or directory of images and
convert the file type as specified by the user"""

import argparse
import os

parser = argparse.ArgumentParser(description = 'Given a single image or directory'
                                 +' convert image filetype(s)')

# arguments
parser.add_argument("name", metavar="<filename>|<dir>",
                    help = "Enter the source image filename or directory")
parser.add_argument("format", metavar="<format>",
                    help = "New file format to change the file(s) to",
                    choices = ["jpg", "jpeg", "png", "bmp", "tiff"])
parser.add_argument("location", metavar="[<output_dir>]",
                    help = "Optionaly add target directory for generated file(s)",
                    default = os.getcwd())

# options
parser.add_argument("-b", "--blur", help = "Blue image", action="store_true")
parser.add_argument("-c", "--color", help = "Color manipulation", action="store_true")

args = parser.parse_args()
print(args)


# determine if args.filname|dir is file or dir
# check if file(s) are actually image files, error if not
# if directory doesn't contain any image files print error
# in directory with images, convert images, ignore rest
# if submitted image is already in specified format, inform user
