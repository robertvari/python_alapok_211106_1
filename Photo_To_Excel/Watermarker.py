from PIL import Image, ImageDraw, ImageFont
import os

# open folder and get all files and folders
photo_folder = r"C:\Work\_PythonSuli\pycore-211106\photos"
file_list = os.listdir(photo_folder)

destination_folder = os.path.join(photo_folder, "_watermarked")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# filter file_list to get only .jpg and .jpeg formats
clean_file_list = []
extensions = [".jpeg", ".jpg"]

for i in file_list:
    name, ext = os.path.splitext(i)

    if not ext.lower() in extensions:
        continue

    clean_file_list.append(os.path.join(photo_folder, i))

for photo_file in clean_file_list:
    img = Image.open(photo_file)

    # resize image
    img.thumbnail((500, 500))

    # create watermark on image
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 90)

    draw.text((0, 120), "Hello World", fill=(255, 0, 0), font=font)

    # save image to destionation
    dest_file_name = os.path.join(destination_folder, os.path.basename(photo_file))
    img.save(dest_file_name)