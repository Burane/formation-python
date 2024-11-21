from dataclasses import dataclass
import resource
import subprocess
import time
import psutil

PYTHON_PATH = "D:\\Documents\\Projets\\Sinay\\formation-python\\TP6\\venv\\Scripts\\python.exe"
# Nom du script Python à tester
# Nombre d'exécutions pour calculer la moyenne
NBR_EXECUTIONS = 10

@dataclass
class ExecTime:
    name: str
    each: list[float]
    max_memory: list[float]

exec_times: list[ExecTime] = []

for j in range(6,7):
    SCRIPT_PYTHON = f"image_processing_v{j}.py"
    # Initialisation de la variable pour stocker le temps total

    print(f"Mesure du temps d'exécution pour {SCRIPT_PYTHON} sur {NBR_EXECUTIONS} exécutions...")

    exec_time = ExecTime(SCRIPT_PYTHON, [], [])

    for i in range(1, NBR_EXECUTIONS + 1):
        # Démarre le chronomètre
        start_time = time.time()

        # Exécute le script Python et attend sa terminaison
        process = subprocess.Popen([PYTHON_PATH, SCRIPT_PYTHON])
        
        # max_memory = 0
        # try:
        #     # Create a psutil Process object
        #     ps_process = psutil.Process(process.pid)
            
        #     # Monitor memory while process is running
        #     while process.poll() is None:
        #         try:
        #             # Get memory info in MB
        #             memory_info = ps_process.memory_info()
        #             max_memory = max(max_memory, memory_info.rss / (1024 * 1024))
        #             time.sleep(0.01)  # Short sleep to reduce overhead
        #         except psutil.NoSuchProcess:
        #             break
                
                

        # Run your subprocess

        # Check max memory usage after it completes
        max_memory_usage = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024  # Convert KB to MB
        print(f"Maximum memory usage by subprocess: {max_memory_usage:.2f} MB")
                    
        # Wait for process to complete
        process.wait()
        
        # except Exception as e:
        #     print(f"Error tracking memory: {e}")

        # Calcule la durée de l'exécution
        end_time = time.time()
        duration = end_time - start_time
        print(f"\tExécution {i} : {duration:.4f} secondes")
        exec_time.max_memory.append(max_memory_usage)
        exec_time.each.append(duration)
        
    exec_times.append(exec_time)
        
    print(f"Temps d'exécution moyen sur {NBR_EXECUTIONS} exécutions : {sum(exec_time.each) / len(exec_time.each):.4f} secondes")
    

def format_table(headers_values: list[(str, list[str])]) -> str:
    COL_WIDTH = 40
    BORDER_WIDTH = COL_WIDTH + 2

    NUM_COL = len(headers_values)

    top_border = f"┌{'┬'.join(['─' * BORDER_WIDTH for _ in range(NUM_COL)])}┐\n"
    separator = f"├{'┼'.join(['─' * BORDER_WIDTH for _ in range(NUM_COL)])}┤\n"
    bottom_border = f"└{'┴'.join(['─' * BORDER_WIDTH for _ in range(NUM_COL)])}┘\n"
    header = f"│{'│'.join([f' {header[0]:^{COL_WIDTH}} ' for header in headers_values])}│\n"

    data = []
    for i in range(len(headers_values[1][1])):
        values = [x[1][i] for x in headers_values]
        s = f"│{'│'.join( [f' {w:^{COL_WIDTH}} ' for w in values] )}│\n"
        data.append(s)

    return f"{top_border}{header}{separator}{''.join(data)}{bottom_border}"
    
headers = ["Name", "Number execution", "Average execution time", "Max memory usage average"]
values = [
    [e.name for e in exec_times],
    [len(e.each) for e in exec_times],
    [f"{sum(e.each) / len(e.each):.4f}s" for e in exec_times],
    [f"{sum(e.max_memory) / len(e.max_memory):.6f} MB" for e in exec_times],
]
table = format_table(list(zip(headers, values)))

print(table)
    
    

