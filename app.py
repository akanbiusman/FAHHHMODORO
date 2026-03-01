from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

AUDIO_FILENAME = "alarm.mp3"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audio")
def get_audio():
    audio_dir = os.path.join(app.root_path, "static", "audio")
    return send_from_directory(audio_dir, AUDIO_FILENAME)


if __name__ == "__main__":
    app.run(debug=True)
