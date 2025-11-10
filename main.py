from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI(title="API de Predicción de Iris")

# Cargar el modelo al inicio
with open('modelo.pkl', 'rb') as f:
    model = pickle.load(f)

# Definir el "schema" de entrada
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[
        data.sepal_length, 
        data.sepal_width, 
        data.petal_length, 
        data.petal_width
    ]])

    prediction = model.predict(features)
    iris_map = {0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'}

    return {"prediction": iris_map[prediction[0]]}

@app.get("/")
def root():
    return {"message": "Bienvenido al 'AI Fabric' con Hugging Face!"}

# Uvicorn run command logic (opcional pero buena práctica)
if __name__ == "__main__":
    import uvicorn
    # Hugging Face Spaces expone la variable PORT
    port = int(os.environ.get("PORT", 7860)) 
    uvicorn.run(app, host="0.0.0.0", port=port)