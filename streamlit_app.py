import streamlit as st
import pandas as pd
import requests

import google.auth.transport.requests
import google.oauth2.id_token


def get_data():
    df = pd.read_gbq("SELECT * FROM `dataset_output.product_distributions`", use_bqstorage_api=True).set_index("product_id")
    return df


df = get_data()
product_id = st.selectbox(label="Product ID", options=df.index)
amount_to_distribute = int(df.loc[product_id].sum())
st.write(f"We need to distribute {amount_to_distribute} products.")
st.bar_chart(df.loc[product_id])