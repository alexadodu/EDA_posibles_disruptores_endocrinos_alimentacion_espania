# 🧪 Lo que el etiquetado de un alimento no te dice

### Análisis Exploratorio de Datos (EDA) para la detección de posibles disruptores endocrinos en la industria alimentaria en España

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Logistic_Regression-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 📋 Descripción del Proyecto

El consumidor actual confía en las etiquetas nutricionales frontales (**Nutri-Score**), sellos ecológicos (**Eco-Score**) y reclamos de marketing (*Zero Azúcar*, *Light*, *Vegano*, *Sin Gluten*) creyendo que toma decisiones saludables. Sin embargo, existe una **exposición invisible** a compuestos químicos añadidos industrialmente que actúan como **Disruptores Endocrinos (DEs) y posibles DEs**.

Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** y modelado estadístico sobre un catálogo de **más de 330,000 productos alimentarios** del mercado español extraídos de *Open Food Facts*, con el objetivo de auditar el fenómeno del *Health Washing* y demostrar qué factores estructurales realmente determinan la presencia de aditivos bajo sospecha hormonal.

---

## 🎯 Hipótesis y Hallazgos Principales

**1. El verdadero motor es el procesamiento (NOVA vs. Nutri-Score):**

* *Resultado:* **Parcialmente confirmada. Nutri-Score evalúa macronutrientes y actúa como un "espejismo": los ultraprocesados (**NOVA 4**) con calificación **Nutri-Score A** alcanzan un **35.4% de prevalencia de DEs**. Los modelos de regresión logística (*statsmodels*) confirman que el grado de procesamiento multiplica exponencialmente el riesgo ($p < 0.001$).**

***2. Sostenibilidad no equivale a seguridad química (Eco-Score):***

* *Resultado:* **Confirmada.** Tener una buena calificación ambiental (Eco-Score A-plus/A/B) no exime al alimento de contener aditivos de riesgo endocrino en categorías como bebidas o lácteos.

***3. La trampa de los reclamos comerciales (*Health Washing*):***

* *Resultado:* **Parcialmente confirmada.** Etiquetas como *"Zero Azúcar"* o *"Light"* disparan el riesgo de contener edulcorantes y aditivos sospechosos (con un Odds Ratio de hasta **7.88x** en *Zero Azúcar*, alcanzando el **67.4%** de prevalencia en bebidas). Ocurre lo contrario con etiquetas "*Plant-based*".

***4. Un problema estructural del modelo industrial (Marcas):***

* *Resultado:* **Confirmada.** La presencia de DEs depende del nivel de ultraprocesamiento (NOVA 4) y no del tipo de fabricante, afectando de manera transversal tanto a marcas de fabricante como a marcas de distribución (marca blanca).

---

## 🗂️ Estructura del Repositorio

El código y la documentación siguen una arquitectura modular para facilitar su reproducibilidad y lectura:

```text
├── src/
│   ├── data/               # Datasets procesados y diccionarios toxicológicos (los archivos pesados se enlazan externamente)
│   ├── dataframes/         # Dataframes generados a raíz de los notebooks (guardando cada cambio)
│   ├── notebooks/          # Notebooks exploratorios y pruebas de contraste de hipótesis
│   └── utils/              # Módulos auxiliares, limpieza de texto (regex) y diccionario de variables (variables.py)
├── memoria/                # Memoria ejecutiva del proyecto (PDF / Documento técnico)
├── presentacion/           # Presentación visual de resultados
└── README.md               # Documentación principal del repositorio
```

---

## 🛠️ Metodología y Pipeline de Datos

1. **Extracción Optimizada (*Chunking*):** Lectura por bloques (`chunksize = 100,000`) de la base de datos global de *Open Food Facts* y filtrado geográfico para España, consolidando **+330,000 registros**.
2. **Ingeniería de Variables (*Feature Engineering*):**
   * Mapeo mediante expresiones regulares (*regex*) de aditivos e ingredientes catalogados como DEs o posibles DEs (colorantes como Eritrosina y Tartrazina, parabenos, antioxidantes sintéticos BHA/BHT/TBHQ y edulcorantes como Aspartamo, Sucralosa y Acesulfamo K) creando el target binario `tiene_algun_DE`.
   * Unificación y normalización de reclamos frontales en `etiquetas_combinadas` y limpieza de fabricantes en `marca`.
3. **Análisis Estadístico y Visualización:**
   * Pruebas de independencia **Chi-cuadrado ($\chi^2$)**.
   * Modelos de **Regresión Logística Multivariante** (`statsmodels`) para aislar variables y calcular **Odds Ratios (OR)** e intervalos de confianza.

---

## 💡 Propuesta de valor

* **Apps de Escaneo y Salud (tipo Yuka / Open Food Facts):** Integración de alertas preventivas de toxicidad industrial basadas en el binomio *NOVA 4 + Riesgo de DEs*.

---

## 🧰 Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Manipulación y Limpieza de Datos:** `pandas`, `numpy`, `re`
* **Análisis Estadístico:** `scipy.stats`, `statsmodels`
* **Visualización de Datos:** `matplotlib`, `seaborn`

---

## ✒️ Autoría

* **Alexandra Dodu** — *Data Science Bootcamp (The Bridge)*
