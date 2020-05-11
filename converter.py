from PIL import Image
import sys
import os

img_source= sys.argv[1] 
img_dest = sys.argv[2]

print(os.listdir(img_source))


if not (os.path.isdir(img_dest) ):
    os.makedirs(img_dest)

if(img_dest[-1] != '\\' ):
    img_dest = img_dest + '\\'


for file in os.listdir(img_source):
    if file.endswith('.jpg'):
        temp = Image.open(img_source + file)
        temp.save(img_dest + file,"png")


