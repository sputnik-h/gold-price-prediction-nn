#!/usr/bin/env /opt/conda/bin/python
# Ensure compatibility
#from __future__ import absolute_import, division, print_function

""
print('Content-Type:text/html') #HTML is following
print("")                          #Leave a blank line

""
# Ensure compatibility
#from __future__ import absolute_import, division, print_function

# Import packages
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

# Import TensorFlow and Keras packages
import tensorflow as tf
from tensorflow import keras

class_names = ['NotGain', 'Gain']

# Load saved model
new_model = keras.models.load_model('saved_models/gold_prediction_model.keras')

""
import cgi
import cgitb
cgitb.enable()

input_data=cgi.FieldStorage()

print('<h1>', 'Prediction Results', '</h1>')

try:
    SP_Ajclose = float(input_data["SP_Ajclose"].value)
    SP_Trend = float(input_data["SP_Trend"].value)
    SF_Price = float(input_data["SF_Price"].value)
    SF_Trend = float(input_data["SF_Trend"].value)
    PLT_Price = float(input_data["PLT_Price"].value)
    PLT_Trend = float(input_data["PLT_Trend"].value)
    EU_Price = float(input_data["EU_Price"].value)
    USDI_Price = float(input_data["USDI_Price"].value)
    USO_Trend = float(input_data["USO_Trend"].value)
    SP_Ajclose_shift_1 = float(input_data["SP_Ajclose_shift_1"].value)
    SP_Trend_shift_1 = float(input_data["SP_Trend_shift_1"].value)
    SF_Price_shift_1 = float(input_data["SF_Price_shift_1"].value)
    SF_Trend_shift_1 = float(input_data["SF_Trend_shift_1"].value)
    PLT_Price_shift_1 = float(input_data["PLT_Price_shift_1"].value)
    PLT_Trend_shift_1 = float(input_data["PLT_Trend_shift_1"].value)
    EU_Price_shift_1 = float(input_data["EU_Price_shift_1"].value)
    USDI_Price_shift_1 = float(input_data["USDI_Price_shift_1"].value)
    USO_Trend_shift_1 = float(input_data["USO_Trend_shift_1"].value)
    Gold_Trend_shift_1 = float(input_data["Gold_Trend_shift_1"].value)

except:
    print('<p>Sorry, we cannot turn your inputs into numbers (floats).</p>')

# Print the values
print('<p>',
      SP_Ajclose, SP_Trend, SF_Price, SF_Trend, 
      PLT_Price, PLT_Trend, EU_Price, USDI_Price, 
      USO_Trend, SP_Ajclose_shift_1, SP_Trend_shift_1, 
      SF_Price_shift_1, SF_Trend_shift_1, PLT_Price_shift_1, 
      PLT_Trend_shift_1, EU_Price_shift_1, USDI_Price_shift_1, 
      USO_Trend_shift_1, Gold_Trend_shift_1,
      '</p>')


#Each ranges from 0 to 1
SingleObservation = np.array([[SP_Ajclose, SP_Trend, SF_Price, SF_Trend, 
      PLT_Price, PLT_Trend, EU_Price, USDI_Price, 
      USO_Trend, SP_Ajclose_shift_1, SP_Trend_shift_1, 
      SF_Price_shift_1, SF_Trend_shift_1, PLT_Price_shift_1, 
      PLT_Trend_shift_1, EU_Price_shift_1, USDI_Price_shift_1, 
      USO_Trend_shift_1, Gold_Trend_shift_1]])

SingleObservationFloat = SingleObservation.astype(float)

SinglePredictionNewModel = new_model.predict(SingleObservationFloat, verbose = 0)

# Print prediction
print('<p>',SinglePredictionNewModel[0,0],'</p>')

print('<p>',class_names[1 if SinglePredictionNewModel[0,0] > 0.5 else 0],'</p>')

print('<h1>','Results are complete','</h1>')
