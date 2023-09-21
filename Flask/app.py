from flask import Flask
from flask import request
from flask import render_template
from transformers import pipeline

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    text = ''
    text_fi = ''
    if request.method == 'POST':
        text = request.form['text']
        if text:
            pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")
            result = pipe(text)
            if result:
                text_fi = result[0].get('translation_text', '')

    return render_template('index.html', text=text, text_fi=text_fi)
