from modules.transform.Transformation import employees_by_quarter, hired_employees_by_department
from flask import Flask, jsonify

app = Flask(__name__)
main_path = "resources/data/input"


@app.route("/employees_by_quarter", methods=["GET"])
def get_employees_by_quarter():
    result_df = employees_by_quarter(main_path)
    return jsonify(result_df.to_dict(orient="records"))


@app.route("/hired_employees", methods=["GET"])
def get_hired_employees_by_department():
    result_df = hired_employees_by_department(main_path)
    return jsonify(result_df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
