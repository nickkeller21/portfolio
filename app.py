import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)
 