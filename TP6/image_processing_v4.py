import queue
import os
import time
from PIL import Image, ImageEnhance, ImageOps
from concurrent.futures import Future, ThreadPoolExecutor, as_completed

# Initialisation des files d'attente
DOSSIER_SORTIE = "images_output_v4"
NBR_IMAGES = 1000

if not os.path.exists(DOSSIER_SORTIE):
    os.makedirs(DOSSIER_SORTIE)

def generer_image(i: int) -> tuple[Image.Image, int]:
    image: Image.Image = Image.new("RGB", (100, 100), (i * 20, i * 20, i * 20))
    return (image, i)


def traiter_images(item: tuple[Image.Image, int]) -> tuple[Image.Image, int]:
    image, i = item
    
    new_width: int = 250
    new_height: int = 250
    
    image = image.resize((new_height, new_width))
    image = ImageOps.grayscale(image)
    image = ImageEnhance.Brightness(image).enhance(1.5)
    
    return (image, i)


def sauvegarder_images(item: tuple[Image.Image, int]):
    image, i = item
    filename = os.path.join(DOSSIER_SORTIE, f"image_{i}_{time.time()}.png")
    image.save(filename)


# Exécution du pipeline
with ThreadPoolExecutor() as executor:
    gen_img_future = [executor.submit(generer_image, i) for i in range(NBR_IMAGES)]
    
    gen_imgs = [future.result() for future in gen_img_future]
    
    traiter_images_future = [executor.submit(traiter_images, img) for img in gen_imgs]

    treated_imgs = [future.result() for future in traiter_images_future]
    
    sauvegarder_images_future = [executor.submit(sauvegarder_images, img) for img in treated_imgs]
    
    for future in sauvegarder_images_future:
        future.result()

