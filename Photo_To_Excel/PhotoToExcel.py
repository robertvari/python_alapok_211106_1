import os
from openpyxl import Workbook
from PIL import Image, ExifTags

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


# list comprehension
# clean_file_list = [i for i in file_list if ".jpg" in i.lower()]

# create excel workbook
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "File Path"
sheet["B1"] = "Date"
sheet["C1"] = "Size"
sheet["D1"] = "Camera"
sheet["E1"] = "Lens"
sheet["F1"] = "ISO"

# open photos and get exif data
for index, photo_file in enumerate(clean_file_list):
    img = Image.open(photo_file)
    image_size = img.size

    row = index + 3

    sheet[f"A{row}"] = photo_file
    sheet[f"C{row}"] = f"{image_size[0]}x{image_size[1]}"


excel_file = os.path.join(photo_folder, "photo_data.xlsx")
workbook.save(excel_file)