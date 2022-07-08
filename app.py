import streamlit as st
st.title("Restaurant Review")
st.subheader("To classify whether the feedback given by the customer is Positive or Negative")

import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib as jb
import pickle
import emoji

load_file = open(r"C:\Users\Lenovo\Documents\Verzeo\model_pickle","rb")
classifier = pickle.load(load_file)

#CUSTOMER INPU DATA
customer_name = st.text_input(label="Customer_name",max_chars=20)
customer_mob  = st.number_input(label="Customer_No")

customer_feedback = st.text_input(label="Customer Feedback",value="",
                           max_chars=100)
st.write("Feedback by the customer is", customer_feedback)
####


#LABEL
label=['Postive','negative']
###

#PREDICT
if st.button("Submit"):
    Result = classifier.predict([customer_feedback])
    st.write("The Review of the customer is classified into",Result[0])
    if Result > 0.0:
        custom_emoji = ":smile:"
        st.write(emoji.emojize(custom_emoji,use_aliases=True))
    else:
        st.write(emoji.emojize(":face_without_mouth:"))
####