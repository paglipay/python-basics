from flask import Flask, request, jsonify
from DecisionTree import DecisionTree
import json
import threading
import uuid

app = Flask(__name__)
sessions_data = {}
flask_process_data = {"OLD_TEXT": ""}
flask_process = {}
module_instances_hash = {}


@app.route("/", methods=["GET"])
def hello_world():
    """
    Route handler for the root endpoint.
    """
    return "Hello, World!"


@app.route("/process/<SESSION>", methods=["POST"])
def process_data(SESSION):
    """
    Route handler for processing data for a specific session.
    """
    if SESSION not in sessions_data:
        sessions_data[SESSION] = {}
    
    data = request.get_json()
    print("Data: ", data)
    
    data_output = {}
    decisionTree = DecisionTree(data, data=data_output)
    
    sessions_data[SESSION] = data_output
    return jsonify(data_output), 200


@app.route("/start/<hash>", methods=["GET", "POST"])
def start(hash):
    if request.method == "POST":
        data = request.get_json()
        print("data: ", data)
        
        if "jobs" in data:
            name = data.pop("jobs")
        else:
            name = hash
        
        d = data
    else:
        d = {}
    
    print("d: ", d)
    
    if hash in flask_process_data:
        flask_process_data[hash].update(d)
        module_instances = module_instances_hash[hash]
    else:
        print("NEW HASH: ", hash)
        flask_process_data[hash] = d
        module_instances_hash[hash] = {}
        module_instances = module_instances_hash[hash]
    
    d = flask_process_data[hash]
    
    if not "uuid" in hash:
        d["uuid"] = hash
    
    thread = threading.Thread(
        target=do_process,
        args=(
            d,
            name,
            module_instances,
        ),
    )
    
    flask_process[hash] = thread
    thread.daemon = False
    thread.start()
    thread.join()
    
    return jsonify(d), 200


def do_process(flask_data, json_file, module_instances):
    if ".json" in json_file:
        c = DecisionTree(
            json.load(open(json_file)),
            tree_name=json_file,
            module_instances=module_instances,
            data=flask_data,
        )
    else:
        c = DecisionTree(
            json_file,
            tree_name=uuid.uuid1(),
            module_instances=module_instances,
            data=flask_data,
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
