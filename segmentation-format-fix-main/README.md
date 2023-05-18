## Segmentation Format Fix

Tools to adapt the format of the dataset for the semantic segmentation algorithm to the training requirements.
--

Personal use.
From: https://github.com/bubbliiiing/segmentation-format-fix.

## Raw Image Processing
When the input original image suffix is not `.jpg`, it cannot be trained properly, you can use `Convert_JPEGImages.py` to modify the original image suffix in batch.
### Steps
1、Origin_JPEGImages_path: specify the images need to be modified with a suffix；    
2、Out_JPEGImages_path: specify the output path；    
3、Modify and run, batch process the original image, process it as an RGB image and change the suffix to `.jpg`.   

## Label Processing
The value of each pixel of the label is the kind to which the pixel belongs, and if it does not match then there will be no training effect.
Use `Convert_SegmentationClass.py` to modify the labels batchly.
### Steps
1、Origin_SegmentationClass_path: specify the labels need to be modified；   
2、Out_SegmentationClass_path: specify the output path；   
3、Origin_Point_Value: specify the original path；   
4、Out_Point_Value: specify the pixel point value corresponding to the output labels；   
5、Modify and run, batch process the labels, process it as an GRAY image and change the suffix to `.png`.
