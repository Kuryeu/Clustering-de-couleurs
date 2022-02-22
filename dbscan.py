<<<<<<< HEAD
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

#Retourne la distance euclidienne entre la position de deux pixels
def euclidian_distance_pixel(p1, p2):
  return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#Retourne la distance euclidienne entre la couleur de deux pixels
def euclidian_distance_color(p1, p2):
  return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def manhattan_distance(p1, p2):
  return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2]))

def DbscanOnImage(imagepath,d,m):
  global first_point,image_array
  k=0
  #Ouverture de l'image qui sera modifié
  image = open(imagepath)
  width, height = image.size
  image_array=np.array(image)
  image_array=image_array.astype('uint32')


  #Initialisation du tableau contenant la liste des pixels non visités
  unvisitedpixel=[]
  for x in range(width):
    for y in range(height):  
      unvisitedpixel.append([x,y,"undefined"])

  #Pile contenant la liste des pixels à visiter pour élaborer un cluster
  stack=[]
  clustercolor=[]

  #Tant qu'on a pas visité tous les pixels
  while(len(unvisitedpixel)!=0):
    print(len(unvisitedpixel))
    first_point = True
    #Choix d'un pixel random et ajout à la pile
    pixelchoosed=random.choice(unvisitedpixel)
    stack.append(pixelchoosed)
    

    #Tant qu'il y a des pixels proches à visiter pour élaborer un cluster
    while(len(stack)!=0):

      current_pixel=stack.pop(0)
      #Explore neighbours
      neighboursList=checkNeighbours(current_pixel,d,image_array,width,height)
      #Define pixel type
      definePixelType(current_pixel,neighboursList,m)

      if(current_pixel[2]=="is_border" and first_point):

        res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == current_pixel[0] and y==current_pixel[1])]
        if res:
              unvisitedpixel.remove(res[0])

        for pixel in neighboursList:
          res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == pixel[0] and y==pixel[1])]
          if res:
              unvisitedpixel.remove(res[0])

      #Création d'un nouveau cluster
      elif(current_pixel[2]=="is_core"):
        
        #Ajout de la couleur du nouveau cluster
        if(first_point):
          clustercolor.append(image_array[current_pixel[1]][current_pixel[0]])
        
        first_point =False
        #Explore neighbours et affectation de la couleur
        image_array=setClusterColor(clustercolor[k],neighboursList,image_array)
        for pixel in neighboursList:
          res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == pixel[0] and y==pixel[1])]
          if res:
              stack.append(res[0])
              unvisitedpixel.remove(res[0])

      elif(current_pixel[2]=="is_noise"):
        #Stop explore
        res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == current_pixel[0] and y==current_pixel[1])]
        if res:
              unvisitedpixel.remove(res[0])        
    if(first_point==False):
      k+=1
      save_im=fromarray(np.uint8(image_array))
      save_im.save("resultdb.png")

      
        


def checkNeighbours(pixel,d,image,width,height):
  nearDistPixels=create_circular_mask(height,width,pixel,d)
  neighbourList=[]
  for neighbour in nearDistPixels:
    if (euclidian_distance_color(image[pixel[1]][pixel[0]],image[neighbour[1]][neighbour[0]]) < d):
      neighbourList.append(neighbour)
  return neighbourList


def create_circular_mask(h,w,pixel,d):
  y,x=np.ogrid[:h,:w]
  mask_pixel=np.where((euclidian_distance_pixel((x,y),pixel) <= d)==True)
  return list(zip(mask_pixel[1],mask_pixel[0]))

def definePixelType(pixel,neighbours,m):
  neighbours_count=len(neighbours)
  if(neighbours_count>=m):
    pixel[2]="is_core"
  elif(neighbours_count<m and neighbours_count!=0):
    pixel[2]="is_border"
  elif(neighbours_count==0):
    pixel[2]="is_noise"
  return pixel

def setClusterColor(pixel,neighbours,image):
  for neighbour in neighbours:
    image[neighbour[1],neighbour[0]]=pixel
  return image


#TEST
# DbscanOnImage("perceval.jpg",10,10)
=======
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

