from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/seguridad')
def seguridad():
    return render_template('seguridad.html')

@app.route('/testers')
def testers():
    return render_template('testers.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
