     ***  USE A PRE-TRAINED IMAGE CLASSIFIER TO IDENTIFY DOG BREEDS  ***

The three CNN model architectures that can be used for the classification are AlexNet, ResNet and VGG.

The three model architectures were all used to classify the dog images in the "pet_images" folder. The table below provides the summary of the results using each of the model architecture:

All model architectures accurately classified dog images and not dog images.
--------------------------+
|  # Total Images  |  40  |
+-------------------------+
|   # Dog Images   |  30  |
+-------------------------+
|# Not Dog Images  |  10  |
+-------------------------+

Time taken to classify the images
+------------------------------------------------------+
| CNN MODEL ARCHITECTURE | AlexNet |  ResNet |   VGG   |
+------------------------------------------------------+
|       TIME TAKEN       |  0:0:2  |  0:0:3  |  0:0:33 |
+------------------------------------------------------+

+-------------------------------------------------------------------------+
|                        |  % Dogs  |  % Breed  |  % Not Dog  |  % Match  |
| CNN MODEL ARCHITECTURE |  Correct |  Correct  |   Correct   |   Labels  |
+-------------------------------------------------------------------------+
|                AlexNet |  100.0%  |   80.0%   |    100.0%   |    75.0%  |
+--------------------------------------------------------------------------
|                 ResNet |  100.0%  |   90.0%   |     90.0%   |    82.5%  |
+--------------------------------------------------------------------------
|                    VGG |  100.0%  |   93.3%   |    100.0%   |    87.5%  |
+-------------------------------------------------------------------------+

Based on the results above, VGG is the best model architecture even though it spent more 
time to classify the images (30 seconds more than the rest of the models).
AlexNet and VGG correctly identify the dog images and not dog images 100% of the time.
VGG provides the best solution since it identifies the correct breed of dogs over 90%
of the time and match labels was over 87.5%. 


