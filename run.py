import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #route decorator
def index(): #index view
    return render_template("index.html")
    
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    
    return render_template("about.html", page_title="About", company=data)
    
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact", list_of_numbers=[1,2,3])
    
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":
    host = os.environ.get("IP")
    port = int(os.environ.get("PORT"))
    
    app.run(host,port,debug= True)