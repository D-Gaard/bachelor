import numpy as np
import math
import raster_geometry as rg
import math
from lineRenderAlgo import Bresenham3D

#construction and functions for the 3d worldsetup and test figures
#(primary,secondary) 0,1,3,4,6,7,8
ANGLES = np.array([(30.7,0.7),(11,20),(-31,-0.1),(-21.5,-24.8),(-24.5,27.3),(0.1,36.7),(49.5,1.3)])
SRC_TO_DETECTOR = 1167
SRC_TO_PATIENT = 705
DETECTOR_TO_PATIENT = SRC_TO_DETECTOR - SRC_TO_PATIENT
MAG_FACTOR =  SRC_TO_DETECTOR/SRC_TO_PATIENT # used to determine box dimensions for projections
IMAGE_DIM = 736 #scale image dim down 1 to get centered image (since uneven)
BOX_DIM = math.ceil(IMAGE_DIM/MAG_FACTOR) # ~ 445

#create cicle in 2D
def createSphere2Drepresentation(radius,width):
  circle = rg.circle(width,radius)
  return circle

#create cordinates coresponding to image of circle
def createTestCoordsForCircle(radius):
  circle = createSphere2Drepresentation(radius,IMAGE_DIM-1).astype(int)

  lines = []

  half_image = (IMAGE_DIM-2)/2
  x_start = half_image
  y_start = half_image

  #loop all pixels and save forground coordinates
  for x in range(0, IMAGE_DIM-1):
    for y in range(0, IMAGE_DIM-1):
      if (circle[x, y] == 1):
        #map coordinates
        lines.append((SRC_TO_PATIENT, x_start - x, y_start-y))

  return lines

#preform bresenham on world setup
def performBresenham3D(lines,detector_to_patient,src_to_patient,box_dim):
  allPoints_list = []

  #Perform Bresenham3D for all points
  for i, points in enumerate(lines):
    all_lineboxes = Bresenham3D(-detector_to_patient, 0, 0, src_to_patient, points[1], points[2])

    #map box cords to world cords
    xyz_max = (box_dim - 1) / 2
    for i, data in enumerate(all_lineboxes):
      x = data[0]
      y = data[1]
      z = data[2]
      if (-xyz_max <= x <= xyz_max and -xyz_max <= y <= xyz_max and -xyz_max <= z <= xyz_max):
        allPoints_list.append((x, y, z))

  return allPoints_list

#save world coords in box coordinates and discarde outside corrdinates
def savePointsWithinSquare(allPoints_list,box_dim):
  box = np.zeros((box_dim, box_dim, box_dim))

  #define positive corner -> box:0,0,0 maps world:poitive corner, -.- , -.-
  x_start2 = int((box_dim -1)/2)
  y_start2 = int((box_dim -1)/2)
  z_start2 = int((box_dim -1)/2)
  for i,data in enumerate(allPoints_list):
    x = data[0] + x_start2
    y = data[1] + y_start2
    z = data[2] + z_start2
    box[x,y,z] = 1
  
