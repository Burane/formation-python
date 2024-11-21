import queue
import os
import time
from PIL import Image, ImageEnhance, ImageOps 

# Initialisation des files d'attente
queue_chargement = queue.Queue()
queue_traitement = queue.Queue()
queue_sauvegarde = queue.Queue()
DOSSIER_SORTIE = "images_output_v3"
NBR_IMAGES = 1000


# Fonction de chargement d'images
def charger_images():
    """Charge les images en mémoire."""
    for i in range(NBR_IMAGES):
        image = Image.new("RGB", (100, 100), (i * 20, i * 20, i * 20))  # Création d'une image de test
        queue_traitement.put((image, i)) # Ajout de l'image générée ("chargée") dans la queue d'instructions.


# Fonction de traitement d'images (moins optimisée)
def traiter_images():
    """Traite les images pixel par pixel."""
    new_width = 250
    new_height = 250
    while not queue_traitement.empty(): # Tant qu'il reste des images à traiter
        data: tuple[Image.Image, int] = queue_traitement.get()
        image, i = data

        image = image.resize((new_height, new_width))
        
        image = ImageOps.grayscale(image)
        image = ImageEnhance.Brightness(image).enhance(1.5)

        # Ajout de l'image traitée dans la queue d'instructions
        queue_sauvegarde.put((image, i))


# Fonction de sauvegarde des images
def sauvegarder_images():
    """Sauvegarde les images dans un dossier."""
    if not os.path.exists(DOSSIER_SORTIE):
        os.makedirs(DOSSIER_SORTIE)
    while not queue_sauvegarde.empty(): # Tant qu'il reste des images à traiter
        image, i = queue_sauvegarde.get() # Ajout de l'image générée ("chargée") dans la queue d'instructions.
        filename = os.path.join(DOSSIER_SORTIE, f"image_{i}_{time.time()}.png")
        image.save(filename)


# Exécution du pipeline
charger_images()
traiter_images()
sauvegarder_images()
