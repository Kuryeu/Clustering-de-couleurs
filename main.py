from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk()
window.title("Projet 2 Forage de données")



def openfile():
    global image
    window.filename = filedialog.askopenfilename(initialdir="./rsc", title = "choisis frr", filetypes=[("all files", "*.*"),("png", "*.png"),("pdf", "*.pdf"),("jpg", "*.jpg")])

    text= Label(window, text=window.filename).pack()
    image= ImageTk.PhotoImage(Image.open(window.filename))
    image_label = Label(image=image).pack()
    algorithm_button = Button ( window, text = "Appliquer algorithme").pack()


open_button = Button(window, text= "Ouvrir image", command=openfile).pack()
window.mainloop()