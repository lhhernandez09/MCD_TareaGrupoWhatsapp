# MCD_TareaGrupoWhatsapp

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Análisis exploratorio de datos dsobre mensajes de un grupo de whatsapp

## Ejecutar la libreta

La libreta principal se encuentra en `notebooks/main.ipynb`. Requiere Python
3.13.2, según se define en `pyproject.toml`.

1. Clona el repositorio y entra al directorio del proyecto.

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd MCD_TareaGrupoWhatsapp
   ```

2. Crea y activa un entorno virtual.

   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

   En Windows, actívalo con:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Instala las dependencias del proyecto.

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

4. Abre `notebooks/main.ipynb` desde VS Code con la extensión de Jupyter, o
   instala JupyterLab y ejecútalo desde la raíz del proyecto:

   ```bash
   python -m pip install jupyterlab
   python -m jupyter lab
   ```

5. En la libreta, selecciona el intérprete del entorno `.venv` y ejecuta las
   celdas en orden, de arriba hacia abajo. La primera celda descarga el modelo
   de español de spaCy (`es_core_news_sm`).

6. La celda `%run ../conf/conf.py` descarga el archivo del chat desde OneDrive
   y lo guarda como `data/raw/chat.txt`. Se necesita conexión a Internet y
   acceso al enlace configurado en `conf/conf.py`. El archivo de chat no se
   incluye en el repositorio por contener información privada.

Al terminar la fase de preparación, se genera el archivo anonimizado
`data/processed/chat_anonimizado.csv`. Las celdas posteriores realizan el
análisis exploratorio y muestran las gráficas.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── dataßß
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         mcd_tareagrupowhatsapp and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── mcd_tareagrupowhatsapp   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes mcd_tareagrupowhatsapp a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------
