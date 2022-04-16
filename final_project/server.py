from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    #textToTranslate={"textToTranslate":textToTranslate,"translated_text":ranslator.englishToFrench(textToTranslate)}
    #translated_text = translator.englishToFrench(textToTranslate)
    return translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    #translated_text = translator.frenchToEnglish(textToTranslate)
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
