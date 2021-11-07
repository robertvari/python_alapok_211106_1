import os

a_folder = r"C:\Work\_PythonSuli\pycore-211106\Alapok 1\A_folder"
b_folder = r"C:\Work\_PythonSuli\pycore-211106\Alapok 1\B_folder"

a_files = os.listdir(a_folder)
b_files = os.listdir(b_folder)

print(f"Files in A_Folder: {a_files}")
print(f"Files in B_Folder: {b_files}")

a_files_set = set(a_files)
b_files_set = set(b_files)


print(f"Same files found: {list(a_files_set & b_files_set)}")