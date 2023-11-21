import io
import os
import json
from PIL import Image

import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect

app = Flask(__name__)
counter = 0

RESULT_FOLDER = os.path.join('static')
app.config['RESULT_FOLDER'] = RESULT_FOLDER

model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt', source='local')
model.eval()

def get_prediction(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    imgs = [img]  # batched list of images

# Inference
    results = model(imgs, size=640)  # includes NMS
    return results

@app.route('/', methods=['GET', 'POST'])
def predict():
    global counter
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return

        img_bytes = file.read()
        results = get_prediction(img_bytes)

        # Asegúrate de que 'counter' es un entero antes de incrementarlo
        counter = int(counter) + 1
        save_dir = 'static' + str(counter)
        results.save(save_dir=save_dir)

        # Usa la variable al redirigir a la imagen resultante
        #return redirect(save_dir + '/image0.jpg')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
