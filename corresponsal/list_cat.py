import fasttext.util
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.manifold import TSNE

# Cargar modelo de FastText en español
fasttext.util.download_model('es', if_exists='ignore')
ft = fasttext.load_model('cc.es.300.bin')

# 🔹 Cargar las columnas únicas desde el archivo
with open("columnas_unicas.txt", "r", encoding="utf-8") as file:
    columnas = [line.strip() for line in file.readlines()]

#Limpieza: Convertimos a minúsculas y eliminamos palabras comunes
stop_words = ["nombre", "codigo", "usuario", "documento", "fecha", "hora"]
columnas_limpias = [re.sub(r'_|-', ' ', col.lower()) for col in columnas]
columnas_limpias = [' '.join([word for word in col.split() if word not in stop_words]) for col in columnas_limpias]

#Generamos los embeddings con FastText
vector_columnas = np.array([ft.get_sentence_vector(col) for col in columnas_limpias])

#Aplicamos DBSCAN para clustering automático
dbscan = DBSCAN(eps=3.5, min_samples=2, metric='cosine')
clusters = dbscan.fit_predict(vector_columnas)

#Crear DataFrame con los resultados
df_resultado = pd.DataFrame({"Columna": columnas, "Cluster": clusters})
df_resultado = df_resultado.sort_values("Cluster")

# 🔹 Imprimir los resultados
print(df_resultado)

#Visualización con t-SNE
tsne = TSNE(n_components=2, random_state=42)
X_embedded = tsne.fit_transform(vector_columnas)

plt.figure(figsize=(10, 6))
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=clusters, cmap="viridis", alpha=0.7)
for i, txt in enumerate(columnas):
    plt.annotate(txt, (X_embedded[i, 0], X_embedded[i, 1]), fontsize=9)
plt.title("Clusters de Columnas con t-SNE y DBSCAN")
plt.show()
