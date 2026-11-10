import numpy as np

import pyproj

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin  # needs to be installed via pip install flask-cors

from backend import get_mean_value_from_table

app = Flask(__name__)
CORS(app, origins=["*", "null"])  # allowing any origin as well as localhost (null)


@app.route("/welcome_to_flask", methods=["GET"])
def welcome_to_flask():
    print("all good")
    return jsonify({"message": "Welcome!"})


@app.route("/arguments", methods=["GET"])
def working_with_arguments():
    my_argument = str(request.args.get("name", "default_name"))
    return jsonify(f"This is how we pass arguments in GET request. My name is {my_argument}")


@app.route("/add_numbers", methods=["GET"])
def add_numbers():
    try:
        input_value_1 = int(request.args.get("num1", 1))
    except ValueError:
        return jsonify("Invalid input for num1")
    print(f"Received argument 1: {input_value_1}")
    input_value_2 = int(request.args.get("num2", 2))
    print(f"Received argument 2: {input_value_2}")
    new_value = input_value_1 + input_value_2
    return jsonify({"output": new_value})


@app.route("/access_with_javascript", methods=["GET"])
@cross_origin()
def javascript_demo():
    """method to demonstrate how to access this endpoint with javascript"""
    # complex python processing
    response = jsonify("This should be shown on your website")
    return response


@app.route("/using_post", methods=["POST"])
@cross_origin()
def using_post():
    user_profile = request.get_json(force=True)
    print(user_profile)
    output_text = f"The app received data from user {user_profile['username']} and password {user_profile['password']}"
    return jsonify(output_text)

# TODO: TASK 1
@app.route("/round_float", methods=["GET"])
def round_float():
    
    val = (request.args.get("value", 1, type=float))
    new_value = round(val, 2)
    return jsonify({"output": new_value})

# TODO: TASK 2 - one method for increase and one method for decrease value

@app.route("/increase_value", methods=["GET"])
@cross_origin()
def increase_value():
    val = int(request.args.get("curr_val", 0))
    return jsonify(val + 1)

@app.route("/decrease_value", methods=["GET"])
@cross_origin()
def decrease_value():
    val = int(request.args.get("curr_val", 0))
    return jsonify(val - 1)

# TODO TASK 3 - POST method to compute sum of list

@app.route("/compute_sum", methods=["POST"])
@cross_origin()
def compute_sum():
    li = request.get_json(force=True)
    li_sum = sum(li)
    return jsonify(li_sum)

# TODO TASK 4 - compute mean value of a column in a table from a database
@app.route("/compute_mean", methods=["GET"])
def compute_mean():
    # retrieve column name from the request arguments
    # TODO
    col_name = request.args.get("column", "value")

    # call backend
    # TODO
    mean_value = get_mean_value_from_table(col_name)

    # return results (mean value) as a json
    # TODO
    return jsonify({"column": col_name, "mean": mean_value})


def create_app():
    return app


if __name__ == "__main__":
    # run
    app.run(debug=True, host="localhost", port=5006)