#Retourne la distance euclidienne entre la position de deux pixels
def euclidian_distance_pixel(p1, p2):
  return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#Retourne la distance euclidienne entre la couleur de deux pixels
def euclidian_distance_color(p1, p2):
  return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def manhattan_distance(p1, p2):
  return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2]))

def DbscanOnImage(imagepath,d,m):
  global first_point,image_array
  k=0
  #Ouverture de l'image qui sera modifié
  image = open(imagepath)
  width, height = image.size
  image_array=np.array(image)
  image_array=image_array.astype('uint32')


  #Initialisation du tableau contenant la liste des pixels non visités
  unvisitedpixel=[]
  for x in range(width):
    for y in range(height):  
      unvisitedpixel.append([x,y,"undefined"])

  #Pile contenant la liste des pixels à visiter pour élaborer un cluster
  stack=[]
  clustercolor=[]

  #Tant qu'on a pas visité tous les pixels
  while(len(unvisitedpixel)!=0):
    print(len(unvisitedpixel))
    first_point = True
    #Choix d'un pixel random et ajout à la pile
    pixelchoosed=random.choice(unvisitedpixel)
    stack.append(pixelchoosed)
    

    #Tant qu'il y a des pixels proches à visiter pour élaborer un cluster
    while(len(stack)!=0):

      current_pixel=stack.pop(0)
      #Explore neighbours
      neighboursList=checkNeighbours(current_pixel,d,image_array,width,height)
      #Define pixel type
      definePixelType(current_pixel,neighboursList,m)

      if(current_pixel[2]=="is_border" and first_point):

        res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == current_pixel[0] and y==current_pixel[1])]
        if res:
              unvisitedpixel.remove(res[0])

        for pixel in neighboursList:
          res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == pixel[0] and y==pixel[1])]
          if res:
              unvisitedpixel.remove(res[0])

      #Création d'un nouveau cluster
      elif(current_pixel[2]=="is_core"):
        
        #Ajout de la couleur du nouveau cluster
        if(first_point):
          clustercolor.append(image_array[current_pixel[1]][current_pixel[0]])
        
        first_point =False
        #Explore neighbours et affectation de la couleur
        image_array=setClusterColor(clustercolor[k],neighboursList,image_array)
        for pixel in neighboursList:
          res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == pixel[0] and y==pixel[1])]
          if res:
              stack.append(res[0])
              unvisitedpixel.remove(res[0])

      elif(current_pixel[2]=="is_noise"):
        #Stop explore
        res = [[x,y,z] for [x,y,z] in unvisitedpixel if (x == current_pixel[0] and y==current_pixel[1])]
        if res:
              unvisitedpixel.remove(res[0])        
    if(first_point==False):
      k+=1
      save_im=fromarray(np.uint8(image_array))
      save_im.save("resultdb.png")

      
        


def checkNeighbours(pixel,d,image,width,height):
  nearDistPixels=create_circular_mask(height,width,pixel,d)
  neighbourList=[]
  for neighbour in nearDistPixels:
    if (euclidian_distance_color(image[pixel[1]][pixel[0]],image[neighbour[1]][neighbour[0]]) < d):
      neighbourList.append(neighbour)
  return neighbourList


def create_circular_mask(h,w,pixel,d):
  y,x=np.ogrid[:h,:w]
  mask_pixel=np.where((euclidian_distance_pixel((x,y),pixel) <= d)==True)
  return list(zip(mask_pixel[1],mask_pixel[0]))

def definePixelType(pixel,neighbours,m):
  neighbours_count=len(neighbours)
  if(neighbours_count>=m):
    pixel[2]="is_core"
  elif(neighbours_count<m and neighbours_count!=0):
    pixel[2]="is_border"
  elif(neighbours_count==0):
    pixel[2]="is_noise"
  return pixel

def setClusterColor(pixel,neighbours,image):
  for neighbour in neighbours:
    image[neighbour[1],neighbour[0]]=pixel
  return image


#TEST
DbscanOnImage("perceval.jpg",10,10)
>>>>>>> e7a73b2841711e677f343beb40d615acaed9a411
