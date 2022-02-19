##################################
#        FORAGE DE DONNES        #
#  TP2 - CLUSTERING DE COULEURS  #
#   Auteur : MELLIER Valentin    #
##################################
#Libs utilisés dans le fichier dbscan.py

from PIL.Image import *
from math import sqrt
import numpy as np
import random

def euclidian_distance(p1, p2):
  return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def manhattan_distance(p1, p2):
  return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2]))

def DbscanOnImage(imagepath,d,m):
    #Ouverture de l'image qui sera modifié
    image = open(imagepath)
    width, height = image.size
    image_array=np.array(image)


    #Définition du tableau contenant la liste des pixels non visités
    unvisitedpixel=[]
    for x in range(width):
      for y in range(height):  
        unvisitedpixel.append((x,y))

    #Pile contenant la liste des pixels à visiter pour élaborer un cluster
    stack=[]

    #Tant qu'on a pas visité tous les pixels
    while(len(unvisitedpixel)!=0):
      #Choix d'un pixel random et ajout à la pile
      stack.append(random.choice(unvisitedpixel))

      #Tant qu'il y a des pixels proches à visiter pour élaborer un cluster
      while(len(stack)!=0):
        current_pixel=stack.pop()
        unvisitedpixel.remove(current_pixel)
        print(current_pixel)

        pixelColor=image_array[current_pixel[1]][current_pixel[0]]

        #Explore neighbours
        


def checkNeighbours(pixel,d,m,image):
  pixelColor=image[pixel[0]][pixel[1]]

  #Get list of neighbours
  neighbours=image[pixel[0]-d,pixel[0]+d][pixel[1]-d,pixel[1]+d]

  #If core point
  #If border point
  #If noise

#def definePixelType(pixel,d,m):

    

    #1 - Choix d'un pixel random, récupération de sa couleur RGB

    #2 - Fonction avec le param d(rayon du cercle) et m (nombre minimum de points dans le cercle)
    #Dessiner un cercle de rayon d autour du point
    # Asignation du type de point:
    # core_point si cnt_neighbour >= m (Dans ce cas création du cluster rassemblant tous les voisins)
    #   Application du même algorithme à chaque sous voisin
    # border_point si cnt_neighbour < m 
    # noise si cnt_neigbour = 0

#TEST
DbscanOnImage("perceval.jpg",3,2)
# a= np.array([[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]])
# print(a[1:1,1:1])