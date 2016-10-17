import os
def rename_files():
    file_path = r"/Users/kuminin/Desktop/Udacity Nanodegree Full Stack/Renaming Files/prank"
    saved_path = os.getcwd()
    # (1) get file names from a given folder.
    file_list = os.listdir(file_path)
    print("Current Working Directory is " + saved_path)
    os.chdir(file_path)
    # (2) for each file, rename filename.
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
