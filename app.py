import streamlit as st
from joblib import load

# Imports the functions we coded above
from header import *
from response import *
from predictor import *

# Load our DecisionTree model into our web app
model = load("model.joblib")

create_header()
input_features = get_user_input()
clicked = st.button("Classify")
if clicked:
  prediction = make_prediction(model, input_features)
  get_app_response(prediction)
