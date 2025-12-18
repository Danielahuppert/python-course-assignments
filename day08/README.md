# Day 08 – Heart Disease Data Analysis

## Overview
In this project, I analyzed a heart disease dataset to explore relationships between clinical features and the presence of heart disease.  
The analysis focuses on data exploration and visualization using **Pandas**, **NumPy**, and **Matplotlib**.

The goal was to perform an interesting analysis and create clear visualizations, rather than building a predictive model.

---

## Dataset
The dataset used is **Heart Disease Prediction**, which contains medical information for 270 patients.

Features include:
- Age
- Sex
- Blood pressure (BP)
- Cholesterol
- Chest pain type
- Maximum heart rate
- Exercise-induced angina
- Other clinical measurements

Target variable:
- **Heart Disease** (`Presence` / `Absence`)

---

## Project Structure
day08/
├── Heart_Disease_Prediction.csv
├── analysis.ipynb
└── README.md

yaml
Copy code

---

## Libraries Used
- pandas
- numpy
- matplotlib

To install the required libraries:
```bash
pip install -r requirements.txt
Analysis Performed
The following analyses were performed in the Jupyter Notebook:

Distribution of heart disease cases (presence vs absence)

Heart disease distribution by sex

Age distribution of patients

Comparison of age between patients with and without heart disease

Comparison of maximum heart rate between patients with and without heart disease

Relationship between chest pain type and heart disease

Correlation analysis between numerical features using a correlation heatmap

Visualizations
Several types of plots were created:

Bar plots

Histograms

Boxplots

Correlation heatmap

These visualizations help highlight trends and relationships between clinical variables and heart disease.

Key Observations:
Heart disease occurrence differs between sexes.

Patients with heart disease tend to show different age and maximum heart rate distributions.

Certain chest pain types are more strongly associated with heart disease.

Correlation analysis reveals relationships between numerical clinical features.

How to Run:
1.Make sure the dataset file is in the same folder as the notebook.

2.Open analysis.ipynb in VS Code or Jupyter.

3.Run the notebook cells from top to bottom