import queue
import os
import time
from PIL import Image, ImageEnhance

# Initialisation des files d'attente
queue_chargement = queue.Queue()
queue_traitement = queue.Queue()
queue_sauvegarde = queue.Queue()
DOSSIER_SORTIE = "images_output_v2"
NBR_IMAGES = 10


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
        image, i = queue_traitement.get() # On va chercher l'image suivante

        # Conversion en niveaux de gris manuelle
        grayscale_image = Image.new("L", (new_width, new_height))
        for x in range(new_width):
            for y in range(new_height):
                r, g, b = image.getpixel((x % 100, y % 100))
                gray = int(0.3 * r + 0.59 * g + 0.11 * b)
                grayscale_image.putpixel((x, y), min(int(gray * 1.5), 255))
        
        # Ajustement manuel de luminosité

        # Ajout de l'image traitée dans la queue d'instructions
        queue_sauvegarde.put((grayscale_image, i))


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
