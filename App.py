from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "This is going to be bothersome"
 
if __name__ == "__main__":
    app.run()
    
    #Run In command prompt "python (file-path)"
    #Open http://localhost:5000/
    #Finish this tutorial https://pythonspot.com/flask-web-app-with-python/
    #Documentation for Flask http://flask.pocoo.org/docs/0.12/
