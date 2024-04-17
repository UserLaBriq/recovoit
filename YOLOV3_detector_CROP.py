##Source : https://stackabuse.com/object-detection-with-imageai-in-python/

from imageai.Detection import ObjectDetection
import os

from PIL import Image

import time

#rogne l'image source (input_path) avec les contours (box) pour la sauvegarder vers l'image destination (output_path)
def image_croper(box,input_path,output_path_cropped_image):
    im = Image.open(input_path)
    im1 = im.crop((box[0], box[1], box[2], box[3]))
    im1 = im1.save(output_path_cropped_image) 

#Renvoie les contours autour de la voiture detectée et sauvegarde l'image de la voiture avec les contours :
def detection_voiture(detector, input_path, output_path):
    detections = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path, minimum_percentage_probability=30) #probabilité d'être une voiture >30%
    
    for eachObject in detections:
        #print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        #print("--------------------------------")

        if eachObject["name"] == "car" :
            return eachObject["box_points"]
        
            
execution_path = os.getcwd()
input_path = os.path.join(execution_path , "./input/")
output_path = os.path.join(execution_path , "./output/")

dir_list=os.listdir(input_path)

detector = ObjectDetection()
##YOLOV3
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "./models/yolov3.pt"))
detector.loadModel()

#loading bar 
iteration_image = 0
for file in dir_list :
    input_path_image = input_path+file
    output_path_image = output_path+file
    output_path_cropped_image = output_path+"cropped/"+file

    box_points = detection_voiture(detector,input_path_image,output_path_image)
    
    if box_points is not None : 
        image_croper(box_points,input_path_image,output_path_cropped_image)

    
    iteration_image=iteration_image+1
    print("IMAGE PROCESSED AND CROPPED : "+str(iteration_image)+"/"+str(len(dir_list))+".")
    print("\t-->image name : \""+file+"\".\n")