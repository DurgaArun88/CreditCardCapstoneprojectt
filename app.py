import streamlit as st
import pickle
import numpy as np
import gzip


dtc=pickle.load(gzip.open('dtc.pkl.gz','rb'))

st.title("CREDIT CARD FRAUD DETECTION")
st.write("This application predicts whether a transaction is valid or fraudulent based on the input data")

st.write("Example_input = [[0.1,1.2,3.2,1.3,1.5,2.2,1.0,1.2,1.3,0.5,0.6,0.7,0.9,2.4,2.4,2.5,2.2,2.6,1.5,1.3,2.6,3.1,3.5,3.6,3.8,2.9,2.7,2.4]]")

input_data = st.text_input('Enter the input data(comma separated values)','')


submit = st.button('Predict')

if submit:
   try:
      input_split_data = input_data.split(',')
      features = np.asarray(input_split_data, dtype=np.float32)
      prediction = dtc.predict(features.reshape(1,-1))

      if prediction[0]==0:
        st.success('Valid Transaction')
      else:
        st.error('Fraud Transaction')

   except ValueError:
    st.error('Invalid input')
   except Exception as e:
    st.error(f'An error occurred: {e}')
