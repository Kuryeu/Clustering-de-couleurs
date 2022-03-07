##################################
#        FORAGE DE DONNES        #
#  TP2 - CLUSTERING DE COULEURS  #
#   Auteur : MELLIER Valentin    #
##################################
#Libs utilisés dans le fichier main.py
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from functools import partial
from turtle import clear, distance, onclick, right, window_height, window_width
from PIL.Image import *
from PIL import Image, ImageTk
from random import *
from math import sqrt
import kmeans
import dbscan


window = Tk()
window.title("Projet 2 Forage de données")
# window.geometry("500x500")


def openfile(method):
    global image
    global result_image_kmeans
    # global image_dbs
    global result_image_dbs

    #del all widgets in comparizon tab
    cleartab()
       
    #file browser
    window.filename = filedialog.askopenfilename(initialdir="./rsc", title = "Choisis une photo mon bro", filetypes=[("png", "*.png"),("jpg", "*.jpg *.jpeg")])
    image= ImageTk.PhotoImage(Image.open(window.filename))


    if method == "kmeans" :
        distance=dist.get()
        #applying kmeans algorithm
        k_value=entry_k.get()
        iter_value = entry_iter.get()
        kmeans.KMeansOnImage(str(window.filename),int(k_value),int(iter_value),dist.get())
    
        #printing input image
        text1= Label(comparizon_frame, text="Before Kmeans").pack()
        image_label = Label(comparizon_frame, image=image).pack()

        #printing output image
        text2= Label(comparizon_frame, text="After Kmeans (k=" + k_value + ", iter=" + iter_value + ", " + distance + " distance)").pack()
        text3= Label(kmeans_frame, text="Kmeans on "+ window.filename + " done !").pack()
        result_image_kmeans= ImageTk.PhotoImage(Image.open("./result/result_image_kmeans.png"))  
        result_image_kmeans_label = Label(comparizon_frame, image=result_image_kmeans).pack()
        # result_image_kmeans_label = Label(kmeans_frame, image=result_image_kmeans).pack()
  
    if method == "dbs" :
        #applying dbscan algorithm        
        m_value=entry_m.get()
        d_value=entry_d.get()
        dbscan.DbscanOnImage(str(window.filename),int(m_value),int(d_value))
    
        #printing input image
        text1= Label(comparizon_frame, text="Before dbscan").pack()
        image_label = Label(comparizon_frame, image=image).pack()

        #printing output image
        text2= Label(comparizon_frame, text="After dbscan (m=" + m_value + ", d=" + d_value + ")").pack()
        text3= Label(dbs_frame, text="Dbscan on "+ window.filename + " done !").pack()
        result_image_dbs= ImageTk.PhotoImage(Image.open("./result/result_image_dbs.png"))  
        result_image_dbs_label = Label(comparizon_frame, image=result_image_dbs).pack()
        # result_image_dbs_label = Label(dbs_frame, image=result_image_dbs).pack()

    
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

dist = StringVar()
dist.set("manhattan")
manhattan = Radiobutton(kmeans_frame, text = "Manhattan distance", variable = dist, value = "manhattan", pady=10).pack()
euclidian = Radiobutton(kmeans_frame, text = "Euclidian distance", variable = dist, value = "euclidian" ).pack()

open_kmeans_button = Button(kmeans_frame,text= "Ouvrir image", command=partial(openfile, "kmeans")).pack()

#dbs frame 
label_d = Label(dbs_frame, text="Choisir valeur de d", pady=10).pack()
entry_d = Entry(dbs_frame)
entry_d.pack()

label_m = Label(dbs_frame, text="Choisir valeur de m", pady=10).pack()
entry_m = Entry(dbs_frame)
entry_m.pack()

open_dbs_button = Button(dbs_frame,text= "Ouvrir image", command=partial(openfile,"dbs")).pack()

#comparizon frame

# clear_button = Button(comparizon_frame, text = "Clear", command=cleartab).pack()


window.mainloop()



