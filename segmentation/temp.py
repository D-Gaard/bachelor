# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import sys
import tempfile
from glob import glob
from natsort import natsorted
import random
from trainValTestGreyscale import getData
import torch
from PIL import Image
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

import monai
from monai.data import create_test_image_2d, list_data_collate, decollate_batch
from monai.inferers import sliding_window_inference
from monai.metrics import DiceMetric
from monai.transforms import (
    Activations,
    AddChanneld,
    AsDiscrete,
    Compose,
    LoadImaged,
    RandCropByPosNegLabeld,
    RandRotate90d,
    ScaleIntensityd,
    EnsureTyped,
    EnsureType,
    RandGaussianNoised,
    RandFlipd,
    Rand2DElasticd
)
from monai.visualize import plot_2d_or_3d_image



monai.config.print_config()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

path_to_grey_img = r"greyscale"
path_to_grey_seg = r"greyscale_out"

#images = natsorted(glob(os.path.join(path_to_grey_img, "IMG*.tiff")))
#segs = natsorted(glob(os.path.join(path_to_grey_seg, "I0*.tiff")))

#val_samples = 10
#random.seed(1234)
#val_idx = random.sample(range(0,len(segs)),val_samples)
#train_idx = [id for id in range(0,len(segs))]
#train_idx = [id for id in train_idx if id not in val_idx]

#train_images = [images[idx] for idx in train_idx]
#masks = [segs[idx] for idx in train_idx] 
#val_images = [images[idx] for idx in val_idx]
#val_masks =   [segs[idx] for idx in val_idx]

train_images, train_segs, val_images, val_segs, _, _ = getData.getImageSegTrainValTest("ALL")

train_files = [{"img": img, "seg": seg}
                for img, seg in zip(train_images, train_segs)]
val_files = [{"img": img, "seg": seg}
                for img, seg in zip(val_images, val_segs)]

# define transforms for image and segmentation
train_transforms = Compose(
    [
        LoadImaged(keys=["img", "seg"]),
        AddChanneld(keys=["img", "seg"]),
        ScaleIntensityd(keys=["img", "seg"]),
        RandFlipd(keys=["img", "seg"], prob=0.5, spatial_axis = 1), #mirror in vertical axis
        RandRotate90d(keys=["img", "seg"], prob=0.75, max_k = 3, spatial_axes=[0, 1]),
        Rand2DElasticd(keys=["img", "seg"], prob = 1, spacing = (10,10), magnitude_range = (1,2), padding_mode = "zeros",
            mode = ["bilinear", "nearest"]),
        RandGaussianNoised(keys=["img"], prob = 0.1, mean = 0, std = 0.1),
        EnsureTyped(keys=["img", "seg"]),  
    ]
)
#RandCropByPosNegLabeld(
#            keys=["img", "seg"], label_key="seg", spatial_size=[192, 192], pos=1, neg=1, num_samples=4
#        ), #REMOVAL?


val_transforms = Compose(
    [
        LoadImaged(keys=["img", "seg"]),
        AddChanneld(keys=["img", "seg"]),
        ScaleIntensityd(keys=["img", "seg"]),
        EnsureTyped(keys=["img", "seg"]),
    ]
)