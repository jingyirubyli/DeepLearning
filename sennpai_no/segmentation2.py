import torch
import numpy as np
import segmentation_models_pytorch as smp
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import albumentations as albu
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import glob
import os
import cv2
import shutil

from torchvision import transforms as T

from torch.utils.data import DataLoader
from torch.utils.data import Dataset as BaseDataset

import torch.nn.functional as F


ENCODER = 'resnet50'
ENCODER_WEIGHTS = 'imagenet'
DEVICE = 'cuda'

file_path = "../data/major-axis-ivc-as/image"
save_path = "../major_axis_ivc_as_test/"

if os.path.exists(save_path)==False:
    os.mkdir(save_path) 

#重み毎回変更
#using weight
best_model = torch.load('./weights/unet_'+ENCODER+'_major_axis_ivc_as.pth')

file = glob.glob(file_path+'/*.png')

mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]

CLASSES = ['ivc', 'liver', 'unlabelled']

for i in file:
    name = os.path.basename(i)
    image = cv2.imread(file_path+"/"+name,1)

    best_model.eval()
    t = T.Compose([T.ToTensor(), T.Normalize(mean, std)])
    image = t(image)
    best_model.to(DEVICE); image=image.to(DEVICE)

    with torch.no_grad():
        image = image.unsqueeze(0)
        output = best_model(image)
        masked = torch.argmax(output, dim=1)
        masked = masked.cpu().squeeze(0)

    img = np.array(masked)
    img = albu.Resize(480,480)(image=img)['image']
    img2 = np.clip(img * 255, 0, 255).astype(np.uint8)
    cv2.imshow("segmentation image", img2)
    cv2.waitKey(1)
    cv2.imwrite(save_path+name , img2)

print("End")