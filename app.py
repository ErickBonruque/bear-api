from flask import Flask, render_template, request
import cv2
from fastai.vision.all import load_learner
import numpy as np
from io import BytesIO
from PIL import Image
from base64 import b64encode

app = Flask(__name__)

# Carregar o modelo treinado
model = load_learner('./model/export.pkl')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Obter a imagem enviada pelo cliente
    image = request.files['image']
    
    # Verifica se o arquivo está vazio
    if image.filename == '':
        return render_template("index.html", prediction="Nenhuma imagem foi enviada")
    # Ler a imagem
    file = image.read()
    
    # Verifica se o buffer da imagem está vazio
    if len(file) == 0:
        return render_template("index.html", prediction="A imagem enviada é inválida")
    
    # Carregar a imagem e aplicar transformações
    img = cv2.imdecode(np.frombuffer(file, np.uint8), -1)
    
    # Verificando se tem mais de 3 dimensões
    if len(img.shape) > 2:
        img = img[:, :, :3]
        
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Realizar a predição
    prediction, _, _ = model.predict(img)
    nome = {
        "black": "Urso Negro",
        "grizzly": "Urso Pardo",
        "teddy": "Urso de Pelúcia",
        "polar": "Urso Polar",
        "sloth": "Urso Preguiça",
        "panda": "Urso Panda",
        "andean": "Urso de Oculos",
        "malayanus": "Urso do Sol",
    }
    descriptions = {
        "black": "./descriptions/black.txt",
        "grizzly": "./descriptions/grizzly.txt",
        "teddy": "./descriptions/teddy.txt",
        "polar": "./descriptions/polar.txt",
        "sloth": "./descriptions/sloth.txt",
        "panda": "./descriptions/panda.txt",
        "andean": "./descriptions/andean.txt",
        "malayanus": "./descriptions/malayanus.txt"
    }
    name = nome[prediction]
    
    with open(descriptions[prediction], 'r', encoding='utf-8') as file:
        description = file.read().replace('\n', '<br>')
    
    # Codificar a imagem em base64
    img_aux = Image.fromarray(img_rgb)
    img_bytesIO = BytesIO()
    img_aux.save(img_bytesIO, format='PNG')
    img_bytes = img_bytesIO.getvalue()

    # Codificar os bytes da imagem para base64
    img_base64 = b64encode(img_bytes).decode('utf-8')

    # Passar a variável img_base64 para o template Flask
    img_inf = f'<img src="data:image/png;base64,{img_base64}" alt="NumPy Array Image">'
    
    # Retornar a predição e a imagem codificada em base64
    return render_template("index.html", prediction=name, about="Sobre o urso " + name + ":", description=description, img_inf=img_inf)


if __name__ == '__main__':
    app.run(debug=True)