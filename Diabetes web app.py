# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:03:32 2024

@author: Amani
"""

import numpy as np
import pickle
import streamlit as st
#loding the sved model
#rb mean read binary
loaded_model=pickle.load(open('C:/Users/Amani/OneDrive/Documents/machine Learning/Diabetes/trained_model.sav','rb'))
""" Create function"""
def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print( prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'

    
def main():
    #given title
    st.title('diabetes prediction web app')
    #gitting input data from user
    
    Pregnancies=st.text_input('number of Pregnancies')
    Glucose=st.text_input(' Glucose Level')
    BloodPressure=st.text_input(' BloodPressure Value')
    SkinThickness=st.text_input(' SkinThickness Value')
    Insulin=st.text_input(' Insulin Value')
    BMI=st.text_input(' BMI Value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age of person')
    
    #cod for prediction
    diagnosis=''
    # create a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
    
    
if __name__ == '__main__' :
     main()