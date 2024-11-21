import queue
import os
import time
from PIL import Image, ImageEnhance, ImageOps
from concurrent.futures import Future, ThreadPoolExecutor, as_completed

# Initialisation des files d'attente
DOSSIER_SORTIE = "images_output_v5"
NBR_IMAGES = 1000

queue_traitement = queue.Queue()
queue_sauvegarde = queue.Queue()

if not os.path.exists(DOSSIER_SORTIE):
    os.makedirs(DOSSIER_SORTIE)

def generer_image() -> None:
    for i in range(NBR_IMAGES):
        image: Image.Image = Image.new("RGB", (100, 100), (i * 20, i * 20, i * 20))
        queue_traitement.put((image, i))
        
    queue_traitement.put("END")
    


def traiter_images() -> None:
    
    while True:
        
        item = queue_traitement.get()
        
        if(item == "END"):
            queue_sauvegarde.put("END")
            break
        
        image, i = item
        
        new_width: int = 250
        new_height: int = 250
        
        image = image.resize((new_height, new_width))
        image = ImageOps.grayscale(image)
        image = ImageEnhance.Brightness(image).enhance(1.5)
        
        queue_sauvegarde.put((image, i))


def sauvegarder_images() -> None:
    while True:
        item = queue_sauvegarde.get()
        
        if(item == "END"):
            break
        
        image, i = item
        filename = os.path.join(DOSSIER_SORTIE, f"image_{i}_{time.time()}.png")
        image.save(filename)
        
        


# Exécution du pipeline
with ThreadPoolExecutor() as executor:
    executor.submit(generer_image)
    executor.submit(traiter_images)
    executor.submit(sauvegarder_images)
