import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('CarPricePredictorModel.pkl','rb'))
st.title("Car Price Prediction")


Car = float(st.text_input("Enter Car Parking availability: ","2"))
Landsize = float(st.text_input("Enter Landsize: ","94"))
BuildingArea = float(st.text_input("Enter BuildingArea: ","100"))
YearBuilt = float(st.text_input("Enter YearBuilt: ","1970"))

featureInput = np.array([[Car,Landsize,BuildingArea,YearBuilt]])

sal = model.predict(featureInput)

st.write(f'Hello, *World!* :sunglasses: . Price : {sal} ')
