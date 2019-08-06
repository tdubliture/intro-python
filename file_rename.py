"""
rename files from a folder
get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""
import os


def rename_files():
    """
    rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\tylerjones10\Desktop\hafb\prank\prankOrig"
    files = os.listdir(folder_dir)
    saved_path = os.getcwd()
    os.chdir(folder_dir)
    for file in files:
        # remove digits from name
        new_file = file.lstrip('0123456789')
        print("old name", file, "new name", new_file)
        # rename file to new name
        os.rename(file,new_file)
    os.chdir(saved_path)



def main():
    """
    test function
    :return: nothing
    """
    rename_files()


if __name__ == '__main__':
    main()
    exit(0)