from genericpath import isdir, isfile
import os
from os.path import join
import shutil

PATH = r'C:/Users/estwi/downloads'
content = os.listdir(PATH)
files = [file for file in content if isfile(join(PATH, file))]

PATH_TEXT_FILES = join(PATH, "text files")
PATH_PDF_FILES = join(PATH, "pdf files")
PATH_EXE_FILES = join(PATH, "exe files")
PATH_DOCX_FILES = join(PATH, "docx files")
PATH_EXCEL_FILES = join(PATH, "excel files")
PATH_IMAGES_FILES = join(PATH, "images files")
PATH_VIDEO_FILES = join(PATH, "video files")
PATH_OTHERS_FILES = join(PATH, "other files")

def move(file, source, destination):
    try:
        if os.path.exists(destination):
            shutil.move(src=source+"/"+file, dst=destination)
        else:
            os.makedirs(destination)
            shutil.move(src=source+"/"+file, dst=destination)
    except FileNotFoundError:
        print("no encuentro esa monda")
    except FileExistsError:
        print("that monda doesnt exist")

for file in files:
    if file.endswith(".txt"):
        move(file, PATH, PATH_TEXT_FILES)
    elif file.endswith(".pdf"):
        move(file, PATH, PATH_PDF_FILES)
    elif file.endswith(".exe"):
        move(file, PATH, PATH_EXE_FILES)
    elif file.endswith(".jpg") or file.endswith(".pgn") or file.endswith(".jpeg") or file.endswith(".gif"):
        move(file, PATH, PATH_DOCX_FILES)
    elif file.endswith(".docx"):
        move(file, PATH, PATH_DOCX_FILES)
    elif file.endswith(".xlsx"):
        move(file, PATH, PATH_EXCEL_FILES)
    elif file.endswith(".mp4"):
        move(file, PATH, PATH_VIDEO_FILES)
    else:
        move(file, PATH, PATH_OTHERS_FILES)

# print(os.getcwd())
# print(__file__)
