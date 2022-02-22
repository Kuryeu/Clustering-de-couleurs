##################################
#        FORAGE DE DONNES        #
#  TP2 - CLUSTERING DE COULEURS  #
#   Auteur : MELLIER Valentin    #
##################################
#Libs utilisés dans le fichier main.py
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from turtle import onclick, right, window_height, window_width
from PIL.Image import *
from PIL import Image, ImageTk
from random import *
from math import sqrt
import kmeans
import dbscan


window = Tk()
window.title("Projet 2 Forage de données")
# window.geometry("500x500")


def openfile_kmeans():
    global image
    global result_image
    for widget in comparizon_frame.winfo_children():
       widget.destroy()
    #file browser
    window.filename = filedialog.askopenfilename(initialdir="./rsc", title = "Appliquer Kmeans sur l'image choisie", filetypes=[("png", "*.png"),("jpg", "*.jpg *.jpeg")])
    image= ImageTk.PhotoImage(Image.open(window.filename))

    #applying kmeans algorithm
    kmeans.KMeansOnImage(str(window.filename),int(entry_k.get()),int(entry_iter.get()))
  
    #printing input image
    text1= Label(comparizon_frame, text="Before Kmeans").pack()
    image_label = Label(comparizon_frame, image=image).pack()

    #printing output image
    text2= Label(comparizon_frame, text="After Kmeans").pack()
    text3= Label(kmeans_frame, text="Kmeans on "+ window.filename + " done !").pack()
    result_image= ImageTk.PhotoImage(Image.open("./result/result_image_kmeans.png"))  
    result_image_label = Label(comparizon_frame, image=result_image).pack()
    # result_image_label = Label(kmeans_frame, image=result_image).pack()

    
def cleartab() :
    for widget in comparizon_frame.winfo_children():
        widget.destroy()
    # clear_button = Button(comparizon_frame, text = "Clear", command=cleartab).pack()


#creating tabs
my_notebook=ttk.Notebook(window)
my_notebook.pack()

comparizon_frame = Frame(my_notebook)
kmeans_frame = Frame(my_notebook, width=500, height=500)
dbs_frame = Frame(my_notebook, width=500, height=500)

comparizon_frame.pack(fill="both",expand=1)
kmeans_frame.pack(fill="both",expand=1)
dbs_frame.pack(fill="both",expand=1)

my_notebook.add(kmeans_frame, text= "Kmeans")
my_notebook.add(dbs_frame, text= "DBScan")
my_notebook.add(comparizon_frame, text= "Comparizon")


my_scrollbar= ttk.Scrollbar(comparizon_frame,orient=VERTICAL)
my_scrollbar.pack(side="right",fill=Y)

#kmeans frame 
label_k = Label(kmeans_frame, text="Choisir valeur de k", pady=10).pack()
entry_k = Entry(kmeans_frame)
entry_k.pack()

label_iter = Label(kmeans_frame, text="Choisir nombre itérations", pady=10).pack()
entry_iter = Entry(kmeans_frame)
entry_iter.pack()

open_kmeans_button = Button(kmeans_frame,text= "Ouvrir image", command=openfile_kmeans).pack()

#comparizon frame

# clear_button = Button(comparizon_frame, text = "Clear", command=cleartab).pack()


window.mainloop()



