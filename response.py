import streamlit as st

def get_app_response(prediction):
  if prediction == 1:
    st.write("The model predicts that the data you entered corresponds with an allosteric site.")
  elif prediction == 0:
    st.write("The model predicts that the data you entered does not correspond with an allosteric site")
  else:
    st.write ("No results yet")
