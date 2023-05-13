# 標準ライブラリ
import json
import base64
import os
import glob
from labelme import utils
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import cv2

img_folder = "/Users/lijingyi/Desktop/lesson-2/data/test"
save_folder = "./ivc-mask"

if not os.path.exists(save_folder):
    os.mkdir(save_folder)
    print("Made save directory.\n")

files=glob.glob(img_folder+"/*.json")

for file in files:

    name = os.path.splitext(os.path.basename(file))[0]
    json_file = open(file)

    json_data = json.load(json_file)

    for i in range(len(json_data['shapes'])):

        points = json_data['shapes'][i]['points']
        label = json_data['shapes'][i]['label']
        # print(len(json_data['shapes']))

        points = [tuple(point) for point in points]

        img_b64 = json_data['imageData']

        img_data = base64.b64decode(img_b64)

        img_pil = utils.img_data_to_pil(img_data)

        w, h = img_pil.size
        mask = Image.new('L', (w, h))
        draw = ImageDraw.Draw(mask)
        draw.polygon(points, fill = 1)

        if os.path.exists(save_folder+"/"+label)==False:
            os.mkdir(save_folder+"/"+label) 



        cv2.imwrite(save_folder + "/"+ label + "/" +name + ".png",np.array(mask)*255)
    # print("%s.json   ->   %s.png" %(name,name))

print("End")