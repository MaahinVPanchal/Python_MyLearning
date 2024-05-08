import os
import shutil

path = r"D:\Users\Owner\Downloads"
file_names = os.listdir(path)

folder_names = ['pdf files', 'video files', 'image files']
for folder_name in folder_names:
    if not os.path.exists(os.path.join(path, folder_name)):
        os.makedirs(os.path.join(path, folder_name))

for file in file_names:
    file_extension = os.path.splitext(file)[1].lower()
    if file_extension in ['.pdf']:
        shutil.move(os.path.join(path, file), os.path.join(path, "pdf files", file))
    elif file_extension in ['.mp4']:
        shutil.move(os.path.join(path, file), os.path.join(path, "video files", file))
    elif file_extension in ['.jpeg', '.jpg', '.png', '.gif']:
        shutil.move(os.path.join(path, file), os.path.join(path, "image files", file))
