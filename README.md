# # EDA — Encuesta de Lectores

## Ver EDA interactivo online
https://f83292a0-a6b7-4fe4-b035-986d562d930b.plotly.app

Análisis exploratorio de datos (EDA) sobre los hábitos de lectura en España (2024), con datos de la encuesta “Radiografía de la lectura en el siglo XXI” realizada por 40dB.

El proyecto combina:
- Análisis descriptivo y limpieza de datos en Python (Jupyter Notebook)
- Visualización interactiva mediante Plotly Dash

---

## Descripción
El objetivo es identificar los motivos por los que los lectores leen menos libros que hace una década.  
Los resultados se presentan en una aplicación interactiva con gráficos de barras, porcentajes y análisis por generación.

---

## Tecnologías
| Librería | Uso principal |
|-----------|----------------|
| Pandas | Limpieza y análisis de datos |
| NumPy | Cálculos y operaciones numéricas |
| Plotly Dash | Visualización web interactiva |
| Matplotlib / Seaborn | Análisis gráfico en el notebook |
| Jupyter Notebook | Entorno de desarrollo y documentación |

---

## Archivos principales
EDA_Arturo_Puig.ipynb     → Notebook con el análisis EDA
app.py                     → Aplicación web interactiva (Dash)
lectores_preparado.csv     → Dataset limpio para la app

---

## Ejecución local

# Instalar dependencias
pip install pandas numpy matplotlib seaborn plotly dash

# Ejecutar la aplicación
python3 app.py

Abre en el navegador:
http://127.0.0.1:8050/

Visualizaciones incluidas
	•	Gráfico circular: distribución de respuestas
	•	Ranking horizontal: motivos principales de desinterés lector
	•	Comparativa generacional
	•	Interpretación y resumen textual

Fuente

Encuesta “Radiografía de la lectura en el siglo XXI”
Noviembre 2024 — España
https://ladespensa.40db.es/

Autor

Arturo Puig
Valencia, España — 2025
Desarrollado con Python, Pandas y Plotly Dash.