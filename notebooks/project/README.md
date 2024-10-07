<h1 align="center">
  <br>
  <b>Econometría MCD - Análisis del consumo de gasolina</b>
</h1>


<p align="center">
  <b>Por: González Lara Luis Fernando, Jiménez García Yoseline, Sepúlveda Furber Miguel Enrique y Luis Enrique Noguera Gil</b>
  <br>
</p>

## Objetivo del Proyecto

Desarrollar un modelo econométrico robusto para pronosticar el consumo de combustible de automóviles, utilizando las características propias de cada vehículo en la base de datos de una empresa de automóviles semi nuevos en México.

## Contextualización del Problema

El consumo de gasolina en los automóviles es un tema de gran relevancia en México debido a su impacto directo en diversos aspectos de la vida cotidiana. En este proyecto, exploramos las implicaciones económicas, ambientales y de salud pública del uso de gasolina.

## Tecnologías Utilizadas

- Python 3 ![Python](https://img.shields.io/badge/Python-3.11-blue)

## Requisitos Previos

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Opcional: [Mamba](https://mamba.readthedocs.io/en/latest/)

## Crear entorno

```bash
conda env create -f environment.yml
activate mcd_econometrics
```

o

```
conda install -c conda-forge mamba
mamba env create -f environment.yml
activate mcd_econometrics
```

# Módulos y módulos por defecto

Para instalar los módulos por defecto ubicados en el directorio scripts, utiliza el siguiente comando:

```
pip install --editable .
```

Para más información sobre los módulos del usuario, consulta `install.md`.

# Estructura resultante del directorio
```
├── LICENSE            <- Licencia open-source si se elige una
├── README.md          <- El README principal para desarrolladores que usen este proyecto
├── econ_mod           <- Directorio de módulos del usuario
├── data
│   ├── external       <- Datos de fuentes de terceros.
│   ├── interim        <- Datos intermedios que han sido transformados.
│   ├── processed      <- Conjuntos de datos finales y canónicos para el modelado.
│   └── raw            <- Datos originales e inalterados.
│
├── docs               <- Un proyecto mkdocs por defecto; consulta www.mkdocs.org para más detalles
│
├── models             <- Modelos entrenados y serializados, predicciones del modelo o resúmenes
│
├── notebooks          <- Jupyter notebooks. La convención de nombres es un número (para orden),
│                         las iniciales del creador, y una breve descripción delimitada por `-`, ej.
│                         `1.0-anony-initial-data-exploration`.
│
├── scripts            <- Módulos y scripts por defecto del proyecto
│
├── references         <- Diccionarios de datos, manuales, y todos los demás materiales explicativos.
│
├── reports            <- Análisis generados en HTML, PDF, LaTeX, etc.
│   └── figures        <- Gráficos y figuras generados para ser utilizados en los reportes
│
├── requirements.txt   <- Archivo de requisitos para reproducir el entorno de análisis, ej.
│                         generado con `pip freeze > requirements.txt`
```
