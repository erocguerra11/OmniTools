from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Configuración de la IA (Gemini)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/seguridad')
def seguridad():
    return render_template('seguridad.html')

@app.route('/testers', methods=['GET', 'POST'])
def testers():
    resultado = ""
    if request.method == 'POST':
        # Aquí recibimos el código que el usuario pega en la web
        codigo_usuario = request.form.get('codigo')
        prompt = f"Actúa como un experto en QA Testing. Analiza errores y mejora este código: {codigo_usuario}"
        
        # Gemini genera la respuesta
        response = model.generate_content(prompt)
        resultado = response.text

    return render_template('testers.html', resultado=resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
