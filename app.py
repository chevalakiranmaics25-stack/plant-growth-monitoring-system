from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3
import pandas as pd

app = Flask(__name__)

model = joblib.load("model/plant_growth_model.pkl")
features = joblib.load("model/feature_names.pkl")


# Database Creation
def create_database():

    conn = sqlite3.connect("plant_data.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS plant_predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plant_height REAL,
            leaf_count INTEGER,
            temperature REAL,
            humidity REAL,
            soil_moisture REAL,
            predicted_growth REAL,
            prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor = conn.cursor()

    # Check whether plant_name column exists
    cursor.execute("PRAGMA table_info(plant_predictions)")
    columns = [row[1] for row in cursor.fetchall()]

    # Add plant_name column to existing database
    if "plant_name" not in columns:
        cursor.execute("""
            ALTER TABLE plant_predictions
            ADD COLUMN plant_name TEXT
        """)

    conn.commit()
    conn.close()


create_database()


# Home Route
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    if not data:
        return jsonify({"error": "No input data received"}), 400

    plant_name = str(data.get("plant_name", "")).strip()

    if not plant_name:
        return jsonify({"error": "Please enter plant name"}), 400

    input_data = {feature: 0 for feature in features}

    numeric_fields = [
        "Height_cm",
        "Leaf_Count",
        "Watering_Amount_ml",
        "Watering_Frequency_days",
        "Room_Temperature_C",
        "Humidity_%",
        "Fertilizer_Amount_ml",
        "Soil_Moisture_%"
    ]

    for field in numeric_fields:

        if field not in data:
            return jsonify({"error": "Missing field: " + field}), 400

        input_data[field] = float(data[field])

    category_fields = [
        "Soil_Type",
        "Fertilizer_Type",
        "Pest_Severity",
        "Sunlight_Exposure",
        "Pest_Presence"
    ]

    for field in category_fields:

        if field not in data:
            return jsonify({"error": "Missing field: " + field}), 400

        column = field + "_" + data[field]

        if column in input_data:
            input_data[column] = 1
        else:
            return jsonify({"error": "Invalid category: " + column}), 400

    df = pd.DataFrame([input_data], columns=features)

    prediction = model.predict(df)

    # Save Prediction in Database
    conn = sqlite3.connect("plant_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO plant_predictions
        (plant_height, leaf_count, temperature, humidity,
         soil_moisture, predicted_growth, plant_name)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        float(data["Height_cm"]),
        int(data["Leaf_Count"]),
        float(data["Room_Temperature_C"]),
        float(data["Humidity_%"]),
        float(data["Soil_Moisture_%"]),
        float(prediction[0]),
        plant_name
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "predicted_new_growth_count": round(float(prediction[0]), 2),
        "plant_name": plant_name
    })


# Prediction History Route
@app.route("/history")
def history():

    conn = sqlite3.connect("plant_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM plant_predictions
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    conn.close()

    return jsonify(records)


if __name__ == "__main__":
    app.run(debug=True)