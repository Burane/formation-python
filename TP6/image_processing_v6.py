import queue
import os
import time
from PIL import Image, ImageEnhance, ImageOps
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
import threading

# Initialisation des files d'attente
DOSSIER_SORTIE = "images_output_v6"
NBR_IMAGES = 1000

queue_traitement = queue.Queue()
queue_sauvegarde = queue.Queue()

a = "d"*10000000

global_counter = 0
threadLock = threading.Lock()

if not os.path.exists(DOSSIER_SORTIE):
    os.makedirs(DOSSIER_SORTIE)


def generer_image() -> None:
    global global_counter
    
    while True:
        with threadLock:
            if global_counter >= NBR_IMAGES:
                queue_traitement.put("END")
                break
            i = global_counter
            global_counter += 1

        image: Image.Image = Image.new("RGB", (100, 100), (i * 20, i * 20, i * 20))
        queue_traitement.put((image, i))




def traiter_images() -> None:

    while True:

        item = queue_traitement.get()

        if item == "END":
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

        if item == "END":
            break

        image, i = item
        filename = os.path.join(DOSSIER_SORTIE, f"image_{i}_{time.time()}.png")
        image.save(filename)


with ThreadPoolExecutor() as executor:
    executor.submit(generer_image)
    executor.submit(traiter_images)
    executor.submit(sauvegarder_images)

    nb_worker = executor._max_workers

    generation_futures = [executor.submit(generer_image) for _ in range(nb_worker)]
        
    processing_futures = [executor.submit(traiter_images) for _ in range(nb_worker)]
    
    saving_futures = [executor.submit(sauvegarder_images) for _ in range(nb_worker)]
    
    for future in generation_futures + processing_futures + saving_futures:
        future.result()