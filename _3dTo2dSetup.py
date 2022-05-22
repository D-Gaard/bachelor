import numpy as np
import nrrd
from scipy.ndimage.interpolation import rotate as SR
import raster_geometry as rg

#create sphere in numpy array
def createSphereIn3d(radius, width):
  circle = rg.sphere(width, radius)
  return circle

#load bitmap nrrd file figure an center in 3d array
def get3dFigure(size,path):
  #load figure
  d, _ = nrrd.read(path)
  #place in center of new figure
  hs = int((size - 1) / 2)
  d_big = np.zeros([size, size, size])
  d_big[hs-133:hs+134, hs-108:hs+108, hs-134:hs+135] = d

  return d_big

#get coords for outline box for visualization 
def get3dBox(size):
  n = int((size-1) / 2)
  frame_x = np.array([-n, -n, -n, -n, n, n, n, n])
  frame_y = np.array([-n, -n, n, n, -n, -n, n, n])
  frame_z = np.array([-n, n, -n, n, -n, n, -n, n])

  return frame_x, frame_y, frame_z

#take list of points and return everypoint in the box centered in 0,0,0 with dim
def getPointsInBox(points,box_dim):
  allPoints_list = []
  xyz_max = (box_dim - 1) / 2
  for i, data in enumerate(points):
    x = data[0]
    y = data[1]
    z = data[2]
    if (-xyz_max <= x <= xyz_max and -xyz_max <= y <= xyz_max and -xyz_max <= z <= xyz_max):
      allPoints_list.append((x, y, z))
  
  return allPoints_list

#rotate box based on primary and secondary angle reverse around z first and then  around y
def rotatePrimSecond(box, prim, sec):
  box2 = np.copy(box)

  box2_rot1 = SR(box2, angle=-prim, axes=(0, 1), reshape=False)
  #scipy rotates then incorect way round the y axis so we revese the angle
  box2_rot2 = SR(box2_rot1, angle=-sec, axes=(0, 2), reshape=False)

  return box2_rot2
