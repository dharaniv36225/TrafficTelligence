import numpy as np
import pickle
import pandas as pd
import os
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__,template_folder='templates')

# Load the trained ML model and scaler
model = pickle.load(open("C:\\Users\\SRINIVAS\\OneDrive\\Desktop\\TrafficVolumeProject\\Flask\\model.pkl", "rb"))
encoder = pickle.load(open("C:\\Users\\SRINIVAS\\OneDrive\\Desktop\\TrafficVolumeProject\\Flask\\encoder.pkl", "rb"))

# Route for home page
@app.route('/')
def home():
    return render_template("index.html")  # Flask will look inside the 'templates' folder

# Route for prediction
@app.route('/predict', methods=["POST","GET"])
def predict():
    # Read form input
    input_feature = [float(x) for x in request.form.values()]
    features_values = [np.array(input_feature)]

    # Column names (same as used during training)
    names = [['holiday', 'temp', 'rain', 'snow', 'weather', 'year', 'month', 'day', 'hours', 'minutes', 'seconds']]


    # Create DataFrame
    data = pd.DataFrame(features_values, columns=names)
    prediction = model.predict(data)
    print(prediction)
    text = "Estimated Traffic Volume is: "
    return render_template("output.html",result = text + str(prediction) +"units")

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(port=port, debug=True, use_reloader=False)

