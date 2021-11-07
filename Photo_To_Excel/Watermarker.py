from PIL import Image, ImageDraw, ImageFont
import os

# open folder and get all files and folders
photo_folder = r"C:\Work\_PythonSuli\pycore-211106\photos"
file_list = os.listdir(photo_folder)


# filter file_list to get only .jpg and .jpeg formats
clean_file_list = []
extensions = [".jpeg", ".jpg"]

for i in file_list:
    name, ext = os.path.splitext(i)

    if not ext.lower() in extensions:
        continue

    clean_file_list.append(os.path.join(photo_folder, i))

print(clean_file_list)