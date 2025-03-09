from modules.transform.Transformation import employees_by_quarter_db, hired_employees_by_department_db
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
main_path = "resources/data/input"


@app.route("/upload_csv", methods=["POST"])
def upload_csv():
    if "file" not in request.files:
        return jsonify({"error": "No se encontró el archivo"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Nombre de archivo no válido"}), 400

    if file.filename == "departments.csv":
        filepath = os.path.join(main_path, "departments", file.filename)
    elif file.filename == "hired_employees.csv":
        filepath = os.path.join(main_path, "employees", file.filename)
    elif file.filename == "Jobs.csv":
        filepath = os.path.join(main_path, "jobs", file.filename)

    file.save(filepath)

    return jsonify({"message": f"Archivo guardado en {filepath}"}), 200


@app.route("/employees_by_quarter", methods=["GET"])
def get_employees_by_quarter():
    result_df = employees_by_quarter_db(main_path)
    return jsonify(result_df.to_dict(orient="records"))


@app.route("/hired_employees", methods=["GET"])
def get_hired_employees_by_department():
    result_df = hired_employees_by_department_db(main_path)
    return jsonify(result_df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
