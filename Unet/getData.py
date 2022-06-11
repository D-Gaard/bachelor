import shutil
import math
import random
import os
from glob import glob
from natsort import natsorted

#pass version as string
def getImageSegPaths(version):
  path_global = r"AllData\img_v" + version
  path_seg = r"\segment"
  path_img = r"\image"

  path_combined_img = path_global + path_img
  path_combined_seg = path_global + path_seg

  images = natsorted(glob(os.path.join(path_combined_img, "IMG*.tiff")))
  segs = natsorted(glob(os.path.join(path_combined_seg, "I*.tiff")))

  return images, segs

#get multiple data sets by passing list of versions as string
def getMultipleImageSegPaths(versionList):
  all_images = []
  all_segs = []
  for i in versionList:
    images, segs = getImageSegPaths(i)
    all_images += images
    all_segs += segs

  return all_images, all_segs

#get split of images and segmentations, by passing split size as int
def getRandomImageSegSplit(imagePaths, segPaths, splitSize, seed=23):
  random.seed(seed)
  split_indexs = random.sample(range(0, len(imagePaths)), splitSize)
  remaining_indexs = [x for x in [i for i in range(
      len(imagePaths))] if x not in split_indexs]

  images_remaining = [imagePaths[i] for i in remaining_indexs]
  segs_remaining = [segPaths[i] for i in remaining_indexs]
  images_split = [imagePaths[i] for i in split_indexs]
  segs_split = [segPaths[i] for i in split_indexs]

  return images_remaining, segs_remaining, images_split , segs_split

#get size of train , val , test split
def getSplitSize(data_list, split_size=[0.70, 0.15, 0.15]):
  total = len(data_list)

  train = int(total*split_size[0])
  val = int(total*split_size[1])
  test = int(total*split_size[2])

  remain = total - val - test - train

  if (remain == 1):
    #add to training
    train += 1
    remain -= 1
  elif (remain == 2):
    #add to val and test
    val += 1
    test += 1
    remain -= 2

  return train, val, test

#get file paths for img and segs for train , val , test
def getTestValTrainSplit(version):
  images, segs = getImageSegPaths(version)

  #get split sizes
  sizeTrain, sizeVal, sizeTest = getSplitSize(images)

  #get train valtest splits and ten val test split
  train_img, train_seg, valTest_img, valTest_seg = getRandomImageSegSplit(
      images, segs, sizeVal + sizeTest)
  val_img, val_seg, test_img, test_seg = getRandomImageSegSplit(
      valTest_img, valTest_seg, sizeVal)

  return train_img, train_seg, val_img, val_seg, test_img, test_seg

#create folders for train val and test
def createNewTestValTrainFolders(version, path=r"AllData\img_v", folders=[r"\train", r"\val", r"\test"]):
  imgSeg_paths = [r"\image", r"\segment"]
  for j in imgSeg_paths:
    total_path = path + version + j
    for i in folders:
      #remove old folder
      if os.path.exists(total_path + i):
        #remove files
        files = glob(total_path + i + "\*")
        for f in files:
          os.remove(f)

        #remove dir
        os.rmdir(total_path + i)

      #now create the folder again
      os.mkdir(total_path + i)

#move img and segs for train val test to respective folders for single version


def copyImgSegToTrainValTestFolder(version, path=r"AllData\img_v"):
  total_path = path + version
  folders = [r"\train", r"\val", r"\test"]
  imgSeg_folders = [r"\image", r"\segment"]

  #first remove old
  createNewTestValTrainFolders(version)
  #get files
  train_img, train_seg, val_img, val_seg, test_img, test_seg = getTestValTrainSplit(
      version)

  imgList = [train_img, val_img, test_img]
  segList = [train_seg, val_seg, test_seg]

  #copy all images to respective folder
  for i in range(len(folders)):
    for f in imgList[i]:
      f_name = os.path.basename(f)
      shutil.copyfile(
          f, total_path + imgSeg_folders[0] + folders[i] + "\\" + f_name)

  #copy all segmentations to respective folder
  for i in range(len(folders)):
    for f in segList[i]:
      f_name = os.path.basename(f)
      shutil.copyfile(
          f, total_path + imgSeg_folders[1] + folders[i] + "\\" + f_name)

#copy multiple versions to test train val folders
def copyMultipleImgSegToTrainValTestFolder(version_list=["0", "1", "3", "4", "6", "7", "8"]):
  for i in version_list:
    copyImgSegToTrainValTestFolder(i)

#create all folder with train val and test images
def copyAllImgSegToTrainValTestFolder(version_all="ALL", path=r"AllData\img_v", version_list=["0", "1", "3", "4", "6", "7", "8"]):
  total_path = path + version_all

  folders = [r"\train", r"\val", r"\test"]
  imgSeg_folders = [r"\image", r"\segment"]

  #create/clear test train val folders
  createNewTestValTrainFolders(version_all)

  #loop all wanted versions and copy each folder
  for version in version_list:
      #get files
      train_img, train_seg, val_img, val_seg, test_img, test_seg = getTestValTrainSplit(
          version)
      imgList = [train_img, val_img, test_img]
      segList = [train_seg, val_seg, test_seg]

      #copy all image files
      for i in range(len(folders)):
        for f in imgList[i]:
          f_name = os.path.basename(f)
          shutil.copyfile(
              f, total_path + imgSeg_folders[0] + folders[i] + "\\" + f_name)

      #copy all segmentation files
      for i in range(len(folders)):
        for f in segList[i]:
          f_name = os.path.basename(f)
          shutil.copyfile(
              f, total_path + imgSeg_folders[1] + folders[i] + "\\" + f_name)

#get train val test image seg paths
def getImageSegTrainValTest(version):
  path_global = r"AllData\img_v" + version

  path_seg = r"\segment"
  path_img = r"\image"

  folders = [r"\train", r"\val", r"\test"]

  #get train
  path_combined_img = path_global + path_img + folders[0]
  path_combined_seg = path_global + path_seg + folders[0]
  train_images = natsorted(glob(os.path.join(path_combined_img, "IMG*.tiff")))
  train_segs = natsorted(glob(os.path.join(path_combined_seg, "I*.tiff")))

  #get val
  path_combined_img = path_global + path_img + folders[1]
  path_combined_seg = path_global + path_seg + folders[1]
  val_images = natsorted(glob(os.path.join(path_combined_img, "IMG*.tiff")))
  val_segs = natsorted(glob(os.path.join(path_combined_seg, "I*.tiff")))

  #get test
  path_combined_img = path_global + path_img + folders[2]
  path_combined_seg = path_global + path_seg + folders[2]
  test_images = natsorted(glob(os.path.join(path_combined_img, "IMG*.tiff")))
  test_segs = natsorted(glob(os.path.join(path_combined_seg, "I*.tiff")))

  return train_images, train_segs, val_images, val_segs, test_images, test_segs
