# Lego Classification
Trying to do classification of lego bricks on [Lego dataset from kaggle](https://www.kaggle.com/joosthazelzet/lego-brick-images/kernels).


### Quick description of python scripts:

* **ImageInfo.py:**

   Basicly just information about image size and pixel value interval
  
* **SeparatingTypes.py:**
  
  There is 50 types of bricks in dataset I've used this script to separate types I wanted to use
  
* **ResizeImages.py:**
  
  Script for resizing images
  
* **LoadAndSaveToH5.py:**
  
  Loads images assings them labels and saves to H5 format
  
* **LoadExpandSaveRWImages.py:**
  
  I've hand picked 100 real world images and expanded the dataset to 1000 using data augmentation
  


