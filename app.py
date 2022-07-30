from flask import Flask, render_template, request as req
import dockers

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/list")
def list_containers():
    return dockers.list_containers_data()
    
@app.route("/run/<name>")
def run_image(name):
    try:
        data = req.args
        dockers.run(name,ports=data.get("ports"),custom_name=data.get("container_name"))
        return True
    except Exception as e:
        print(e)
        return False, 400
    
@app.route("/stop/<id>")
def stop_container(id):
    try:
        dockers.stop_container(id)
        return True
    except Exception as e:
        print(e)
        return False, 400
    
@app.route("/start/<id>")
def stop_container(id):
    try:
        dockers.start_container(id)
        return True
    except Exception as e:
        print(e)
        return False, 400
    
@app.route("/images")
def stop_container(id):
    try:
        return dockers.list_images_names()
    except Exception as e:
        print(e)
        return False, 400

if __name__ == "__main__":
    app.run(port=8080,debug=True)