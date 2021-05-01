#import libraries
import numpy as np
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('regression_model1.pkl', 'rb'))

## Note : 
## Request to please enter numerical inputs in the front end since the model requires numbers as input

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI

    
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2) 
    return render_template('index.html', prediction_text='Air quality Index is :{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)