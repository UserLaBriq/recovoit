# recovoit
Car detector on image and crop

Dans le dossier "models" mettre le modèle souhaité : 
Ici "yolov3.pt" téléchargeable sur https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/

Installer les librairies : 
$ pip install tensorflow
$ pip install opencv-python
$ pip install keras
$ pip install imageAI


Entrer vos images de voiture brutes dans le dossier "input".
Vous pouvez executer le script "YOLOV3_detector_CROP.py" et observer les images avec les rectangles, le pourcentage de probabilité d'être une voiture dans le dossier 
"output" et les images rognées sur la voiture dans le dossier "output/cropped".

@Jul