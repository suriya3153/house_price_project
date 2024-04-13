import streamlit as st
import pickle
import sklearn
import numpy as np
import pandas as pd

X = pd.read_csv('output.csv')
locations = list(X.columns[3:])

def predict_price(location, sqft, bath, bhk):    
    loc_index = np.where(X.columns == location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return lr_clf.predict([x])[0]

with open('banglore_home_prices_models.pickle', 'rb') as f:
    lr_clf = pickle.load(f)
    
area = st.text_input("area (Square feet)", "0")
area=int(area)
bhk = st.slider("Select the number of BHK", 1, 5, key='bhk_slider')
bath = st.slider("Select the number of Bathrooms", 1, 5, key='bath_slider')
location = st.selectbox("Location: ",locations) 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if st.button('Estimate Price'):
    price=predict_price(location,area,bath,bhk) # assuming you wanted to use 'area' not 'name'
    price=round(price,2)
    st.warning(str(price)+" Lakh")
