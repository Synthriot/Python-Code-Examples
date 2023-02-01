from tkinter import *
from tkinter import filedialog as f
from io import open

title = "Editor | Bloc de notas basico Python"
root = Tk()
root.title(title)
root.geometry("1500x600")
#commands
url_file = ""
def NewFile():
    global url_file
    text.delete(1.0,"end")
    url_file = "Nuevo Archivo "
    root.title(url_file + title)
def openFile():
    global url_file
    url_file = f.askopenfilename(initialdir = '.', filetypes = ((
        "Todos los archivos", "*.*"
    ),), title = "Abrir archivo ")
    if url_file != "":
        file = open(url_file, 'r')
        content = file.read()
        text.delete(1.0,"end")
        text.insert('insert', content)
        file.close()
        root.title(url_file + title)
def saveFile():
    global url_file
    if url_file != "":
        content = text.get(1.0,"end")
        file = open(url_file, 'w+')
        root.title("Archivo guardado " + url_file+ title)
        file.close()
    else:
        file = f.asksaveasfile(title = "Save File", mode = 'w', defaultextension = ".*")
        if file is not None:
            url_file = file.name
            content = text.get(1.0, "end-1c")
            file = open(url_file,'w+')
            file.write(content)
            root.title("Archivo guardado " + url_file + title)
            file.close()
        else:
            url_file = ""
            root.title("Archivo cancelado " + url_file + title)
def exit():
    root.quit()
#Menú

menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Nuevo archivo", command = NewFile)
file_menu.add_command(label="Abrir archivo", command=openFile)
file_menu.add_command(label="Guardar archivo", command=saveFile)
file_menu.add_command(label="Salir", command = exit)

menubar.add_cascade(menu = file_menu, label="Archivo")

#TextBox

text = Text(root)
text.pack(fill = "both", expand = 1)
text.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 14))
#Run
root.config(menu = menubar)
root.mainloop()