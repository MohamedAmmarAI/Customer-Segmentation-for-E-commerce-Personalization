# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import datetime as dt

# Load the pre-trained models
with open('rfm_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('rfm_pca.pkl', 'rb') as f:
    pca = pickle.load(f)

with open('rfm_kmeans.pkl', 'rb') as f:
    kmeans = pickle.load(f)

# Streamlit app title
st.title("Customer Segmentation - RFM Classification")

# User inputs for base features
customer_id = st.text_input("Enter Customer ID", value="12345")
invoice_date = st.date_input("Enter Invoice Date")
quantity = st.number_input("Enter Quantity", min_value=1)
unit_price = st.number_input("Enter Unit Price", min_value=0.0)

# Today's date to calculate recency
today_date = pd.Timestamp(dt.date.today())

# Step 1: Calculate Recency, Frequency, and Monetary
recency = (today_date - pd.Timestamp(invoice_date)).days
frequency = 1  # Assuming 1 transaction for simplicity
monetary = quantity * unit_price

# Display the extracted RFM values
st.subheader("Extracted RFM Values")
st.write(f"Recency: {recency} days")
st.write(f"Frequency: {frequency}")
st.write(f"Monetary: ${monetary:.2f}")

# Step 2: Preprocess and classify
if st.button('Classify Customer'):
    # Create DataFrame for RFM features
    rfm_features = pd.DataFrame({
        'Recency': [recency],
        'Frequency': [frequency],
        'Monetary': [monetary]
    })

    # Apply scaling using the previously trained scaler
    rfm_scaled = scaler.transform(rfm_features)

    # Apply PCA
    rfm_pca = pca.transform(rfm_scaled)

    # Predict the cluster using KMeans
    cluster = kmeans.predict(rfm_pca)[0]

    # Display the predicted cluster
    st.success(f"The customer belongs to Cluster {cluster}")

    # Cluster description mapping
    if cluster == 1:
        st.write("Segment: High Value Champions")
    elif cluster == 2:
        st.write("Segment: At-Risk Customers")
    elif cluster == 3:
        st.write("Segment: Promising Newcomers")
    else:
        st.write("Segment: Unknown")

    # Optional: Provide a detailed description for each cluster
    cluster_descriptions = {
        1: 'These are your top customers who buy frequently and spend the most.',
        2: 'These customers are at risk of leaving and need re-engagement.',
        3: 'New or promising customers showing signs of potential loyalty.'
    }
    st.write(f"Detailed Description: {cluster_descriptions.get(cluster, 'No description available')}")
