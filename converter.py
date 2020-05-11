from PIL import Image
import sys
import os

img_source= sys.argv[1] 
img_dest = sys.argv[2]

#* makes a dir if it is not present 
if not (os.path.isdir(img_dest) ):
    os.makedirs(img_dest)

#* adds \ to to the img dest dir if the \ is not specified
if(img_dest[-1] != '\\' ):
    img_dest = img_dest + '\\'

#* Loops through the files in dir specified
for file in os.listdir(img_source):
    if file.endswith('.jpg'):
        image_file = Image.open(img_source + file)
        replaced_file = file.replace('jpg','png')
        image_file.save(f'{img_dest}{replaced_file}',"png")
        print(f'Converted and saved {file}')


