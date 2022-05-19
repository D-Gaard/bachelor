import numpy as np
import nrrd

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
