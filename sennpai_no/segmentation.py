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

from torch.utils.data import DataLoader
from torch.utils.data import Dataset as BaseDataset

#-----------ここは変更----------
ENCODER = 'efficientnet-b1'
ENCODER_WEIGHTS = 'imagenet'
DEVICE = 'cuda'

#using weight
best_model = torch.load('./weights/unet_'+ENCODER+'_ivc_c_major.pth')
#best_model = torch.load('重みの名前')
file_path = "./data/c_major_axis/testimage"
save_path = "./image_result_c_major/"
#-------------------------------

#torch.backends.cudnn.enabled = False

if os.path.exists(save_path)==False:
    os.mkdir(save_path)

def to_tensor(x, **kwargs):
    return x.transpose(2, 0, 1).astype('float32')

def get_validation_augmentation():
    """Add paddings to make image shape divisible by 32"""
    test_transform = [
        #albu.Crop(80, 0, 400, 320, always_apply=True),
        #albu.Crop(214, 0, 534, 320, always_apply=True),
        albu.Resize(height=320, width=320, always_apply=True),
        #albu.PadIfNeeded(384, 480),
    ]
    return albu.Compose(test_transform)

def get_preprocessing(preprocessing_fn):
    _transform = [
        albu.Lambda(image=preprocessing_fn),
        albu.Lambda(image=to_tensor, mask=to_tensor),
    ]
    return albu.Compose(_transform)

file = glob.glob(file_path+'/*.png')

preprocessing_fn = smp.encoders.get_preprocessing_fn(ENCODER, ENCODER_WEIGHTS)

#一枚ずつ

image = cv2.imread("./data/c_major_axis/testimage/pic151.png")

print(image.shape)

h, w =image.shape[0], image.shape[1]

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = get_validation_augmentation()(image=image)
image = image['image']
image = get_preprocessing(preprocessing_fn)(image=image)
image = image['image']

x_tensor = torch.from_numpy(image).to(DEVICE).unsqueeze(0)

pr_mask = best_model.predict(x_tensor)
pr_mask = (pr_mask.squeeze().cpu().numpy().round())

img = np.array(pr_mask)
img = albu.Resize(h,w)(image=img)['image']
img2 = np.clip(img * 255, 0, 255).astype(np.uint8)

ret, img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("segmentation result",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

for i in file:
    name = os.path.basename(i)
    image = cv2.imread(file_path+"/"+name)

    h, w =image.shape[0], image.shape[1]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = get_validation_augmentation()(image=image)
    image = image['image']
    image = get_preprocessing(preprocessing_fn)(image=image)
    image = image['image']

    x_tensor = torch.from_numpy(image).to(DEVICE).unsqueeze(0)

    pr_mask = best_model.predict(x_tensor)
    pr_mask = (pr_mask.squeeze().cpu().numpy().round())

    img = np.array(pr_mask)
    img = albu.Resize(h,w)(image=img)['image']
    img2 = np.clip(img * 255, 0, 255).astype(np.uint8)

    ret, img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite(save_path+name, img2)

    # cv2.imshow("",img2)
    # cv2.Waitkey(0)
    # cv2.Allwindowsdestroy()

"""

print("End")