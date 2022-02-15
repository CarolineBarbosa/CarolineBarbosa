import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image


######################################################
################## CONTAINER #########################
######################################################
with st.container():

    st.title('Transaction verification')

    ## parameters input

    transaction_type = st.selectbox(
        'Transaction type:',
        ('PAYMENT', 'TRANSFER', "CASH_IN", 'CASH_OUT', "DEBIT"))

    amount =st.text_input('Amount', '')
    st.write('The total amount for {} is $'.format(transaction_type.lower()), amount)

    name_dest =st.text_input('Send to:', '')

    # start buton
    is_fraud = np.random.choice([True, False])


    if st.button('Verify'):
        is_fraud = np.random.choice([True, False])

        with st.spinner('Verifying...'):
            time.sleep(5)
        if is_fraud:
            st.error('This is a {} might be a fraud!'.format(transaction_type.lower()))
        else:
            st.success('sucess!')


######################################################
################## SIDE BAR ##########################
######################################################

image = Image.open('data/input/logo.png')
basewidth = 150
wpercent = (basewidth/float(image.size[0]))
hsize = int((float(image.size[1])*float(wpercent)))
img = image.resize((basewidth,hsize), Image.ANTIALIAS)

st.sidebar.image(img, use_column_width= 'auto')
st.sidebar.write("Hello User")

add_selectbox = st.sidebar.selectbox(
    "Transaction origin",
    ("Facebook pay", "Paypall", "other")
)