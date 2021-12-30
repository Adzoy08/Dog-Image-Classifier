#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: SAMUEL DUAH BOADI
# DATE CREATED: 16 OCTOBER 2021                                 
# REVISED DATE: 
# PURPOSE: The function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
# 
def get_pet_labels(image_dir = 'pet_images/'):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    The CODE formats the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}
    filename_list = listdir(image_dir)
    pet_labels = listdir(image_dir)
    for i in range(len(pet_labels)):
        #Skips the hidden file in the directory since it's not a pet image.
        if pet_labels[i][0].startswith('.'):
            print('NB: The', pet_labels[i], 'was excluded from the pet label since it\'s a hidden file and not an image to be classified.')
        
        else:
            pet_labels[i] = pet_labels[i].lower()   
            pet_labels[i] = pet_labels[i].replace("_", " ")
            pet_labels[i] = ''.join([n for n in pet_labels[i] if not n.isdigit()])
            pet_labels[i] = pet_labels[i].replace(" .jpg", "")
            
            if filename_list[i] not in results_dic:
                results_dic[filename_list[i]] = [pet_labels[i]]
        
            else:
                print("** Warning: Key=", filename_list[i], "already exists in results_dic with value =", results_dic[filename_list[i]])

    return results_dic
