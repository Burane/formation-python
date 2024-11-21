import subprocess
import time

# Nom du script Python à tester
SCRIPT_PYTHON = "TP6/image_processing_v1.py"
# Nombre d'exécutions pour calculer la moyenne
NBR_EXECUTIONS = 10

# Initialisation de la variable pour stocker le temps total
total_time = 0.0

print(f"Mesure du temps d'exécution pour {SCRIPT_PYTHON} sur {NBR_EXECUTIONS} exécutions...")

for i in range(1, NBR_EXECUTIONS + 1):
    # Démarre le chronomètre
    start_time = time.time()

    # Exécute le script Python et attend sa terminaison
    subprocess.run(["python", SCRIPT_PYTHON])

    # Calcule la durée de l'exécution
    end_time = time.time()
    duration = end_time - start_time

    print(f"Exécution {i} : {duration:.4f} secondes")

    # Additionne la durée au temps total
    total_time += duration

# Calcul de la moyenne du temps d'exécution
average_time = total_time / NBR_EXECUTIONS

# Affiche le résultat
print(f"\nTemps d'exécution moyen sur {NBR_EXECUTIONS} exécutions : {average_time:.4f} secondes")