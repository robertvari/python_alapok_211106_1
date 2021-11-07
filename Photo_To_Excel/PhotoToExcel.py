import os
from openpyxl import Workbook
from PIL import Image


photo_folder = r"C:\Work\_PythonSuli\pycore-211106\photos"
file_list = os.listdir(photo_folder)

clean_file_list = []
extensions = [".jpeg", ".jpg"]

for i in file_list:
    name, ext = os.path.splitext(i)

    if not ext.lower() in extensions:
        continue

    clean_file_list.append(i)

print(file_list)
print(clean_file_list)