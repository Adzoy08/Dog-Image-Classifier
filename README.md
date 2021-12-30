# DOG IMAGE CLASSIFIER
## USE A PRE-TRAINED IMAGE CLASSIFIER TO IDENTIFY DOG BREEDS
By: S. D. Boadi

***
## Table of Contents
1. Project Overview
2. File Descriptions
3. Specifications
4. CNN Model Architectures
5. How To Run The Program
6. Expected Results
---
## Project Overview
A project work submitted to [Udacity](https://www.udacity.com/ "Udacity Home") in partial fulfillment of the requirements for the nanodegree in AI Programming with Python.
The project was to showcase my Python skills by coding with three different pre-trained image classifiers. 

---
## File Descriptions
* _dognames.txt_ contains the names of dog breeds.
* _uploaded_images_ folder contains the images to be classified.
* The codes were splitted into different python files.

---
## Specifications
The image in the uploaded_images for classification should have an aspect ratio of 1:1.
You should have Python 3.7 or above installed.

---
## CNN Model Architectures
The three Convolutional Neural Network model architectures that can be used for the classification are AlexNet, ResNet and VGG.
The three model architectures were all used to classify the dog images in the "pet_images" folder. The table below provides the summary of the results using each of the model architecture:

All model architectures accurately classified dog images and not dog images.
| | |
|----|----|
|   Total Images  |  40  |
|    Dog Images   |  30  |
| Not Dog Images  |  10  |

Time taken to classify the images
| | | | |
|----|----|----|----| 
|CNN MODEL ARCHITECTURE|AlexNet|ResNet|VGG|
|TIME TAKEN|0:0:2|0:0:3|0:0:33|

| | | | |
|----|----|----|----|
|CNN MODEL ARCHITECTURE|% Dogs Correct|% Breed Correct|% Not Dog Correct|% Match Labels|
|AlexNet|100.0%|80.0%|100.0%|75.0%|
|ResNet|100.0%|90.0%|90.0%|82.5%|
|VGG|100.0%|93.3%|100.0%|87.5%|

---
## How To Run The Program
Run the check_images.py file
```
python check_images.py --dir uploaded_images --arch vgg --dogfile dognames.txt
```
alexnet or resnet can be used in place of vgg. <br />
`--dir uploaded_images --arch vgg --dogfile dognames.txt` when not provided will still run with the same arguments as default. 

---
## Expected Results
The application identifies the image whether it is a dog image or not. If it is a dog image, it then identifies the dog breed and provide an estimate of the dog breed that is most resembling.