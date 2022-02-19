from tkinter import *
from tkinter import filedialog
from PIL.Image import *
from PIL import Image, ImageTk
from random import *
from math import sqrt

window = Tk()
window.title("Projet 2 Forage de données")



def openfile():
    global image
    window.filename = filedialog.askopenfilename(initialdir="./rsc", title = "choisis frr", filetypes=[("png", "*.png"),("jpg", "*.jpg *.jpeg")])

    text= Label(window, text=window.filename).pack()
    image= ImageTk.PhotoImage(Image.open(window.filename))
    print (window.filename)
    image_label = Label(image=image).pack()
    algorithm_button = Button ( window, text = "Appliquer algorithme", command=KMeansOnImage(str(window.filename),4,10)).pack()

def euclidian_distance(p1, p2):
  return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def manhattan_distance(p1, p2):
  return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2]))



def KMeansOnImage(imagepath,k,iter):

    #Ouverture de l'image de référence
    untouch_image=open(imagepath).load()
    #Ouverture de l'image qui sera modifié
    touch_image = open(imagepath)
    #Récupération des dimensions
    width, height = touch_image.size
    #Génération aléatoire de k centroïdes dans l'image
    centroids = generateKColors(k,touch_image)

    #Chargement de l'image qui sera modifiée
    Update_image = touch_image.load()

    for i in range(0,iter):
        #Variable contenant les pixels rattachés à chaque centroïde
        get_pix_for_each_centroids=[[] for r in range(k)]
        #On parcourt l'image
        for x in range(width):
            for y in range(height):                    
                centroids_dist_from_pix=[]
                #Pour chaque centroïde
                for elem in centroids:
                    #On stocke les distances du pixel(x,y) à chaque centroïde
                    centroids_dist_from_pix.append(manhattan_distance(elem,untouch_image[x,y]))
                #On assigne le pixel au centroïde le plus proche
                get_pix_for_each_centroids[centroids_dist_from_pix.index(min(centroids_dist_from_pix))].append(untouch_image[x,y])
                Update_image[x,y] = centroids[centroids_dist_from_pix.index(min(centroids_dist_from_pix))] 

        #On replace chaque centroïde en calculant la moyenne des distances aux autres pixels
        centroids=computeMean(centroids, get_pix_for_each_centroids)
    touch_image.save("result/result_image.png")

        
        
    
def computeMean(centroids, centroidsPixList):
    #On calcule la moyenne et on retourne la nouvelle valeur du centroïde
    for elem in centroidsPixList:
        r_sum=0
        g_sum=0
        b_sum=0
        for rgbtuple in elem:
            r_sum+=rgbtuple[0]
            g_sum+=rgbtuple[1]
            b_sum+=rgbtuple[2]
        centroids[centroidsPixList.index(elem)]=(int(r_sum/(len(elem)+1)),int(g_sum/(len(elem)+1)),int(b_sum/(len(elem)+1)))
    return centroids

#Définition de centroïdes random dans l'image
def generateKColors(k,image):
    init_Kcentroid_list=[]
    for i in range(0,k):
        init_Kcentroid_list.append(image.getpixel((randint(0,image.size[0]-1),randint(0,image.size[1]-1))))
    return init_Kcentroid_list





open_button = Button(window, text= "Ouvrir image", command=openfile).pack()
window.mainloop()