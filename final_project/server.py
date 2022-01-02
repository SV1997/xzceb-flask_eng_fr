import translate.languagetr
from flask import Flask, render_template, request
import json
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='template')

@app.route("/")
def renderIndexPage(): # Write the code to render template
    return render_template('index.html')
@app.route("/englishToFrench")
def translateToFrench():
    textToTranslate = request.form.get('textToTranslate')
    t=translate.languagetr.en2fr(textToTranslate)
    return t
    # return "Translated text to French"

@app.route("/frenchToEnglish")
def translateToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text=translate.languagetr.fr2en(textToTranslate)# Write your code here

    return f"{translated_text}"


app.run(host="0.0.0.0", port=8080,debug=True)
