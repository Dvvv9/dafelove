from flask import Flask, render_template
import subprocess
import time
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/amor")
def amor():
    fotos = [
        'foto1.jpg',
        'foto2.jpg',
        'foto3.jpg',
        'foto4.jpg',
        'foto5.jpg',
        'foto6.jpg'
    ]
    return render_template("amor.html", fotos=fotos)

if __name__ == "__main__":
    port = 5000
    subprocess.Popen(["ngrok", "http", str(port)])
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:4040")
    app.run(port=port)
