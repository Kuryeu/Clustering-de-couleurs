##################################
#        FORAGE DE DONNES        #
#  TP2 - CLUSTERING DE COULEURS  #
# Auteurs : - MELLIER Valentin   #
#           - LAUGIER Alexis     #
##################################
#Libs utilisés dans le fichier dbscan.py

from PIL.Image import *
from math import sqrt
import numpy as np
import random


#Retourne la distance euclidienne entre la couleur de deux pixels
def euclidian_distance_color(p1, p2):
  return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

#Retourne la distance manhattan entre la couleur de deux pixels
def manhattan_distance_color(p1, p2):
  return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2]))

#Fonction appliquant l'algo Dbscan à l'image (d: distance, m: nombre de noeuds dans un cluster)
def DbscanOnImage(imagepath,d,m):
  global first_point,image_array_old,image_array_new,unvisitedpixel,k
  k=0

  #Ouverture de l'image qui sera analysée
  image_old = open(imagepath)
  width, height = image_old.size
  image_array_old=np.array(image_old)
  image_array_old=image_array_old.astype('int')

  #Ouverture de l'image qui sera modifiée
  image_new = open(imagepath) 
  image_array_new=np.array(image_new)
  image_array_new=image_array_new.astype('int')

  #Initialisation du tableau contenant la liste des pixels non visités
  unvisitedpixel=[]
  for x in range(width):
    for y in range(height):  
      unvisitedpixel.append((y,x))

  #Pile contenant la liste des pixels à visiter pour élaborer des clusters
  stack=[]
  #Tableau contenant la couleur de chaque cluster
  clustercolor=[]

  #Tant qu'on a pas visité tous les pixels
  while(len(unvisitedpixel)!=0):

    #Affichage de l'avancée des pixels restant
    print(len(unvisitedpixel))
    first_point = True

    #Choix d'un pixel random et ajout à la pile
    stack.append(random.choice(unvisitedpixel))
    
    #Tant qu'il y a des pixels proches à visiter pour élaborer un cluster
    while(len(stack)!=0):

      current_pixel=stack.pop()

      #On explore les voisins
      neighboursList=checkNeighbours(current_pixel,d,image_array_old)

      #On définit le type de pixel (Noeud coeur/bordure/bruit)
      current_pixel=definePixelType(current_pixel,neighboursList,m)
      
      #Si le pixel est une bordure et qu'il n'y a pas encore de cluster établit
      if(current_pixel[2] & first_point):

        #On indique le pixel et les voisins comme visités
        unvisitedpixel.remove((current_pixel[0][0],current_pixel[0][1]))
        neighboursList=set(neighboursList)&set(unvisitedpixel) 
        continue

      #On marque le pixel actuel comme visité et on vérifie qu'il n'y en a pas déjà visité dans la liste des voisins
      unvisitedpixel.remove((current_pixel[0][0],current_pixel[0][1]))
      neighboursList=set(neighboursList)&set(unvisitedpixel) 

      #Si noeud coeur, création d'un nouveau cluster
      if(current_pixel[1]):
        if(first_point==True):
          clustercolor.append(image_array_old[current_pixel[0][0]][current_pixel[0][1]])
          first_point =False
          
        #Affectation de la couleur aux voisins
        image_array_new=setClusterColor(clustercolor[k],neighboursList,image_array_new)

        #Ajout des voisins à la stack pour exploration
        for pixel in neighboursList:
          if pixel not in stack:
            stack.append(pixel)
        continue
        
      #Si noeud bordure
      elif(current_pixel[2]):
        #On assigne la couleur du pixel à la couleur du cluster courant
        image_array_new[current_pixel[0][0]][current_pixel[0][1]]=clustercolor[k]
        continue

      #Si aucun pixel voisin
      elif(current_pixel[3]):
        continue

    if(first_point==False):
      k+=1
  save_im=fromarray(np.uint8(image_array_new))
  save_im.save("fraisetest.png")


#Vérif si le centre ne fait pas partie des voisins
def checkNeighbours(pixel,d,image):
  distances = np.linalg.norm(image - image[pixel[0], pixel[1]], ord=2, axis=2)
  x, y = np.where((distances <= d) & (distances!=0))
  return list(zip(x, y))

#Définition du type de pixel
def definePixelType(pixel,neighbours,m):
  neighbours_count=len(neighbours)
  if(neighbours_count>=m):
    #Coeur
    return (pixel,True,False,False)
  elif(neighbours_count<m and neighbours_count>0):
    #Bordure
    return (pixel,False,True,False)
  elif(neighbours_count==0):
    #Bruit
    return (pixel,False,False,True)

#On assigne la couleur du cluster aux pixels de l'image concerné
def setClusterColor(pixel,neighbours,image):
  for neighbour in neighbours:
    image[neighbour[0],neighbour[1]]=pixel
  return image

#Test
#DbscanOnImage("fraise.jpg",3,2)