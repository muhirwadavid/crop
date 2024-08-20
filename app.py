from flask import Flask, request, render_template
import joblib
import numpy as np
from werkzeug.serving import run_simple

app = Flask(__name__)
#app.config['DEBUG'] = True
model = joblib.load('rf_model.pkl')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    user_input = [float(x) for x in request.form.values()]

   # Convert input to numpy array and reshape it to fit the model
    input_array = np.array(user_input).reshape(1, -1)
   
    # Predict the result using the loaded model
    prediction = model.predict(input_array)
   
    # Return the result to the user
    return render_template('index.html', prediction_text=f'Predicted result: {prediction[0]}')

if __name__ == '__main__':
    run_simple('localhost',5000,app)