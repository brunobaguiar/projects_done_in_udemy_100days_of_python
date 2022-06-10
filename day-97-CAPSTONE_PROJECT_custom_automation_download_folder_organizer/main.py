import os
from pprint import pprint

# Find Downloads folder
DOWNLOAD_PATH = os.path.normpath('C:/Users/PC/Downloads')


## ------------------------- 1. move files to extension folder ------------------------------------------------------##
def move_files_to_extension_folder():
    # Create a dict with keys as extension folders and values as a list of each extension file
    file_mappings = {}
    for filename in os.listdir(DOWNLOAD_PATH):
        # Check if the file is not a folder
        if not os.path.isdir(os.path.join(DOWNLOAD_PATH, filename)):
            # Get the file type
            file_type = filename.split('.')[-1]
            # If folder already exists, just append filename to respective folder
            try:
                file_mappings[file_type].append(filename)
            # If folder do not exist, crate folder and append filename to respective folder
            except KeyError:
                file_mappings[file_type] = []
                file_mappings[file_type].append(filename)
    pprint(file_mappings)

    # Move all files into the right folder
    for folder_name, folder_items in file_mappings.items():
        folder_path = os.path.join(DOWNLOAD_PATH, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for folder_item in folder_items:
            # Note that must include the filename in both the source and destination arguments. If it is changed,
            # the file will be renamed as well as moved. "
            source = os.path.join(DOWNLOAD_PATH, folder_item)
            destination = os.path.join(folder_path, folder_item)
            pprint(f"Move from {source} to {destination}")
            # Renaming a file path like this, will move this file to the next path
            # In case of moving through different disks, better use shutil
            # Could use shutil module for this "shutil.move(source, destination)
            os.rename(source, destination)


## ------------------------- 2. Move files to download folder ------------------------------------------------------##
def move_files_to_download_folder():
    # Create a list of folders inside Download folder
    downloads_folders = []
    for folder_name in os.listdir(DOWNLOAD_PATH):
        folder_full_path = os.path.join(DOWNLOAD_PATH, folder_name)
        # If it is a folder, move files inside it to Downloads main folder
        if os.path.isdir(folder_full_path):
            for folder_item in os.listdir(folder_full_path):
                source = os.path.join(folder_full_path, folder_item)
                destination = os.path.join(DOWNLOAD_PATH, folder_item)
                pprint(f"Move from {source} to {destination}")
                os.rename(source, destination)
            # If is a folder, and it is empty, delete folder
            if os.path.isdir(folder_full_path):
                os.rmdir(folder_full_path)


## ------------------------- 3. Move files to specified folder ------------------------------------------------------##

# Describe folder path and destination
FOLDER_PATH = os.path.normpath(
    'C:/Users/PC/Documents/Projetos Portifólio/brazilian_it_jobs_analysis/dataset/Vagas TI Consultoria/ChatExport_2022-06-08/photos')
DESTINATION_PATH = os.path.normpath(
    'C:/Users/PC/Documents/Projetos Portifólio/brazilian_it_jobs_analysis/dataset/Vagas TI Consultoria/ChatExport_2022-06-08/photos/delete')


def move_files_to_folder():
    for filename in os.listdir(FOLDER_PATH):
        # Choose the key word of the files to move
        if "thumb" in filename:
            print("find")
            source = os.path.join(FOLDER_PATH, filename)
            destination = os.path.join(DESTINATION_PATH, filename)
            pprint(f"Move from {source} to {destination}")
            # Comment above line to test before move the files
            os.rename(source, destination)


choose = input(
    'Type "1" for move files to extension folder or "2" to move files to download folder" or "3" to move files to specified folder"')
if choose == "1":
    move_files_to_extension_folder()
elif choose == "2":
    move_files_to_download_folder()
elif choose == "3":
    move_files_to_folder()
else:
    pass
