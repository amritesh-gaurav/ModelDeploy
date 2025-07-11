import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('CustomerPredictorModel.pkl','rb'))
st.title("Customer Segmentation")

age = float(st.text_input("Enter Age: ","22"))
salary = float(st.text_input("Enter Salary: ","100000"))

featureInput = np.array([[age,salary]])

sal = model.predict(featureInput)

st.write(f'Hello, *World!* :sunglasses: . Customer Group : {sal} ')
