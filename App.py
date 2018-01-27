from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__,template_folder='C:/Users/admin/Documents/ProtoWebsite/ProtoWebsite/Template')
 
@app.route("/", methods=['GET'])
def index():
    return render_template("test.html",)
 
@app.route("/home", methods=['GET'])
def home():
  name = "Henry"
  return (name)
 
       
 
if __name__ == "__main__":
    app.run()
    
    #Run In command prompt "python (file-path)"
    #Open http://localhost:5000/
    #Finish this tutorial https://pythonspot.com/flask-web-app-with-python/
    #Documentation for Flask http://flask.pocoo.org/docs/0.12/
