**Background**

Personal use.
From：[Github](https://github.com/spytensor/prepare_detection_dataset)

**Newly upload**

- (28/03/2019)
    - Release: `csv2labelme`


<h4 id="1">1. Intro</h4>

Convert between several common data formats;
The use of the universal intermediary `csv` format:

- csv to coco
- csv to voc
- labelme to coco
- labelme to voc
- csv to json

<h4 id="2">2. Standard formats</h4>

Before using the conversion script, clarify:

<h5 id="2.1">2.1 csv</h5>

You'd better try to modify the codes or labels first, rather than running the scripts directly.
The csv format should be:

- `csv/`
    - `labels.csv`
    - `images/`
        - `image1.jpg`
        - `image2.jpg`
        - `...`

`labels.csv`  look: 

`/path/to/image,xmin,ymin,xmax,ymax,label`

For example:

```
/mfs/dataset/face/0d4c5e4f-fc3c-4d5a-906c-105.jpg,450,154,754,341,face
/mfs/dataset/face/0ddfc5aea-fcdac-421-92dad-144.jpg,143,154,344,341,face
...
```
Note: Please use absolute path for image path

<h5 id="2.2">2.2 voc</h5>

The standard voc data format：

- `VOC2007/`
    - `Annotations/`
        - `0d4c5e4f-fc3c-4d5a-906c-105.xml`
        - `0ddfc5aea-fcdac-421-92dad-144/xml`
        - `...`
    - `ImageSets/`
        - `Main/`
            - `train.txt`
            - `test.txt`
            - `val.txt`
            - `trainval.txt`
    - `JPEGImages/`
        - `0d4c5e4f-fc3c-4d5a-906c-105.jpg`
        - `0ddfc5aea-fcdac-421-92dad-144.jpg`
        - `...`

<h5 id="2.3">2.3 coco</h5>

No `test` here.

- `coco/`
    - `annotations/`
        - `instances_train2017.json`
        - `instances_val2017.json`
    - `images/`
        - `train2017/`
            - `0d4c5e4f-fc3c-4d5a-906c-105.jpg`
            - `...`
        - `val2017`
            - `0ddfc5aea-fcdac-421-92dad-144.jpg`
            - `...`

<h5 id="2.4">2.4 labelme</h5>


- `labelme/`
    - `0d4c5e4f-fc3c-4d5a-906c-105.json`
    - `0d4c5e4f-fc3c-4d5a-906c-105.jpg`
    - `0ddfc5aea-fcdac-421-92dad-144.json`
    - `0ddfc5aea-fcdac-421-92dad-144.jpg`

Json file:

```json
{
  "version": "3.6.16",
  "flags": {},
  "shapes": [
    {
      "label": "helmet",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          131,
          269
        ],
        [
          388,
          457
        ]
      ],
      "shape_type": "rectangle"
    }
  ],
  "lineColor": [
    0,
    255,
    0,
    128
  ],
  "fillColor": [
    255,
    0,
    0,
    128
  ],
  "imagePath": "004ffe6f-c3e2-3602-84a1-ecd5f437b113.jpg",
  "imageData": ""   # too long ,so not show here
  "imageHeight": 1080,
  "imageWidth": 1920
}
```

<h4 id="3">3. How to use scripts</h4>

<h5 id="3.1">3.1 csv2coco</h5>

First change `csv2coco.py` configures:

```
classname_to_id = {"person": 1}  # for your dataset classes
csv_file = "labels.csv"  # annatations file path
image_dir = "images/"    # original image path
saved_coco_path = "./"   # path to save converted coco dataset
```

Run `python csv2coco.py`

It will automatically create a folder and copy the image to the corresponding location, and after running, you will get the following：

- `coco/`
    - `annotations/`
        - `instances_train2017.json`
        - `instances_val2017.json`
    - `images/`
        - `train2017/`
            - `0d4c5e4f-fc3c-4d5a-906c-105.jpg`
            - `...`
        - `val2017`
            - `0ddfc5aea-fcdac-421-92dad-144.jpg`
            - `...`

<h5 id="3.2">3.2 csv2voc</h5>

First change `csv2voc.py` configures:

```
csv_file = "labels.csv"
saved_path = ".VOC2007/" # path to save converted voc dataset     
image_save_path = "./JPEGImages/"   # converted voc images path
image_raw_parh = "images/"          # original image path
```

Run `python csv2voc.py`

Also create a folder and copy, get the following：


- `VOC2007/`
    - `Annotations/`
        - `0d4c5e4f-fc3c-4d5a-906c-105.xml`
        - `0ddfc5aea-fcdac-421-92dad-144/xml`
        - `...`
    - `ImageSets/`
        - `Main/`
            - `train.txt`
            - `test.txt`
            - `val.txt`
            - `trainval.txt`
    - `JPEGImages/`
        - `0d4c5e4f-fc3c-4d5a-906c-105.jpg`
        - `0ddfc5aea-fcdac-421-92dad-144.jpg`
        - `...`

<h5 id="3.3">3.3 labelme2coco</h5>

First change `labelme2coco.py` configures:

```
classname_to_id = {"person": 1}  # for your dataset classes
labelme_path = "labelme/"  # path for labelme dataset
saved_coco_path = "./"     # path for saved coco dataset
```
Run `python labelme2coco.py`，output file is like`csv2coco`

<h5 id="3.4">3.4 labelme2voc</h5>

First change `labelme2voc.py` configures:

```
labelme_path = "labelme/"  # path for labelme dataset
saved_coco_path = "./"     # path for saved coco dataset
```
Run `python labelme2voc.py`，output file is like `csv2voc`

<h5 id="3.5">3.5 csv2labelme</h5>

First change `csv2labelme.py` configures:

```
image_path = "./images/"  # path for images
csv_file = "./"     # path for csv annotations
```
Run `python csv2labelme.py`，output `json` will be saved at `image_path`,switch the path and directly to `labelme` to check the labels.


<h4 id="4">4. Universal medium csv</h4>

Mainstream detection frameworks rarely support this format of data input(No information is given on how to transfer to .csv -------not because it's simple).
Here is how to write the annotation information to `csv`

```python
info = [[filename0,"xmin ymin xmax ymax label0"],
          filename1,"xmin ymin xmax ymax label1"]
csv_labels = open("csv_labels.csv","w")
for filename,bboxes in info:
    bbox = bboxes.split(" ")
    label = bbox[-1]
    csv_labels.write(filename+","+bbox[0]+","+bbox[1]+","+bbox[2]+","+bbox[3]+","+label+"\n")
csv_labels.close()
```

PS:How to read from the original label file to get the label information

### TODO
- 1. [ ] Multiprocessing
