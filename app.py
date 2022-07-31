import traceback
from flask import Flask, render_template, request as req, jsonify, redirect
import os
import dockers

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/list.html")
def list():
    return render_template("list.html")

@app.route("/config.html")
def config():
    return render_template("config.html")

@app.route("/stats.html")
def stats():
    return render_template("stats.html")

@app.route("/list")
def list_containers():
    return jsonify(dockers.list_containers_data())

@app.route("/stats")
def stats_containers():
    return jsonify(dockers.list_containers_stats())
    
@app.route("/run")
def run_image():
    try:
        data = req.args
        if data.get("name"):
            dockers.run(data.get("name"),ports=data.get("ports"),custom_name=data.get("container_name"))
            return redirect("/")
        return "Error", 500
    except Exception as e:
        print(e)
        return "Error", 400
    
@app.route("/config",methods=["POST"])
def config_image():
    try:
        data = req.form
        print(req.args,req.files,req.form)
        name = data.get("name")
        if name:
            file = req.files.get("file")
            # file.save(os.path.join("./files",name + ".txt"))
            dockers.config(file,custom_name=name)
            return redirect("/")
        return "Error", 500
    except Exception as e:
        print(e)
        print(traceback.print_exc())
        return "Error", 400
    
@app.route("/stop/<id>")
def stop_container(id):
    try:
        dockers.stop_container(id)
        return "Success"
    except Exception as e:
        print(e)
        return "Error", 400
    
@app.route("/kill/<id>")
def kill_container(id):
    try:
        dockers.kill_container(id)
        return "Success"
    except Exception as e:
        print(e)
        return "Error", 400
    
@app.route("/remove/<id>")
def remove_container(id):
    try:
        dockers.remove_container(id)
        return "Success"
    except Exception as e:
        print(e)
        return "Error", 400
    
@app.route("/start/<id>")
def start_container(id):
    try:
        dockers.start_container(id)
        return "Success"
    except Exception as e:
        print(e)
        return "Error", 400
    
@app.route("/images")
def images(id):
    try:
        return jsonify(dockers.list_images_names())
    except Exception as e:
        print(e)
        return "Error", 400

if __name__ == "__main__":
    app.run(port=8080,debug=True)