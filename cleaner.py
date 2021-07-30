from tkinter import *
from tkinter import messagebox
from genericpath import isdir, isfile
import os
from os.path import join
import shutil

info = ["/".join(str(os.getcwd()).split("\\")[0:3]),"","","",""]

def move(file, source, destination):
    try:
        if os.path.exists(destination):
            shutil.move(src=source+"/"+file, dst=destination)
        else:
            os.makedirs(destination)
            shutil.move(src=source+"/"+file, dst=destination)
    except FileNotFoundError:
        messagebox.showerror("File not found","The file was not found")
    except FileExistsError:
        messagebox.showerror("File not exist","The file doest not exist")
                
def show_data(data, element):
    
    info[0]+=f"/{data}"
    print(info[0])
    element.pack_forget()
    search_files(info[0])

def search_files(data):   
    try:
        content = os.listdir(data)
        if data.lower() == "c:/users/"+data.split("/")[2].lower():
            main_folders = [file for file in content if isdir(join(data,file)) and not file.startswith(".")]
            main_folders.remove("My Documents")      
            main_folders.remove("Application Data")      
            main_folders.remove("PrintHood")      
            main_folders.remove("Cookies")      
            main_folders.remove("Local Settings")  
            main_folders.remove("NetHood")     
            main_folders.remove("Recent")   
            main_folders.remove("SendTo")   
            main_folders.remove("Templates")   
            main_folders.remove("Start Menu")   
        else:
            main_folders = [folder for folder in content if isdir(join(data, folder))]
        if len(main_folders)==0:
            messagebox.showwarning("There are not more folders","You must click the sort button ")
        else:
            info[1] = data
            info[2] = content
            info[3] = main_folders
            actual = StringVar(root)
            actual.set(main_folders[0])
            main_folders_list = OptionMenu(root, actual, *main_folders, command=lambda x:show_data(actual.get(),main_folders_list))
            main_folders_list.pack()
            info[4] = main_folders_list
            search_button.pack_forget()
    except PermissionError:
        messagebox.showerror("nokas","no puedes entrar vale mia")

def sort_files(PATH):
    try:
        content = os.listdir(PATH)
        files = [file for file in content if isfile(join(PATH, file))]
        print(files)
        if len(files)==0:
            messagebox.showwarning("There are not files","This folder does not contain files to sort")
        else:
            PATH_TEXT_FILES = join(PATH, "Text files")
            PATH_PDF_FILES = join(PATH, "Pdf files")
            PATH_EXE_FILES = join(PATH, "Exe files")
            PATH_PRESENTATIONS_FILES = join(PATH, "Presentations files")
            PATH_EXCEL_FILES = join(PATH, "Data files")
            PATH_IMAGES_FILES = join(PATH, "Images files")
            PATH_VIDEO_FILES = join(PATH, "Video files")
            PATH_AUDIO_FILES = join(PATH, "Audio files")
            PATH_COMPRESSED_FILES = join(PATH, "Compressed files")
            PATH_PROJECTS_FILES = join(PATH,"Projets files")
            PATH_OTHERS_FILES = join(PATH, "other files")

            for file in files:
                if file.endswith(".txt") or file.endswith(".docx"):
                    move(file, PATH, PATH_TEXT_FILES)
                elif file.endswith(".pdf"):
                    move(file, PATH, PATH_PDF_FILES)
                elif file.endswith(".exe"):
                    move(file, PATH, PATH_EXE_FILES)
                elif file.endswith(".jpg") or file.endswith(".pgn") or file.endswith(".jpeg") or file.endswith(".gif"):
                    move(file, PATH, PATH_IMAGES_FILES)
                elif file.endswith(".xlsx") or file.endswith(".csv"):
                    move(file, PATH, PATH_EXCEL_FILES)
                elif file.endswith(".rar") or file.endswith(".zip") or file.endswith(".arj") or file.endswith(".z") or file.endswith(".dev") or file.endswith(".pkg") or file.endswith(".rpm"):
                    move(file, PATH, PATH_COMPRESSED_FILES)
                elif file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".mid") or file.endswith(".ogg") or file.endswith(".aac") or file.endswith(".flac") or file.endswith(".cda"):
                    move(file, PATH, PATH_AUDIO_FILES)
                elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".wmv") or file.endswith(".div"):
                    move(file, PATH, PATH_VIDEO_FILES)
                elif file.endswith(".py") or file.endswith(".java") or file.endswith(".js") or file.endswith(".m") or file.endswith(".html") or file.endswith(".cpp") or file.endswith(".html") or file.endswith(".Rproj"):
                    move(file, PATH, PATH_PROJECTS_FILES)       
                elif file.endswith(".pptx") or file.endswith(".ppt"):
                    move(file, PATH, PATH_PRESENTATIONS_FILES)                             
                else:
                    move(file, PATH, PATH_OTHERS_FILES)
            messagebox.showinfo("Files sorted successfully", "The files have been sorted")
    except:
        messagebox.showerror("Error", "There was an error during execution")

def delete_path(data):
    if (len(data.split("/"))==3):
        info[0] = info[0]
    else:
        info[0] = "/".join(data.split("/")[0:len(data.split("/"))-1])
        info[4].pack_forget()
        search_files(info[0])

root = Tk()

root.title("CLEARBOT")
root.resizable(0,0)
WIDTH = 500
HEIGHT = 500
x_ventana = root.winfo_screenwidth() // 2 - WIDTH // 2
y_ventana = root.winfo_screenheight() // 2 - HEIGHT // 2
posicion = str(WIDTH) + "x" + str(HEIGHT) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
delete_button = Button(root,text="go back", command=lambda:delete_path(info[0])).pack()
sort_button = Button(root,text="sort files", command=lambda:sort_files(info[0])).pack()
search_button = Button(root,text="search files", command=lambda:search_files(info[0]))
search_button.pack()


root.mainloop()

