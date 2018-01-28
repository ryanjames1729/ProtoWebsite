from flask import Flask, flash, redirect, render_template, request, session, abort
import time
app = Flask(__name__,template_folder='C:/Users/admin/Documents/ProtoWebsite/ProtoWebsite/Template')


@app.route("/", methods=['GET'])
def index():
    name= "henry"
    question = "This is where a question will go "
    words = question.split()
    question_words= []
    i = 0 
    string = ""
    while (i< len(words)):
        question_words.append(words[i])
        string = " ".join(question_words)
        i += 1
        time.sleep(1)
        return render_template("test.html",name=name,TestQuestion=string)
 

@app.route("/home", methods=['GET'])
def home():
  return (name)
 
       
 
if __name__ == "__main__":
    app.run()
    
    #Run In command prompt "python (file-path)"
    #Open http://localhost:5000/
    #Finish this tutorial https://pythonspot.com/flask-web-app-with-python/
    #Documentation for Flask http://flask.pocoo.org/docs/0.12/
