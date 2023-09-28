from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'https://github.com/AniruthDCoder'


if name == "main":
    app.run()
