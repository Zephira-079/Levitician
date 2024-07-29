from flask import Flask, render_template
import threading
import subprocess
from waitress import serve
import config

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


def run():
    if __name__ == "__main__":
        serve(app, host="0.0.0.0", port=8080)


def thread_run():
    t = threading.Thread(target=run)
    t.start()
    try:
        subprocess.run(["py", "Levitician.py"])
    except:
        subprocess.run(["python3", "Levitician.py"])
    finally:
        print("An Error has Occur (unspecified error)")
        exit()


thread_run()
