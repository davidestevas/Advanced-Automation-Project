# Advanced Automation Project Structure

*A logical, reasonably standardized, but flexible project structure for doing and sharing work. (based on [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/))*

This repository contains the base structure for Advanced Automation project. In a near future, your thesis can also use this structure to make your work available for contributions from other authors. 

Please follow the folder structure presented as close as you can. As all projects have different requirements, you will probably have to change the structure a bit to fit your needs.

### Folder structure

The directory structure of your new project looks like this (please adjust the structure and its description to best fit your project): 

```
├── README.md          <- The top-level README for contributers of this project.
│
├── data
│   ├── raw            <- The original, immutable data dump.
│   ├── interim        <- Intermediate data that has been transformed.
│   └── processed      <- The final, canonical data sets for modeling.
│
├── docs               <- Documents
│   ├── reports        <- Generated analysis as HTML, PDF, LaTeX, DOCX etc.
│   ├── figures        <- Generated graphics and figures to be used in reporting
│   └── project/thesis <- Project/Thesis source files
│       └── templates  <- Templates (if available)
│
├── references         <- Articles, books and other references used in your project. It is good practice to  
|                         reference these materials in the comments of your code.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering), the creator's  
|                         initials, and a short `-` delimited description, e.g. `1.0-aa-initial-data-exploration`.
│
├── requirements.txt   <- The file with instructions for reproducing the project environment (software).  
|                         Indicates the version of  software you are using. If using Python, you can do 
|                         `pip freeze > requirements.txt`  to generate a list with the version of the 
|                         different packages you use
│
├── code               <- Source code for use in this project.
|    ├── data          <- Scripts to download, generate and process data
|    │   └── make_dataset.py/m
|    │   └── process_dataset.py/m
|    │
|    ├── algorithms    <- Functions to create models, run models, optization algorithms, etc.
|    │
|    ├── results       <- Scripts to apply the algorithms and obtain the results of your project
|    │
|    └── visualization <- Scripts and functions for visualizations
|
└── laboratory         <- Laboratory classes (add only the necessary files)
     ├── L1_Git        <- Github
     ├── L2_GCollab    <- Cloud Computing: Google Collab
     ├── L3_DB         <- Databases and SQL Query
     └── L4_Arduino    <- Hardware implementation: Arduino
```


### Readme file

This file, `README.md`, should be used to include all information on the files included in the project and how to make them work.

It makes use of Markdown, which is a markup language focused on readability. You can find information on the main syntax of Markdown in:

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Markdown Basics Guide](https://markdown-guide.readthedocs.io/en/latest/basics.html)

Multiple text editors, such as Visual Studio Code, Sublime Text, Atom, Notepad++ have extensions that you can install to transform the Markdown file (.md) into a .pdf or .html.

# Predictive Maintenance for Turbofan Engines (NASA C-MAPSS)
### Advanced Automation (2025/26) - Group 28

## 1. Project Overview
This project focuses on **Data Analysis** and **Predictive Maintenance**, aiming to predict the **Remaining Useful Life (RUL)** of turbofan engines using sensor data. The project was developed as part of the Advanced Automation course (1st year MEMec).

We compare different machine learning approaches—ranging from simple linear baselines to advanced Deep Learning methods—to handle complex operational conditions and failure modes.

**Dataset:** [NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation)](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data)
* **FD001:** Simple (Sea Level, 1 Fault)
* **FD002:** Complex (6 Operating Conditions, 1 Fault)
* **FD003:** Medium (Sea Level, 2 Faults)
* **FD004:** Hard (6 Operating Conditions, 2 Faults)

## 2. Project Structure
The project follows a structured engineering approach, separating data, experimental notebooks, and modular production code.

```text
├── data
│   ├── raw            <- Original immutable data (train_FDxxx.txt, test_FDxxx.txt)
│   └── processed      <- Canonical data sets for modeling (processed CSVs)
│
├── docs               <- Documentation and Reports
│   ├── reports        <- Final Project Report (PDF)
│   └── figures        <- Generated graphics (Comparison Charts, Loss Curves)
│
├── references         <- Explanatory materials and manuals
│   ├── Damage Propagation Modeling.pdf    <- NASA technical explanation of the data
│   ├── readme.txt                         <- Original dataset documentation
│   └── AA 2526 Group Project Instructions.pdf
│
├── notebooks          <- Jupyter Notebooks for Exploration & Analysis
│   ├── 1.0-aa-initial-exploration.ipynb    <- Data Loading & Feature Selection
│   ├── 2.0-aa-linear-baseline.ipynb        <- Method 1: Linear Regression
│   ├── 3.0-aa-random-forest.ipynb          <- Method 2: Random Forest
│   ├── 4.0-aa-lstm-deep-learning.ipynb     <- Method 3: LSTM (Deep Learning)
│   ├── 5.0-aa-svr-method.ipynb             <- Method 4: SVR
│   └── 6.0-aa-final-comparison.ipynb       <- Visualizing final results
│
├── code               <- Modular Source Code (Production Pipeline)
│   ├── algorithms     
│   │   └── models.py           <- Architecture definitions for LSTM, RF, and SVR
│   ├── data           
│   │   └── make_dataset.py     <- Scripts to load, clean, and engineer features
│   └── visualization  
│       └── plot_results.py     <- Standardized plotting functions
│
├── requirements.txt   <- Dependencies for reproducing the environment
└── README.md          <- Project documentation
