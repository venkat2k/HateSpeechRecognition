from HateSpeechDetection import HateSpeechDetector
from flask import *
import warnings
warnings.filterwarnings("ignore")
##tool = HateSpeechDetector("english")
##additional = ["u", "ok", "yo", "a", "b", "lol", "lmao", "ur", "amp", "ya", "woof", "my", "this", "i ", "im ", "yo", "my ", "u ", "this "]
##tool.train()
##def predict(text):
##    print(tool.predict(text))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("comments.html")

