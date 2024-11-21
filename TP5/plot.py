import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Générer des valeurs pour x
x = np.linspace(0.1, 10, 400)  # Utilisation de 0.1 pour éviter log(0)

# Créer un DataFrame Pandas avec x comme données d'entrée
data = pd.DataFrame({"x": x})

# Définir les fonctions pour chaque courbe
data['y_linear'] = data['x']  # f(x) = x
data['y_logarithmic'] = np.log(data['x'])  # f(x) = log(x)
data['y_square'] = data['x']**2  # f(x) = x^2
data['y_cubic'] = data['x']**3  # f(x) = x^3

# Appliquer une régression linéaire pour la courbe linéaire (f(x) = x)
# Nous voulons prédire y_linear à partir de x

X = data[['x']]  # Les valeurs de x
y = data['y_linear']  # Les valeurs de y_linear

# Créer un modèle de régression linéaire
model = LinearRegression()
model.fit(X, y)

# Prédire les valeurs linéaires basées sur le modèle
data['y_linear_pred'] = model.predict(X)

# Créer une figure avec 2x2 sous-graphiques
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Tracer chaque courbe sur un subplot différent

# Courbe linéaire avec régression
axes[0, 0].plot(data['x'], data['y_linear'], label="Linéaire (f(x) = x)", color="blue")
axes[0, 0].plot(data['x'], data['y_linear_pred'], label="Régression linéaire", linestyle='--', color="black")
axes[0, 0].set_title("Linéaire (f(x) = x) avec Régression")
axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("f(x)")
axes[0, 0].legend()
axes[0, 0].grid(True)

# Courbe logarithmique
axes[0, 1].plot(data['x'], data['y_logarithmic'], label="Logarithmique (f(x) = log(x))", color="green")
axes[0, 1].set_title("Logarithmique (f(x) = log(x))")
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("f(x)")
axes[0, 1].grid(True)

# Courbe carrée
axes[1, 0].plot(data['x'], data['y_square'], label="Carrée (f(x) = x^2)", color="red")
axes[1, 0].set_title("Carrée (f(x) = x^2)")
axes[1, 0].set_xlabel("x")
axes[1, 0].set_ylabel("f(x)")
axes[1, 0].grid(True)

# Courbe cubique
axes[1, 1].plot(data['x'], data['y_cubic'], label="Cubique (f(x) = x^3)", color="purple")
axes[1, 1].set_title("Cubique (f(x) = x^3)")
axes[1, 1].set_xlabel("x")
axes[1, 1].set_ylabel("f(x)")
axes[1, 1].grid(True)

# Ajuster l'espacement entre les sous-graphes
plt.tight_layout()

# Afficher le graphique
plt.show()