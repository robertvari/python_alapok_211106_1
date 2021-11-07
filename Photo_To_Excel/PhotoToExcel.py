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
sheet["E1"] = "Focal Length"
sheet["F1"] = "ISO"

# open photos and get exif data
for index, photo_file in enumerate(clean_file_list):
    img = Image.open(photo_file)
    image_size = img.size

    row = index + 3

    # photo path
    sheet[f"A{row}"] = photo_file

    # image size
    sheet[f"C{row}"] = f"{image_size[0]}x{image_size[1]}"

    # get exif data
    exif_data = img._getexif()
    if not exif_data:
        continue

    for key, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(key)

        if tag_name == "ISOSpeedRatings":
            sheet[f"F{row}"] = value

        if tag_name == "DateTime":
            sheet[f"B{row}"] = value

        if tag_name == "Model":
            sheet[f"D{row}"] = value

        if tag_name == "FocalLength":
            sheet[f"E{row}"] = str(value)


excel_file = os.path.join(photo_folder, "photo_data.xlsx")
workbook.save(excel_file)