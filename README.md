# 🌱 Smart Plant Growth Monitoring and Prediction System

## 📌 Project Overview

The Smart Plant Growth Monitoring and Prediction System is a machine learning-based web application designed to monitor plant growth and predict new plant growth based on environmental and plant-related inputs.

The system allows users to enter plant details, monitor growth conditions, view prediction results, and track previous predictions.

## 🎯 Objectives

- Monitor plant growth conditions.
- Predict new plant growth using Machine Learning.
- Visualize plant-related data through charts.
- Store and display prediction history.
- Provide a simple and user-friendly web interface.

## ✨ Features

- Plant details input.
- Machine Learning-based growth prediction.
- Plant name management.
- Interactive data visualizations.
- Prediction history.
- SQLite database integration.
- Web-based user interface.

## 🛠️ Technologies Used

| Component | Technologies |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Machine Learning | Scikit-learn, Linear Regression |
| Data Processing | Pandas |
| Data Visualization | Matplotlib |
| Database | SQLite |
| Development Tools | VS Code, Jupyter Notebook |
| Version Control | Git, GitHub |

## 📂 Project Structure

```text
Plant-Growth-Monitoring-System/
│
├── app.py
├── model/
│   ├── plant_growth_model.pkl
│   └── feature_names.pkl
│
├── templates/
│   └── index.html
│
├── dataset/
├── docs/
├── static/
├── visualizations/
│
├── check_dataset.py
├── check.ipynb
├── cleaning.ipynb
├── data_visualization.ipynb
├── machine_learning.ipynb
├── statistics_analysis.ipynb
│
├── cleaned_plant_growth.csv
├── plant growth dataset.csv
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/chevalakiranmaics25-stack/plant-growth-monitoring-system.git
```

### 2. Open Project Folder

```bash
cd plant-growth-monitoring-system
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000
```

## 🤖 Machine Learning

- Algorithm: Linear Regression
- Target Variable: `New_Growth_Count`
- Input: Plant growth and environmental parameters.
- Output: Predicted new growth count.

The prediction is an estimate based on the trained dataset and model.

## 🗄️ Database

SQLite is used to store plant prediction details, including:

- Plant Name
- Plant Height
- Leaf Count
- Temperature
- Humidity
- Soil Moisture
- Predicted Growth
- Prediction Date

## 👩‍💻 Project Information

**Project Name:** Smart Plant Growth Monitoring and Prediction System

**GitHub Repository:**  
https://github.com/chevalakiranmaics25-stack/plant-growth-monitoring-system

## 📜 License

This project is developed for academic and educational purposes.